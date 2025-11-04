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
        4,1,36,405,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,3,0,99,8,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,108,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,122,8,3,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,3,7,144,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,166,8,8,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,177,8,9,1,10,1,10,1,10,1,10,1,10,3,
        10,184,8,10,1,11,1,11,3,11,188,8,11,1,12,1,12,1,12,1,12,3,12,194,
        8,12,1,13,1,13,1,13,1,13,1,13,3,13,201,8,13,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,221,8,17,1,18,1,18,1,18,3,18,226,8,18,1,19,1,19,1,19,1,
        19,1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,
        23,3,23,245,8,23,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,3,25,255,
        8,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        3,27,269,8,27,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,291,8,29,
        1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,
        305,8,31,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,3,33,323,8,33,1,34,1,34,1,34,1,34,1,34,
        1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,3,34,339,8,34,1,34,
        1,34,1,34,1,34,5,34,345,8,34,10,34,12,34,348,9,34,1,35,1,35,1,35,
        1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,3,36,361,8,36,1,37,1,37,
        1,37,1,37,1,37,3,37,368,8,37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,
        1,39,3,39,378,8,39,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,
        3,41,389,8,41,1,42,1,42,1,42,1,42,1,42,3,42,396,8,42,1,43,1,43,1,
        43,1,43,1,43,1,43,1,43,1,43,0,1,68,44,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,72,74,76,78,80,82,84,86,0,1,1,0,25,28,409,0,98,1,0,0,0,
        2,100,1,0,0,0,4,107,1,0,0,0,6,121,1,0,0,0,8,123,1,0,0,0,10,127,1,
        0,0,0,12,133,1,0,0,0,14,143,1,0,0,0,16,165,1,0,0,0,18,176,1,0,0,
        0,20,183,1,0,0,0,22,187,1,0,0,0,24,193,1,0,0,0,26,200,1,0,0,0,28,
        202,1,0,0,0,30,206,1,0,0,0,32,212,1,0,0,0,34,220,1,0,0,0,36,225,
        1,0,0,0,38,227,1,0,0,0,40,231,1,0,0,0,42,234,1,0,0,0,44,236,1,0,
        0,0,46,244,1,0,0,0,48,246,1,0,0,0,50,254,1,0,0,0,52,256,1,0,0,0,
        54,268,1,0,0,0,56,270,1,0,0,0,58,290,1,0,0,0,60,292,1,0,0,0,62,304,
        1,0,0,0,64,306,1,0,0,0,66,322,1,0,0,0,68,338,1,0,0,0,70,349,1,0,
        0,0,72,360,1,0,0,0,74,367,1,0,0,0,76,369,1,0,0,0,78,377,1,0,0,0,
        80,379,1,0,0,0,82,388,1,0,0,0,84,395,1,0,0,0,86,397,1,0,0,0,88,89,
        5,34,0,0,89,90,6,0,-1,0,90,99,3,0,0,0,91,92,5,24,0,0,92,93,6,0,-1,
        0,93,99,3,0,0,0,94,95,5,36,0,0,95,96,6,0,-1,0,96,99,3,0,0,0,97,99,
        5,0,0,1,98,88,1,0,0,0,98,91,1,0,0,0,98,94,1,0,0,0,98,97,1,0,0,0,
        99,1,1,0,0,0,100,101,3,4,2,0,101,102,5,0,0,1,102,3,1,0,0,0,103,104,
        3,6,3,0,104,105,3,4,2,0,105,108,1,0,0,0,106,108,1,0,0,0,107,103,
        1,0,0,0,107,106,1,0,0,0,108,5,1,0,0,0,109,122,3,40,20,0,110,122,
        3,30,15,0,111,122,3,12,6,0,112,122,3,10,5,0,113,122,3,16,8,0,114,
        122,3,28,14,0,115,122,3,8,4,0,116,122,3,70,35,0,117,122,3,86,43,
        0,118,119,3,80,40,0,119,120,5,5,0,0,120,122,1,0,0,0,121,109,1,0,
        0,0,121,110,1,0,0,0,121,111,1,0,0,0,121,112,1,0,0,0,121,113,1,0,
        0,0,121,114,1,0,0,0,121,115,1,0,0,0,121,116,1,0,0,0,121,117,1,0,
        0,0,121,118,1,0,0,0,122,7,1,0,0,0,123,124,5,3,0,0,124,125,3,4,2,
        0,125,126,5,4,0,0,126,9,1,0,0,0,127,128,5,31,0,0,128,129,5,1,0,0,
        129,130,3,42,21,0,130,131,5,2,0,0,131,132,3,6,3,0,132,11,1,0,0,0,
        133,134,5,29,0,0,134,135,5,1,0,0,135,136,3,42,21,0,136,137,5,2,0,
        0,137,138,3,6,3,0,138,139,3,14,7,0,139,13,1,0,0,0,140,141,5,30,0,
        0,141,144,3,6,3,0,142,144,1,0,0,0,143,140,1,0,0,0,143,142,1,0,0,
        0,144,15,1,0,0,0,145,146,5,32,0,0,146,147,5,1,0,0,147,148,3,18,9,
        0,148,149,5,5,0,0,149,150,3,22,11,0,150,151,5,5,0,0,151,152,3,24,
        12,0,152,153,5,2,0,0,153,154,3,6,3,0,154,166,1,0,0,0,155,156,5,32,
        0,0,156,157,5,1,0,0,157,158,3,18,9,0,158,159,5,5,0,0,159,160,3,22,
        11,0,160,161,5,5,0,0,161,162,3,24,12,0,162,163,5,2,0,0,163,164,5,
        5,0,0,164,166,1,0,0,0,165,145,1,0,0,0,165,155,1,0,0,0,166,17,1,0,
        0,0,167,168,3,32,16,0,168,169,5,34,0,0,169,170,3,36,18,0,170,171,
        3,34,17,0,171,177,1,0,0,0,172,173,3,38,19,0,173,174,3,20,10,0,174,
        177,1,0,0,0,175,177,1,0,0,0,176,167,1,0,0,0,176,172,1,0,0,0,176,
        175,1,0,0,0,177,19,1,0,0,0,178,179,5,16,0,0,179,180,3,38,19,0,180,
        181,3,20,10,0,181,184,1,0,0,0,182,184,1,0,0,0,183,178,1,0,0,0,183,
        182,1,0,0,0,184,21,1,0,0,0,185,188,3,42,21,0,186,188,1,0,0,0,187,
        185,1,0,0,0,187,186,1,0,0,0,188,23,1,0,0,0,189,190,3,60,30,0,190,
        191,3,26,13,0,191,194,1,0,0,0,192,194,1,0,0,0,193,189,1,0,0,0,193,
        192,1,0,0,0,194,25,1,0,0,0,195,196,5,16,0,0,196,197,3,60,30,0,197,
        198,3,26,13,0,198,201,1,0,0,0,199,201,1,0,0,0,200,195,1,0,0,0,200,
        199,1,0,0,0,201,27,1,0,0,0,202,203,5,33,0,0,203,204,3,42,21,0,204,
        205,5,5,0,0,205,29,1,0,0,0,206,207,3,32,16,0,207,208,5,34,0,0,208,
        209,3,36,18,0,209,210,3,34,17,0,210,211,5,5,0,0,211,31,1,0,0,0,212,
        213,7,0,0,0,213,33,1,0,0,0,214,215,5,16,0,0,215,216,5,34,0,0,216,
        217,3,36,18,0,217,218,3,34,17,0,218,221,1,0,0,0,219,221,1,0,0,0,
        220,214,1,0,0,0,220,219,1,0,0,0,221,35,1,0,0,0,222,223,5,15,0,0,
        223,226,3,42,21,0,224,226,1,0,0,0,225,222,1,0,0,0,225,224,1,0,0,
        0,226,37,1,0,0,0,227,228,5,34,0,0,228,229,5,15,0,0,229,230,3,42,
        21,0,230,39,1,0,0,0,231,232,3,38,19,0,232,233,5,5,0,0,233,41,1,0,
        0,0,234,235,3,44,22,0,235,43,1,0,0,0,236,237,3,48,24,0,237,238,3,
        46,23,0,238,45,1,0,0,0,239,240,5,13,0,0,240,241,3,48,24,0,241,242,
        3,46,23,0,242,245,1,0,0,0,243,245,1,0,0,0,244,239,1,0,0,0,244,243,
        1,0,0,0,245,47,1,0,0,0,246,247,3,52,26,0,247,248,3,50,25,0,248,49,
        1,0,0,0,249,250,5,12,0,0,250,251,3,52,26,0,251,252,3,50,25,0,252,
        255,1,0,0,0,253,255,1,0,0,0,254,249,1,0,0,0,254,253,1,0,0,0,255,
        51,1,0,0,0,256,257,3,56,28,0,257,258,3,54,27,0,258,53,1,0,0,0,259,
        260,5,6,0,0,260,261,3,56,28,0,261,262,3,54,27,0,262,269,1,0,0,0,
        263,264,5,7,0,0,264,265,3,56,28,0,265,266,3,54,27,0,266,269,1,0,
        0,0,267,269,1,0,0,0,268,259,1,0,0,0,268,263,1,0,0,0,268,267,1,0,
        0,0,269,55,1,0,0,0,270,271,3,60,30,0,271,272,3,58,29,0,272,57,1,
        0,0,0,273,274,5,9,0,0,274,275,3,60,30,0,275,276,3,58,29,0,276,291,
        1,0,0,0,277,278,5,8,0,0,278,279,3,60,30,0,279,280,3,58,29,0,280,
        291,1,0,0,0,281,282,5,11,0,0,282,283,3,60,30,0,283,284,3,58,29,0,
        284,291,1,0,0,0,285,286,5,10,0,0,286,287,3,60,30,0,287,288,3,58,
        29,0,288,291,1,0,0,0,289,291,1,0,0,0,290,273,1,0,0,0,290,277,1,0,
        0,0,290,281,1,0,0,0,290,285,1,0,0,0,290,289,1,0,0,0,291,59,1,0,0,
        0,292,293,3,64,32,0,293,294,3,62,31,0,294,61,1,0,0,0,295,296,5,17,
        0,0,296,297,3,64,32,0,297,298,3,62,31,0,298,305,1,0,0,0,299,300,
        5,18,0,0,300,301,3,64,32,0,301,302,3,62,31,0,302,305,1,0,0,0,303,
        305,1,0,0,0,304,295,1,0,0,0,304,299,1,0,0,0,304,303,1,0,0,0,305,
        63,1,0,0,0,306,307,3,68,34,0,307,308,3,66,33,0,308,65,1,0,0,0,309,
        310,5,19,0,0,310,311,3,68,34,0,311,312,3,66,33,0,312,323,1,0,0,0,
        313,314,5,20,0,0,314,315,3,68,34,0,315,316,3,66,33,0,316,323,1,0,
        0,0,317,318,5,21,0,0,318,319,3,68,34,0,319,320,3,66,33,0,320,323,
        1,0,0,0,321,323,1,0,0,0,322,309,1,0,0,0,322,313,1,0,0,0,322,317,
        1,0,0,0,322,321,1,0,0,0,323,67,1,0,0,0,324,325,6,34,-1,0,325,339,
        5,24,0,0,326,339,5,34,0,0,327,328,5,1,0,0,328,329,3,42,21,0,329,
        330,5,2,0,0,330,339,1,0,0,0,331,339,3,80,40,0,332,333,5,14,0,0,333,
        339,3,68,34,5,334,335,5,22,0,0,335,339,3,68,34,4,336,337,5,23,0,
        0,337,339,3,68,34,3,338,324,1,0,0,0,338,326,1,0,0,0,338,327,1,0,
        0,0,338,331,1,0,0,0,338,332,1,0,0,0,338,334,1,0,0,0,338,336,1,0,
        0,0,339,346,1,0,0,0,340,341,10,2,0,0,341,345,5,22,0,0,342,343,10,
        1,0,0,343,345,5,23,0,0,344,340,1,0,0,0,344,342,1,0,0,0,345,348,1,
        0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,69,1,0,0,0,348,346,1,0,
        0,0,349,350,3,32,16,0,350,351,5,34,0,0,351,352,5,1,0,0,352,353,3,
        72,36,0,353,354,5,2,0,0,354,355,5,5,0,0,355,71,1,0,0,0,356,357,3,
        76,38,0,357,358,3,74,37,0,358,361,1,0,0,0,359,361,1,0,0,0,360,356,
        1,0,0,0,360,359,1,0,0,0,361,73,1,0,0,0,362,363,5,16,0,0,363,364,
        3,76,38,0,364,365,3,74,37,0,365,368,1,0,0,0,366,368,1,0,0,0,367,
        362,1,0,0,0,367,366,1,0,0,0,368,75,1,0,0,0,369,370,3,32,16,0,370,
        371,5,34,0,0,371,372,3,78,39,0,372,77,1,0,0,0,373,374,5,16,0,0,374,
        375,5,34,0,0,375,378,3,78,39,0,376,378,1,0,0,0,377,373,1,0,0,0,377,
        376,1,0,0,0,378,79,1,0,0,0,379,380,5,34,0,0,380,381,5,1,0,0,381,
        382,3,82,41,0,382,383,5,2,0,0,383,81,1,0,0,0,384,385,3,42,21,0,385,
        386,3,84,42,0,386,389,1,0,0,0,387,389,1,0,0,0,388,384,1,0,0,0,388,
        387,1,0,0,0,389,83,1,0,0,0,390,391,5,16,0,0,391,392,3,42,21,0,392,
        393,3,84,42,0,393,396,1,0,0,0,394,396,1,0,0,0,395,390,1,0,0,0,395,
        394,1,0,0,0,396,85,1,0,0,0,397,398,3,32,16,0,398,399,5,34,0,0,399,
        400,5,1,0,0,400,401,3,72,36,0,401,402,5,2,0,0,402,403,3,8,4,0,403,
        87,1,0,0,0,26,98,107,121,143,165,176,183,187,193,200,220,225,244,
        254,268,290,304,322,338,344,346,360,367,377,388,395
    ]

