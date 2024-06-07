import csv
import re

def clean_text(text):
    if not text:
        return ""
    # Convert to lowercase
    text = text.lower()
    
    partialDetection = ['com', 'news', 'http', '@', '#', 'dot']
    
    text = ' '.join(word for word in text.split() if not any(partial_word in word for partial_word in partialDetection))
    
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'(\d+)(\D+)(\d+)', r'\2', text)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    
    text = ' '.join(word for word in text.split() if len(word) <= 10)
    text = ' '.join(word for word in text.split() if not re.search(r'(.)\1\1', word))
    text = ' '.join(word for word in text.split() if not re.search(r'\d', word) or not re.search(r'[a-zA-Z]', word))
    text = ' '.join(word for word in text.split() if not re.search(r'[bcdfghjklmnpqrstvwxyz]{3}', word))
    
    wordsToRemove = ['dan', 'serta', 'lagipula', 'setelah', 'sejak', 'selanjutnya', 'tetapi', 'melainkan', 
                    'sedangkan', 'atau', 'ataupun', 'maupun', 'untuk', 'agar', 'supaya', 'sebab', 'karena', 
                    'sehingga', 'sampai', 'akibatnya', 'lalu', 'kemudian', 'jika', 'kalau', 'jikalau', 'apabila', 
                    'walaupun', 'maupun', 'meskipoun', 'biarpun', 'seperti', 'sebagai', 'bagaikan', 'biar', 
                    'biarpun', 'bahkan', 'yaitu', 'yakni', 'kecuali', 'selain', 'goblok', 'tolol', 'jancuk',
                    'rt', 'tengil', 're', 'detikbali', 'fuck', 'lo', 'lu', 'letoy', 'cengeng', 'n', 'o', 'pantat']
    
    text = ' '.join(word for word in text.split() if word not in wordsToRemove)
    
    replacements = {
        '01': 'anies',
        'paslon 01': 'anies',
        'paslon 1': 'anies',
        'nomor urut 1': 'anies',
        'pendukung 01': 'pendukung anies',
        '02': 'prabowo',
        'paslon 02': 'prabowo',
        'paslon 2': 'prabowo',
        'nomor urut 2': 'prabowo',
        'pendukung 02': 'anies',
        'ayahbowo': 'prabowo',
        '03': 'ganjar',
        'paslon 03': 'ganjar',
        'paslon 3': 'ganjar',
        'nomor urut 3': 'ganjar',
        'no urut 3': 'ganjar',
        
        'bawaslu': 'badan pengawas pemilu',
    }
    
    text = ' '.join(word for word in text.split() if len(word) >= 3)
    for word, replacement in replacements.items():
        text = text.replace(word, replacement)
    
    return text

input_file = r"C:\Users\Mikhael\Downloads\Satria-Data\Data\DataTrain.csv"
output_file = r"C:\Users\Mikhael\Downloads\Satria-Data\Data\trainPrototype.csv"

try:
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile)
        
        # Write header to the output file
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            # text_id = row[0]  # get the text ID
            text = row[0]  # get the text
            label = row[1]  # get the label
            
            # Clean the text
            cleaned_text = clean_text(text)
            
            # Write the cleaned text and the label to the output file
            writer.writerow([cleaned_text, label])
except Exception as e:
    print(f"An error occurred: {e}")