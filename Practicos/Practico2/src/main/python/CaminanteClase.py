from compiladorVisitor import compiladorVisitor
from compiladorParser import compiladorParser

class CaminanteClase(compiladorVisitor):
    def __init__(self):
        self.instr = 0

    def visitPrograma(self, ctx:compiladorParser.ProgramaContext):
        print("Programa procesado")
        return self.visitChildren(ctx)
    
    def visitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        self.instr += 1
        print("Intrsuccion " + str(self.instr))
        print("\t" + ctx.getText())
        return self.visitChildren(ctx)
    