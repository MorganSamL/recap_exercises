from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
punctuation = ",.;:!?"
punctuation2 = ",.;:!?\"'()[]{}-*<>"

# url = "http://wikiroulette.co/"
# url = "https://en.wikipedia.org/wiki/Tyrannosaurus"
# fd = urlopen(url)


fd = open("trex.txt", "r")

longest = ""
size = 0

for line in fd:
    #  line = line.decode()
    for c in punctuation:
        line = line.replace(c, " ")
    words = line.split()
    for word in words:
        if len(word) > size:
            size = len(word)
            longest = word
print("longest words is:", longest)
fd.close()

fd = open("trex.txt", "r")
all_words = []
twice = []
amount = 0
for line in fd:
    #  line = line.decode()
    for c in punctuation2:
        line = line.replace(c, " ")
    words = line.split()
    for word in words:
        if word not in all_words:
            all_words.append(word)
        elif word not in twice:
            twice.append(word)
            amount = amount+1



            
all_words.sort()
print("all the words are", all_words)
print("distinct words", len(all_words))

print("amount of words that appear at least twice: ", amount)
# write a program that counts all the distinct words that appear at least twice in the file


