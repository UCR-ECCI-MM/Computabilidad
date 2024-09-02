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

    # HTML tags
    'TAG_P',
    'TAG_P_CLOSURE',
    'ATTRIBUTE_CLASS',
    'TAG_UL',
    'TAG_UL_CLOSURE',
    'TAG_LI',
    'TAG_LI_CLOSURE',
    'TAG_A',
    'TAG_A_CLOSURE',
    'ATTRIBUTE_HREF', 
    'TAG_H1_4',
    'TAG_H1_4_CLOSURE',
    'TAG_STRONG',
    'TAG_STRONG_CLOSURE',
    'TAG_TD',
    'TAG_TD_CLOSURE',
    'TAG_TR',
    'TAG_TR_CLOSURE',
    'TAG_BR',
    'TAG_I',
    'TAG_I_CLOSURE',
    'TAG_EM',
    'TAG_EM_CLOSURE',
    'TAG_B',
    'TAG_B_CLOSURE',
    'TAG_TABLE',
    'TAG_TABLE_CLOSURE',
    'ATTRIBUTE_BORDER',
    'TAG_THEAD',
    'TAG_THEAD_CLOSURE',
    'TAG_TH',
    'TAG_TH_CLOSURE',
    'ATTRIBUTE_COLSPAN',
    'TAG_TBODY',
    'TAG_TBODY_CLOSURE',
    'TAG_TOPIC',
    'TAG_TOPIC_CLOSURE',
    'ATTRIBUTE_LINKTEXT',
    'TAG_COMMENT',
    'TAG_COMMENT_CLOSURE',
    'TAG_IMAGE',
    'TAG_IMAGE_CLOSURE',
    'ATTRIBUTE_SRC',
    'TAG_STYLE',

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

"""
TEXT_OF_ATTRIBUTE matches text enclosed in double quotes,
but not including text with nested double quotes.
"""
t_TEXT_OF_ATTRIBUTE = r'"[^"]*"'

"""
TEXT_OF_TAG matches text that does not contain '<', '>', '"', '=' or '?>'.
"""
t_TEXT_OF_TAG = r'(?!\?>)[^<>"]+'


# Regular expression rules for Language mapped topic tags
t_TAG_LANGUAGE_MAPPED_TOPIC = r'<language-mapped-topic'
t_TAG_LANGUAGE_MAPPED_TOPIC_CLOSURE = r'</language-mapped-topic'

# Regular expression rules for Full summary tags
t_TAG_FULL_SUMMARY = r'<full-summary'
t_TAG_FULL_SUMMARY_CLOSURE = r'</full-summary'

# HTML's tags
t_TAG_P = r'<p'
t_TAG_P_CLOSURE = r'</p>'
t_TAG_UL = r'<ul>'
t_TAG_UL_CLOSURE = r'</ul>'
t_TAG_LI = r'<li>'
t_TAG_LI_CLOSURE = r'</li>'
t_TAG_A = r'<a'
t_TAG_A_CLOSURE = r'</a>'
t_TAG_H1_4 = r'<h[1-4]>'
t_TAG_H1_4_CLOSURE = r'</h[1-4]>'
t_TAG_STRONG =  r'<strong>'
t_TAG_STRONG_CLOSURE = r'</strong>'
t_TAG_TD = r'<td'
t_TAG_TD_CLOSURE = r'</td>'
t_TAG_TR = r'<tr'
t_TAG_TR_CLOSURE = r'</tr>'
t_TAG_BR = r'<br/>'
t_TAG_I_CLOSURE = r'<i>'
t_TAG_I = r'</i>'
t_TAG_EM = r'<em>'
t_TAG_EM_CLOSURE = r'</em>'
t_TAG_B = r'<b>'
t_TAG_B_CLOSURE = r'</b>'
t_TAG_TABLE = r'<table'
t_TAG_TABLE_CLOSURE = r'</table>'
t_TAG_THEAD = r'<thead>'
t_TAG_THEAD_CLOSURE = r'</thead>'
t_TAG_TH = r'<th'
t_TAG_TH_CLOSURE = r'</th>'
t_TAG_TBODY = r'<tbody>'
t_TAG_TBODY_CLOSURE = r'</tbody>'
t_TAG_TOPIC = r'<topic'
t_TAG_TOPIC_CLOSURE = r'</topic'
t_TAG_COMMENT = r'<!--'
t_TAG_COMMENT_CLOSURE = r'-->'
t_TAG_IMAGE = r'<img'
t_TAG_IMAGE_CLOSURE = r'/>'
t_TAG_STYLE = r'<style(.*?)</style> '


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

# HTML's tags
def t_ATTRIBUTE_CLASS(t):
    r'class='
    return t

def t_ATTRIBUTE_HREF(t):
    r'href='
    return t

def t_ATTRIBUTE_BORDER(t):
    r'border='
    return t

def t_ATTRIBUTE_COLSPAN(t):
    r'colspan='
    return t

def t_ATTRIBUTE_LINKTEXT(t):
    r'(?i)linktext='
    return t

def t_ATTRIBUTE_SRC(t):
    r'src='
    return t

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
    caracter = input("Press a Key to continue: ")
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
