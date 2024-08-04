# Computadoras y programas

## Objetivos

- Comprender los respectivos roles del hardware y el software en los sistemas informáticos.

- Aprender qué estudian los informáticos y las técnicas que utilizan. 

- Comprender el diseño básico de una computadora moderna.

- Comprender la forma y función de los lenguajes de programación informática.

- Comenzar a utilizar el lenguaje de programación Python.

- Aprender sobre modelos caóticos y sus implicaciones para la informática.

## 1.1 La máquina universal

Casi todo el mundo ha utilizado una computadora en algún momento. Quizás hayas jugado juegos en ella o la hayas usado para escribir un artículo, comprar en línea, escuchar música o conectarte con tus amigos a través de redes sociales. 

Las computadoras se utilizan para predecir el clima, diseñar aviones, hacer películas, administrar negocios, realizar transacciones financieras y controlar fábricas.
¿Alguna vez te has parado a preguntarte qué es exactamente una computadora? ¿Cómo puede un dispositivo realizar tantas tareas diferentes? Estas preguntas básicas son el punto de partida para aprender sobre computadoras y programación de computadoras.

Una computadora moderna puede definirse como: *"una máquina que almacena y manipula información bajo el control de un programa modificable".* 

Hay dos elementos clave en esta definición: 

- **La primera es que las computadoras son dispositivos para manipular información.** 

- **La segunda es que las computadoras funcionan bajo el control de un programa modificable.**

Comencemos analizando que quiere decir que **las computadoras son dispositivos para manipular información**.

Esto significa que podemos poner información en una computadora, y ésta puede transformarla en formas nuevas y útiles, y luego generar o mostrar la información para nuestra interpretación.

Las computadoras no son las únicas máquinas que manipulan información. Cuando usa una calculadora simple para sumar una columna de números, está ingresando información (los números) y la calculadora procesa la información para calcular una suma acumulada que luego se muestra.



``` mermaid
graph LR
    A(["Los números <sub>(Entrada)</sub>"]) --> B(["Calculos aritméticos <sub>(Proceso)</sub>"]) --> C(["Resultado de la operación <sub>(Salida)</sub>"])
```


Otro ejemplo sencillo es una bomba de gasolina. A medida que llena el tanque, la bomba utiliza ciertas entradas: el precio actual de la gasolina por litro y señales de un sensor que lee la tasa de gasolina que fluye hacia el automóvil. La bomba transforma esta información en información sobre cuánta gasolina consumió y cuánto dinero debe.


``` mermaid
graph LR
    A(["Precio y cantidad de litros <sub>(Entrada)</sub>"]) --> B(["Calculos aritméticos <sub>(Proceso)</sub>"]) --> C(["Total a pagar <sub>(Salida)</sub>"])
```

No consideraríamos ni la calculadora ni el surtidor de gasolina como *computadoras completas*, porque son sistemas diseñados para realizar una tarea única y específica, mientras que una computadora completa **funciona bajo el control de un programa modificable.** ¿Qué significa esto exactamente?

!!! info "¿Qué es un programa?"
    Un **programa** es un conjunto detallado de instrucciones paso a paso que le dicen a una computadora exactamente qué hacer.

Si cambiamos el programa, entonces la computadora realiza una secuencia diferente de acciones y, por lo tanto, realiza una tarea diferente. Es esta flexibilidad la que permite que tu PC sea en un momento un procesador de textos, en el siguiente un planificador financiero y, más tarde, un juego de arcade. La máquina sigue siendo la misma, pero el programa que la controla cambia.

Cada computadora es solo una máquina para ejecutar (realizar) programas. Hay muchos tipos diferentes de computadoras. Es posible que esté familiarizado con Macin toshes, PC, portátiles, tabletas y teléfonos inteligentes, pero hay literalmente miles de otros tipos de computadoras, tanto reales como teóricas. Uno de los descubrimientos notables de la informática es la constatación de que todas estas computadoras diferentes tienen el mismo poder; Con una programación adecuada, cada computadora puede hacer básicamente todas las cosas que cualquier otra computadora puede hacer. En este sentido, la PC que puedas tener sobre tu escritorio es realmente una máquina universal. Puede hacer cualquier cosa que usted desee, siempre que pueda describir la tarea a realizar con suficiente detalle. ¡Esa sí que es una máquina poderosa!