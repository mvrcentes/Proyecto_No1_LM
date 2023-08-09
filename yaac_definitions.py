from ply.src.ply import yacc
from lex_definitions import tokens
from graphviz import Digraph


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def plot_tree(root, graph=None):
    if graph is None:
        graph = Digraph()
        graph.node(name=str(id(root)), label=root.value)
    if root.left:
        graph.node(name=str(id(root.left)), label=root.left.value)
        graph.edge(str(id(root)), str(id(root.left)))
        plot_tree(root.left, graph)
    if root.right:
        graph.node(name=str(id(root.right)), label=root.right.value)
        graph.edge(str(id(root)), str(id(root.right)))
        plot_tree(root.right, graph)
    return graph

def p_expression_value(p):
    '''
    expression : VARIABLE
                | CONSTANT
    '''
    p[0] = Node(p[1])

def p_expression_negation(p):
    '''
    expression : NEGATION expression
    '''
    node = Node(p[1])
    node.right = p[2]
    p[0] = node

def p_factor_grouped(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2]

# def p_expression(p):
#     '''
#     expression : expression CONJUNCTION expression
#                | expression DISJUNCTION expression
#                | expression IMPLICATION expression
#                | expression BICONDITIONAL expression
#     '''
#     node = Node(p[2])
#     node.left = p[1]
#     node.right = p[3]
#     p[0] = node

#-----------------------------------------------------------

def p_expression(p):
    '''
    expression : expression CONJUNCTION expression
               | expression DISJUNCTION expression
               | expression IMPLICATION expression
               | expression BICONDITIONAL expression
    '''
    node = Node(p[2])
    node.left = p[1]
    node.right = p[3]
    p[0] = node

#-----------------------------------------------------------

def p_error(p):
    print(f'Syntax error at {p.value!r}')

# Construccion del Parser
parser = yacc.yacc()