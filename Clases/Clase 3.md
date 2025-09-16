**Expresiones Regulares**

*Analizar Sintactico Descendiente*

D = Derivar
M= Match

S:(S)S              (())()
    |
    ; 
    $S              (())()$D
    $S)S(           (())()$M
    $S)S             ())()$D
    $S)S)S(          ())()$M
    $S)S)S            ))()$D
    $S)S)             ))()$M
    $S)S               )()$D
    $S)                )()$M
    $S                  ()$D
    $S)S(               ()$M
    $S)S                 )$D
    $S)                  )$M
    $S                    $D
    $                     $OK



    

