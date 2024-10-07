import ply.yacc as yacc
from lexer import tokens

# Dictionary used to save the parsing result
xml_dict = {'total': None,
            'date_created': None, 
            'time_created': None,
            # the different health topics are store in a list
            'health_topics': []}


def p_medi_plus_xml(t):
    'medi_plus_xml : header body TAG_HEALTH_TOPICS_CLOSURE'
    xml_dict["total"] = t[1][1] # save the number of health topics in the XML
    xml_dict['date_created'] = t[1][3] # save the date of creation
    xml_dict['time_created'] = t[1][5] # save the time of creation
    

def p_header(t):
    'header : header_version_encoding TAG_DOCTYPE tag_health_topics_nt'
    t[0] = t[3]


def p_header_version_encoding(t):
    'header_version_encoding : TAG_XML ATTRIBUTE_VERSION TEXT_OF_ATTRIBUTE ATTRIBUTE_ENCODING TEXT_OF_ATTRIBUTE XML_TAG_CLOSURE'

    
def p_tag_health_topics(t):
    'tag_health_topics_nt : TAG_HEALTH_TOPICS ATTRIBUTE_TOTAL NUMBER ATTRIBUTE_DATE_GENERATED DATE TIME TAG_CLOSURE'
    # Save total and creation date/time in a tuple and send it to the higher production 
    t[0] = ("total", t[3], "date_created", t[5][1:], "time_created", t[6])


def p_body(t):
    '''body : tag_health_topic_nt tags_under_health_topic TAG_HEALTH_TOPIC_CLOSURE body 
            | empty'''
    if (len(t) > 2):
        # We use the `id` as the key for the health topic
        # The health topic is saved directly in `xml_dict`, without being sent to a higher production 
        xml_dict['health_topics'].append({'attributes' : t[1], 'tags' : t[2]})

        
def p_health_topic_nt(t):
    'tag_health_topic_nt : TAG_HEALTH_TOPIC attributes_health_topic TAG_CLOSURE'
    # save the attributes of tag <health-topic>
    t[0] = t[2]


def p_attributes_health_topic(t):
    '''attributes_health_topic : ATTRIBUTE_META_DESC TEXT_OF_ATTRIBUTE ATTRIBUTE_TITLE TEXT_OF_ATTRIBUTE ATTRIBUTE_URL URL ATTRIBUTE_ID NUMBER ATTRIBUTE_LANGUAGE TEXT_OF_ATTRIBUTE ATTRIBUTE_DATE_CREATED DATE
                               | ATTRIBUTE_URL URL ATTRIBUTE_ID NUMBER ATTRIBUTE_LANGUAGE TEXT_OF_ATTRIBUTE'''
    # save the attributes of tag <health-topic> in a dictionary
    if (len(t) == 13):
        t[0] = {t[1][:-1] : t[2][1:-1], t[3][:-1] : t[4][1:-1], t[5][:-1] : t[6][1:-1], 
                t[7][:-1] : t[8], t[9][:-1] : t[10][1:-1], t[11][:-1] : t[12][1:-1]}
    else:
        t[0] = {t[1][:-1] : t[2][1:-1], t[3][:-1] : t[4], t[5][:-1] : t[6][1:-1]}


def p_tags_under_health_topic(t):
    'tags_under_health_topic : tag_also_called_nt TAG_FULL_SUMMARY tag_group_nt tag_language_mapped_topic_nt tag_mesh_heading_nt tag_other_language_nt tag_primary_institute_nt tag_related_topic_nt tag_see_reference_nt tag_site_nt'
    t[0] = {}
    # tags are saved in a dictionary
    if (t[1] != None):
        t[0]['also-called'] = t[1]
    t[0]['group'] = t[3]
    t[0]['full-summary'] = t[2]
    if(t[4] != None):
        t[0]['language-mapped-topic'] = t[4]
    if(t[5] != None):
        t[0]['mesh-heading'] = t[5]
    if(t[6] != None):
        t[0]['other-language'] = t[6]
    if(t[7] != None):
        t[0]['primary_institute'] = t[7]
    if(t[8] != None):
        t[0]['related_topic'] = t[8]
    if(t[9] != None):
        t[0]['see_reference'] = t[9]
    t[0]['site'] = t[10]
    

def p_tag_also_called_nt(t):
    '''tag_also_called_nt : TAG_ALSO_CALLED text_of_tag_nt TAG_ALSO_CALLED_CLOSURE tag_also_called_nt
                          | empty'''
    if (len(t) > 2):
        # tags that can be repeated are stored in a list
        if (t[4] != None):
            t[0] = t[4]
            t[0].append(t[2])
        else:
            t[0] = [t[2]]
            

def p_tag_language_mapped_topic_nt(t):
    '''tag_language_mapped_topic_nt : TAG_LANGUAGE_MAPPED_TOPIC attributes_health_topic TAG_CLOSURE text_of_tag_nt TAG_LANGUAGE_MAPPED_TOPIC_CLOSURE 
                                    | empty'''
    if (len(t) > 2):
        # save attributes and tag text
        t[0] = {'attributes': t[2], 'tag-text': t[4]}


