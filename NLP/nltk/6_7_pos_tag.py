"""
Part-of-Speech (POS) Tagging
POS tagging is a process in natural language processing (NLP) where each word in a sentence is assigned a part of speech, 
such as noun, verb, adjective, etc. 
This helps in understanding the grammatical structure of the sentence.
"""

import nltk
nltk.data.path.append(r'..\..\temp_folder')
nltk.download('punkt_tab', download_dir=r'..\..\temp_folder')
nltk.download('averaged_perceptron_tagger_eng', download_dir=r'..\..\temp_folder')
nltk.download('maxent_ne_chunker_tab', download_dir=r'..\..\temp_folder')
nltk.download('words', download_dir=r'..\..\temp_folder')
print("----------\n")

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

sentence = "Barack Obama was born in Hawaii"
tokenized_output = word_tokenize(sentence)
pos_words = pos_tag(tokenized_output)

print(pos_words)

"""
Named Entity Recognition (NER) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text 
into predefined categories such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc.

NN: Noun, singular or mass --> Named Entity Recognition
VB: Verb, base form
JJ: Adjective
RB: Adverb
NNS: Noun, plural
NNP: Proper noun, singular --> Named Entity Recognition
NNPS: Proper noun, plural --> Named Entity Recognition
VBD: Verb, past tense
VBG: Verb, gerund or present participle
VBN: Verb, past participle
VBP: Verb, non-3rd person singular present
VBZ: Verb, 3rd person singular present
PRP: Personal pronoun
PRP$: Possessive pronoun
IN: Preposition or subordinating conjunction
DT: Determiner
CD: Cardinal number
UH: Interjection
"""

#Chunking

"""
Chunking is a technique used in natural language processing (NLP) to group words into meaningful units, or "chunks." 
These chunks often represent phrases, such as noun phrases (NP) or verb phrases (VP), 
which are easier to analyze than individual words.
"""
from nltk.chunk import ne_chunk

chunks = ne_chunk(pos_words)
print(chunks)

from nltk.chunk import RegexpParser

regex_grammer = "NP: {<DT>?<JJ>*<NN>}"
regex_parser = RegexpParser(regex_grammer)
regex_parser_words = regex_parser.parse(pos_words)
print(regex_parser_words)