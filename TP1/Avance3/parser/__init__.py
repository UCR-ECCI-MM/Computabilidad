import ply.yacc as yacc
from lexer import tokens

def p_medi_plus_xml(t):
    'medi_plus_xml : header body TAG_HEALTH_TOPICS_CLOSURE'
    print(f'[p_medi_plus_xml]: {t[3]}')

def p_header(t):
    'header : header_version_encoding TAG_DOCTYPE tag_health_topics_nt'
    print(f'[p_header]: {t[2]}')

def p_header_version_encoding(t):
    'header_version_encoding : TAG_XML ATTRIBUTE_VERSION TEXT_OF_ATTRIBUTE ATTRIBUTE_ENCODING TEXT_OF_ATTRIBUTE XML_TAG_CLOSURE'
    print(f'[p_header_version_encoding]: {t[1]} + {t[2]} + {t[3]} + {t[4]} + {t[5]} + {t[6]}')
    
def p_tag_health_topics(t):
    'tag_health_topics_nt : TAG_HEALTH_TOPICS ATTRIBUTE_TOTAL NUMBER ATTRIBUTE_DATE_GENERATED DATE TIME TAG_CLOSURE'
    print(f'[p_tag_health_topics]: {t[1]} + {t[2]} + {t[3]} + {t[4]} + {t[5]} + {t[6]} + {t[7]}')

def p_body(t):
    '''body : tag_health_topic_nt tags_under_health_topic TAG_HEALTH_TOPIC_CLOSURE body 
            | empty'''
    if(len(t) > 2):
        print(f'[p_body]: {t[3]}')

def p_health_topic_nt(t):
    'tag_health_topic_nt : TAG_HEALTH_TOPIC attributes_health_topic TAG_CLOSURE'
    print(f'[tag_health_topic_nt]: {t[1]} + {t[3]}') 

def p_attributes_health_topic(t):
    '''attributes_health_topic : ATTRIBUTE_META_DESC TEXT_OF_ATTRIBUTE ATTRIBUTE_TITLE TEXT_OF_ATTRIBUTE ATTRIBUTE_URL URL ATTRIBUTE_ID NUMBER ATTRIBUTE_LANGUAGE TEXT_OF_ATTRIBUTE ATTRIBUTE_DATE_CREATED DATE
                               | ATTRIBUTE_URL URL ATTRIBUTE_ID NUMBER ATTRIBUTE_LANGUAGE TEXT_OF_ATTRIBUTE'''
    if(len(t) == 13):
        print(f'[p_attributes_health_topic]: {t[1]} + {t[2]} + {t[3]} + {t[4]} + {t[5]} + {t[6]} + {t[7]} + {t[8]} + {t[9]} + {t[10]} + {t[11]} + {t[12]}')
    else:
        print(f'[p_attributes_health_topic]: {t[1]} + {t[2]} + {t[3]} + {t[4]} + {t[5]} + {t[6]}')

def p_tags_under_health_topic(t):
    'tags_under_health_topic : empty' 

