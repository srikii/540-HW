"""python program to read the words in file
    author:srikanth"""

from collections import defaultdict
from string import punctuation
from collections import Counter
from operator import itemgetter


def book_words(file):

    f = open(file, 'r', encoding="utf-8")
    dd = defaultdict(int)
    letters=defaultdict(int)
    res=Counter()
    char=0
    for line in f:    
        char =char + len(line)
        for char2 in line.lower():
            letters[char2] +=1
            res += Counter(char2)
        for word in line.split():
            word = word.lower()
            punc_translator = str.maketrans({key: None for key in punctuation})
            cleanString = word.translate(punc_translator)
            dd[cleanString] += 1
    print("characters in the file using counter\n" ,res)

    c= sorted(letters.items(), key=itemgetter(1), reverse=True)
    print("\ncharacters in the file using defaultdict: \n",c)

    print("\nnumber of characters in the file is: ",char)
    
    s = sorted(dd.items(), key=itemgetter(1), reverse=True)
    print("\ntop 25 words and number of its occurance are: ")
    for i in range(0, 25):
        print(s[i])

    print("\nnumber of distinct words are: ", len(dd))
    print("\nnumber of words are", sum(dd.values()),"\n\n")
    return 


def main():
    #file = "D:\\college\\test\\p9.txt"
    file = input("enter file path: ")
    try:
        book_words(file)
    except IndexError:
        print("less than 25 unique words in the file")
    except FileNotFoundError:
        print("file not found")


if __name__ == '__main__':
    main()
