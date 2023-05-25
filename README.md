# Innoem_task1_preprocessing
I am sharing what I have done with the given tasks on my internship. I hope that these tasks will help me a lot in learning important technologies like NLP, Machine Learning, Deep Learning.
Text Preprocessing and Word Cloud Generation
Introduction
In this project, the goal was to write a Python function that performs text preprocessing on a given corpus of text. The function should eliminate stop words and clean the text from punctuation and unnecessary characters. Additionally, we needed to create a word cloud to visualize the distribution of words in the text and save the resulting word cloud as an image. Finally, we were required to save the word distribution as a CSV file.
![Ekran görüntüsü 2023-05-25 203024](https://github.com/eneskaya20/Innoem_task1_preprocessing/assets/72800099/4125df30-87db-4742-a82d-4fa51902e43b)
## Methodology:
To accomplish this task, we followed these steps:

We loaded the corpus of text from a .txt file.
Converted all text to lower case.
Removed punctuation and unnecessary characters using regular expressions.
Tokenized the text into individual words using NLTK.
Removed stop words using NLTK's built-in English stop words list.
Lemmatized the remaining words using NLTK's WordNetLemmatizer.
Generated a word cloud using the wordcloud package in Python.
Saved the word cloud as an image file.
Saved the word distribution as a CSV file.
## Results:
The resulting preprocessed text was used to generate a word cloud. The size of each word in the cloud corresponds to its frequency in the text. An image of the word cloud was saved to disk as a PNG file. Additionally, the word distribution was saved as a CSV file for further analysis.

## Conclusion:
Text preprocessing is an important step in natural language processing (NLP). By eliminating stop words and cleaning the text from punctuation and unnecessary characters, we can improve the accuracy of NLP algorithms. The resulting word cloud provides an easy way to visualize the distribution of words in the text, while the CSV file can be used for further analysis.

