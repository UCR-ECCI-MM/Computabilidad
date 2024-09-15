"""
------------------------------------------------------------
This module is the starting point of the whole application.
------------------------------------------------------------
"""
from lexer import tokenize
from parser import parser

def main():
    """ Main procedure. Load XML file and call the tokenizer. """
    with open("data/mediplus_example.xml", "r", encoding='utf-8') as file:
        data = file.read()
        parser.parse(data)

if __name__ == "__main__":
    main()
