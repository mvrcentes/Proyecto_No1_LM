from ply.src.ply import lex

# Definición de los tokens (símbolos léxicos)
tokens = [
    'VARIABLE',     # Variables proposicionales
    'NEGATION',     # Operador de negación (~)
    'CONJUNCTION',  # Operador de conjunción (^)
    'DISJUNCTION',  # Operador de disjunción (o)
    'IMPLICATION',  # Operador de implicación (=>)
    'EQUIVALENCE',  # Operador de equivalencia (<=>)
    'LPAREN',       # Paréntesis izquierdo
    'RPAREN',       # Paréntesis derecho
    'ZERO',         # Constante 0
    'ONE',          # Constante 1
]

# Expresiones regulares para los tokens
t_VARIABLE = r'[p-zP-Z]'  # Letras de p a z para variables proposicionales
t_NEGATION = r'~'
t_CONJUNCTION = r'\^'
t_DISJUNCTION = r'o'
t_IMPLICATION = r'=>'
t_EQUIVALENCE = r'<=>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ZERO = r'0'
t_ONE = r'1'

# Ignorar espacios en blanco y saltos de línea
t_ignore = ' \t\n'

# Manejo de errores léxicos
def t_error(t):
    print("Caracter no válido:", t.value[0])
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()