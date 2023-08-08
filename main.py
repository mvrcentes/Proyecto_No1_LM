import lex_definitions as lexer
import yacc_definitions as parser

# Prueba del analizador léxico y sintáctico
entrada = '((p=>q)^p)'

lexer.lexer.input(entrada)
for tok in lexer.lexer:
    print(tok)

resultado = parser.parser.parse(entrada)
print(resultado)
