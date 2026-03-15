SAMPLES, = glob_wildcards("data/{sample}.fastq")

rule all:
    input:
        expand("results/{sample}.csv", sample=SAMPLES),
        expand("results/{sample}_read_length_95pct.png", sample=SAMPLES),
        expand("results/{sample}_gc_content.png", sample=SAMPLES),
        expand("results/{sample}_mean_quality.png", sample=SAMPLES),
        expand("results/nanoplot/{sample}", sample=SAMPLES)


rule qc_analyzer:
    input:
        "data/{sample}.fastq"
    output:
        "results/{sample}.csv"
    shell:
        """
        python calculation.py {input} {output}
        """


rule plot_qc_metrics:
    input:
        "results/{sample}.csv"
    output:
        "results/{sample}_read_length_95pct.png",
        "results/{sample}_gc_content.png",
        "results/{sample}_mean_quality.png"
    shell:
        """
        python visualization.py {input} {output[0]} {output[1]} {output[2]}
        """


rule nanoplot_qc:
    input:
        "data/{sample}.fastq"
    output:
        directory("results/nanoplot/{sample}")
    shell:
        """
        NanoPlot --fastq {input} --outdir {output} --threads 4
        """
