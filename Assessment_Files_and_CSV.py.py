# 1)The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
#Find the total number of characters in the file and save to the variable num.

fileref = open("travel_plans.txt", "r")
contents = fileref.read()
num = len(contents)
print(num)
fileref.close()


# 2)We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
#Find the total number of words in the file and assign this value to the variable num_words.

num_words = 0
fileref = "emotion_words.txt"

with open(fileref, 'r') as file:
    for line in file:
        num_words += len(line.split())

print("number of words : ", num_words)


# 3)Assign to the variable num_lines the number of lines in the file school_prompt.txt.

fileref = open("school_prompt.txt", "r")
lines = fileref.readlines()
num_lines = len(lines)
print(num_lines)
fileref.close()


# 4)Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

txt_file = open("school_prompt.txt", "r")
beginning_chars = txt_file.read(30)
print(beginning_chars)


# 5)Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

three = []

with open("school_prompt.txt", "r") as file:
    three = [line.split()[2] for line in file]
    print(three)


# 6)Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

file = open("emotion_words.txt","r")
line = file.readlines()
emotions = []
for words in line:
    word = words.split()
    emotions.append(word[0])
print(emotions)


# 7)Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

txt_file = open("travel_plans.txt", "r")
first_chars = txt_file.read(33)
print(first_chars)


# 8)Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, 
#then add the word to a list called p_words.

txt_file = open("school_prompt.txt", "r")
p_words = []
txt_file = txt_file.read()
wordlist = txt_file.split()

for i in wordlist:
    if 'p' in i:
        p_words.append(i)

print(p_words)
