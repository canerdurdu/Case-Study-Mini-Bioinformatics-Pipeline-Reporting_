# Mini Bioinformatics QC Pipeline for Long-Read Sequencing

This project implements a **reproducible bioinformatics pipeline** for performing quality control (QC) and statistical analysis on **long-read sequencing FASTQ data**.

The pipeline was developed as a case study for analyzing sequencing data and generating a simple reports.

The workflow automatically:

- Performs QC analysis for long-read sequencing data
- Calculates per-read statistics
- Generates distribution plots
- Produces summary statistics

The goal is to help determine whether the sequencing data quality is sufficient before proceeding to downstream steps such as alignment.

---

# System Requirements

⚠️ **Important:**  
This pipeline is designed to run in a **Linux environment**. It was tested on a Linux-based system using Conda.

If you are using **Windows**, it is recommended to run the pipeline through:

- **WSL (Windows Subsystem for Linux)**, or
- a **Linux virtual machine**

This ensures compatibility with **Snakemake, Conda environments, and NanoPlot**.

---

# Project Structure

```

project/
│
├── data/
│   └── sample.fastq
│
├── results/
│   ├── sample.csv
│   ├── sample_read_length_95pct.png
│   ├── sample_gc_content.png
│   ├── sample_mean_quality.png
│   └── nanoplot/
│
├── calculation.py
├── visualization.py
├── Snakefile
├── environment.yml
└── README.md

````

---

# Environment Setup

All required dependencies are defined in the environment.yml file to ensure reproducibility of the workflow.

Create the Conda environment:

```bash
conda env create -f environment.yml
conda activate environment
````

---

# Running the Pipeline

Place the FASTQ file inside the **data** directory.

The pipeline consists of three main steps:

1. NanoPlot quality control analysis for long-read sequencing data
2. Custom Python script for per-read statistics
3. Visualization of statistical distributions

Example:

```
data/sample.fastq
```

Run the pipeline:

```bash
snakemake --cores 1
```

Snakemake will automatically execute the following steps:

* NanoPlot QC analysis
* Custom read statistics calculation
* Data visualization

All outputs will be saved in the **results** directory.

---

# Output Summary

The pipeline generates the following outputs.

## QC Analysis

```
results/nanoplot/
```

## Read Statistics

```
results/sample.csv
```

## Distribution Plots

```
results/sample_read_length_95pct.png
results/sample_gc_content.png
results/sample_mean_quality.png
```

These outputs allow quick assessment of sequencing data quality before proceeding with downstream analysis.

```
# Email Draft for Professor Kılıç

Dear Professor,

I performed quality control and read statistics analysis on the FASTQ file you provided using a Snakemake-based pipeline that I developed. As part of the analysis, I examined and visualized the distributions of read length, GC content, and mean read quality scores.

The dataset contains a total of 81,011 reads. The average read length is approximately 1038 bp, and the distribution shows a wide range that is characteristic of long-read sequencing technologies. The mean read quality score was calculated to be approximately Q = 17.9. In long-read sequencing data, average quality scores are typically expected to be around Q ≈ 20; therefore, the observed values correspond to a typical and acceptable quality level.

When examining the GC content distribution, a single prominent peak around ~53% was observed. This suggests that there is no evident GC bias in the dataset and that the sequences exhibit a generally homogeneous GC distribution.

Overall, the QC results indicate that the dataset is consistent with typical long-read sequencing characteristics and that the data quality appears sufficient to proceed with downstream analyses such as alignment.

If you would like, I would be happy to share the generated plots and the full analysis outputs as well.

Best regards.

