# Generated from /home/cele/Repositorios Git/DHS/Practicos/Practico2/src/main/python/compilador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete generic visitor for a parse tree produced by compiladorParser.

class compiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladorParser#programa.
    def visitPrograma(self, ctx:compiladorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladorParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instruccion.
    def visitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#bloque.
    def visitBloque(self, ctx:compiladorParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracion.
    def visitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#inicializador.
    def visitInicializador(self, ctx:compiladorParser.InicializadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listavar.
    def visitListavar(self, ctx:compiladorParser.ListavarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#tipo.
    def visitTipo(self, ctx:compiladorParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignacion.
    def visitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iwhile.
    def visitIwhile(self, ctx:compiladorParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iif.
    def visitIif(self, ctx:compiladorParser.IifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ielse.
    def visitIelse(self, ctx:compiladorParser.IelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ifor.
    def visitIfor(self, ctx:compiladorParser.IforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#f_inicializacion.
    def visitF_inicializacion(self, ctx:compiladorParser.F_inicializacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#f_inicializador.
    def visitF_inicializador(self, ctx:compiladorParser.F_inicializadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#f_lista_inic.
    def visitF_lista_inic(self, ctx:compiladorParser.F_lista_inicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#f_condicion.
    def visitF_condicion(self, ctx:compiladorParser.F_condicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#f_actualizacion.
    def visitF_actualizacion(self, ctx:compiladorParser.F_actualizacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#f_lista_cya.
    def visitF_lista_cya(self, ctx:compiladorParser.F_lista_cyaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#f_lista_prima.
    def visitF_lista_prima(self, ctx:compiladorParser.F_lista_primaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#exp_for.
    def visitExp_for(self, ctx:compiladorParser.Exp_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#opalc.
    def visitOpalc(self, ctx:compiladorParser.OpalcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#exp_l.
    def visitExp_l(self, ctx:compiladorParser.Exp_lContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#exp_l_prima.
    def visitExp_l_prima(self, ctx:compiladorParser.Exp_l_primaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#exp_comp.
    def visitExp_comp(self, ctx:compiladorParser.Exp_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#exp_comp_prima.
    def visitExp_comp_prima(self, ctx:compiladorParser.Exp_comp_primaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#exp_a.
    def visitExp_a(self, ctx:compiladorParser.Exp_aContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#exp_a_prima.
    def visitExp_a_prima(self, ctx:compiladorParser.Exp_a_primaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#term.
    def visitTerm(self, ctx:compiladorParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#term_prima.
    def visitTerm_prima(self, ctx:compiladorParser.Term_primaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#factor.
    def visitFactor(self, ctx:compiladorParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#prototipo.
    def visitPrototipo(self, ctx:compiladorParser.PrototipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#funcion.
    def visitFuncion(self, ctx:compiladorParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#lista_parametros.
    def visitLista_parametros(self, ctx:compiladorParser.Lista_parametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametros.
    def visitParametros(self, ctx:compiladorParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametros_prima.
    def visitParametros_prima(self, ctx:compiladorParser.Parametros_primaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:compiladorParser.Llamada_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#lista_argumentos.
    def visitLista_argumentos(self, ctx:compiladorParser.Lista_argumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#argumentos.
    def visitArgumentos(self, ctx:compiladorParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#argumentos_prima.
    def visitArgumentos_prima(self, ctx:compiladorParser.Argumentos_primaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ireturn.
    def visitIreturn(self, ctx:compiladorParser.IreturnContext):
        return self.visitChildren(ctx)



del compiladorParser