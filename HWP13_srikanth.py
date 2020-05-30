'''python program to return a graph of emails sent in a week
    author : srikanth'''
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import os
import sys


def file_operation(file):
    try:
        fhand = open(file)
    except FileNotFoundError:
        print("file not found")
        exit()
    dd = defaultdict(int)
    for line in fhand:
        line = line.strip()
        if line.startswith('From'):
            l = line[5:]
            if '@' and '.' in l:
                l=l.split()
                if len(l) > 1: 
                    dd[l[1]] += 1
    
    days=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    mails=list()
    for k in days:
        try:
            i=dd.pop(k)
        except KeyError:
            i=0
        mails.append(i)

    y_pos=np.arange(len(days))
    plt.bar(y_pos, mails)
    plt.xticks(y_pos, days)
    plt.title("mails sent each day")
    plt.ylabel("number of emails")
    plt.show()



def main():
    file = input("enter file path: ")
    x = file_operation(file)


if __name__ == '__main__':
    main()
