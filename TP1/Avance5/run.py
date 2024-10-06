"""
This is the starting point for the whole program.
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=3000, debug=False)


# The following code correspond to the main() of lexer-parser program:
"""
------------------------------------------------------------
This module is the starting point of the whole application.
------------------------------------------------------------
"""
"""
from parser import parser
from parser import xml_dict

def main():
    " Main procedure. Load XML file and call the tokenizer. "
    #with open("data/mediplus_example.xml", "r", encoding='utf-8') as file:
    with open("data/mplus_topics_2024-08-10(2).xml", "r", encoding='utf-8') as file:
        data = file.read()
        parser.parse(data)
    print(xml_dict)

if __name__ == "__main__":
    main()
"""
