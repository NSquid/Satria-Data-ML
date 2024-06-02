import csv

input_file = r"C:\Users\Mikhael\Downloads\Satria-Data\Data\DataTrain.csv"
output_file = r"C:\Users\Mikhael\Downloads\Satria-Data\Data\textTrainUncleaned.csv"

try:
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile)
        for row in reader:
            writer.writerow([row[0]])  # write only the first column to the output file
except Exception as e:
    print(f"An error occurred: {e}")