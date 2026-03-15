import sys
import csv
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


input_fastq = sys.argv[1]
output_csv = sys.argv[2]

with open(output_csv, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["ID", "Length", "GC_Content", "Average_QC"])

    for record in SeqIO.parse(input_fastq, 'fastq'):
        seq_len = len(record.seq)

        # 0 uzunluk kontrolü (Hata almamak için şart)
        if seq_len == 0:
            continue

        gc_content = round(gc_fraction(record.seq) * 100, 2)
        quality_scores = record.letter_annotations['phred_quality']
        avg_quality = round(sum(quality_scores) / seq_len, 2)

        writer.writerow([record.id, seq_len, gc_content, avg_quality])
