grammar compilador;
// =========================================
// REGLAS LÉXICAS 
// =========================================
fragment LETRA  : [A-Za-z] ;
fragment DIGITO : [0-9] ;

NUMERO: DIGITO+;

//Enteros (positivos y negativos)
ENTERO : '-'? DIGITO+ ;

//Palabras reservadas
INT : 'int' ;
DOUBLE : 'double' ;
IF    : 'if' ;
ELSE  : 'else' ;
FOR   : 'for' ;
WHILE : 'while' ;
RETURN : 'return' ;

//Operadores
SUMA : '+' ;
RESTA : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
ASIG : '=' ;
//comparadores
MENOR : '<' ;
MAYOR : '>' ;
MENOR_IGUAL : '<=' ;
MAYOR_IGUAL : '>=' ;
IGUAL : '==' ;
DIFERENTE : '!=' ;
//operadores logicos
AND : '&&' ;
OR  : '||' ;
NOT : '!' ; 
//
INC : '++' ;
DEC : '--' ;

//Caracteres 
PA  : '(' ;
PC  : ')' ;
LLA : '{' ;
LLC : '}' ;
CA  : '[' ;
CC  : ']' ;
PYC : ';' ;

//Identificadores (variables y funciones)
ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

// Extras (coma, espacios, etc.)
COMA : ',' ;
WS : [ \n\r\t] -> skip ;
OTRO : . ;

// =========================================
// REGLAS GRAMATICALES PRINCIPALES
// =========================================
programa 
    : instrucciones EOF 
    ;

instrucciones 
    : instruccion instrucciones
    |                            
    ;

instruccion 
    : asignacion
    | declaracion
    | iif
    | iwhile
    | ifor
    | bloque
    | ireturn
    | prototipo
    | funcion
    | llamada_funcion PYC  
    ;
    
////////////////////////////////////////////////
//RECONOCIMIENTO DE BLOQUE DE CODIGO
////////////////////////////////////////////////
bloque
    : LLA instrucciones LLC
    ;

////////////////////////////////////////////////
//DECLARACIONES
////////////////////////////////////////////////
// Declaración de variables
declaracion 
    : tipo ID inicializador listavar PYC 
    ;
inicializador
    : ASIG opalc
    |
    ;

listavar 
    : COMA ID inicializador listavar 
    | 
    ;

// Tipos básicos
tipo 
    : INT 
    | DOUBLE 
    ;

////////////////////////////////////////////////
//ASIGNACIONES
////////////////////////////////////////////////
asignacion 
    : ID ASIG opalc PYC 
    ;

////////////////////////////////////////////////
// ESTRUCTURA DE CONTROL
////////////////////////////////////////////////
// While
iwhile 
    : WHILE PA opalc PC instruccion 
    ;

//If / else 
iif 
    : IF PA opalc PC instruccion ielse 
    ;

ielse 
    : ELSE instruccion 
    | // vacío (epsilon)
    ;

//For
ifor 
    : FOR PA forInit PYC forCond PYC forUpdate PC instruccion 
    ;

// Inicialización: puede ser una declaración o una asignación
forInit 
    : declaracion 
    | asignacion 
    ;

// Condición: una expresión (por ahora opalc)
forCond 
    : opalc
    ;

// Actualización: una asignación
forUpdate 
    : asignacion 
    ;


////////////////////////////////////////////////
// OPERACIONES ARITMETICOLOGICAS
////////////////////////////////////////////////
// La regla principal, debido a q es descendiente, primero van los de menor presecedencia que son los logicos
opalc
    : exp_l
    ;

// Expresiones Lógicas (precedencia más baja: ||, &&)
exp_l
    : exp_comp exp_l_prima
    ;

exp_l_prima
    : OR exp_comp exp_l_prima
    | AND exp_comp exp_l_prima
    |
    ;

// Expresiones de Comparación (<, >, ==, !=, etc.)
exp_comp
    : exp_a exp_comp_prima
    ;

exp_comp_prima
    : MENOR exp_a exp_comp_prima
    | MAYOR exp_a exp_comp_prima
    | MENOR_IGUAL exp_a exp_comp_prima
    | MAYOR_IGUAL exp_a exp_comp_prima
    | IGUAL exp_a exp_comp_prima
    | DIFERENTE exp_a exp_comp_prima
    |
    ;

// Expresiones Aritméticas (+, -)
exp_a
    : term exp_a_prima
    ;

exp_a_prima
    : SUMA term exp_a_prima
    | RESTA term exp_a_prima
    |
    ;

// Términos (*, /, %)
term
    : factor term_prima
    ;

term_prima
    : MULT factor term_prima
    | DIV factor term_prima
    | MOD factor term_prima
    |
    ;

// Factores (números, IDs, paréntesis, operadores unarios)
factor
    : NUMERO
    | llamada_funcion // Nueva regla
    | ID // Mantienes ID para variables
    | PA exp_l PC
    | NOT factor
    | RESTA factor
    | INC factor
    | DEC factor
    ;

////////////////////////////////////////////////
// FUNCIONES
////////////////////////////////////////////////
// Prototipo
prototipo
    : tipo ID PA lista_parametros PC PYC
    ;

// Definición
funcion
    : tipo ID PA lista_parametros PC bloque
    ;

lista_parametros
    : parametros        // Opción 1: la lista no está vacía
    |                   // Opción 2: la lista está vacía
    ;

parametros
    : tipo ID parametros_prima // El primer parámetro
    |
    ;

parametros_prima
    : COMA tipo ID parametros_prima // El resto de los parámetros
    |                               // Fin de la lista
    ;

//Llamada
llamada_funcion
    : ID PA lista_argumentos PC
    ;

lista_argumentos
    : argumentos        // Opción 1: la lista no está vacía
    |                   // Opción 2: la lista está vacía
    ;
argumentos
    : opalc argumentos_prima // El primer argumento
    |
    ;
argumentos_prima
    : COMA opalc argumentos_prima // El resto de los argumentos
    |                             // Fin de la lista
    ;
// Return
ireturn
    : RETURN opalc PYC
    ;

