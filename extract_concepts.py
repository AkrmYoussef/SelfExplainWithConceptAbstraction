import re
import csv

# The filename of the CSV file
input_filename = 'scripts/resultDistilBert.csv'
output_filename = 'scripts/additionals/extracted_sentences.txt'

def extract_sentences(text):
    # Regular expression to match sentences within single or double quotes
    # The pattern will capture text within single quotes ('') or double quotes ("")
    pattern = re.compile(r'\'([^\']+)\'|\"([^\"]+)\"')
    matches = pattern.findall(text)
    # Each match is a tuple where text can be in either the 1st or 2nd element, depending on the quote type
    # We concatenate the non-empty elements from these tuples
    return [sentence for match in matches for sentence in match if sentence]

def main():
    # Open the output file for writing
    with open(output_filename, 'w', encoding='utf-8') as txtfile:
        # Read the CSV file
        with open(input_filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header
            for row in reader:
                if row:  # Check if the row is not empty
                    text = row[0]
                    found_sentences = extract_sentences(text)
                    if found_sentences:
                        # Join the sentences with commas and write to the file
                        txtfile.write(found_sentences[0] + '\n')
    
    print(f'Sentences have been extracted and saved to {output_filename}')

if __name__ == '__main__':
    main()