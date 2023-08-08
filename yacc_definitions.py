from ply.src.ply import yacc
from lex_definitions import tokens  # Asegúrate de que tengas definidos los tokens del analizador léxico
from graphviz import Digraph


G = Digraph(format='png')


# Reglas de la gramática
def p_formula_variable(p):
    '''formula : VARIABLE'''
    p[0] = p[1]

def p_formula_negation(p):
    '''formula : NEGATION formula'''
    p[0] = ('~', p[2])

def p_formula_binary(p):
    '''formula : formula CONJUNCTION formula
               | formula DISJUNCTION formula
               | formula IMPLICATION formula
               | formula EQUIVALENCE formula'''
    p[0] = (p[2], p[1], p[3])

def p_formula_parentheses(p):
    '''formula : LPAREN formula RPAREN'''
    p[0] = p[2]

def p_formula_constant(p):
    '''formula : ZERO
               | ONE'''
    p[0] = p[1]

# Manejo de errores sintácticos
def p_error(p):
    print("Error de sintaxis en la entrada:", p)

# Construir el analizador sintáctico
parser = yacc.yacc()

def build_tree(p, parent_node=None):
    node_id = str(id(p))

    if isinstance(p, tuple):  # Comprobar si p es una tupla (nodo interno)
        # Agregar nodo al grafo
        G.node(node_id, label=str(p[0]))  # El primer elemento de la tupla es el operador

        if parent_node is not None:
            G.edge(parent_node, node_id)

        for i in range(1, len(p)):
            build_tree(p[i], node_id)
    else:  # Si p es una cadena (hoja)
        G.node(node_id, label=p)

        if parent_node is not None:
            G.edge(parent_node, node_id)

# Prueba del analizador sintáctico y construcción del grafo
entrada = '((p=>q)^p)'
resultado = parser.parse(entrada)
build_tree(resultado)

# Guardar el grafo en un archivo y mostrarlo
output_file = "syntax_tree"
G.render(output_file, view=True)