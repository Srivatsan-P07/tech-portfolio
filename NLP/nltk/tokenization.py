"""
1. Tokenization is the process of splitting text into smaller units called tokens, such as words, sentences, or characters.  
2. It helps clean and preprocess text data for analysis or machine learning models.  
3. It facilitates understanding by allowing the analysis of individual tokens like keywords.  
4. Tokenization improves tasks like search, translation, and sentiment analysis.  
5. It is customizable, making it adaptable to different needs, like handling punctuation or special characters.  
"""
import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer

text = """ Hello, world! Let's test tokenization: 123 times, with symbols like @, #, $, %, and more! """

word_token = word_tokenize(text)
sent_token = sent_tokenize(text)

word_regex_tokenizer = RegexpTokenizer(r'\w') #This pattern matches one character at a time.
word_regex_token = word_regex_tokenizer.tokenize(text)

digit_regex_tokenizer = RegexpTokenizer(r'\d') #This pattern matches one digit at a time.
digit_regex_token = digit_regex_tokenizer.tokenize(text)

print('word token: ', word_token)
print('\nsentence token: ', sent_token)
print('\nword regex token: ', word_regex_token)
print('\ndigit regex token: ', digit_regex_token)