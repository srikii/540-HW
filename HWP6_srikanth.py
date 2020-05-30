'''python program to return the average of sum in a line starting with a particular string
    author : srikanth'''


def file_operation(file):
    try:
        fhand = open(file)
    except FileNotFoundError:
        print("file not found")
        return
    i = 0.0
    count = 0
    for line in fhand:
        line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence:'):
            try:
                l = float(line[19:])
            except ValueError:
                continue
            count += 1
            i += l
    try:
        avg = round((i/count), 4)
    except ZeroDivisionError:
        avg = 0
    return avg


def main():
    file = input("enter file name: ")
    x = file_operation(file)
    print("average is: ", x)


if __name__ == '__main__':
    main()
