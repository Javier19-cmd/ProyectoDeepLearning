import csv

def txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(";") for line in stripped if line)
        with open(csv_file, 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)

# Uso del script
txt_to_csv('power.txt', 'power.csv')
