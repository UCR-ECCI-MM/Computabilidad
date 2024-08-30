import ply.lex as lex

def proof():
    print("Hello world!")



# EXAMPLE
# TODO: Modify the code bellow
# ------------------------------------------------------------
 # calclex.py
 #
 # tokenizer for a simple expression evaluator for
 # numbers and +,-,*,/
 # ------------------------------------------------------------
import ply.lex as lex
 
# List of token names.   This is always required
tokens = (
    # XML Header
    'XML_TAG',
    'XML_CLOSURE',
    'ATTRIBUTE_VERSION',
    'ATTRIBUTE_ENCODING',
    'ATTRIBUTE_TEXT',


    # TODO: remove following tokens
    'NUMBER',
)
 
# Regular expression rules for simple tokens
# XML Header
t_XML_TAG = r'<\?xml'
t_XML_CLOSURE = r'\?>'
t_ATTRIBUTE_VERSION = r'version='
t_ATTRIBUTE_ENCODING = r'encoding='
t_ATTRIBUTE_TEXT = r'"[^"]*"' # Capture text enclosed in double quotes but not including cases with double inner quotation marks 

 
# A regular expression rule with some action code
def t_NUMBER(t):
     r'\d+'
     t.value = int(t.value)    
     return t
 
 # Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
 
def tokenize(data):
# Build the lexer
    lexer = lex.lex()

    # Give the lexer some input
    lexer.input(data)
    
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)