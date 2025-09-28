# Generated from /home/cele/Repositorios Git/DHS/Practicos/Practico2/src/main/python/compilador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete listener for a parse tree produced by compiladorParser.
class compiladorListener(ParseTreeListener):

    # Enter a parse tree produced by compiladorParser#programa.
    def enterPrograma(self, ctx:compiladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladorParser#programa.
    def exitPrograma(self, ctx:compiladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladorParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladorParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladorParser#instruccion.
    def enterInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladorParser#instruccion.
    def exitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladorParser#bloque.
    def enterBloque(self, ctx:compiladorParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladorParser#bloque.
    def exitBloque(self, ctx:compiladorParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracion.
    def enterDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracion.
    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladorParser#inicializador.
    def enterInicializador(self, ctx:compiladorParser.InicializadorContext):
        pass

    # Exit a parse tree produced by compiladorParser#inicializador.
    def exitInicializador(self, ctx:compiladorParser.InicializadorContext):
        pass


    # Enter a parse tree produced by compiladorParser#listavar.
    def enterListavar(self, ctx:compiladorParser.ListavarContext):
        pass

    # Exit a parse tree produced by compiladorParser#listavar.
    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        pass


    # Enter a parse tree produced by compiladorParser#tipo.
    def enterTipo(self, ctx:compiladorParser.TipoContext):
        pass

    # Exit a parse tree produced by compiladorParser#tipo.
    def exitTipo(self, ctx:compiladorParser.TipoContext):
        pass


    # Enter a parse tree produced by compiladorParser#asignacion.
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#asignacion.
    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#iwhile.
    def enterIwhile(self, ctx:compiladorParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladorParser#iwhile.
    def exitIwhile(self, ctx:compiladorParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladorParser#iif.
    def enterIif(self, ctx:compiladorParser.IifContext):
        pass

    # Exit a parse tree produced by compiladorParser#iif.
    def exitIif(self, ctx:compiladorParser.IifContext):
        pass


    # Enter a parse tree produced by compiladorParser#ielse.
    def enterIelse(self, ctx:compiladorParser.IelseContext):
        pass

    # Exit a parse tree produced by compiladorParser#ielse.
    def exitIelse(self, ctx:compiladorParser.IelseContext):
        pass


    # Enter a parse tree produced by compiladorParser#ifor.
    def enterIfor(self, ctx:compiladorParser.IforContext):
        pass

    # Exit a parse tree produced by compiladorParser#ifor.
    def exitIfor(self, ctx:compiladorParser.IforContext):
        pass


    # Enter a parse tree produced by compiladorParser#f_inicializacion.
    def enterF_inicializacion(self, ctx:compiladorParser.F_inicializacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#f_inicializacion.
    def exitF_inicializacion(self, ctx:compiladorParser.F_inicializacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#f_inicializador.
    def enterF_inicializador(self, ctx:compiladorParser.F_inicializadorContext):
        pass

    # Exit a parse tree produced by compiladorParser#f_inicializador.
    def exitF_inicializador(self, ctx:compiladorParser.F_inicializadorContext):
        pass


    # Enter a parse tree produced by compiladorParser#f_lista_inic.
    def enterF_lista_inic(self, ctx:compiladorParser.F_lista_inicContext):
        pass

    # Exit a parse tree produced by compiladorParser#f_lista_inic.
    def exitF_lista_inic(self, ctx:compiladorParser.F_lista_inicContext):
        pass


    # Enter a parse tree produced by compiladorParser#f_condicion.
    def enterF_condicion(self, ctx:compiladorParser.F_condicionContext):
        pass

    # Exit a parse tree produced by compiladorParser#f_condicion.
    def exitF_condicion(self, ctx:compiladorParser.F_condicionContext):
        pass


    # Enter a parse tree produced by compiladorParser#f_actualizacion.
    def enterF_actualizacion(self, ctx:compiladorParser.F_actualizacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#f_actualizacion.
    def exitF_actualizacion(self, ctx:compiladorParser.F_actualizacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#f_lista_a.
    def enterF_lista_a(self, ctx:compiladorParser.F_lista_aContext):
        pass

    # Exit a parse tree produced by compiladorParser#f_lista_a.
    def exitF_lista_a(self, ctx:compiladorParser.F_lista_aContext):
        pass


    # Enter a parse tree produced by compiladorParser#f_lista_prima.
    def enterF_lista_prima(self, ctx:compiladorParser.F_lista_primaContext):
        pass

    # Exit a parse tree produced by compiladorParser#f_lista_prima.
    def exitF_lista_prima(self, ctx:compiladorParser.F_lista_primaContext):
        pass


    # Enter a parse tree produced by compiladorParser#exp_for.
    def enterExp_for(self, ctx:compiladorParser.Exp_forContext):
        pass

    # Exit a parse tree produced by compiladorParser#exp_for.
    def exitExp_for(self, ctx:compiladorParser.Exp_forContext):
        pass


    # Enter a parse tree produced by compiladorParser#opalc.
    def enterOpalc(self, ctx:compiladorParser.OpalcContext):
        pass

    # Exit a parse tree produced by compiladorParser#opalc.
    def exitOpalc(self, ctx:compiladorParser.OpalcContext):
        pass


    # Enter a parse tree produced by compiladorParser#exp_l.
    def enterExp_l(self, ctx:compiladorParser.Exp_lContext):
        pass

    # Exit a parse tree produced by compiladorParser#exp_l.
    def exitExp_l(self, ctx:compiladorParser.Exp_lContext):
        pass


    # Enter a parse tree produced by compiladorParser#exp_l_prima.
    def enterExp_l_prima(self, ctx:compiladorParser.Exp_l_primaContext):
        pass

    # Exit a parse tree produced by compiladorParser#exp_l_prima.
    def exitExp_l_prima(self, ctx:compiladorParser.Exp_l_primaContext):
        pass


    # Enter a parse tree produced by compiladorParser#exp_comp.
    def enterExp_comp(self, ctx:compiladorParser.Exp_compContext):
        pass

    # Exit a parse tree produced by compiladorParser#exp_comp.
    def exitExp_comp(self, ctx:compiladorParser.Exp_compContext):
        pass


    # Enter a parse tree produced by compiladorParser#exp_comp_prima.
    def enterExp_comp_prima(self, ctx:compiladorParser.Exp_comp_primaContext):
        pass

    # Exit a parse tree produced by compiladorParser#exp_comp_prima.
    def exitExp_comp_prima(self, ctx:compiladorParser.Exp_comp_primaContext):
        pass


    # Enter a parse tree produced by compiladorParser#exp_a.
    def enterExp_a(self, ctx:compiladorParser.Exp_aContext):
        pass

    # Exit a parse tree produced by compiladorParser#exp_a.
    def exitExp_a(self, ctx:compiladorParser.Exp_aContext):
        pass


    # Enter a parse tree produced by compiladorParser#exp_a_prima.
    def enterExp_a_prima(self, ctx:compiladorParser.Exp_a_primaContext):
        pass

    # Exit a parse tree produced by compiladorParser#exp_a_prima.
    def exitExp_a_prima(self, ctx:compiladorParser.Exp_a_primaContext):
        pass


    # Enter a parse tree produced by compiladorParser#term.
    def enterTerm(self, ctx:compiladorParser.TermContext):
        pass

    # Exit a parse tree produced by compiladorParser#term.
    def exitTerm(self, ctx:compiladorParser.TermContext):
        pass


    # Enter a parse tree produced by compiladorParser#term_prima.
    def enterTerm_prima(self, ctx:compiladorParser.Term_primaContext):
        pass

    # Exit a parse tree produced by compiladorParser#term_prima.
    def exitTerm_prima(self, ctx:compiladorParser.Term_primaContext):
        pass


    # Enter a parse tree produced by compiladorParser#factor.
    def enterFactor(self, ctx:compiladorParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladorParser#factor.
    def exitFactor(self, ctx:compiladorParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladorParser#prototipo.
    def enterPrototipo(self, ctx:compiladorParser.PrototipoContext):
        pass

    # Exit a parse tree produced by compiladorParser#prototipo.
    def exitPrototipo(self, ctx:compiladorParser.PrototipoContext):
        pass


    # Enter a parse tree produced by compiladorParser#funcion.
    def enterFuncion(self, ctx:compiladorParser.FuncionContext):
        pass

    # Exit a parse tree produced by compiladorParser#funcion.
    def exitFuncion(self, ctx:compiladorParser.FuncionContext):
        pass


    # Enter a parse tree produced by compiladorParser#lista_parametros.
    def enterLista_parametros(self, ctx:compiladorParser.Lista_parametrosContext):
        pass

    # Exit a parse tree produced by compiladorParser#lista_parametros.
    def exitLista_parametros(self, ctx:compiladorParser.Lista_parametrosContext):
        pass


    # Enter a parse tree produced by compiladorParser#parametros.
    def enterParametros(self, ctx:compiladorParser.ParametrosContext):
        pass

    # Exit a parse tree produced by compiladorParser#parametros.
    def exitParametros(self, ctx:compiladorParser.ParametrosContext):
        pass


    # Enter a parse tree produced by compiladorParser#parametros_prima.
    def enterParametros_prima(self, ctx:compiladorParser.Parametros_primaContext):
        pass

    # Exit a parse tree produced by compiladorParser#parametros_prima.
    def exitParametros_prima(self, ctx:compiladorParser.Parametros_primaContext):
        pass


    # Enter a parse tree produced by compiladorParser#llamada_funcion.
    def enterLlamada_funcion(self, ctx:compiladorParser.Llamada_funcionContext):
        pass

    # Exit a parse tree produced by compiladorParser#llamada_funcion.
    def exitLlamada_funcion(self, ctx:compiladorParser.Llamada_funcionContext):
        pass


    # Enter a parse tree produced by compiladorParser#lista_argumentos.
    def enterLista_argumentos(self, ctx:compiladorParser.Lista_argumentosContext):
        pass

    # Exit a parse tree produced by compiladorParser#lista_argumentos.
    def exitLista_argumentos(self, ctx:compiladorParser.Lista_argumentosContext):
        pass


    # Enter a parse tree produced by compiladorParser#argumentos.
    def enterArgumentos(self, ctx:compiladorParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by compiladorParser#argumentos.
    def exitArgumentos(self, ctx:compiladorParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by compiladorParser#argumentos_prima.
    def enterArgumentos_prima(self, ctx:compiladorParser.Argumentos_primaContext):
        pass

    # Exit a parse tree produced by compiladorParser#argumentos_prima.
    def exitArgumentos_prima(self, ctx:compiladorParser.Argumentos_primaContext):
        pass


    # Enter a parse tree produced by compiladorParser#ireturn.
    def enterIreturn(self, ctx:compiladorParser.IreturnContext):
        pass

    # Exit a parse tree produced by compiladorParser#ireturn.
    def exitIreturn(self, ctx:compiladorParser.IreturnContext):
        pass



del compiladorParser