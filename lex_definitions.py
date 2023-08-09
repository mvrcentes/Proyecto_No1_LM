from ply.src.ply import lex

# tokens = ('NEGATION',
#           'CONJUNCTION',
#           'DISJUNCTION',
#           'IMPLICATION',
#           'BICONDITIONAL',
#           'LPAREN',
#           'RPAREN',
#           'VARIABLE',
#           'CONSTANT')

# Definicion de Tokens
tokens = ('NEGATION',
          'CONJUNCTION',
          'DISJUNCTION',
          'IMPLICATION',
          'BICONDITIONAL',
          'LPAREN',
          'RPAREN',
          'VARIABLE',
          'CONSTANT')


# Definicion de Tokens
# t_ignore = ' \t'
# t_NEGATION = r'\~'
# t_CONJUNCTION = r'\^'
# t_DISJUNCTION = r'o'
# t_IMPLICATION = r'→'
# t_BICONDITIONAL = r'↔'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_VARIABLE = r'[pqrstuvwxyz]'
# t_CONSTANT = r'[01]'

# -----------------------------------------------------------
# t_IGNORE = r' \t'  # Cambiado para simplificar
t_NEGATION = r'\~'
t_CONJUNCTION = r'\^'
t_DISJUNCTION = r'o'
t_IMPLICATION = r'=>'
t_BICONDITIONAL = r'<=>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_VARIABLE = r'[p-zP-Z]'  # Cambiado para incluir todas las letras
t_CONSTANT = r'[01]'

# -----------------------------------------------------------

def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

precedence = (
    ('left', 'IMPLICATION', 'BICONDITIONAL'),
    ('left', 'DISJUNCTION'),
    ('left', 'CONJUNCTION'),
    ('left', 'NEGATION')
)

lexer = lex.lex()