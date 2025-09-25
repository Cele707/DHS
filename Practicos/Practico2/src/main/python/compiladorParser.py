# Generated from /home/cele/Repositorios Git/DHS/Practicos/Practico2/src/main/python/compilador.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,316,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,80,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,94,8,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,109,8,5,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,117,8,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,3,11,142,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,13,1,13,3,13,156,8,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,176,8,
        18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,3,20,206,8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,3,22,220,8,22,1,23,1,23,1,23,1,24,1,24,1,
        24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,238,8,
        24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,3,25,255,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,3,28,273,8,28,1,29,1,
        29,1,29,1,29,1,29,3,29,280,8,29,1,30,1,30,1,30,1,30,1,30,1,30,3,
        30,288,8,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,3,32,297,8,32,1,33,
        1,33,1,33,1,33,3,33,303,8,33,1,34,1,34,1,34,1,34,1,34,3,34,310,8,
        34,1,35,1,35,1,35,1,35,1,35,0,0,36,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,0,1,1,0,3,4,319,0,72,1,0,0,0,2,79,1,0,0,0,4,93,1,0,0,0,6,95,
        1,0,0,0,8,99,1,0,0,0,10,108,1,0,0,0,12,116,1,0,0,0,14,118,1,0,0,
        0,16,120,1,0,0,0,18,125,1,0,0,0,20,131,1,0,0,0,22,141,1,0,0,0,24,
        143,1,0,0,0,26,155,1,0,0,0,28,157,1,0,0,0,30,159,1,0,0,0,32,161,
        1,0,0,0,34,163,1,0,0,0,36,175,1,0,0,0,38,177,1,0,0,0,40,205,1,0,
        0,0,42,207,1,0,0,0,44,219,1,0,0,0,46,221,1,0,0,0,48,237,1,0,0,0,
        50,254,1,0,0,0,52,256,1,0,0,0,54,263,1,0,0,0,56,272,1,0,0,0,58,279,
        1,0,0,0,60,287,1,0,0,0,62,289,1,0,0,0,64,296,1,0,0,0,66,302,1,0,
        0,0,68,309,1,0,0,0,70,311,1,0,0,0,72,73,3,2,1,0,73,74,5,0,0,1,74,
        1,1,0,0,0,75,76,3,4,2,0,76,77,3,2,1,0,77,80,1,0,0,0,78,80,1,0,0,
        0,79,75,1,0,0,0,79,78,1,0,0,0,80,3,1,0,0,0,81,94,3,16,8,0,82,94,
        3,8,4,0,83,94,3,20,10,0,84,94,3,18,9,0,85,94,3,24,12,0,86,94,3,6,
        3,0,87,94,3,70,35,0,88,94,3,52,26,0,89,94,3,54,27,0,90,91,3,62,31,
        0,91,92,5,33,0,0,92,94,1,0,0,0,93,81,1,0,0,0,93,82,1,0,0,0,93,83,
        1,0,0,0,93,84,1,0,0,0,93,85,1,0,0,0,93,86,1,0,0,0,93,87,1,0,0,0,
        93,88,1,0,0,0,93,89,1,0,0,0,93,90,1,0,0,0,94,5,1,0,0,0,95,96,5,29,
        0,0,96,97,3,2,1,0,97,98,5,30,0,0,98,7,1,0,0,0,99,100,3,14,7,0,100,
        101,5,34,0,0,101,102,3,10,5,0,102,103,3,12,6,0,103,104,5,33,0,0,
        104,9,1,0,0,0,105,106,5,15,0,0,106,109,3,32,16,0,107,109,1,0,0,0,
        108,105,1,0,0,0,108,107,1,0,0,0,109,11,1,0,0,0,110,111,5,35,0,0,
        111,112,5,34,0,0,112,113,3,10,5,0,113,114,3,12,6,0,114,117,1,0,0,
        0,115,117,1,0,0,0,116,110,1,0,0,0,116,115,1,0,0,0,117,13,1,0,0,0,
        118,119,7,0,0,0,119,15,1,0,0,0,120,121,5,34,0,0,121,122,5,15,0,0,
        122,123,3,32,16,0,123,124,5,33,0,0,124,17,1,0,0,0,125,126,5,8,0,
        0,126,127,5,27,0,0,127,128,3,32,16,0,128,129,5,28,0,0,129,130,3,
        4,2,0,130,19,1,0,0,0,131,132,5,5,0,0,132,133,5,27,0,0,133,134,3,
        32,16,0,134,135,5,28,0,0,135,136,3,4,2,0,136,137,3,22,11,0,137,21,
        1,0,0,0,138,139,5,6,0,0,139,142,3,4,2,0,140,142,1,0,0,0,141,138,
        1,0,0,0,141,140,1,0,0,0,142,23,1,0,0,0,143,144,5,7,0,0,144,145,5,
        27,0,0,145,146,3,26,13,0,146,147,5,33,0,0,147,148,3,28,14,0,148,
        149,5,33,0,0,149,150,3,30,15,0,150,151,5,28,0,0,151,152,3,4,2,0,
        152,25,1,0,0,0,153,156,3,8,4,0,154,156,3,16,8,0,155,153,1,0,0,0,
        155,154,1,0,0,0,156,27,1,0,0,0,157,158,3,32,16,0,158,29,1,0,0,0,
        159,160,3,16,8,0,160,31,1,0,0,0,161,162,3,34,17,0,162,33,1,0,0,0,
        163,164,3,38,19,0,164,165,3,36,18,0,165,35,1,0,0,0,166,167,5,23,
        0,0,167,168,3,38,19,0,168,169,3,36,18,0,169,176,1,0,0,0,170,171,
        5,22,0,0,171,172,3,38,19,0,172,173,3,36,18,0,173,176,1,0,0,0,174,
        176,1,0,0,0,175,166,1,0,0,0,175,170,1,0,0,0,175,174,1,0,0,0,176,
        37,1,0,0,0,177,178,3,42,21,0,178,179,3,40,20,0,179,39,1,0,0,0,180,
        181,5,16,0,0,181,182,3,42,21,0,182,183,3,40,20,0,183,206,1,0,0,0,
        184,185,5,17,0,0,185,186,3,42,21,0,186,187,3,40,20,0,187,206,1,0,
        0,0,188,189,5,18,0,0,189,190,3,42,21,0,190,191,3,40,20,0,191,206,
        1,0,0,0,192,193,5,19,0,0,193,194,3,42,21,0,194,195,3,40,20,0,195,
        206,1,0,0,0,196,197,5,20,0,0,197,198,3,42,21,0,198,199,3,40,20,0,
        199,206,1,0,0,0,200,201,5,21,0,0,201,202,3,42,21,0,202,203,3,40,
        20,0,203,206,1,0,0,0,204,206,1,0,0,0,205,180,1,0,0,0,205,184,1,0,
        0,0,205,188,1,0,0,0,205,192,1,0,0,0,205,196,1,0,0,0,205,200,1,0,
        0,0,205,204,1,0,0,0,206,41,1,0,0,0,207,208,3,46,23,0,208,209,3,44,
        22,0,209,43,1,0,0,0,210,211,5,10,0,0,211,212,3,46,23,0,212,213,3,
        44,22,0,213,220,1,0,0,0,214,215,5,11,0,0,215,216,3,46,23,0,216,217,
        3,44,22,0,217,220,1,0,0,0,218,220,1,0,0,0,219,210,1,0,0,0,219,214,
        1,0,0,0,219,218,1,0,0,0,220,45,1,0,0,0,221,222,3,50,25,0,222,223,
        3,48,24,0,223,47,1,0,0,0,224,225,5,12,0,0,225,226,3,50,25,0,226,
        227,3,48,24,0,227,238,1,0,0,0,228,229,5,13,0,0,229,230,3,50,25,0,
        230,231,3,48,24,0,231,238,1,0,0,0,232,233,5,14,0,0,233,234,3,50,
        25,0,234,235,3,48,24,0,235,238,1,0,0,0,236,238,1,0,0,0,237,224,1,
        0,0,0,237,228,1,0,0,0,237,232,1,0,0,0,237,236,1,0,0,0,238,49,1,0,
        0,0,239,255,5,1,0,0,240,255,3,62,31,0,241,255,5,34,0,0,242,243,5,
        27,0,0,243,244,3,34,17,0,244,245,5,28,0,0,245,255,1,0,0,0,246,247,
        5,24,0,0,247,255,3,50,25,0,248,249,5,11,0,0,249,255,3,50,25,0,250,
        251,5,25,0,0,251,255,3,50,25,0,252,253,5,26,0,0,253,255,3,50,25,
        0,254,239,1,0,0,0,254,240,1,0,0,0,254,241,1,0,0,0,254,242,1,0,0,
        0,254,246,1,0,0,0,254,248,1,0,0,0,254,250,1,0,0,0,254,252,1,0,0,
        0,255,51,1,0,0,0,256,257,3,14,7,0,257,258,5,34,0,0,258,259,5,27,
        0,0,259,260,3,56,28,0,260,261,5,28,0,0,261,262,5,33,0,0,262,53,1,
        0,0,0,263,264,3,14,7,0,264,265,5,34,0,0,265,266,5,27,0,0,266,267,
        3,56,28,0,267,268,5,28,0,0,268,269,3,6,3,0,269,55,1,0,0,0,270,273,
        3,58,29,0,271,273,1,0,0,0,272,270,1,0,0,0,272,271,1,0,0,0,273,57,
        1,0,0,0,274,275,3,14,7,0,275,276,5,34,0,0,276,277,3,60,30,0,277,
        280,1,0,0,0,278,280,1,0,0,0,279,274,1,0,0,0,279,278,1,0,0,0,280,
        59,1,0,0,0,281,282,5,35,0,0,282,283,3,14,7,0,283,284,5,34,0,0,284,
        285,3,60,30,0,285,288,1,0,0,0,286,288,1,0,0,0,287,281,1,0,0,0,287,
        286,1,0,0,0,288,61,1,0,0,0,289,290,5,34,0,0,290,291,5,27,0,0,291,
        292,3,64,32,0,292,293,5,28,0,0,293,63,1,0,0,0,294,297,3,66,33,0,
        295,297,1,0,0,0,296,294,1,0,0,0,296,295,1,0,0,0,297,65,1,0,0,0,298,
        299,3,32,16,0,299,300,3,68,34,0,300,303,1,0,0,0,301,303,1,0,0,0,
        302,298,1,0,0,0,302,301,1,0,0,0,303,67,1,0,0,0,304,305,5,35,0,0,
        305,306,3,32,16,0,306,307,3,68,34,0,307,310,1,0,0,0,308,310,1,0,
        0,0,309,304,1,0,0,0,309,308,1,0,0,0,310,69,1,0,0,0,311,312,5,9,0,
        0,312,313,3,32,16,0,313,314,5,33,0,0,314,71,1,0,0,0,17,79,93,108,
        116,141,155,175,205,219,237,254,272,279,287,296,302,309
    ]

