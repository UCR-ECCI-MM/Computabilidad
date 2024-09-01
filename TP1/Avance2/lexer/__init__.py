import ply.lex as lex


# LEXER for XML file of MedilinePlus (https://medlineplus.gov/)
# ------------------------------------------------------------
# This module allow tokenize the data provinient of a XML  file of MedlinePlus
 # ------------------------------------------------------------
import ply.lex as lex

# List of token names
tokens = (
    # XML Header
    'TAG_XML',
    'XML_TAG_CLOSURE',
    'ATTRIBUTE_VERSION',
    'ATTRIBUTE_ENCODING',
    # DOCTYPE tag
    'TAG_DOCTYPE',
    # Health-topics tag
    'TAG_HEALTH_TOPICS',
    'ATTRIBUTE_TOTAL',
    'ATTRIBUTE_DATE_GENERATED',
    # Health-topic tag
    'TAG_HEALTH_TOPIC',
    'TAG_HEALTH_TOPIC_CLOSURE',
    'ATTRIBUTE_ID', 
    'ATTRIBUTE_DATE_CREATED',
    'ATTRIBUTE_LANGUAGE',
    'ATTRIBUTE_META_DESC',
    'ATTRIBUTE_URL', 
    'ATTRIBUTE_TITLE',
    # Tags under <health-topic>
    'TAG_LANGUAGE_MAPPED_TOPIC',
    'TAG_LANGUAGE_MAPPED_TOPIC_CLOSURE',
    'TAG_ALSO_CALLED',
    'TAG_ALSO_CALLED_CLOSURE',

    # '>' token
    'TAG_CLOSURE',

    # Tokens corresponding to texts
    'TEXT_OF_ATTRIBUTE',
    'TEXT_OF_TAG',

)
 
# Regular expression rules for simple tokens:
# XML Header
t_TAG_XML = r'<\?xml'
t_XML_TAG_CLOSURE = r'\?>'
# DOCTYPE tag
# Note: we don't use this tag in the application, so we just create one token that will be discarted later
t_TAG_DOCTYPE = r'<\!DOCTYPE [^>]*>'
# Health-topics tag
t_TAG_HEALTH_TOPICS = r'<health-topics'
# Health-topic tag
t_TAG_HEALTH_TOPIC = r'<health-topic'
t_TAG_HEALTH_TOPIC_CLOSURE = r'</health-topic'
# Tags under <health-topic>
# Also-called tag
t_TAG_ALSO_CALLED = r'<also-called>'
t_TAG_ALSO_CALLED_CLOSURE = r'</also-called>'
# TAG closure: this token must be used when a tag had attributes that were extracted as tokens.
t_TAG_CLOSURE = '>'
# The following regular expressions are used to capture text
t_TEXT_OF_ATTRIBUTE = r'"[^"]*"' # capture text enclosed in double quotes but not including text with double inner quotation marks.
t_TEXT_OF_TAG = r'[^<>\?"]+' # capture text that does not contain '<', '>', '"', '=' or '?'.
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
# language-mapped-topic tag
t_TAG_LANGUAGE_MAPPED_TOPIC = r'<language-mapped-topic'
t_TAG_LANGUAGE_MAPPED_TOPIC_CLOSURE = r'</language-mapped-topic'

# Tokens defined by functions:
# ATTRIBUTES
# IMPORTANT: Attributes are defined as functions so that their regular expressions are called before TEXT_OF_TAG.
# XML Header
def t_ATTRIBUTE_VERSION(t):
    r'version='
    return t

def t_ATTRIBUTE_ENCODING(t):
    r'encoding='
    return t

# Health-topics tag
def t_ATTRIBUTE_TOTAL(t):
    r'total='
    return t

def t_ATTRIBUTE_DATE_GENERATED(t):
    r'date-generated='
    return t
 
# Health-topic tag
def t_ATTRIBUTE_ID(t):
    r'id='
    return t

def t_ATTRIBUTE_DATE_CREATED(t):
    r'date-created='
    return t

def t_ATTRIBUTE_LANGUAGE(t):
    r'language='
    return t

def t_ATTRIBUTE_META_DESC(t):
    r'meta-desc='
    return t

def t_ATTRIBUTE_URL(t): 
    r'url='
    return t

def t_ATTRIBUTE_TITLE(t):
    r'title='
    return t
 
# Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
 
# Tokenize the input string and print each token
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