import ply.yacc as yacc
from lexer import tokens

def p_medi_plus_xml(t):
    'medi_plus_xml : header body TAG_HEALTH_TOPICS_CLOSURE'

parser = yacc.yacc()