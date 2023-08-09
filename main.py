from ply.src.ply import yacc
from graphviz import Digraph
from lex_definitions import lexer
from yaac_definitions import parser, plot_tree

def main():
    entrada = '((p=>q)^p)'
    
    lexer.input(entrada)
    for tok in lexer:
        print(tok)
    
    resultado = parser.parse(entrada)
    tree_graph = plot_tree(resultado)
    tree_graph.view(filename="syntax_tree.png")

if __name__ == "__main__":
    main()
