print("First we will look at The Great Gatsby")
from urllib.request import urlopen

url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"

local_name = "greatgatsby.txt"
import certifi
import ssl


def save_locally():
    with open(local_name, "w") as local_fp:
        with urlopen(url, context=ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)


#get the number of unique words
punctuation = ",;.!-()?"
def get_unique_words():
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            #remove punctuation
            for p in punctuation:
                 line = line.replace(p, " ")
            line = line.lower()
            #get the words:
            for word in line.split():
                unique_words [word] = unique_words.get(word, 0) + 1

    return unique_words

save_locally()
unique_words = get_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse = True)
print(most_frequent)
for word in most_frequent[:10]:
    for unique_word, value in unique_words.items():
        if word == value:
            print(f"common words {unique_word} appears {value} times")
            break

unique_word_count = len(unique_words)
print("The number of unique words in The Great Gatsby is: " + str(unique_word_count))

print("Next, we will look at Pride and Prejudice")
from urllib.request import urlopen

url1 = "https://www.gutenberg.org/files/1342/1342-0.txt"

local_name1 = "prideandprejudice.txt"
import certifi
import ssl


def save_locally1():
    with open(local_name1, "w") as local_fp:
        with urlopen(url1, context=ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)


#get the number of unique words
punctuation = ",;.!-()?"
def get_unique_words1():
    unique_words1 = {}
    with open(local_name1) as fp:
        for line in fp:
            #remove punctuation
            for p in punctuation:
                 line = line.replace(p, " ")
            line = line.lower()
            #get the words:
            for word in line.split():
                unique_words1 [word] = unique_words1.get(word, 0) + 1

    return unique_words1

save_locally1()
unique_words1 = get_unique_words1()
most_frequent1 = list(unique_words1.values())
most_frequent1.sort(reverse = True)
print(most_frequent1)
for word in most_frequent1[:10]:
    for unique_word1, value in unique_words1.items():
        if word == value:
            print(f"common words {unique_word1} appears {value} times")
            break

unique_word_count1 = len(unique_words1)
print("The number of unique words in Pride and Prejudice is: " + str(unique_word_count1))

if unique_word_count > unique_word_count1:
    print("The Great Gatsby has more distinct words than Pride and Prejudice")
elif unique_word_count < unique_word_count1:
    print("Pride and Prejudice has more distinct words than The Great Gatsby")
else:
    print("Both books have the same amount of distinct words")

#Which author has more distinct words longer than 7 characters?
#Great gatsby
#I am unsure how to do this



