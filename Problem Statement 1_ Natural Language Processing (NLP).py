import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import re

# Ensure necessary NLTK data files are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text, lower=True, remove_stopwords=True, lemmatize=True, stem=False, handle_numbers=True):
        
    # Convert to lowercase if specified
    if lower:
        text = text.lower()
    
    # Tokenize the text into words
    tokens = word_tokenize(text)
    
    # Initialize tools
    stop_words = set(stopwords.words('english')) if remove_stopwords else set()
    lemmatizer = WordNetLemmatizer() if lemmatize else None
    stemmer = PorterStemmer() if stem else None
    
    # Process tokens
    processed_tokens = []
    for token in tokens:
        # Remove punctuation and special characters
        token = re.sub(r'\W', '', token)
        
        # Handle numbers (replace with placeholder "NUM")
        if handle_numbers and token.isdigit():
            token = 'NUM'
        
        # Skip empty tokens
        if not token:
            continue
        
        # Remove stop words
        if remove_stopwords and token in stop_words:
            continue
        
        # Apply lemmatization or stemming
        if lemmatize and lemmatizer:
            token = lemmatizer.lemmatize(token)
        elif stem and stemmer:
            token = stemmer.stem(token)
        
        processed_tokens.append(token)
    
    return processed_tokens

# Accept user input
text = input("Enter text to preprocess: ")

# Prompt user for options
lower = input("Convert to lowercase? (y/n): ").strip().lower() == 'y'
remove_stopwords = input("Remove stopwords? (y/n): ").strip().lower() == 'y'
lemmatize = input("Apply lemmatization? (y/n): ").strip().lower() == 'y'
stem = input("Apply stemming? (y/n): ").strip().lower() == 'y'
handle_numbers = input("Replace numbers with 'NUM'? (y/n): ").strip().lower() == 'y'

# Process the text based on user choices
tokens = preprocess_text(
    text, 
    lower=lower, 
    remove_stopwords=remove_stopwords, 
    lemmatize=lemmatize, 
    stem=stem, 
    handle_numbers=handle_numbers
)

# Display the processed tokens
print("Processed tokens:", tokens)
