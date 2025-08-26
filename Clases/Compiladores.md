
# Compiladores

**Etapas de compilación:**

Frontend (Independiente del HW) _Lenguaje:_ `C/C++/Fortran` → Middlend (Independiente del Lenguaje y HW) → Backend (Independiente del Lenguaje) _Arquitectura:_ `x86/ARM/MIPS`
                                                       
**Ejemplos compiladores**
- GCC
- Clang
- LLVM

**Sistemas Operativos**
- Linux
- Windows
- MAC OS (compra kernel de FreeBSD)
- Unix → (Free/Open/Net)BSD

*Compilación cruzada (cross-compilation)* → trabajas en un lado, y luego lo ejecutas en otro

**Etapas del compilador**

A lo largo de todas las etapas tiene un controlador de errores y un gestor de tablas de simbolos(guarda los nombres de las variables, tipo, etc)

Etapa de Análisis:
1. _Analizador Léxico:_ Verifica q las palabras en el codigo fuente son palabras del lenguaje. Esta viendo la ortografia, se asegura q se estan cumpliendo las reglas del lenguaje. Recibe string de caracteres y los va separando en los tokens, obteniendo las palablas. → Tokens 

2. _Analizador Sintáctico:_ Verifica el orden de las palabras apropiado al lenguaje, que este bien estructurada por ejemplo: La árbol vuela', esto es correcto ya q esta bien estructurasda (Articulo/Sujeto/Verbo). → Árbol Sintáctico

3. _Analizador Semántico:_ Verifica el significado de las cosas, por ejemplo: 'La arbol vuela`, ahí surge error.

Etapa de Síntesis:

4. _Generador codigo intermedio_: Convertir lenguaje de alto nivel a uno tipo ensamblador.

5. _Optimizador código intermedio_

Antes de esto, todo era más abrastracto pero desde acá es dependiente del HW, ya no es abstracto

6. _Generador códgo objetivo_

7. _Optimizador códgo objetivo_

**No se q titulo es xd**

→ Codigo fuente del programador:

[Ejemplo Código fuente](CompiladoresCodigo.cpp)

→ Preprocesador (Codigo fuente puro) :

Expande cosas como `#define`, `#include`, no verifica errores. Si pongo bibliotecas 


 `gcc -E CompiladoresCodigo.cpp -o compilacionCodigo.i`

[Obtenemos entonces codigo despues del preprocesamiento](compilacionCodigo.i)

→ Compilador (Ensablador Arq. Destino):

 `gcc -S CompiladoresCodigo.cpp -o compilacionCodigo.S`

 [Obtenemos el codigo ensamblador (en Assambly)](compilacionCodigo.S)

 → Ensamblador (Codigo Objeto):

  `gcc -c CompiladoresCodigo.cpp -o compilacionCodigo.o`
 
 [Obtenemos codigo de maquina sin enlazar](compilacionCodigo.o)

 → Linker (Codigo máquina):

 `gcc CompiladoresCodigo.cpp -o compilacionCodigo`

 [Obtenemos el archivo ejecutable](compilacionCodigo)

 Bibliotecas enlazadas de forma dinámica, cuando ejecuto el programa se agrega la informacion para pedir al SO los bibliotecas. 


