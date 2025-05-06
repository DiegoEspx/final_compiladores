# Generated from OrdenesServicios.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OrdenesServiciosParser import OrdenesServiciosParser
else:
    from OrdenesServiciosParser import OrdenesServiciosParser

# This class defines a complete generic visitor for a parse tree produced by OrdenesServiciosParser.

class OrdenesServiciosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OrdenesServiciosParser#script.
    def visitScript(self, ctx:OrdenesServiciosParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrdenesServiciosParser#command.
    def visitCommand(self, ctx:OrdenesServiciosParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrdenesServiciosParser#loadCmd.
    def visitLoadCmd(self, ctx:OrdenesServiciosParser.LoadCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrdenesServiciosParser#filterCmd.
    def visitFilterCmd(self, ctx:OrdenesServiciosParser.FilterCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrdenesServiciosParser#aggregateCmd.
    def visitAggregateCmd(self, ctx:OrdenesServiciosParser.AggregateCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrdenesServiciosParser#printCmd.
    def visitPrintCmd(self, ctx:OrdenesServiciosParser.PrintCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrdenesServiciosParser#aggFunc.
    def visitAggFunc(self, ctx:OrdenesServiciosParser.AggFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrdenesServiciosParser#value.
    def visitValue(self, ctx:OrdenesServiciosParser.ValueContext):
        return self.visitChildren(ctx)



del OrdenesServiciosParser