# Primera app con Flask del curso de Udemy

# REST
Es una forma de pensar acerca de cómo responde un servidor

#### No sólo responde con datos
Responde con recursos - dependiendo del request pertinente.

## Stateless
Un request no puede depender de otro request.
El servidor sólo sabe/conoce acerca del request en curso, no de requests anteriores.

Ej: se hace post de un nuevo item. Se guarda en la base de datos y ya. El servidor lo deja en la base de datos y "se olvida".
Dicho de otra manera, no guarda info al respecto de nada. Siempre debe consultar la base de datos.