class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'int'", "'double'", 
                     "'if'", "'else'", "'for'", "'while'", "'return'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'='", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "'!='", "'&&'", "'||'", "'!'", "'++'", 
                     "'--'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
                     "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "NUMERO", "ENTERO", "INT", "DOUBLE", 
                      "IF", "ELSE", "FOR", "WHILE", "RETURN", "SUMA", "RESTA", 
                      "MULT", "DIV", "MOD", "ASIG", "MENOR", "MAYOR", "MENOR_IGUAL", 
                      "MAYOR_IGUAL", "IGUAL", "DIFERENTE", "AND", "OR", 
                      "NOT", "INC", "DEC", "PA", "PC", "LLA", "LLC", "CA", 
                      "CC", "PYC", "ID", "COMA", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_bloque = 3
    RULE_declaracion = 4
    RULE_inicializador = 5
    RULE_listavar = 6
    RULE_tipo = 7
    RULE_asignacion = 8
    RULE_iwhile = 9
    RULE_iif = 10
    RULE_ielse = 11
    RULE_ifor = 12
    RULE_forInit = 13
    RULE_forCond = 14
    RULE_forUpdate = 15
    RULE_opalc = 16
    RULE_exp_l = 17
    RULE_exp_l_prima = 18
    RULE_exp_comp = 19
    RULE_exp_comp_prima = 20
    RULE_exp_a = 21
    RULE_exp_a_prima = 22
    RULE_term = 23
    RULE_term_prima = 24
    RULE_factor = 25
    RULE_prototipo = 26
    RULE_funcion = 27
    RULE_lista_parametros = 28
    RULE_parametros = 29
    RULE_parametros_prima = 30
    RULE_llamada_funcion = 31
    RULE_lista_argumentos = 32
    RULE_argumentos = 33
    RULE_argumentos_prima = 34
    RULE_ireturn = 35

    ruleNames =  [ "programa", "instrucciones", "instruccion", "bloque", 
                   "declaracion", "inicializador", "listavar", "tipo", "asignacion", 
                   "iwhile", "iif", "ielse", "ifor", "forInit", "forCond", 
                   "forUpdate", "opalc", "exp_l", "exp_l_prima", "exp_comp", 
                   "exp_comp_prima", "exp_a", "exp_a_prima", "term", "term_prima", 
                   "factor", "prototipo", "funcion", "lista_parametros", 
                   "parametros", "parametros_prima", "llamada_funcion", 
                   "lista_argumentos", "argumentos", "argumentos_prima", 
                   "ireturn" ]

    EOF = Token.EOF
    NUMERO=1
    ENTERO=2
    INT=3
    DOUBLE=4
    IF=5
    ELSE=6
    FOR=7
    WHILE=8
    RETURN=9
    SUMA=10
    RESTA=11
    MULT=12
    DIV=13
    MOD=14
    ASIG=15
    MENOR=16
    MAYOR=17
    MENOR_IGUAL=18
    MAYOR_IGUAL=19
    IGUAL=20
    DIFERENTE=21
    AND=22
    OR=23
    NOT=24
    INC=25
    DEC=26
    PA=27
    PC=28
    LLA=29
    LLC=30
    CA=31
    CC=32
    PYC=33
    ID=34
    COMA=35
    WS=36
    OTRO=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compiladorParser.EOF, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.instrucciones()
            self.state = 73
            self.match(compiladorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladorParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 7, 8, 9, 29, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.instruccion()
                self.state = 76
                self.instrucciones()
                pass
            elif token in [-1, 30]:
                self.enterOuterAlt(localctx, 2)

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


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladorParser.IifContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladorParser.IwhileContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladorParser.IforContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def ireturn(self):
            return self.getTypedRuleContext(compiladorParser.IreturnContext,0)


        def prototipo(self):
            return self.getTypedRuleContext(compiladorParser.PrototipoContext,0)


        def funcion(self):
            return self.getTypedRuleContext(compiladorParser.FuncionContext,0)


        def llamada_funcion(self):
            return self.getTypedRuleContext(compiladorParser.Llamada_funcionContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladorParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.declaracion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.iif()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.iwhile()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 85
                self.ifor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.bloque()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 87
                self.ireturn()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 88
                self.prototipo()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 89
                self.funcion()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 90
                self.llamada_funcion()
                self.state = 91
                self.match(compiladorParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladorParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladorParser.LLC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladorParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(compiladorParser.LLA)
            self.state = 96
            self.instrucciones()
            self.state = 97
            self.match(compiladorParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inicializador(self):
            return self.getTypedRuleContext(compiladorParser.InicializadorContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compiladorParser.ListavarContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladorParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.tipo()
            self.state = 100
            self.match(compiladorParser.ID)
            self.state = 101
            self.inicializador()
            self.state = 102
            self.listavar()
            self.state = 103
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def opalc(self):
            return self.getTypedRuleContext(compiladorParser.OpalcContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_inicializador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicializador" ):
                listener.enterInicializador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicializador" ):
                listener.exitInicializador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializador" ):
                return visitor.visitInicializador(self)
            else:
                return visitor.visitChildren(self)




    def inicializador(self):

        localctx = compiladorParser.InicializadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inicializador)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(compiladorParser.ASIG)
                self.state = 106
                self.opalc()
                pass
            elif token in [33, 35]:
                self.enterOuterAlt(localctx, 2)

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


    class ListavarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inicializador(self):
            return self.getTypedRuleContext(compiladorParser.InicializadorContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compiladorParser.ListavarContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listavar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListavar" ):
                listener.enterListavar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListavar" ):
                listener.exitListavar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListavar" ):
                return visitor.visitListavar(self)
            else:
                return visitor.visitChildren(self)




    def listavar(self):

        localctx = compiladorParser.ListavarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_listavar)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(compiladorParser.COMA)
                self.state = 111
                self.match(compiladorParser.ID)
                self.state = 112
                self.inicializador()
                self.state = 113
                self.listavar()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)

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


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladorParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladorParser.DOUBLE, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = compiladorParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def opalc(self):
            return self.getTypedRuleContext(compiladorParser.OpalcContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladorParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(compiladorParser.ID)
            self.state = 121
            self.match(compiladorParser.ASIG)
            self.state = 122
            self.opalc()
            self.state = 123
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladorParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def opalc(self):
            return self.getTypedRuleContext(compiladorParser.OpalcContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_iwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIwhile" ):
                listener.enterIwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIwhile" ):
                listener.exitIwhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIwhile" ):
                return visitor.visitIwhile(self)
            else:
                return visitor.visitChildren(self)




    def iwhile(self):

        localctx = compiladorParser.IwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(compiladorParser.WHILE)
            self.state = 126
            self.match(compiladorParser.PA)
            self.state = 127
            self.opalc()
            self.state = 128
            self.match(compiladorParser.PC)
            self.state = 129
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladorParser.IF, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def opalc(self):
            return self.getTypedRuleContext(compiladorParser.OpalcContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def ielse(self):
            return self.getTypedRuleContext(compiladorParser.IelseContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_iif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIif" ):
                listener.enterIif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIif" ):
                listener.exitIif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIif" ):
                return visitor.visitIif(self)
            else:
                return visitor.visitChildren(self)




    def iif(self):

        localctx = compiladorParser.IifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(compiladorParser.IF)
            self.state = 132
            self.match(compiladorParser.PA)
            self.state = 133
            self.opalc()
            self.state = 134
            self.match(compiladorParser.PC)
            self.state = 135
            self.instruccion()
            self.state = 136
            self.ielse()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compiladorParser.ELSE, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_ielse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIelse" ):
                listener.enterIelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIelse" ):
                listener.exitIelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIelse" ):
                return visitor.visitIelse(self)
            else:
                return visitor.visitChildren(self)




    def ielse(self):

        localctx = compiladorParser.IelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ielse)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(compiladorParser.ELSE)
                self.state = 139
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladorParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def forInit(self):
            return self.getTypedRuleContext(compiladorParser.ForInitContext,0)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.PYC)
            else:
                return self.getToken(compiladorParser.PYC, i)

        def forCond(self):
            return self.getTypedRuleContext(compiladorParser.ForCondContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(compiladorParser.ForUpdateContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_ifor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfor" ):
                listener.enterIfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfor" ):
                listener.exitIfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfor" ):
                return visitor.visitIfor(self)
            else:
                return visitor.visitChildren(self)




    def ifor(self):

        localctx = compiladorParser.IforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(compiladorParser.FOR)
            self.state = 144
            self.match(compiladorParser.PA)
            self.state = 145
            self.forInit()
            self.state = 146
            self.match(compiladorParser.PYC)
            self.state = 147
            self.forCond()
            self.state = 148
            self.match(compiladorParser.PYC)
            self.state = 149
            self.forUpdate()
            self.state = 150
            self.match(compiladorParser.PC)
            self.state = 151
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(compiladorParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = compiladorParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_forInit)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.declaracion()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.asignacion()
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


    class ForCondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opalc(self):
            return self.getTypedRuleContext(compiladorParser.OpalcContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_forCond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCond" ):
                listener.enterForCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCond" ):
                listener.exitForCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCond" ):
                return visitor.visitForCond(self)
            else:
                return visitor.visitChildren(self)




    def forCond(self):

        localctx = compiladorParser.ForCondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forCond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.opalc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(compiladorParser.AsignacionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = compiladorParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.asignacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_l(self):
            return self.getTypedRuleContext(compiladorParser.Exp_lContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_opalc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpalc" ):
                listener.enterOpalc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpalc" ):
                listener.exitOpalc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpalc" ):
                return visitor.visitOpalc(self)
            else:
                return visitor.visitChildren(self)




    def opalc(self):

        localctx = compiladorParser.OpalcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_opalc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.exp_l()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_lContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_comp(self):
            return self.getTypedRuleContext(compiladorParser.Exp_compContext,0)


        def exp_l_prima(self):
            return self.getTypedRuleContext(compiladorParser.Exp_l_primaContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_exp_l

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_l" ):
                listener.enterExp_l(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_l" ):
                listener.exitExp_l(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_l" ):
                return visitor.visitExp_l(self)
            else:
                return visitor.visitChildren(self)




    def exp_l(self):

        localctx = compiladorParser.Exp_lContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp_l)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.exp_comp()
            self.state = 164
            self.exp_l_prima()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_l_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(compiladorParser.OR, 0)

        def exp_comp(self):
            return self.getTypedRuleContext(compiladorParser.Exp_compContext,0)


        def exp_l_prima(self):
            return self.getTypedRuleContext(compiladorParser.Exp_l_primaContext,0)


        def AND(self):
            return self.getToken(compiladorParser.AND, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_exp_l_prima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_l_prima" ):
                listener.enterExp_l_prima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_l_prima" ):
                listener.exitExp_l_prima(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_l_prima" ):
                return visitor.visitExp_l_prima(self)
            else:
                return visitor.visitChildren(self)




    def exp_l_prima(self):

        localctx = compiladorParser.Exp_l_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp_l_prima)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(compiladorParser.OR)
                self.state = 167
                self.exp_comp()
                self.state = 168
                self.exp_l_prima()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(compiladorParser.AND)
                self.state = 171
                self.exp_comp()
                self.state = 172
                self.exp_l_prima()
                pass
            elif token in [28, 33, 35]:
                self.enterOuterAlt(localctx, 3)

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


    class Exp_compContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_a(self):
            return self.getTypedRuleContext(compiladorParser.Exp_aContext,0)


        def exp_comp_prima(self):
            return self.getTypedRuleContext(compiladorParser.Exp_comp_primaContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_exp_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_comp" ):
                listener.enterExp_comp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_comp" ):
                listener.exitExp_comp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_comp" ):
                return visitor.visitExp_comp(self)
            else:
                return visitor.visitChildren(self)




    def exp_comp(self):

        localctx = compiladorParser.Exp_compContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exp_comp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.exp_a()
            self.state = 178
            self.exp_comp_prima()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_comp_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOR(self):
            return self.getToken(compiladorParser.MENOR, 0)

        def exp_a(self):
            return self.getTypedRuleContext(compiladorParser.Exp_aContext,0)


        def exp_comp_prima(self):
            return self.getTypedRuleContext(compiladorParser.Exp_comp_primaContext,0)


        def MAYOR(self):
            return self.getToken(compiladorParser.MAYOR, 0)

        def MENOR_IGUAL(self):
            return self.getToken(compiladorParser.MENOR_IGUAL, 0)

        def MAYOR_IGUAL(self):
            return self.getToken(compiladorParser.MAYOR_IGUAL, 0)

        def IGUAL(self):
            return self.getToken(compiladorParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(compiladorParser.DIFERENTE, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_exp_comp_prima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_comp_prima" ):
                listener.enterExp_comp_prima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_comp_prima" ):
                listener.exitExp_comp_prima(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_comp_prima" ):
                return visitor.visitExp_comp_prima(self)
            else:
                return visitor.visitChildren(self)




    def exp_comp_prima(self):

        localctx = compiladorParser.Exp_comp_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp_comp_prima)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(compiladorParser.MENOR)
                self.state = 181
                self.exp_a()
                self.state = 182
                self.exp_comp_prima()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(compiladorParser.MAYOR)
                self.state = 185
                self.exp_a()
                self.state = 186
                self.exp_comp_prima()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.match(compiladorParser.MENOR_IGUAL)
                self.state = 189
                self.exp_a()
                self.state = 190
                self.exp_comp_prima()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 192
                self.match(compiladorParser.MAYOR_IGUAL)
                self.state = 193
                self.exp_a()
                self.state = 194
                self.exp_comp_prima()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 196
                self.match(compiladorParser.IGUAL)
                self.state = 197
                self.exp_a()
                self.state = 198
                self.exp_comp_prima()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 6)
                self.state = 200
                self.match(compiladorParser.DIFERENTE)
                self.state = 201
                self.exp_a()
                self.state = 202
                self.exp_comp_prima()
                pass
            elif token in [22, 23, 28, 33, 35]:
                self.enterOuterAlt(localctx, 7)

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


    class Exp_aContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def exp_a_prima(self):
            return self.getTypedRuleContext(compiladorParser.Exp_a_primaContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_exp_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_a" ):
                listener.enterExp_a(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_a" ):
                listener.exitExp_a(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_a" ):
                return visitor.visitExp_a(self)
            else:
                return visitor.visitChildren(self)




    def exp_a(self):

        localctx = compiladorParser.Exp_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp_a)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.term()
            self.state = 208
            self.exp_a_prima()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_a_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compiladorParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def exp_a_prima(self):
            return self.getTypedRuleContext(compiladorParser.Exp_a_primaContext,0)


        def RESTA(self):
            return self.getToken(compiladorParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_exp_a_prima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_a_prima" ):
                listener.enterExp_a_prima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_a_prima" ):
                listener.exitExp_a_prima(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_a_prima" ):
                return visitor.visitExp_a_prima(self)
            else:
                return visitor.visitChildren(self)




    def exp_a_prima(self):

        localctx = compiladorParser.Exp_a_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp_a_prima)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(compiladorParser.SUMA)
                self.state = 211
                self.term()
                self.state = 212
                self.exp_a_prima()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.match(compiladorParser.RESTA)
                self.state = 215
                self.term()
                self.state = 216
                self.exp_a_prima()
                pass
            elif token in [16, 17, 18, 19, 20, 21, 22, 23, 28, 33, 35]:
                self.enterOuterAlt(localctx, 3)

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


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def term_prima(self):
            return self.getTypedRuleContext(compiladorParser.Term_primaContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.factor()
            self.state = 222
            self.term_prima()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladorParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def term_prima(self):
            return self.getTypedRuleContext(compiladorParser.Term_primaContext,0)


        def DIV(self):
            return self.getToken(compiladorParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladorParser.MOD, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_term_prima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_prima" ):
                listener.enterTerm_prima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_prima" ):
                listener.exitTerm_prima(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_prima" ):
                return visitor.visitTerm_prima(self)
            else:
                return visitor.visitChildren(self)




    def term_prima(self):

        localctx = compiladorParser.Term_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_term_prima)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(compiladorParser.MULT)
                self.state = 225
                self.factor()
                self.state = 226
                self.term_prima()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(compiladorParser.DIV)
                self.state = 229
                self.factor()
                self.state = 230
                self.term_prima()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.match(compiladorParser.MOD)
                self.state = 233
                self.factor()
                self.state = 234
                self.term_prima()
                pass
            elif token in [10, 11, 16, 17, 18, 19, 20, 21, 22, 23, 28, 33, 35]:
                self.enterOuterAlt(localctx, 4)

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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladorParser.NUMERO, 0)

        def llamada_funcion(self):
            return self.getTypedRuleContext(compiladorParser.Llamada_funcionContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def exp_l(self):
            return self.getTypedRuleContext(compiladorParser.Exp_lContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def NOT(self):
            return self.getToken(compiladorParser.NOT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def RESTA(self):
            return self.getToken(compiladorParser.RESTA, 0)

        def INC(self):
            return self.getToken(compiladorParser.INC, 0)

        def DEC(self):
            return self.getToken(compiladorParser.DEC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(compiladorParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.llamada_funcion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.match(compiladorParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 242
                self.match(compiladorParser.PA)
                self.state = 243
                self.exp_l()
                self.state = 244
                self.match(compiladorParser.PC)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 246
                self.match(compiladorParser.NOT)
                self.state = 247
                self.factor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 248
                self.match(compiladorParser.RESTA)
                self.state = 249
                self.factor()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 250
                self.match(compiladorParser.INC)
                self.state = 251
                self.factor()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 252
                self.match(compiladorParser.DEC)
                self.state = 253
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrototipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def lista_parametros(self):
            return self.getTypedRuleContext(compiladorParser.Lista_parametrosContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_prototipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrototipo" ):
                listener.enterPrototipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrototipo" ):
                listener.exitPrototipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototipo" ):
                return visitor.visitPrototipo(self)
            else:
                return visitor.visitChildren(self)




    def prototipo(self):

        localctx = compiladorParser.PrototipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_prototipo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.tipo()
            self.state = 257
            self.match(compiladorParser.ID)
            self.state = 258
            self.match(compiladorParser.PA)
            self.state = 259
            self.lista_parametros()
            self.state = 260
            self.match(compiladorParser.PC)
            self.state = 261
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def lista_parametros(self):
            return self.getTypedRuleContext(compiladorParser.Lista_parametrosContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = compiladorParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.tipo()
            self.state = 264
            self.match(compiladorParser.ID)
            self.state = 265
            self.match(compiladorParser.PA)
            self.state = 266
            self.lista_parametros()
            self.state = 267
            self.match(compiladorParser.PC)
            self.state = 268
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_parametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametros(self):
            return self.getTypedRuleContext(compiladorParser.ParametrosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_lista_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_parametros" ):
                listener.enterLista_parametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_parametros" ):
                listener.exitLista_parametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_parametros" ):
                return visitor.visitLista_parametros(self)
            else:
                return visitor.visitChildren(self)




    def lista_parametros(self):

        localctx = compiladorParser.Lista_parametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_lista_parametros)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.parametros()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def parametros_prima(self):
            return self.getTypedRuleContext(compiladorParser.Parametros_primaContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = compiladorParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_parametros)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.tipo()
                self.state = 275
                self.match(compiladorParser.ID)
                self.state = 276
                self.parametros_prima()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)

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


    class Parametros_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def parametros_prima(self):
            return self.getTypedRuleContext(compiladorParser.Parametros_primaContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_parametros_prima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros_prima" ):
                listener.enterParametros_prima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros_prima" ):
                listener.exitParametros_prima(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros_prima" ):
                return visitor.visitParametros_prima(self)
            else:
                return visitor.visitChildren(self)




    def parametros_prima(self):

        localctx = compiladorParser.Parametros_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_parametros_prima)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(compiladorParser.COMA)
                self.state = 282
                self.tipo()
                self.state = 283
                self.match(compiladorParser.ID)
                self.state = 284
                self.parametros_prima()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)

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


    class Llamada_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def lista_argumentos(self):
            return self.getTypedRuleContext(compiladorParser.Lista_argumentosContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_llamada_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada_funcion" ):
                listener.enterLlamada_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada_funcion" ):
                listener.exitLlamada_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada_funcion" ):
                return visitor.visitLlamada_funcion(self)
            else:
                return visitor.visitChildren(self)




    def llamada_funcion(self):

        localctx = compiladorParser.Llamada_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_llamada_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(compiladorParser.ID)
            self.state = 290
            self.match(compiladorParser.PA)
            self.state = 291
            self.lista_argumentos()
            self.state = 292
            self.match(compiladorParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_argumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumentos(self):
            return self.getTypedRuleContext(compiladorParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_lista_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_argumentos" ):
                listener.enterLista_argumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_argumentos" ):
                listener.exitLista_argumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_argumentos" ):
                return visitor.visitLista_argumentos(self)
            else:
                return visitor.visitChildren(self)




    def lista_argumentos(self):

        localctx = compiladorParser.Lista_argumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_lista_argumentos)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.argumentos()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opalc(self):
            return self.getTypedRuleContext(compiladorParser.OpalcContext,0)


        def argumentos_prima(self):
            return self.getTypedRuleContext(compiladorParser.Argumentos_primaContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = compiladorParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_argumentos)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 11, 24, 25, 26, 27, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.opalc()
                self.state = 299
                self.argumentos_prima()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)

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


    class Argumentos_primaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def opalc(self):
            return self.getTypedRuleContext(compiladorParser.OpalcContext,0)


        def argumentos_prima(self):
            return self.getTypedRuleContext(compiladorParser.Argumentos_primaContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_argumentos_prima

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos_prima" ):
                listener.enterArgumentos_prima(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos_prima" ):
                listener.exitArgumentos_prima(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos_prima" ):
                return visitor.visitArgumentos_prima(self)
            else:
                return visitor.visitChildren(self)




    def argumentos_prima(self):

        localctx = compiladorParser.Argumentos_primaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_argumentos_prima)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(compiladorParser.COMA)
                self.state = 305
                self.opalc()
                self.state = 306
                self.argumentos_prima()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)

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


    class IreturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladorParser.RETURN, 0)

        def opalc(self):
            return self.getTypedRuleContext(compiladorParser.OpalcContext,0)


        def PYC(self):
            return self.getToken(compiladorParser.PYC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_ireturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIreturn" ):
                listener.enterIreturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIreturn" ):
                listener.exitIreturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIreturn" ):
                return visitor.visitIreturn(self)
            else:
                return visitor.visitChildren(self)




    def ireturn(self):

        localctx = compiladorParser.IreturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ireturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(compiladorParser.RETURN)
            self.state = 312
            self.opalc()
            self.state = 313
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





