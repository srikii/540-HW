'''python program to return the sender who has sent the maximum messages
    author : srikanth'''
from collections import Counter


def file_operation(file):
    try:
        fhand = open(file)
    except FileNotFoundError:
        print("file not found")
        exit()
    s = list()
    for line in fhand:
        line = line.strip()
        if line.startswith('From:'):
            l = line[5:]
            if '@' and '.' in l:
                s.append(l)
            else:
                continue

    return(Counter(s).most_common(1))


def main():
    file = input("enter file path: ")
    x = file_operation(file)
    print("the maximum messages is sent by:", x)


if __name__ == '__main__':
    main()
