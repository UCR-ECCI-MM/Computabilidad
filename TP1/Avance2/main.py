from lexer import proof, tokenize

def main():
    proof()
    # test it out
    data = '''
    3 + 4 * 10
    + -20 *2
    '''
    tokenize(data)


if __name__ == "__main__":
    main()
