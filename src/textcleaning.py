import json

import nltk
from nltk.corpus import stopwords
staph = stopwords.words('english')
staph.append("like")
staph.append("got")
staph.append("get")
staph.append("know")
staph.append("aint")
staph.append("dont")
staph.append("go")


# BELOW CODE COMBINES ALL WORDS FROM A PARTICULAR ARTIST FOR ANALYSIS


# Define Individual Path
#
#path = "/Users/matthewhwang/Galvanize/Capstone1/Data/Discographies/_Mastered_Cleaned/Kendrick_Master_Discography_Cleaned.txt"

# Loop Thru Discography of Artist into a Master Word List
#
# with open(path, 'r') as f:
#     contents = json.load(f)["Discography"]
#     all_words = []
#     for each in contents:
#         for words in each["lyrics"].split():
#             all_words.append(words.lower())
    
# Remove stop words
#
# reduced = [word for word in all_words if word not in staph]

# P