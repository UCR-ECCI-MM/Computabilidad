"""
LEXER for XML file of MedilinePlus (https://medlineplus.gov/)
------------------------------------------------------------
This module allow tokenize the data provinient of a XML  file of MedlinePlus
------------------------------------------------------------
"""
from ply import lex

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
    'TAG_HEALTH_TOPICS_CLOSURE',
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
    'TAG_FULL_SUMMARY',
    'TAG_FULL_SUMMARY_CLOSURE',
    'TAG_ALSO_CALLED',
    'TAG_ALSO_CALLED_CLOSURE',
    'TAG_SEE_REFERENCE',
    'TAG_SEE_REFERENCE_CLOSURE',
    'TAG_GROUP',
    'TAG_GROUP_CLOSURE',

    # Mesh heading tags
    'TAG_MESH_HEADING',
    'TAG_MESH_HEADING_CLOSURE',
    'TAG_DESCRIPTOR',
    'TAG_DESCRIPTOR_CLOSURE',
    'TAG_QUALIFIER', 
    'TAG_QUALIFIER_CLOSURE',

    # Related topic tags
    'TAG_RELATED_TOPIC',
    'TAG_RELATED_TOPIC_CLOSURE',

    # Other language tags
    'TAG_OTHER_LANGUAGE',
    'TAG_OTHER_LANGUAGE_CLOSURE',
    'ATTRIBUTE_VERNACULAR_NAME',

    # Primary institute tags
    'TAG_PRIMARY_INSTITUTE',
    'TAG_PRIMARY_INSTITUTE_CLOSURE',

    # Site tags
    'TAG_SITE',
    'TAG_SITE_CLOSURE',
    'TAG_INFORMATION_CATEGORY',
    'TAG_INFORMATION_CATEGORY_CLOSURE',
    'TAG_ORGANIZATION',
    'TAG_ORGANIZATION_CLOSURE',
    'TAG_STANDARD_DESCRIPTION',
    'TAG_STANDARD_DESCRIPTION_CLOSURE',
    'ATTRIBUTE_LANGUAGE_MAPPED_URL',

    # '>' token
    'TAG_CLOSURE',
    
    # Token corresponding to numbers
    'NUMBER',
    
    # Token corresponding to URL
    'URL',
    
    # Tokens corresponding to date and time
    'DATE',
    'TIME',

    # Tokens corresponding to texts
    'TEXT_OF_ATTRIBUTE',
    'TEXT_OF_TAG',
)

# Regular expression rules for simple tokens:
# XML Header
t_TAG_XML = r'<\?xml'
t_XML_TAG_CLOSURE = r'\?>'

"""
TAG_DOCTYPE matches the top level tag.
Note: we don't use this tag in the application, so we just create one token that
will be discarted later.
"""
t_TAG_DOCTYPE = r'<\!DOCTYPE [^>]*>'

# Regular expression rules for Health topic and Health topics tags
t_TAG_HEALTH_TOPICS = r'<health-topics'
t_TAG_HEALTH_TOPICS_CLOSURE = r'</health-topics>'
t_TAG_HEALTH_TOPIC = r'<health-topic'
t_TAG_HEALTH_TOPIC_CLOSURE = r'</health-topic>'

# Regular expression rules for Mesh heading tags
t_TAG_MESH_HEADING = r'<mesh-heading>'
t_TAG_MESH_HEADING_CLOSURE = r'</mesh-heading>'
t_TAG_DESCRIPTOR = r'<descriptor'
t_TAG_DESCRIPTOR_CLOSURE = r'</descriptor>'
t_TAG_QUALIFIER = r'<qualifier'
t_TAG_QUALIFIER_CLOSURE = r'</qualifier>'

# Regular expression rules for Related topic tags
t_TAG_RELATED_TOPIC = r'<related-topic'
t_TAG_RELATED_TOPIC_CLOSURE = r'</related-topic>'

# Regular expression rules for Other language tags
t_TAG_OTHER_LANGUAGE = r'<other-language'
t_TAG_OTHER_LANGUAGE_CLOSURE = r'</other-language>'

# Regular expression rules for Primary institute tags
t_TAG_PRIMARY_INSTITUTE = r'<primary-institute'
t_TAG_PRIMARY_INSTITUTE_CLOSURE = r'</primary-institute>'

