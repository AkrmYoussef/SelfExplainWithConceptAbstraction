import re

def recombine_text(text):
    # Regular expression to find patterns with ## and remove space before ##
    corrected_text = re.sub(r'\s+(##)', r'\1', text)
    # Remove the ## markers now
    corrected_text = corrected_text.replace('##', '')
    # Correct the negated verbs
    corrected_text = re.sub(r'(\w+)\s+n\s+\'\s+t', r"\1n't", corrected_text)
    corrected_text = re.sub(r'(\w+)\s+ca\s+n\s+\'\s+t', r"can't", corrected_text)
    corrected_text = re.sub(r'(\w+)\s+do\s+n\s+\'\s+t', r"don't", corrected_text)
    corrected_text = re.sub(r'it\s+\'\s+s', r"it's", corrected_text)
    corrected_text = re.sub(r'\s*\'\s*', "'", corrected_text)
    corrected_text = re.sub(r'\s*-\s*', "-", corrected_text)
    return corrected_text

def process_file(input_file, output_file):
    # Read from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Correct the text
    corrected_text = recombine_text(text)
    
    # Write to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(corrected_text)

# Example usage:
input_file = 'scripts/additionals/extracted_sentences.txt'
output_file = 'scripts/additionals/cleaned_sentences.txt'
process_file(input_file, output_file)