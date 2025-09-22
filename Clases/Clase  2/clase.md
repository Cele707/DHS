# ANTLR

## Expresiones regulares

- . → Cualquier caracter (excepto espacio en blanco)
- ? → 0 o 1 caracteres
- \* → 0 o más caracteres
- \+ → 1 o más caracteres

comando grep →  puede buscar cosas 

`grep -o text.* NombreArchivo`

**Operaciones**
-  a b  → yuxtaposicion 
- a | b → seleccion
- (a b) → agrupacion 
- [a-b] → secuencia, desde a(caracter ascii) hasta b(caracter ascii), tambien puede ser numeros:

`Ejemplo: [00-30] = ([0-2][0-9]) | "30" → 00, 01, 02, ... , 29, 30`

`[-+*/] el - solo es metacaracter al inicio`

`["0"|"1"\t] → " 0 | 1 
- ~a → negacion