# Regular expression rules for Site tags
t_TAG_SITE = r'<site'
t_TAG_SITE_CLOSURE = r'</site>'
t_TAG_INFORMATION_CATEGORY = r'<information-category>'
t_TAG_INFORMATION_CATEGORY_CLOSURE = r'</information-category>'
t_TAG_ORGANIZATION = r'<organization>'
t_TAG_ORGANIZATION_CLOSURE = r'</organization>'
t_TAG_STANDARD_DESCRIPTION = r'<standard-description>'
t_TAG_STANDARD_DESCRIPTION_CLOSURE = r'</standard-description>'

"""
Tags under <health-topic>
"""
t_TAG_ALSO_CALLED = r'<also-called>'
t_TAG_ALSO_CALLED_CLOSURE = r'</also-called>'

"""
TAG_CLOSURE must be used when a tag had attributes that were extracted as
tokens.
"""
t_TAG_CLOSURE = '>'


# Regular expression rules for Language mapped topic tags
t_TAG_LANGUAGE_MAPPED_TOPIC = r'<language-mapped-topic'
t_TAG_LANGUAGE_MAPPED_TOPIC_CLOSURE = r'</language-mapped-topic'


# Regular expression rules for See reference tags
t_TAG_SEE_REFERENCE = r'<see-reference'
t_TAG_SEE_REFERENCE_CLOSURE = r'</see-reference'


# Regular expression rules for Group tags
t_TAG_GROUP = r'<group'
t_TAG_GROUP_CLOSURE = r'</group'

"""
The following are Tokens defined by functions.

IMPORTANT: Attributes are defined as functions so that their regular expressions
are called before TEXT_OF_TAG.
"""

def t_TAG_FULL_SUMMARY(t):
    r'<full-summary>([\s\S]*?)</full-summary>'
    """
    TAG_FULL_SUMMARY matches and extract text content between <full-summary> and </full-summary>.
    """
    t.value = t.value[14:-15]
    return t

def t_NUMBER(t):
    r'"\d+"'
    t.value = int(t.value[1:-1]) # remove double quotes
    return t

def t_URL(t):
    r'"(https|http)://[a-zA-Z0-9\.-]+(/[^"\s]*)?"'
    return t

def t_DATE(t):
    r'"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}["\b]'
    return t

def t_TIME(t):
    r'([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])"'
    t.value = t.value[:-1] # remove double quote
    return t

def t_ATTRIBUTE_VERSION(t):
    r'version='
    return t

def t_ATTRIBUTE_ENCODING(t):
    r'encoding='
    return t

def t_ATTRIBUTE_TOTAL(t):
    r'total='
    return t

def t_ATTRIBUTE_DATE_GENERATED(t):
    r'date-generated='
    return t

# Health-topic tag
def t_ATTRIBUTE_ID(t):
    r'(?i)id='
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

# Other language tags
def t_ATTRIBUTE_VERNACULAR_NAME(t):
    r'vernacular-name='
    return t

# Site tags
def t_ATTRIBUTE_LANGUAGE_MAPPED_URL(t):
    r'language-mapped-url='
    return t

""" NOTE: the current PLY version considers the order of the token declaration in the regex evaluation,
 even when it is a simply declaration. So, text tokens are declared last to avoid problems with
 the evaluation order. 
"""
"""
TEXT_OF_ATTRIBUTE matches text enclosed in double quotes,
but not including text with nested double quotes.
"""
t_TEXT_OF_ATTRIBUTE = r'"[^"]*"'

"""
TEXT_OF_TAG matches text that does not contain '<', '>', '"', '=' or '?>'.
"""
t_TEXT_OF_TAG = r'(?!\?>)[^<>"]+'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
"""
t_ignore matches a string containing ignored characters (spaces and tabs)
"""
t_ignore  = ' \t'

def t_error(t):
    """Error handling rule"""
    print("*****ERROR*****")
    print(f"Illegal character '{str(t.value[0])}'")
    character = input("Press a Key to continue: ")
    t.lexer.skip(1)

def tokenize(data):
    """Tokenize the input string and print each token."""
    # Build the lexer
    lexer = lex.lex()

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            # No more input
            break     
        print(tok)
        