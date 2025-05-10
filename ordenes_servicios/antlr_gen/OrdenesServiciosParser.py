# Generated from OrdenesServicios.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5-\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\4\3\2")
        buf.write("\b\13\3\2\16\17\2\66\2\27\3\2\2\2\4 \3\2\2\2\6\"\3\2\2")
        buf.write("\2\b%\3\2\2\2\n.\3\2\2\2\f\63\3\2\2\2\16\65\3\2\2\2\20")
        buf.write("\67\3\2\2\2\22\23\5\4\3\2\23\24\7\20\2\2\24\26\3\2\2\2")
        buf.write("\25\22\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2")
        buf.write("\2\30\32\3\2\2\2\31\27\3\2\2\2\32\33\7\2\2\3\33\3\3\2")
        buf.write("\2\2\34!\5\6\4\2\35!\5\b\5\2\36!\5\n\6\2\37!\5\f\7\2 ")
        buf.write("\34\3\2\2\2 \35\3\2\2\2 \36\3\2\2\2 \37\3\2\2\2!\5\3\2")
        buf.write("\2\2\"#\7\3\2\2#$\7\16\2\2$\7\3\2\2\2%&\7\4\2\2&\'\7\5")
        buf.write("\2\2\'(\7\16\2\2()\7\f\2\2),\5\20\t\2*+\7\r\2\2+-\5\b")
        buf.write("\5\2,*\3\2\2\2,-\3\2\2\2-\t\3\2\2\2./\7\6\2\2/\60\5\16")
        buf.write("\b\2\60\61\7\5\2\2\61\62\7\16\2\2\62\13\3\2\2\2\63\64")
        buf.write("\7\7\2\2\64\r\3\2\2\2\65\66\t\2\2\2\66\17\3\2\2\2\678")
        buf.write("\t\3\2\28\21\3\2\2\2\5\27 ,")
        return buf.getvalue()