"""
DONE:
MEDI_PLUS_XML -> HEADER BODY tag-health-topics-closure
HEADER -> header-version-encoding tag-doctype TAG-HEALTH-TOPICS  
TAG-HEALTH-TOPICS -> tag-health-topics attribute-total number attribute-date-generated date time closure
BODY -> TAG-HEALTH-TOPIC-NT TAGS-UNDER-HEALTH-TOPIC tag-health-topic-closure BODY | ɛ
TAG-HEALTH-TOPIC-NT -> tag-health-topic ATTRIBUTES-HEALTH-TOPIC closure  
ATTRIBUTES-HEALTH-TOPIC -> attribute-meta-desc text-of-attribute attribute-title text-of- attribute attribute-url url-text attribute-id number attribute-language text-of-attribute attribute-date-created date

WORK_IN_PROGRESS:
TAGS-UNDER-HEALTH-TOPIC -> TAG-ALSO-CALLED-NT TAG_LANGUAGE-MAPPED-TOPIC-NT tag-full-summary TAG-GROUP-NT TAG-SEE-REFERENCE-NT TAG-MESH-HEADING-NT TAG-RELATED-TOPIC-NT TAG-OTHER-LANGUAGE-NT TAG-PRIMARY-INSTITUTE-NT TAG-SITE-NT


TODO:
TAGS-UNDER-HEALTH-TOPIC -> TAG-ALSO-CALLED-NT TAG_LANGUAGE-MAPPED-TOPIC-NT tag-full-summary TAG-GROUP-NT TAG-SEE-REFERENCE-NT TAG-MESH-HEADING-NT TAG-RELATED-TOPIC-NT TAG-OTHER-LANGUAGE-NT TAG-PRIMARY-INSTITUTE-NT TAG-SITE-NT
TAG-ALSO-CALLED-NT -> tag-also-called text-of-tag tag-also-called-closure TAG-ALSO-CALLED-NT | ɛ
TAG_LANGUAGE-MAPPED-TOPIC-NT -> language-mapped-topic ATTRIBUTES-HEALTH-TOPIC closure text-of-tag language-mapped-topic-closure | ɛ
TAG-GROUP-NT -> tag-group attribute-id number attribute-url url-text tag-group-closure TAG-GROUP-NT | tag-group attribute-id number attribute-url url-text tag-group-closure
TAG-SEE-REFERENCE-NT -> tag-see-reference text-of-tag tag-see-reference-closure TAG-SEE-REFERENCE-NT | ɛ
TAG-MESH-HEADING-NT -> tag-mesh-heading TAG-DESCRIPTOR-NT tag-mesh-heading-closure 
TAG-DESCRIPTOR-NT -> tag-descriptor attribute-id number closure text-of-tag tag-descriptor-closure TAG-DESCRIPTOR-NT | tag-descriptor attribute-id number closure text-of-tag tag-descriptor-closure 
TAG-RELATED-TOPIC-NT -> tag-related-topic attribute-url url-text attribute-id number closure text-of-tag tag-related-topic-closure TAG-RELATED-TOPIC-NT | ɛ 
TAG-OTHER-LANGUAGE-NT -> tag-other-language attribute-vernacular-name text-of-attribute attribute-url url-text closure text-of-tag tag-other-language-closure TAG-OTHER-LANGUAGE-NT | ɛ
TAG-PRIMARY-INSTITUTE-NT -> tag-primary-institute attribute-url url-text closure text-of-tag tag-primary-institute-closure | ɛ
TAG-SITE-NT -> tag-site attribute-title text-of-attribute attribute-url url-text attribute-language-mapped-url url-text TAGS-UNDER-SITE tag-site-closure | tag-site attribute-title text-of-attribute attribute-url url-text TAGS-UNDER-SITE tag-site-closure
TAGS-UNDER-SITE -> TAG-INFORMATION-CATEGORY-NT TAG-ORGANIZATION-NT TAG-STANDARD-DESCRIPTION-NT
TAG-INFORMATION-CATEGORY-NT -> tag-information-category text-of-tag tag-information-category-closure TAG-INFORMATION-CATEGORY-NT | tag-information-category text-of-tag tag-information-category-closure
TAG-ORGANIZATION-NT -> tag-organization text-of-tag tag-organization-closure TAG-ORGANIZATION-NT | tag-organization text-of-tag tag-organization-closure | ɛ
TAG-STANDARD-DESCRIPTION-NT -> tag-standard-description text-of-tag tag-standard-description-closure TAG-STANDARD-DESCRIPTION-NT | tag-standard-description text-of-tag tag-standard-description-closure

"""
def p_empty(t):
    'empty :'
    
def p_error(t):
    print("Syntax error at '%s'" % t.value)


parser = yacc.yacc()