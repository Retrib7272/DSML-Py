def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    if n % 2 != 0:
        if n >= 2100:
            print("grand master")
        if n >= 1900 and n <= 2100:
            print("candidate master")
        if n >= 1600 and n <= 1900:
            print("expert")
        if n >= 1400 and n <= 1600:
            print("pupil")
        else:
            print("newbie")
    elif n % 2 == 0:
        if n >= 2100:
            print("GRAND MASTER")
        if n >= 1900 and n <= 2100:
            print("CANDIDATE MASTER")
        if n >= 1600 and n <= 1900:
            print("EXPERT")
        if n >= 1400 and n <= 1600:
            print("PUPIL")
        else:
            print("NEWBIE")

    return 0

if __name__ == '__main__':
    main()
