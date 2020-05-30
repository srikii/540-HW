'''python script to convert singular to plurals
    author: srikanth'''

def plural(p):      #plural function taking input as a string
    s = p.split()   #splitting string elements into different elements in the list
    new_word=[]     #empty list to store new words

    for i in s:

        if i.endswith(('ay', 'ey', 'iy', 'oy', 'uy')):
            new=i+'s'
            new_word.append(new)

        elif i.endswith('y'):
            new=i[:-1]+'ies'
            new_word.append(new)

        elif i.endswith(('o', 'ch', 's', 'sh', 'x' ,'z')):
            new=i+'es'
            new_word.append(new)

        else:
            new=i+'s'
            new_word.append(new)

    new_str = ' '.join(new_word)       #join the new list elements back to a large string
    print(new_str)


def main():

    p = input('Enter input: ')
    if p.isalpha() == True:
        plural(p)
    else:
        print("invalid input. IP must contain only alphabets ")

if __name__ == "__main__":
    main()