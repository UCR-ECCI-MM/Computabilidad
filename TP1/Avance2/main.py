from lexer import tokenize

def main():
    with open("data/mediplus_example.xml", "r", encoding='utf-8') as file:
        data = file.read()
        tokenize(data)


if __name__ == "__main__":
    main()
