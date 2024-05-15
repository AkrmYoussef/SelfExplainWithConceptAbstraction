import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

# Read and process sentences
with open('scripts/additionals/cleaned_sentences.txt', 'r') as file:
    sentences = file.readlines()  # Read each line as a separate sentence
sentences = [s.strip() for s in sentences]  # Strip whitespace and newlines

# Define a set of number words
number_words = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million', 'billion'}

def extract_and_map(sentence):
    results = []
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    for word, tag in tagged:
        if word.lower() in stop_words or not word.isalnum() or word.lower() in number_words:
            # Keep stopwords, punctuation, and number words unchanged
            results.append((word, None))
        else:
            # Process only non-stopwords, non-number, and alphanumeric words
            synsets = wn.synsets(word, pos=get_wordnet_pos(tag))
            if synsets:
                results.append((word, synsets[0]))
            else:
                results.append((word, None))
    return results

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return None

def abstract_with_hypernyms(mapped_words):
    abstracted_sentence = []
    for word, synset in mapped_words:
        if synset:
            hypernyms = synset.hypernyms()
            if hypernyms:
                abstracted_word = hypernyms[0].lemma_names()[0]
            else:
                # No hypernym, try synonyms
                synonyms = synset.lemmas()
                if synonyms:
                    abstracted_word = synonyms[0].name()  # Use the first synonym
                else:
                    abstracted_word = word  # Use the original word if no synonym available
        else:
            abstracted_word = word  # This includes stopwords, punctuation, and number words
        abstracted_sentence.append(abstracted_word)
    return ' '.join(abstracted_sentence)

# Process sentences and write each abstracted line to a file
with open('scripts/additionals/abstracted_concepts.txt', 'w') as output_file:
    for sentence in sentences:
        mapped_words = extract_and_map(sentence)
        abstracted_text = abstract_with_hypernyms(mapped_words)
        output_file.write(abstracted_text + '\n')  # Write each abstracted sentence on a new line

print("Abstracted text has been written to 'abstracted_concepts.txt'")