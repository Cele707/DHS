# 
Listener -> Cuando sucede evento de gramatica le avise

Enter del simbolo inicial = primer evento 
Salida del simbolo inicial = ultimo evento

El listener esta siempre pisando el archivo original del listener, por lo que hacemos otro q extiende. No hay q poner todo, solo lo q necesitamos

Cuando entramos en un nodo, no sabemos que hay dentro de la regla. Por lo q pocas acciones pueden hacerse cuando inicia, hay muchas más cuando sale.

La cantidad de hijos depende de la gramatica que hayamos escrito.

-------------------------------------------------------------------------------------------------

Encuentra un bloque (encuentra "{" ) -> Agrega contexto en la tabla de simbolos y luego lo cierra cuando encuentra otro {

Agrego simbolo cuando hay una declaracion, cuando sale exitDeclaracion, nombre con getChild. Va estar en una pila, busca en contexto local y si no existe la agrega

buscarSimbolo busca en contexto local y luego va hacia arriba y se dice error si no esta