def p_tag_group_nt(t): 
    '''tag_group_nt : TAG_GROUP ATTRIBUTE_URL URL ATTRIBUTE_ID NUMBER TAG_CLOSURE text_of_tag_nt TAG_GROUP_CLOSURE tag_group_nt
                    | TAG_GROUP ATTRIBUTE_URL URL ATTRIBUTE_ID NUMBER TAG_CLOSURE text_of_tag_nt TAG_GROUP_CLOSURE'''
    # save attributes and tag text
    group_dic = {'attributes': {t[2][:-1]: t[3][1:-1], t[4][:-1]: t[5]}, 'tag-text': t[7]}
    if (len(t) == 10):
        t[0] = t[9]
        t[0].append(group_dic)
    else: 
        t[0] = [group_dic]


def p_tag_see_reference_nt(t):
    '''tag_see_reference_nt : TAG_SEE_REFERENCE text_of_tag_nt TAG_SEE_REFERENCE_CLOSURE tag_see_reference_nt
                            | empty'''
    if (len(t) > 2):
        # tags that can be repeated are stored in a list
        if (t[4] != None):
            t[0] = t[4]
            t[0].append(t[2])
        else:
            t[0] = [t[2]]


def p_tag_mesh_heading_nt(t):
    '''tag_mesh_heading_nt : TAG_MESH_HEADING tag_descriptor_nt TAG_MESH_HEADING_CLOSURE tag_mesh_heading_nt
                           | empty'''
    if (len(t)) > 2:
        if (t[4] != None):
            t[0] = t[4]
            # tags that can be repeated are stored in a list
            t[0].append(t[2])
        else:
            t[0] = [t[2]]


def p_tag_descriptor_nt(t):
    '''tag_descriptor_nt : TAG_DESCRIPTOR ATTRIBUTE_ID TEXT_OF_ATTRIBUTE TAG_CLOSURE text_of_tag_nt TAG_DESCRIPTOR_CLOSURE tag_descriptor_nt
                         | TAG_DESCRIPTOR ATTRIBUTE_ID TEXT_OF_ATTRIBUTE TAG_CLOSURE text_of_tag_nt TAG_DESCRIPTOR_CLOSURE
                         | TAG_QUALIFIER ATTRIBUTE_ID TEXT_OF_ATTRIBUTE TAG_CLOSURE text_of_tag_nt TAG_QUALIFIER_CLOSURE tag_descriptor_nt
                         | TAG_QUALIFIER ATTRIBUTE_ID TEXT_OF_ATTRIBUTE TAG_CLOSURE text_of_tag_nt TAG_QUALIFIER_CLOSURE'''
    # save attributes and tag text in a dictionary
    descriptor_dict = {'attributes': {t[2][:-1]: t[3][1:-1]}, 'tag-text': t[5]}
    if (len(t) == 8):
        t[0] = t[7]
        t[0].append(descriptor_dict)
    else:
        t[0] = [descriptor_dict]


def p_tag_related_topic_nt(t): 
    '''tag_related_topic_nt : TAG_RELATED_TOPIC ATTRIBUTE_URL URL ATTRIBUTE_ID NUMBER TAG_CLOSURE text_of_tag_nt TAG_RELATED_TOPIC_CLOSURE tag_related_topic_nt
                            | empty'''         
    # save attributes and tag text
    if (len(t) > 2): 
        related_topic_dic = {'attributes': {t[2][:-1]: t[3][1:-1], t[4][:-1]: t[5]}, 'tag-text': t[7]}
        if (t[9] != None):
            # tags that can be repeated are stored in a list
            t[0] = t[9]
            t[0].append(related_topic_dic)
        else: 
            t[0] = [related_topic_dic]


def p_tag_other_language_nt(t):
    '''tag_other_language_nt : TAG_OTHER_LANGUAGE ATTRIBUTE_VERNACULAR_NAME TEXT_OF_ATTRIBUTE ATTRIBUTE_URL URL TAG_CLOSURE text_of_tag_nt TAG_OTHER_LANGUAGE_CLOSURE tag_other_language_nt
                            |  TAG_OTHER_LANGUAGE ATTRIBUTE_VERNACULAR_NAME TEXT_OF_ATTRIBUTE ATTRIBUTE_URL TEXT_OF_ATTRIBUTE TAG_CLOSURE text_of_tag_nt TAG_OTHER_LANGUAGE_CLOSURE tag_other_language_nt 
                            | empty'''
    if(len(t) > 2): 
        language_dic = {'attributes': {t[2][:-1]: t[3][1:-1], t[4][:-1]: t[5]}, 'tag-text': t[7]}
        if (t[9] != None):
            t[0] = t[9]
            # tags that can be repeated are stored in a list
            t[0].append(language_dic)
        else:
            t[0] = [language_dic]


