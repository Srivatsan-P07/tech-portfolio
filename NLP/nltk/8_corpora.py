"""
Corpora are large and structured sets of texts used for linguistic research and natural language processing (NLP). 
They can be built-in collections provided by libraries like NLTK or custom collections created by users.
"""

import nltk

# Download
nltk.data.path.append(r'..\..\temp_folder')
nltk.download('gutenberg', download_dir=r'..\..\temp_folder')
nltk.download('reuters', download_dir=r'..\..\temp_folder')
nltk.download('brown', download_dir=r'..\..\temp_folder')

from nltk.corpus import gutenberg, reuters, brown

gutenberg_text = gutenberg.fileids()
print(gutenberg_text)

reuters_text = reuters.fileids()
print(reuters_text)