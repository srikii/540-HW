"""python program to read the line using regular expressions 
    author: srikanth"""
import re


def expression_oper(file):
    try:
        fp = open(file, 'r')
    except FileNotFoundError:
        print("cant find file: ", file)
        exit()
    else:
        with fp:
            i = list()
            for line in fp:
                line = line.strip()
                x = re.findall('^New Revision: ([0-9.]+)', line)
                if len(x) > 0:
                    i = i+x
            num = [int(x) for x in i]
            return(num)


def main():
    #file = "D:\\college\\test\\mbo.txt"
    file = input("enter the file path: ")
    x = expression_oper(file)
    try:
        print("average: ", round((sum(x)/len(x)), 1))
        print("lines: ", len(x))
    except ZeroDivisionError:
        print("no occurance of the pattern: ")
    


if __name__ == '__main__':
    main()
