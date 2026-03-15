import sys
import pandas as pd
import matplotlib.pyplot as plt


def calculate_n50(lengths):
    lengths = sorted(lengths, reverse=True)
    total = sum(lengths)
    cumulative = 0

    for length in lengths:
        cumulative += length
        if cumulative >= total / 2:
            return length


def create_plot_with_table(data,title,xlabel,output_file,stats_items,hist_color,bg_color,table_header_color,vlines=None):

    fig, ax = plt.subplots(figsize=(8, 6))

    # Figure background
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor("#fcfbf7")

    # Histogram
    ax.hist(
        data,
        bins=50,
        color=hist_color,
        edgecolor="#5f5750",
        alpha=0.92
    )

    # Vertical statistic lines
    if vlines:
        for line in vlines:
            ax.axvline(
                x=line["x"],
                color=line["color"],
                linewidth=2.0
            )

    ax.set_title(title, fontsize=14, fontweight="bold", color="#4a433c")
    ax.set_xlabel(xlabel, color="#4a433c")
    ax.set_ylabel("Frequency", color="#4a433c")
    ax.tick_params(axis="both", colors="#5a5148")

    for spine in ax.spines.values():
        spine.set_color("#7e746a")
        spine.set_linewidth(0.8)

    # Table content
    cell_text = [[item["label"], item["value"]] for item in stats_items]

    table = plt.table(
        cellText=cell_text,
        colLabels=["Statistic", "Value"],
        cellLoc="center",
        loc="bottom",
        bbox=[0.0, -0.60, 1, 0.38]
    )

    table.scale(1, 1.5)

    # Table styling
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#7e746a")
        cell.set_linewidth(0.6)

        if row == 0:
            cell.set_facecolor(table_header_color)
            cell.set_text_props(color="#3c352f", weight="bold")
        else:
            item = stats_items[row - 1]
            cell.set_facecolor(item["color"])
            cell.set_text_props(color="#3c352f", weight="bold")

    plt.subplots_adjust(bottom=0.50)
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close()




if len(sys.argv) != 5:
    print("Usage: python visualization.py <input.csv> <length_png> <gc_png> <quality_png>")
    sys.exit(1)

input_csv = sys.argv[1]
length_png = sys.argv[2]
gc_png = sys.argv[3]
quality_png = sys.argv[4]

df = pd.read_csv(input_csv)


# Read Length Graph

lengths = df["Length"].dropna()

q95 = lengths.quantile(0.95)
zoom_lengths = lengths[lengths <= q95]

n50 = round(calculate_n50(lengths), 2)
mean_len = round(lengths.mean(), 2)
median_len = round(lengths.median(), 2)

length_stats_items = [
    {"label": "N50", "value": n50, "color": "#d9b3c3"},
    {"label": "Mean", "value": mean_len, "color": "#e7c39f"},
    {"label": "Median", "value": median_len, "color": "#b9d4c2"}
]

length_vlines = [
    {"x": n50, "color": "#b56a8a"},
    {"x": mean_len, "color": "#c58a4a"},
    {"x": median_len, "color": "#5f9c7b"}
]

create_plot_with_table(
    zoom_lengths,
    "Read Length Distribution (0–95% Quantile Zoom)",
    "Read Length (bp)",
    length_png,
    length_stats_items,
    hist_color="#8fb4c9",
    bg_color="#f4efe6",
    table_header_color="#d8c8ae",
    vlines=length_vlines
)


# GC Content Graph

gc = df["GC_Content"].dropna()

gc_mean = round(gc.mean(), 2)
gc_median = round(gc.median(), 2)

gc_stats_items = [
    {"label": "Mean GC (%)", "value": gc_mean, "color": "#c7ddc0"},
    {"label": "Median GC (%)", "value": gc_median, "color": "#e2e6c8"}]


create_plot_with_table(
    gc,
    "GC Content Distribution",
    "GC Content (%)",
    gc_png,
    gc_stats_items,
    hist_color="#7faa7a",
    bg_color="#f3f5e8",
    table_header_color="#c9d7b8",
    vlines=None)


# Mean Quality Score

quality = df["Average_QC"].dropna()

quality_mean = round(quality.mean(), 2)
quality_median = round(quality.median(), 2)

quality_stats_items = [
    {"label": "Mean Quality Score", "value": quality_mean, "color": "#c8c0e3"},
    {"label": "Median Quality Score", "value": quality_median, "color": "#e5c7a8"}]

quality_vlines = [
    {"x": quality_mean, "color": "#8573b6"},
    {"x": quality_median, "color": "#c48a52"}]

create_plot_with_table(
    quality,
    "Mean Read Quality Score Distribution",
    "Mean Read Quality Score (Phred)",
    quality_png,
    quality_stats_items,
    hist_color="#c8a86b",
    bg_color="#f7f0e5",
    table_header_color="#dfccb0",
    vlines=quality_vlines)
