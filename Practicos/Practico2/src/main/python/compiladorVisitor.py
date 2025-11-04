# Generated from /home/cele/Repositorios Git/DHS/Practicos/Practico2/src/main/python/compilador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete generic visitor for a parse tree produced by compiladorParser.

class compiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladorParser#s.
    def visitS(self, ctx:compiladorParser.SContext):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by compiladorParser#forInicializacion.
    def visitForInicializacion(self, ctx:compiladorParser.ForInicializacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listaExpASIG.
    def visitListaExpASIG(self, ctx:compiladorParser.ListaExpASIGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#forCond.
    def visitForCond(self, ctx:compiladorParser.ForCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#forActualizacion.
    def visitForActualizacion(self, ctx:compiladorParser.ForActualizacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listaActualizacion.
    def visitListaActualizacion(self, ctx:compiladorParser.ListaActualizacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ireturn.
    def visitIreturn(self, ctx:compiladorParser.IreturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracion.
    def visitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#tipo.
    def visitTipo(self, ctx:compiladorParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listavar.
    def visitListavar(self, ctx:compiladorParser.ListavarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#inic.
    def visitInic(self, ctx:compiladorParser.InicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expASIG.
    def visitExpASIG(self, ctx:compiladorParser.ExpASIGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignacion.
    def visitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#opal.
    def visitOpal(self, ctx:compiladorParser.OpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expOR.
    def visitExpOR(self, ctx:compiladorParser.ExpORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#o.
    def visitO(self, ctx:compiladorParser.OContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expAND.
    def visitExpAND(self, ctx:compiladorParser.ExpANDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#a.
    def visitA(self, ctx:compiladorParser.AContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expIGUAL.
    def visitExpIGUAL(self, ctx:compiladorParser.ExpIGUALContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#i.
    def visitI(self, ctx:compiladorParser.IContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expCOMP.
    def visitExpCOMP(self, ctx:compiladorParser.ExpCOMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#c.
    def visitC(self, ctx:compiladorParser.CContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#exp.
    def visitExp(self, ctx:compiladorParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#e.
    def visitE(self, ctx:compiladorParser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#term.
    def visitTerm(self, ctx:compiladorParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#t.
    def visitT(self, ctx:compiladorParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#factor.
    def visitFactor(self, ctx:compiladorParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#prototipo.
    def visitPrototipo(self, ctx:compiladorParser.PrototipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametros.
    def visitParametros(self, ctx:compiladorParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listaParametros.
    def visitListaParametros(self, ctx:compiladorParser.ListaParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#parametro.
    def visitParametro(self, ctx:compiladorParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listaID.
    def visitListaID(self, ctx:compiladorParser.ListaIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#llamada.
    def visitLlamada(self, ctx:compiladorParser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#listaArg.
    def visitListaArg(self, ctx:compiladorParser.ListaArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#argumentos.
    def visitArgumentos(self, ctx:compiladorParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#funcion.
    def visitFuncion(self, ctx:compiladorParser.FuncionContext):
        return self.visitChildren(ctx)



del compiladorParser