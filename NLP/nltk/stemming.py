"""
What is Stemming?
Stemming is a process in natural language processing (NLP) that reduces words to their root or base form. 
The goal is to group together different forms of a word so they can be analyzed as a single item. 
For example, the words "running," "runner," and "ran" can all be reduced to the stem "run."

# Types of Stemmers

## Porter Stemmer

Developed by Martin Porter in 1980, the Porter Stemmer is one of the most widely used stemming algorithms.
It uses a set of rules to remove common suffixes from English words.
Example: "running" becomes "run," "happiness" becomes "happi."

## Lancaster Stemmer

Also known as the Paice-Husk Stemmer, it is more aggressive than the Porter Stemmer.
It uses a larger set of rules and can sometimes produce shorter stems.
Example: "running" becomes "run," "happiness" becomes "happy."

## Snowball Stemmer

An improvement on the Porter Stemmer, developed by Martin Porter himself.
It is more flexible and can be used for multiple languages.
Example: "running" becomes "run," "happiness" becomes "happi."
"""