class OrdenesServiciosParser ( Parser ):

    grammarFileName = "OrdenesServicios.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "'filter'", "'column'", "'aggregate'", 
                     "'print'", "'count'", "'sum'", "'average'", "'between'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "LOAD", "FILTER", "COLUMN", "AGGREGATE", 
                      "PRINT", "COUNT", "SUM", "AVERAGE", "BETWEEN", "OPERATOR", 
                      "LOGIC_OP", "STRING", "NUMBER", "FIN_INSTRUCCION", 
                      "WS" ]

    RULE_script = 0
    RULE_command = 1
    RULE_loadCmd = 2
    RULE_filterCmd = 3
    RULE_aggregateCmd = 4
    RULE_printCmd = 5
    RULE_aggFunc = 6
    RULE_value = 7

    ruleNames =  [ "script", "command", "loadCmd", "filterCmd", "aggregateCmd", 
                   "printCmd", "aggFunc", "value" ]

    EOF = Token.EOF
    LOAD=1
    FILTER=2
    COLUMN=3
    AGGREGATE=4
    PRINT=5
    COUNT=6
    SUM=7
    AVERAGE=8
    BETWEEN=9
    OPERATOR=10
    LOGIC_OP=11
    STRING=12
    NUMBER=13
    FIN_INSTRUCCION=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(OrdenesServiciosParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OrdenesServiciosParser.CommandContext)
            else:
                return self.getTypedRuleContext(OrdenesServiciosParser.CommandContext,i)


        def FIN_INSTRUCCION(self, i:int=None):
            if i is None:
                return self.getTokens(OrdenesServiciosParser.FIN_INSTRUCCION)
            else:
                return self.getToken(OrdenesServiciosParser.FIN_INSTRUCCION, i)

        def getRuleIndex(self):
            return OrdenesServiciosParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = OrdenesServiciosParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OrdenesServiciosParser.LOAD) | (1 << OrdenesServiciosParser.FILTER) | (1 << OrdenesServiciosParser.AGGREGATE) | (1 << OrdenesServiciosParser.PRINT))) != 0):
                self.state = 16
                self.command()
                self.state = 17
                self.match(OrdenesServiciosParser.FIN_INSTRUCCION)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(OrdenesServiciosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadCmd(self):
            return self.getTypedRuleContext(OrdenesServiciosParser.LoadCmdContext,0)


        def filterCmd(self):
            return self.getTypedRuleContext(OrdenesServiciosParser.FilterCmdContext,0)


        def aggregateCmd(self):
            return self.getTypedRuleContext(OrdenesServiciosParser.AggregateCmdContext,0)


        def printCmd(self):
            return self.getTypedRuleContext(OrdenesServiciosParser.PrintCmdContext,0)


        def getRuleIndex(self):
            return OrdenesServiciosParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = OrdenesServiciosParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OrdenesServiciosParser.LOAD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.loadCmd()
                pass
            elif token in [OrdenesServiciosParser.FILTER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.filterCmd()
                pass
            elif token in [OrdenesServiciosParser.AGGREGATE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.aggregateCmd()
                pass
            elif token in [OrdenesServiciosParser.PRINT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.printCmd()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(OrdenesServiciosParser.LOAD, 0)

        def STRING(self):
            return self.getToken(OrdenesServiciosParser.STRING, 0)

        def getRuleIndex(self):
            return OrdenesServiciosParser.RULE_loadCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadCmd" ):
                listener.enterLoadCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadCmd" ):
                listener.exitLoadCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadCmd" ):
                return visitor.visitLoadCmd(self)
            else:
                return visitor.visitChildren(self)




    def loadCmd(self):

        localctx = OrdenesServiciosParser.LoadCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(OrdenesServiciosParser.LOAD)
            self.state = 33
            self.match(OrdenesServiciosParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(OrdenesServiciosParser.FILTER, 0)

        def COLUMN(self):
            return self.getToken(OrdenesServiciosParser.COLUMN, 0)

        def STRING(self):
            return self.getToken(OrdenesServiciosParser.STRING, 0)

        def OPERATOR(self):
            return self.getToken(OrdenesServiciosParser.OPERATOR, 0)

        def value(self):
            return self.getTypedRuleContext(OrdenesServiciosParser.ValueContext,0)


        def LOGIC_OP(self):
            return self.getToken(OrdenesServiciosParser.LOGIC_OP, 0)

        def filterCmd(self):
            return self.getTypedRuleContext(OrdenesServiciosParser.FilterCmdContext,0)


        def getRuleIndex(self):
            return OrdenesServiciosParser.RULE_filterCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterCmd" ):
                listener.enterFilterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterCmd" ):
                listener.exitFilterCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterCmd" ):
                return visitor.visitFilterCmd(self)
            else:
                return visitor.visitChildren(self)




    def filterCmd(self):

        localctx = OrdenesServiciosParser.FilterCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterCmd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(OrdenesServiciosParser.FILTER)
            self.state = 36
            self.match(OrdenesServiciosParser.COLUMN)
            self.state = 37
            self.match(OrdenesServiciosParser.STRING)
            self.state = 38
            self.match(OrdenesServiciosParser.OPERATOR)
            self.state = 39
            self.value()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OrdenesServiciosParser.LOGIC_OP:
                self.state = 40
                self.match(OrdenesServiciosParser.LOGIC_OP)
                self.state = 41
                self.filterCmd()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGREGATE(self):
            return self.getToken(OrdenesServiciosParser.AGGREGATE, 0)

        def aggFunc(self):
            return self.getTypedRuleContext(OrdenesServiciosParser.AggFuncContext,0)


        def COLUMN(self):
            return self.getToken(OrdenesServiciosParser.COLUMN, 0)

        def STRING(self):
            return self.getToken(OrdenesServiciosParser.STRING, 0)

        def getRuleIndex(self):
            return OrdenesServiciosParser.RULE_aggregateCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateCmd" ):
                listener.enterAggregateCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateCmd" ):
                listener.exitAggregateCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateCmd" ):
                return visitor.visitAggregateCmd(self)
            else:
                return visitor.visitChildren(self)




    def aggregateCmd(self):

        localctx = OrdenesServiciosParser.AggregateCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aggregateCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(OrdenesServiciosParser.AGGREGATE)
            self.state = 45
            self.aggFunc()
            self.state = 46
            self.match(OrdenesServiciosParser.COLUMN)
            self.state = 47
            self.match(OrdenesServiciosParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(OrdenesServiciosParser.PRINT, 0)

        def getRuleIndex(self):
            return OrdenesServiciosParser.RULE_printCmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintCmd" ):
                listener.enterPrintCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintCmd" ):
                listener.exitPrintCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintCmd" ):
                return visitor.visitPrintCmd(self)
            else:
                return visitor.visitChildren(self)




    def printCmd(self):

        localctx = OrdenesServiciosParser.PrintCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(OrdenesServiciosParser.PRINT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COUNT(self):
            return self.getToken(OrdenesServiciosParser.COUNT, 0)

        def SUM(self):
            return self.getToken(OrdenesServiciosParser.SUM, 0)

        def AVERAGE(self):
            return self.getToken(OrdenesServiciosParser.AVERAGE, 0)

        def BETWEEN(self):
            return self.getToken(OrdenesServiciosParser.BETWEEN, 0)

        def getRuleIndex(self):
            return OrdenesServiciosParser.RULE_aggFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggFunc" ):
                listener.enterAggFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggFunc" ):
                listener.exitAggFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggFunc" ):
                return visitor.visitAggFunc(self)
            else:
                return visitor.visitChildren(self)




    def aggFunc(self):

        localctx = OrdenesServiciosParser.AggFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_aggFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OrdenesServiciosParser.COUNT) | (1 << OrdenesServiciosParser.SUM) | (1 << OrdenesServiciosParser.AVERAGE) | (1 << OrdenesServiciosParser.BETWEEN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(OrdenesServiciosParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(OrdenesServiciosParser.STRING, 0)

        def getRuleIndex(self):
            return OrdenesServiciosParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = OrdenesServiciosParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            _la = self._input.LA(1)
            if not(_la==OrdenesServiciosParser.STRING or _la==OrdenesServiciosParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





