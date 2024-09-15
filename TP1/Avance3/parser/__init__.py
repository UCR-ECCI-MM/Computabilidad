import ply.yacc as yacc
from lexer import tokens

def p_medi_plus_xml(t):
    'medi_plus_xml : header body TAG_HEALTH_TOPICS_CLOSURE'
    print(t[3])

def p_header(t):
    'header : header_version_encoding TAG_DOCTYPE tag_health_topics_nt'
    print(t[2])

def p_header_version_encoding(t):
    'header_version_encoding : TAG_XML ATTRIBUTE_VERSION TEXT_OF_ATTRIBUTE ATTRIBUTE_ENCODING TEXT_OF_ATTRIBUTE XML_TAG_CLOSURE'
    print(f'{t[1]} + {t[2]} + {t[3]} + {t[4]} + {t[5]} + {t[6]}')
    
def p_tag_health_topics(t):
    'tag_health_topics_nt : TAG_HEALTH_TOPICS ATTRIBUTE_TOTAL NUMBER ATTRIBUTE_DATE_GENERATED DATE TIME TAG_CLOSURE'
    print(f'{t[1]} + {t[2]} + {t[3]} + {t[4]} + {t[5]} + {t[6]} + {t[7]}')

def p_body(t):
    'body : empty'
    #'''body : tag_health_topic_nt tags_under_health_topic TAG_HEALTH_TOPIC_CLOSURE body 
     #       | empty'''

"""
DONE:
MEDI_PLUS_XML -> HEADER BODY tag-health-topics-closure
HEADER -> header-version-encoding tag-doctype TAG-HEALTH-TOPICS  
TAG-HEALTH-TOPICS -> tag-health-topics attribute-total number attribute-date-generated date time closure

WORK_IN_PROGRESS:
BODY -> TAG-HEALTH-TOPIC-NT TAGS-UNDER-HEALTH-TOPIC tag-health-topic-closure BODY | ɛ

TODO:
TAG-HEALTH-TOPIC-NT -> tag-health-topic ATTRIBUTES-HEALTH-TOPIC closure   
ATTRIBUTES-HEALTH-TOPIC -> attribute-meta-desc text-of-attribute attribute-title text-of- attribute attribute-url url-text attribute-id number attribute-language text-of-attribute attribute-date-created date
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