class compiladorParser ( Parser ):

    grammarFileName = "compilador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'=='", 
                     "'!='", "'>'", "'<'", "'>='", "'<='", "'&&'", "'||'", 
                     "'!'", "'='", "','", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'++'", "'--'", "<INVALID>", "'int'", "'double'", "'float'", 
                     "'void'", "'if'", "'else'", "'while'", "'for'", "'return'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "IGUAL", 
                      "DISTINTO", "MAYOR", "MENOR", "MAYORIG", "MENORIG", 
                      "AND", "OR", "NOT", "ASIG", "COMA", "SUMA", "RESTA", 
                      "MULT", "DIV", "MOD", "INC", "DEC", "NUMERO", "INT", 
                      "DOUBLE", "FLOAT", "VOID", "IF", "ELSE", "WHILE", 
                      "FOR", "RETURN", "ID", "WS", "OTRO" ]

    RULE_s = 0
    RULE_programa = 1
    RULE_instrucciones = 2
    RULE_instruccion = 3
    RULE_bloque = 4
    RULE_iwhile = 5
    RULE_iif = 6
    RULE_ielse = 7
    RULE_ifor = 8
    RULE_forInicializacion = 9
    RULE_listaExpASIG = 10
    RULE_forCond = 11
    RULE_forActualizacion = 12
    RULE_listaActualizacion = 13
    RULE_ireturn = 14
    RULE_declaracion = 15
    RULE_tipo = 16
    RULE_listavar = 17
    RULE_inic = 18
    RULE_expASIG = 19
    RULE_asignacion = 20
    RULE_opal = 21
    RULE_expOR = 22
    RULE_o = 23
    RULE_expAND = 24
    RULE_a = 25
    RULE_expIGUAL = 26
    RULE_i = 27
    RULE_expCOMP = 28
    RULE_c = 29
    RULE_exp = 30
    RULE_e = 31
    RULE_term = 32
    RULE_t = 33
    RULE_factor = 34
    RULE_prototipo = 35
    RULE_parametros = 36
    RULE_listaParametros = 37
    RULE_parametro = 38
    RULE_listaID = 39
    RULE_llamada = 40
    RULE_listaArg = 41
    RULE_argumentos = 42
    RULE_funcion = 43

    ruleNames =  [ "s", "programa", "instrucciones", "instruccion", "bloque", 
                   "iwhile", "iif", "ielse", "ifor", "forInicializacion", 
                   "listaExpASIG", "forCond", "forActualizacion", "listaActualizacion", 
                   "ireturn", "declaracion", "tipo", "listavar", "inic", 
                   "expASIG", "asignacion", "opal", "expOR", "o", "expAND", 
                   "a", "expIGUAL", "i", "expCOMP", "c", "exp", "e", "term", 
                   "t", "factor", "prototipo", "parametros", "listaParametros", 
                   "parametro", "listaID", "llamada", "listaArg", "argumentos", 
                   "funcion" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    PYC=5
    IGUAL=6
    DISTINTO=7
    MAYOR=8
    MENOR=9
    MAYORIG=10
    MENORIG=11
    AND=12
    OR=13
    NOT=14
    ASIG=15
    COMA=16
    SUMA=17
    RESTA=18
    MULT=19
    DIV=20
    MOD=21
    INC=22
    DEC=23
    NUMERO=24
    INT=25
    DOUBLE=26
    FLOAT=27
    VOID=28
    IF=29
    ELSE=30
    WHILE=31
    FOR=32
    RETURN=33
    ID=34
    WS=35
    OTRO=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._NUMERO = None # Token
            self._OTRO = None # Token

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def s(self):
            return self.getTypedRuleContext(compiladorParser.SContext,0)


        def NUMERO(self):
            return self.getToken(compiladorParser.NUMERO, 0)

        def OTRO(self):
            return self.getToken(compiladorParser.OTRO, 0)

        def EOF(self):
            return self.getToken(compiladorParser.EOF, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = compiladorParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                localctx._ID = self.match(compiladorParser.ID)
                print("ID ->" + (None if localctx._ID is None else localctx._ID.text) + "<--") 
                self.state = 90
                self.s()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                localctx._NUMERO = self.match(compiladorParser.NUMERO)
                print("NUMERO ->" + (None if localctx._NUMERO is None else localctx._NUMERO.text) + "<--") 
                self.state = 93
                self.s()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                localctx._OTRO = self.match(compiladorParser.OTRO)
                print("Otro ->" + (None if localctx._OTRO is None else localctx._OTRO.text) + "<--") 
                self.state = 96
                self.s()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.match(compiladorParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.instrucciones()
            self.state = 101
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
        self.enterRule(localctx, 4, self.RULE_instrucciones)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 25, 26, 27, 28, 29, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.instruccion()
                self.state = 104
                self.instrucciones()
                pass
            elif token in [-1, 4]:
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


        def ireturn(self):
            return self.getTypedRuleContext(compiladorParser.IreturnContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladorParser.BloqueContext,0)


        def prototipo(self):
            return self.getTypedRuleContext(compiladorParser.PrototipoContext,0)


        def funcion(self):
            return self.getTypedRuleContext(compiladorParser.FuncionContext,0)


        def llamada(self):
            return self.getTypedRuleContext(compiladorParser.LlamadaContext,0)


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
        self.enterRule(localctx, 6, self.RULE_instruccion)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.declaracion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.iif()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.iwhile()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.ifor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 114
                self.ireturn()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 115
                self.bloque()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 116
                self.prototipo()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 117
                self.funcion()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 118
                self.llamada()
                self.state = 119
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
        self.enterRule(localctx, 8, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(compiladorParser.LLA)
            self.state = 124
            self.instrucciones()
            self.state = 125
            self.match(compiladorParser.LLC)
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

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


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
        self.enterRule(localctx, 10, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(compiladorParser.WHILE)
            self.state = 128
            self.match(compiladorParser.PA)
            self.state = 129
            self.opal()
            self.state = 130
            self.match(compiladorParser.PC)
            self.state = 131
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

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


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
        self.enterRule(localctx, 12, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(compiladorParser.IF)
            self.state = 134
            self.match(compiladorParser.PA)
            self.state = 135
            self.opal()
            self.state = 136
            self.match(compiladorParser.PC)
            self.state = 137
            self.instruccion()
            self.state = 138
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
        self.enterRule(localctx, 14, self.RULE_ielse)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(compiladorParser.ELSE)
                self.state = 141
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

        def forInicializacion(self):
            return self.getTypedRuleContext(compiladorParser.ForInicializacionContext,0)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladorParser.PYC)
            else:
                return self.getToken(compiladorParser.PYC, i)

        def forCond(self):
            return self.getTypedRuleContext(compiladorParser.ForCondContext,0)


        def forActualizacion(self):
            return self.getTypedRuleContext(compiladorParser.ForActualizacionContext,0)


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
        self.enterRule(localctx, 16, self.RULE_ifor)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(compiladorParser.FOR)
                self.state = 146
                self.match(compiladorParser.PA)
                self.state = 147
                self.forInicializacion()
                self.state = 148
                self.match(compiladorParser.PYC)
                self.state = 149
                self.forCond()
                self.state = 150
                self.match(compiladorParser.PYC)
                self.state = 151
                self.forActualizacion()
                self.state = 152
                self.match(compiladorParser.PC)
                self.state = 153
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(compiladorParser.FOR)
                self.state = 156
                self.match(compiladorParser.PA)
                self.state = 157
                self.forInicializacion()
                self.state = 158
                self.match(compiladorParser.PYC)
                self.state = 159
                self.forCond()
                self.state = 160
                self.match(compiladorParser.PYC)
                self.state = 161
                self.forActualizacion()
                self.state = 162
                self.match(compiladorParser.PC)
                self.state = 163
                self.match(compiladorParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compiladorParser.ListavarContext,0)


        def expASIG(self):
            return self.getTypedRuleContext(compiladorParser.ExpASIGContext,0)


        def listaExpASIG(self):
            return self.getTypedRuleContext(compiladorParser.ListaExpASIGContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_forInicializacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInicializacion" ):
                listener.enterForInicializacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInicializacion" ):
                listener.exitForInicializacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInicializacion" ):
                return visitor.visitForInicializacion(self)
            else:
                return visitor.visitChildren(self)




    def forInicializacion(self):

        localctx = compiladorParser.ForInicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forInicializacion)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.tipo()
                self.state = 168
                self.match(compiladorParser.ID)
                self.state = 169
                self.inic()
                self.state = 170
                self.listavar()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.expASIG()
                self.state = 173
                self.listaExpASIG()
                pass
            elif token in [5]:
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


    class ListaExpASIGContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def expASIG(self):
            return self.getTypedRuleContext(compiladorParser.ExpASIGContext,0)


        def listaExpASIG(self):
            return self.getTypedRuleContext(compiladorParser.ListaExpASIGContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listaExpASIG

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaExpASIG" ):
                listener.enterListaExpASIG(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaExpASIG" ):
                listener.exitListaExpASIG(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaExpASIG" ):
                return visitor.visitListaExpASIG(self)
            else:
                return visitor.visitChildren(self)




    def listaExpASIG(self):

        localctx = compiladorParser.ListaExpASIGContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_listaExpASIG)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(compiladorParser.COMA)
                self.state = 179
                self.expASIG()
                self.state = 180
                self.listaExpASIG()
                pass
            elif token in [5]:
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


    class ForCondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


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
        self.enterRule(localctx, 22, self.RULE_forCond)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 14, 22, 23, 24, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.opal()
                pass
            elif token in [5]:
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


    class ForActualizacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


        def listaActualizacion(self):
            return self.getTypedRuleContext(compiladorParser.ListaActualizacionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_forActualizacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForActualizacion" ):
                listener.enterForActualizacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForActualizacion" ):
                listener.exitForActualizacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForActualizacion" ):
                return visitor.visitForActualizacion(self)
            else:
                return visitor.visitChildren(self)




    def forActualizacion(self):

        localctx = compiladorParser.ForActualizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forActualizacion)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 14, 22, 23, 24, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.exp()
                self.state = 190
                self.listaActualizacion()
                pass
            elif token in [2]:
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


    class ListaActualizacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


        def listaActualizacion(self):
            return self.getTypedRuleContext(compiladorParser.ListaActualizacionContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listaActualizacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaActualizacion" ):
                listener.enterListaActualizacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaActualizacion" ):
                listener.exitListaActualizacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaActualizacion" ):
                return visitor.visitListaActualizacion(self)
            else:
                return visitor.visitChildren(self)




    def listaActualizacion(self):

        localctx = compiladorParser.ListaActualizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_listaActualizacion)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(compiladorParser.COMA)
                self.state = 196
                self.exp()
                self.state = 197
                self.listaActualizacion()
                pass
            elif token in [2]:
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

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


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
        self.enterRule(localctx, 28, self.RULE_ireturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(compiladorParser.RETURN)
            self.state = 203
            self.opal()
            self.state = 204
            self.match(compiladorParser.PYC)
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

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


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
        self.enterRule(localctx, 30, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.tipo()
            self.state = 207
            self.match(compiladorParser.ID)
            self.state = 208
            self.inic()
            self.state = 209
            self.listavar()
            self.state = 210
            self.match(compiladorParser.PYC)
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

        def FLOAT(self):
            return self.getToken(compiladorParser.FLOAT, 0)

        def VOID(self):
            return self.getToken(compiladorParser.VOID, 0)

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
        self.enterRule(localctx, 32, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
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


    class ListavarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compiladorParser.InicContext,0)


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
        self.enterRule(localctx, 34, self.RULE_listavar)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(compiladorParser.COMA)
                self.state = 215
                self.match(compiladorParser.ID)
                self.state = 216
                self.inic()
                self.state = 217
                self.listavar()
                pass
            elif token in [5]:
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


    class InicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_inic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInic" ):
                listener.enterInic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInic" ):
                listener.exitInic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInic" ):
                return visitor.visitInic(self)
            else:
                return visitor.visitChildren(self)




    def inic(self):

        localctx = compiladorParser.InicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_inic)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(compiladorParser.ASIG)
                self.state = 223
                self.opal()
                pass
            elif token in [5, 16]:
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


    class ExpASIGContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladorParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expASIG

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpASIG" ):
                listener.enterExpASIG(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpASIG" ):
                listener.exitExpASIG(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpASIG" ):
                return visitor.visitExpASIG(self)
            else:
                return visitor.visitChildren(self)




    def expASIG(self):

        localctx = compiladorParser.ExpASIGContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expASIG)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(compiladorParser.ID)
            self.state = 228
            self.match(compiladorParser.ASIG)
            self.state = 229
            self.opal()
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

        def expASIG(self):
            return self.getTypedRuleContext(compiladorParser.ExpASIGContext,0)


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
        self.enterRule(localctx, 40, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.expASIG()
            self.state = 232
            self.match(compiladorParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expOR(self):
            return self.getTypedRuleContext(compiladorParser.ExpORContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compiladorParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expOR()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpORContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expAND(self):
            return self.getTypedRuleContext(compiladorParser.ExpANDContext,0)


        def o(self):
            return self.getTypedRuleContext(compiladorParser.OContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expOR

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpOR" ):
                listener.enterExpOR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpOR" ):
                listener.exitExpOR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpOR" ):
                return visitor.visitExpOR(self)
            else:
                return visitor.visitChildren(self)




    def expOR(self):

        localctx = compiladorParser.ExpORContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expOR)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.expAND()
            self.state = 237
            self.o()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(compiladorParser.OR, 0)

        def expAND(self):
            return self.getTypedRuleContext(compiladorParser.ExpANDContext,0)


        def o(self):
            return self.getTypedRuleContext(compiladorParser.OContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_o

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterO" ):
                listener.enterO(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitO" ):
                listener.exitO(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitO" ):
                return visitor.visitO(self)
            else:
                return visitor.visitChildren(self)




    def o(self):

        localctx = compiladorParser.OContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_o)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(compiladorParser.OR)
                self.state = 240
                self.expAND()
                self.state = 241
                self.o()
                pass
            elif token in [2, 5, 16]:
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


    class ExpANDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expIGUAL(self):
            return self.getTypedRuleContext(compiladorParser.ExpIGUALContext,0)


        def a(self):
            return self.getTypedRuleContext(compiladorParser.AContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expAND

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpAND" ):
                listener.enterExpAND(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpAND" ):
                listener.exitExpAND(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpAND" ):
                return visitor.visitExpAND(self)
            else:
                return visitor.visitChildren(self)




    def expAND(self):

        localctx = compiladorParser.ExpANDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expAND)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.expIGUAL()
            self.state = 247
            self.a()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(compiladorParser.AND, 0)

        def expIGUAL(self):
            return self.getTypedRuleContext(compiladorParser.ExpIGUALContext,0)


        def a(self):
            return self.getTypedRuleContext(compiladorParser.AContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA" ):
                listener.enterA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA" ):
                listener.exitA(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA" ):
                return visitor.visitA(self)
            else:
                return visitor.visitChildren(self)




    def a(self):

        localctx = compiladorParser.AContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_a)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(compiladorParser.AND)
                self.state = 250
                self.expIGUAL()
                self.state = 251
                self.a()
                pass
            elif token in [2, 5, 13, 16]:
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


    class ExpIGUALContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expCOMP(self):
            return self.getTypedRuleContext(compiladorParser.ExpCOMPContext,0)


        def i(self):
            return self.getTypedRuleContext(compiladorParser.IContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expIGUAL

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpIGUAL" ):
                listener.enterExpIGUAL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpIGUAL" ):
                listener.exitExpIGUAL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpIGUAL" ):
                return visitor.visitExpIGUAL(self)
            else:
                return visitor.visitChildren(self)




    def expIGUAL(self):

        localctx = compiladorParser.ExpIGUALContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expIGUAL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.expCOMP()
            self.state = 257
            self.i()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGUAL(self):
            return self.getToken(compiladorParser.IGUAL, 0)

        def expCOMP(self):
            return self.getTypedRuleContext(compiladorParser.ExpCOMPContext,0)


        def i(self):
            return self.getTypedRuleContext(compiladorParser.IContext,0)


        def DISTINTO(self):
            return self.getToken(compiladorParser.DISTINTO, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_i

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterI" ):
                listener.enterI(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitI" ):
                listener.exitI(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitI" ):
                return visitor.visitI(self)
            else:
                return visitor.visitChildren(self)




    def i(self):

        localctx = compiladorParser.IContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_i)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(compiladorParser.IGUAL)
                self.state = 260
                self.expCOMP()
                self.state = 261
                self.i()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(compiladorParser.DISTINTO)
                self.state = 264
                self.expCOMP()
                self.state = 265
                self.i()
                pass
            elif token in [2, 5, 12, 13, 16]:
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


    class ExpCOMPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


        def c(self):
            return self.getTypedRuleContext(compiladorParser.CContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_expCOMP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpCOMP" ):
                listener.enterExpCOMP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpCOMP" ):
                listener.exitExpCOMP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpCOMP" ):
                return visitor.visitExpCOMP(self)
            else:
                return visitor.visitChildren(self)




    def expCOMP(self):

        localctx = compiladorParser.ExpCOMPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expCOMP)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.exp()
            self.state = 271
            self.c()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOR(self):
            return self.getToken(compiladorParser.MENOR, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladorParser.ExpContext,0)


        def c(self):
            return self.getTypedRuleContext(compiladorParser.CContext,0)


        def MAYOR(self):
            return self.getToken(compiladorParser.MAYOR, 0)

        def MENORIG(self):
            return self.getToken(compiladorParser.MENORIG, 0)

        def MAYORIG(self):
            return self.getToken(compiladorParser.MAYORIG, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_c

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC" ):
                listener.enterC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC" ):
                listener.exitC(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitC" ):
                return visitor.visitC(self)
            else:
                return visitor.visitChildren(self)




    def c(self):

        localctx = compiladorParser.CContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_c)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(compiladorParser.MENOR)
                self.state = 274
                self.exp()
                self.state = 275
                self.c()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(compiladorParser.MAYOR)
                self.state = 278
                self.exp()
                self.state = 279
                self.c()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.match(compiladorParser.MENORIG)
                self.state = 282
                self.exp()
                self.state = 283
                self.c()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 285
                self.match(compiladorParser.MAYORIG)
                self.state = 286
                self.exp()
                self.state = 287
                self.c()
                pass
            elif token in [2, 5, 6, 7, 12, 13, 16]:
                self.enterOuterAlt(localctx, 5)

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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladorParser.EContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compiladorParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.term()
            self.state = 293
            self.e()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compiladorParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladorParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladorParser.EContext,0)


        def RESTA(self):
            return self.getToken(compiladorParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = compiladorParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_e)
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(compiladorParser.SUMA)
                self.state = 296
                self.term()
                self.state = 297
                self.e()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.match(compiladorParser.RESTA)
                self.state = 300
                self.term()
                self.state = 301
                self.e()
                pass
            elif token in [2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16]:
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


        def t(self):
            return self.getTypedRuleContext(compiladorParser.TContext,0)


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
        self.enterRule(localctx, 64, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.factor(0)
            self.state = 307
            self.t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladorParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladorParser.TContext,0)


        def DIV(self):
            return self.getToken(compiladorParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladorParser.MOD, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compiladorParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_t)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(compiladorParser.MULT)
                self.state = 310
                self.factor(0)
                self.state = 311
                self.t()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(compiladorParser.DIV)
                self.state = 314
                self.factor(0)
                self.state = 315
                self.t()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                self.match(compiladorParser.MOD)
                self.state = 318
                self.factor(0)
                self.state = 319
                self.t()
                pass
            elif token in [2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18]:
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

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def llamada(self):
            return self.getTypedRuleContext(compiladorParser.LlamadaContext,0)


        def NOT(self):
            return self.getToken(compiladorParser.NOT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladorParser.FactorContext,0)


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



    def factor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = compiladorParser.FactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_factor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 325
                self.match(compiladorParser.NUMERO)
                pass

            elif la_ == 2:
                self.state = 326
                self.match(compiladorParser.ID)
                pass

            elif la_ == 3:
                self.state = 327
                self.match(compiladorParser.PA)
                self.state = 328
                self.opal()
                self.state = 329
                self.match(compiladorParser.PC)
                pass

            elif la_ == 4:
                self.state = 331
                self.llamada()
                pass

            elif la_ == 5:
                self.state = 332
                self.match(compiladorParser.NOT)
                self.state = 333
                self.factor(5)
                pass

            elif la_ == 6:
                self.state = 334
                self.match(compiladorParser.INC)
                self.state = 335
                self.factor(4)
                pass

            elif la_ == 7:
                self.state = 336
                self.match(compiladorParser.DEC)
                self.state = 337
                self.factor(3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 344
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = compiladorParser.FactorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                        self.state = 340
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 341
                        self.match(compiladorParser.INC)
                        pass

                    elif la_ == 2:
                        localctx = compiladorParser.FactorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                        self.state = 342
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 343
                        self.match(compiladorParser.DEC)
                        pass

             
                self.state = 348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def parametros(self):
            return self.getTypedRuleContext(compiladorParser.ParametrosContext,0)


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
        self.enterRule(localctx, 70, self.RULE_prototipo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.tipo()
            self.state = 350
            self.match(compiladorParser.ID)
            self.state = 351
            self.match(compiladorParser.PA)
            self.state = 352
            self.parametros()
            self.state = 353
            self.match(compiladorParser.PC)
            self.state = 354
            self.match(compiladorParser.PYC)
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

        def parametro(self):
            return self.getTypedRuleContext(compiladorParser.ParametroContext,0)


        def listaParametros(self):
            return self.getTypedRuleContext(compiladorParser.ListaParametrosContext,0)


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
        self.enterRule(localctx, 72, self.RULE_parametros)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.parametro()
                self.state = 357
                self.listaParametros()
                pass
            elif token in [2]:
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


    class ListaParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def parametro(self):
            return self.getTypedRuleContext(compiladorParser.ParametroContext,0)


        def listaParametros(self):
            return self.getTypedRuleContext(compiladorParser.ListaParametrosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listaParametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaParametros" ):
                listener.enterListaParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaParametros" ):
                listener.exitListaParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaParametros" ):
                return visitor.visitListaParametros(self)
            else:
                return visitor.visitChildren(self)




    def listaParametros(self):

        localctx = compiladorParser.ListaParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_listaParametros)
        try:
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(compiladorParser.COMA)
                self.state = 363
                self.parametro()
                self.state = 364
                self.listaParametros()
                pass
            elif token in [2]:
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


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compiladorParser.TipoContext,0)


        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def listaID(self):
            return self.getTypedRuleContext(compiladorParser.ListaIDContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = compiladorParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.tipo()
            self.state = 370
            self.match(compiladorParser.ID)
            self.state = 371
            self.listaID()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def listaID(self):
            return self.getTypedRuleContext(compiladorParser.ListaIDContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listaID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaID" ):
                listener.enterListaID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaID" ):
                listener.exitListaID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaID" ):
                return visitor.visitListaID(self)
            else:
                return visitor.visitChildren(self)




    def listaID(self):

        localctx = compiladorParser.ListaIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_listaID)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(compiladorParser.COMA)
                self.state = 374
                self.match(compiladorParser.ID)
                self.state = 375
                self.listaID()
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


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladorParser.ID, 0)

        def PA(self):
            return self.getToken(compiladorParser.PA, 0)

        def listaArg(self):
            return self.getTypedRuleContext(compiladorParser.ListaArgContext,0)


        def PC(self):
            return self.getToken(compiladorParser.PC, 0)

        def getRuleIndex(self):
            return compiladorParser.RULE_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada" ):
                listener.enterLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada" ):
                listener.exitLlamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada" ):
                return visitor.visitLlamada(self)
            else:
                return visitor.visitChildren(self)




    def llamada(self):

        localctx = compiladorParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_llamada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(compiladorParser.ID)
            self.state = 380
            self.match(compiladorParser.PA)
            self.state = 381
            self.listaArg()
            self.state = 382
            self.match(compiladorParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def argumentos(self):
            return self.getTypedRuleContext(compiladorParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return compiladorParser.RULE_listaArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaArg" ):
                listener.enterListaArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaArg" ):
                listener.exitListaArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaArg" ):
                return visitor.visitListaArg(self)
            else:
                return visitor.visitChildren(self)




    def listaArg(self):

        localctx = compiladorParser.ListaArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_listaArg)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 14, 22, 23, 24, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.opal()
                self.state = 385
                self.argumentos()
                pass
            elif token in [2]:
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


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladorParser.COMA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladorParser.OpalContext,0)


        def argumentos(self):
            return self.getTypedRuleContext(compiladorParser.ArgumentosContext,0)


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
        self.enterRule(localctx, 84, self.RULE_argumentos)
        try:
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(compiladorParser.COMA)
                self.state = 391
                self.opal()
                self.state = 392
                self.argumentos()
                pass
            elif token in [2]:
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

        def parametros(self):
            return self.getTypedRuleContext(compiladorParser.ParametrosContext,0)


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
        self.enterRule(localctx, 86, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.tipo()
            self.state = 398
            self.match(compiladorParser.ID)
            self.state = 399
            self.match(compiladorParser.PA)
            self.state = 400
            self.parametros()
            self.state = 401
            self.match(compiladorParser.PC)
            self.state = 402
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[34] = self.factor_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def factor_sempred(self, localctx:FactorContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




