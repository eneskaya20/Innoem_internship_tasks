import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import csv
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
wnl = WordNetLemmatizer()


# 1- we must lower the text
def text_lowercase(text):
    return text.lower()


# 2- Remove numbers
def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result


# 3- Remove punctuation
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


# 4- Remove whitespace from text
def remove_whitespace(text):
    return " ".join(text.split())


# 5- Removing stopwords using nltk so that we are left with meaningful ones.
def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text


# 6- Lemmatazing words using nltk
def lemmatize_word(text):
    lemmas = [wnl.lemmatize(word, pos ='v') for word in text]
    return lemmas


input_str = " From the bustling streets of New York City to the serene landscapes of the countryside, there is no shortage of breathtaking sights to explore in the United States. The country boasts a diverse range of natural wonders, including majestic mountains, stunning coastlines, and vast deserts. One such iconic landmark is the Grand Canyon, located in Arizona. Spanning over 277 miles in length, the Grand Canyon is a true marvel of nature. Its layered rock formations reveal a mesmerizing history that dates back millions of years. Visitors can hike along its rim, marveling at the sheer scale and beauty of this natural wonder. Heading east, one cannot miss the vibrant city of Las Vegas, known for its dazzling lights and lively entertainment scene. Home to numerous world-class casinos, hotels, and shows, Las Vegas is a playground for those seeking excitement and glamour. From the famous Las Vegas Strip to the thrilling performances of Cirque du Soleil, the city offers endless opportunities for entertainment."
input_lowered = text_lowercase(input_str)
input_numremoved = remove_numbers(input_lowered)
input_puncremoved = remove_punctuation(input_numremoved)
input_spaceremoved = remove_whitespace(input_puncremoved)
input_stopremoved = remove_stopwords(input_spaceremoved)
input_final = lemmatize_word(input_stopremoved)

print(input_final)

with open('words.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(input_final)


df = pd.read_csv(r"words.csv", encoding="latin-1")

# Generate word cloud
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = set(STOPWORDS),
                min_font_size = 10).generate(' '.join(input_final))

# Plot the word cloud
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

# Show the plot
plt.show()
