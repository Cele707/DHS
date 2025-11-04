# Generated from /home/cele/Repositorios Git/DHS/Practicos/Practico2/src/main/python/compilador.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete listener for a parse tree produced by compiladorParser.
class compiladorListener(ParseTreeListener):

    # Enter a parse tree produced by compiladorParser#s.
    def enterS(self, ctx:compiladorParser.SContext):
        pass

    # Exit a parse tree produced by compiladorParser#s.
    def exitS(self, ctx:compiladorParser.SContext):
        pass


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


    # Enter a parse tree produced by compiladorParser#forInicializacion.
    def enterForInicializacion(self, ctx:compiladorParser.ForInicializacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#forInicializacion.
    def exitForInicializacion(self, ctx:compiladorParser.ForInicializacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaExpASIG.
    def enterListaExpASIG(self, ctx:compiladorParser.ListaExpASIGContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaExpASIG.
    def exitListaExpASIG(self, ctx:compiladorParser.ListaExpASIGContext):
        pass


    # Enter a parse tree produced by compiladorParser#forCond.
    def enterForCond(self, ctx:compiladorParser.ForCondContext):
        pass

    # Exit a parse tree produced by compiladorParser#forCond.
    def exitForCond(self, ctx:compiladorParser.ForCondContext):
        pass


    # Enter a parse tree produced by compiladorParser#forActualizacion.
    def enterForActualizacion(self, ctx:compiladorParser.ForActualizacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#forActualizacion.
    def exitForActualizacion(self, ctx:compiladorParser.ForActualizacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaActualizacion.
    def enterListaActualizacion(self, ctx:compiladorParser.ListaActualizacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaActualizacion.
    def exitListaActualizacion(self, ctx:compiladorParser.ListaActualizacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#ireturn.
    def enterIreturn(self, ctx:compiladorParser.IreturnContext):
        pass

    # Exit a parse tree produced by compiladorParser#ireturn.
    def exitIreturn(self, ctx:compiladorParser.IreturnContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracion.
    def enterDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracion.
    def exitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladorParser#tipo.
    def enterTipo(self, ctx:compiladorParser.TipoContext):
        pass

    # Exit a parse tree produced by compiladorParser#tipo.
    def exitTipo(self, ctx:compiladorParser.TipoContext):
        pass


    # Enter a parse tree produced by compiladorParser#listavar.
    def enterListavar(self, ctx:compiladorParser.ListavarContext):
        pass

    # Exit a parse tree produced by compiladorParser#listavar.
    def exitListavar(self, ctx:compiladorParser.ListavarContext):
        pass


    # Enter a parse tree produced by compiladorParser#inic.
    def enterInic(self, ctx:compiladorParser.InicContext):
        pass

    # Exit a parse tree produced by compiladorParser#inic.
    def exitInic(self, ctx:compiladorParser.InicContext):
        pass


    # Enter a parse tree produced by compiladorParser#expASIG.
    def enterExpASIG(self, ctx:compiladorParser.ExpASIGContext):
        pass

    # Exit a parse tree produced by compiladorParser#expASIG.
    def exitExpASIG(self, ctx:compiladorParser.ExpASIGContext):
        pass


    # Enter a parse tree produced by compiladorParser#asignacion.
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#asignacion.
    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#opal.
    def enterOpal(self, ctx:compiladorParser.OpalContext):
        pass

    # Exit a parse tree produced by compiladorParser#opal.
    def exitOpal(self, ctx:compiladorParser.OpalContext):
        pass


    # Enter a parse tree produced by compiladorParser#expOR.
    def enterExpOR(self, ctx:compiladorParser.ExpORContext):
        pass

    # Exit a parse tree produced by compiladorParser#expOR.
    def exitExpOR(self, ctx:compiladorParser.ExpORContext):
        pass


    # Enter a parse tree produced by compiladorParser#o.
    def enterO(self, ctx:compiladorParser.OContext):
        pass

    # Exit a parse tree produced by compiladorParser#o.
    def exitO(self, ctx:compiladorParser.OContext):
        pass


    # Enter a parse tree produced by compiladorParser#expAND.
    def enterExpAND(self, ctx:compiladorParser.ExpANDContext):
        pass

    # Exit a parse tree produced by compiladorParser#expAND.
    def exitExpAND(self, ctx:compiladorParser.ExpANDContext):
        pass


    # Enter a parse tree produced by compiladorParser#a.
    def enterA(self, ctx:compiladorParser.AContext):
        pass

    # Exit a parse tree produced by compiladorParser#a.
    def exitA(self, ctx:compiladorParser.AContext):
        pass


    # Enter a parse tree produced by compiladorParser#expIGUAL.
    def enterExpIGUAL(self, ctx:compiladorParser.ExpIGUALContext):
        pass

    # Exit a parse tree produced by compiladorParser#expIGUAL.
    def exitExpIGUAL(self, ctx:compiladorParser.ExpIGUALContext):
        pass


    # Enter a parse tree produced by compiladorParser#i.
    def enterI(self, ctx:compiladorParser.IContext):
        pass

    # Exit a parse tree produced by compiladorParser#i.
    def exitI(self, ctx:compiladorParser.IContext):
        pass


    # Enter a parse tree produced by compiladorParser#expCOMP.
    def enterExpCOMP(self, ctx:compiladorParser.ExpCOMPContext):
        pass

    # Exit a parse tree produced by compiladorParser#expCOMP.
    def exitExpCOMP(self, ctx:compiladorParser.ExpCOMPContext):
        pass


    # Enter a parse tree produced by compiladorParser#c.
    def enterC(self, ctx:compiladorParser.CContext):
        pass

    # Exit a parse tree produced by compiladorParser#c.
    def exitC(self, ctx:compiladorParser.CContext):
        pass


    # Enter a parse tree produced by compiladorParser#exp.
    def enterExp(self, ctx:compiladorParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladorParser#exp.
    def exitExp(self, ctx:compiladorParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladorParser#e.
    def enterE(self, ctx:compiladorParser.EContext):
        pass

    # Exit a parse tree produced by compiladorParser#e.
    def exitE(self, ctx:compiladorParser.EContext):
        pass


    # Enter a parse tree produced by compiladorParser#term.
    def enterTerm(self, ctx:compiladorParser.TermContext):
        pass

    # Exit a parse tree produced by compiladorParser#term.
    def exitTerm(self, ctx:compiladorParser.TermContext):
        pass


    # Enter a parse tree produced by compiladorParser#t.
    def enterT(self, ctx:compiladorParser.TContext):
        pass

    # Exit a parse tree produced by compiladorParser#t.
    def exitT(self, ctx:compiladorParser.TContext):
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


    # Enter a parse tree produced by compiladorParser#parametros.
    def enterParametros(self, ctx:compiladorParser.ParametrosContext):
        pass

    # Exit a parse tree produced by compiladorParser#parametros.
    def exitParametros(self, ctx:compiladorParser.ParametrosContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaParametros.
    def enterListaParametros(self, ctx:compiladorParser.ListaParametrosContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaParametros.
    def exitListaParametros(self, ctx:compiladorParser.ListaParametrosContext):
        pass


    # Enter a parse tree produced by compiladorParser#parametro.
    def enterParametro(self, ctx:compiladorParser.ParametroContext):
        pass

    # Exit a parse tree produced by compiladorParser#parametro.
    def exitParametro(self, ctx:compiladorParser.ParametroContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaID.
    def enterListaID(self, ctx:compiladorParser.ListaIDContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaID.
    def exitListaID(self, ctx:compiladorParser.ListaIDContext):
        pass


    # Enter a parse tree produced by compiladorParser#llamada.
    def enterLlamada(self, ctx:compiladorParser.LlamadaContext):
        pass

    # Exit a parse tree produced by compiladorParser#llamada.
    def exitLlamada(self, ctx:compiladorParser.LlamadaContext):
        pass


    # Enter a parse tree produced by compiladorParser#listaArg.
    def enterListaArg(self, ctx:compiladorParser.ListaArgContext):
        pass

    # Exit a parse tree produced by compiladorParser#listaArg.
    def exitListaArg(self, ctx:compiladorParser.ListaArgContext):
        pass


    # Enter a parse tree produced by compiladorParser#argumentos.
    def enterArgumentos(self, ctx:compiladorParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by compiladorParser#argumentos.
    def exitArgumentos(self, ctx:compiladorParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by compiladorParser#funcion.
    def enterFuncion(self, ctx:compiladorParser.FuncionContext):
        pass

    # Exit a parse tree produced by compiladorParser#funcion.
    def exitFuncion(self, ctx:compiladorParser.FuncionContext):
        pass



del compiladorParser