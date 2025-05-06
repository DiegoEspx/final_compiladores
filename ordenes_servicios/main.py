import sys
from antlr4 import *
from antlr_gen.OrdenesServiciosLexer import OrdenesServiciosLexer
from antlr_gen.OrdenesServiciosParser import OrdenesServiciosParser
from visitor import MyVisitor

def main():
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    lexer = OrdenesServiciosLexer(input_stream)
    token_stream = CommonTokenStream(lexer)  # ✅ ESTA ES LA VARIABLE CORRECTA
    parser = OrdenesServiciosParser(token_stream)  # ✅ AQUÍ USAMOS token_stream
    tree = parser.script()

    visitor = MyVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
