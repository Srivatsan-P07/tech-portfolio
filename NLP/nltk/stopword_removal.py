"""
Stopword removal is the process of eliminating common words, known as **stopwords**, from a text. 
These words (e.g., "is," "the," "and," "a") typically don't add significant meaning to the analysis and are often ignored in NLP tasks.

Why It's Important:
1. **Text Simplification**: It helps reduce the size of the text by removing less meaningful words.
2. **Focus on Key Information**: Enables algorithms to focus on important, content-rich words.
3. **Improves Performance**: Streamlines computations and enhances model efficiency in tasks like sentiment analysis or search engine optimization.
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure NLTK resources are downloaded (only required once)
nltk.download('stopwords')
nltk.download('punkt')

# Sample text
text = "This is an example showing how to remove stopwords from a sentence."

# Tokenize the text
tokens = word_tokenize(text)

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords using list comprehension , advisable to convert all to lower
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Output the filtered tokens
print("Filtered Tokens:", filtered_tokens)