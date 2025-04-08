"""
Lemmatization is the process of converting a word to its base or dictionary form (called a lemma). 
Unlike stemming, which simply trims words to their root form, lemmatization considers the context and the morphological analysis of words. 
This ensures that the base form obtained is a valid word found in the dictionary.
"""

import nltk
from nltk.stem import WordNetLemmatizer

nltk.data.path.append(r'D:\tech-portfolio\temp_folder')
nltk.download('wordnet', download_dir=r'D:\tech-portfolio\temp_folder')

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("running", pos='v'))