def p_tag_primary_institute_nt(t): 
    '''tag_primary_institute_nt :  TAG_PRIMARY_INSTITUTE ATTRIBUTE_URL URL TAG_CLOSURE text_of_tag_nt TAG_PRIMARY_INSTITUTE_CLOSURE
                                | empty'''
    if(len(t) > 2):
        t[0] = {'attributes': {t[2][:-1]: t[3][1:-1]}, 'tag-text': t[5]}

        
def p_tag_site_nt(t):
    '''tag_site_nt : TAG_SITE ATTRIBUTE_TITLE TEXT_OF_ATTRIBUTE ATTRIBUTE_URL URL ATTRIBUTE_LANGUAGE_MAPPED_URL URL TAG_CLOSURE tags_under_site TAG_SITE_CLOSURE tag_site_nt
                   | TAG_SITE ATTRIBUTE_TITLE TEXT_OF_ATTRIBUTE ATTRIBUTE_URL URL ATTRIBUTE_LANGUAGE_MAPPED_URL URL TAG_CLOSURE tags_under_site TAG_SITE_CLOSURE
                   | TAG_SITE ATTRIBUTE_TITLE TEXT_OF_ATTRIBUTE ATTRIBUTE_URL URL TAG_CLOSURE tags_under_site TAG_SITE_CLOSURE tag_site_nt 
                   | TAG_SITE ATTRIBUTE_TITLE TEXT_OF_ATTRIBUTE ATTRIBUTE_URL URL TAG_CLOSURE tags_under_site TAG_SITE_CLOSURE'''
    len_t = len(t)
    if (len_t == 12):
        t[0] = t[11]
        t[0].append({'attributes': {t[2][:-1]: t[3][1:-1], t[4][:-1]: t[5][1:-1], t[6][:-1]: t[7][1:-1]}, 
                      'tags': t[9]})
    elif (len_t == 11):
        t[0] = [{'attributes': {t[2][:-1]: t[3][1:-1], t[4][:-1]: t[5][1:-1], t[6][:-1]: t[7][1:-1]}, 
                      'tags': t[9]}]
    elif (len_t == 10):
        t[0] = t[9]
        t[0].append({'attributes': {t[2][:-1]: t[3][1:-1], t[4][:-1]: t[5][1:-1]}, 
                      'tags': t[7]})
    else:
        t[0] = [{'attributes': {t[2][:-1]: t[3][1:-1], t[4][:-1]: t[5][1:-1]}, 
                      'tags': t[7]}]
        

def p_tags_under_site(t):
    'tags_under_site : tag_information_category_nt tag_organization_nt tag_standard_description_nt'
    t[0] = {}
    if (t[1] != None):
        t[0]['information-category'] = t[1]
    if (t[2] != None):
        t[0]['organization'] = t[2]
    if (t[3] != None):
        t[0]['standard-description'] = t[3]


def p_tag_information_category_nt(t):
    '''tag_information_category_nt : TAG_INFORMATION_CATEGORY text_of_tag_nt TAG_INFORMATION_CATEGORY_CLOSURE tag_information_category_nt
                                   | empty'''
    if(len(t) > 2): 
        if (t[4] != None):
            t[0] = t[4]
            t[0].append(t[2])
        else:
            t[0] = [t[2]]
            

def p_tag_organization_nt(t):
    '''tag_organization_nt : TAG_ORGANIZATION text_of_tag_nt TAG_ORGANIZATION_CLOSURE tag_organization_nt 
                           | empty'''
    if(len(t) > 2): 
        if (t[4] != None):
            t[0] = t[4]
            t[0].append(t[2])
        else:
            t[0] = [t[2]]


def p_tag_standard_description_nt(t):
    '''tag_standard_description_nt : TAG_STANDARD_DESCRIPTION text_of_tag_nt TAG_STANDARD_DESCRIPTION_CLOSURE tag_standard_description_nt
                                   | empty'''
    if (len(t) > 2): 
        if (t[4] != None):
            t[0] = t[4]
            t[0].append(t[2])
        else:
            t[0] = [t[2]]


def p_text_of_tag_nt(t):
    '''text_of_tag_nt : TEXT_OF_TAG text_of_tag_auxiliary_nt
    '''
    # concatenate the string and send to a superior production rule
    t[0] = t[1] + t[2]


def p_text_of_tag_auxiliary_nt(t):
    '''text_of_tag_auxiliary_nt : TEXT_OF_ATTRIBUTE text_of_tag_auxiliary_nt
                                | TEXT_OF_ATTRIBUTE TEXT_OF_TAG text_of_tag_auxiliary_nt
                                | empty
    '''
    # concatenate the string and send to a superior production rule
    if (len(t) == 3):
        t[0] = t[1][1:-1] + t[2]
    elif (len(t) == 4):
        t[0] = t[1][1:-1] + t[2] + t[3]
    else:
        t[0] = ""
        

def p_empty(t):
    'empty :'

    
def p_error(t):
    # Raise an exception
    raise SyntaxError("Parser error at '%s'" % t.value)


parser = yacc.yacc()