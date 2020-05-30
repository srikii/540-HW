'''python program to return the number of unique senders in a file
    author : srikanth'''


def file_operation(file):
    try:
        fhand = open(file)
    except FileNotFoundError:
        print("file not found")
        exit()
    s = set()
    count = 0
    for line in fhand:
        line = line.strip()
        if line.startswith('From:'):
            l = line[5:]
            if '@' and '.' in l:
                s.add(l)
            else:
                continue
            count += 1
    
    print("total number of emails sent: ", count)
    return s


def main():
    file = input("enter file path: ")
    x = file_operation(file)
    #print("the unique senders are: ", x)
    print("total number of unique senders: ", len(x))


if __name__ == '__main__':
    main()