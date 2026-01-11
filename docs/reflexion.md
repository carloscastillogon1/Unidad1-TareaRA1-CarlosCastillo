## Reflexión personal: Comparación de la infraestructura de seguridad de los lenguajes


Después de desarrollar esta aplicación y estudiar la teoría, queda claro que la seguridad de un programa empieza por el lenguaje que elegimos. No todos los
lenguajes protegen el sistema de la misma forma:

1. **La gestión de la memoria**

   
Existen lenguajes como C o C++ donde el programador tiene el control total de la memoria del ordenador. Esto los hace muy rápidos, pero también muy peligrosos. 
Un error común, como el desbordamiento de búfer, puede permitir que un atacante tome el control del sistema. Si se hubiera programado el lavadero en C, cualquier
falloal introducir datos podría haber bloqueado la máquina.

En cambio, Python (el lenguaje que se ha usado) gestiona la memoria de forma automática. Tiene un sistema llamado Garbage Collector que se encarga de limpiar lo
que no se usa y evita que el programador cometa esos errores graves de memoria. Por eso se dice que es un lenguaje "seguro de memoria".

2. **Lenguajes modernos y seguros (Rust)**

   
Es interesante mencionar lenguajes más nuevos como Rust. Este lenguaje intenta se superior a los dos antes mencionados: es tan rápido como C pero mucho más seguro.
Su diseño impide que el programa se ejecute si detecta que hay un riesgo de seguridad en la memoria. Es una opción que se está usando mucho hoy en día para
infraestructuras críticas.


3. **Tipado de datos**

   
También influye cómo el lenguaje trata los datos:

- **Lenguajes como Python:** Son flexibles, pero a veces los errores de tipo aparecen solo cuando el programa ya se está ejecutando
  (por ejemplo, si el usuario escribe letras donde se espera un número).

- **Lenguajes como Java:** Son más estrictos y te obligan a definir cada dato desde el principio, lo que ayuda a evitar fallos lógicos antes de que el programa se
  ponga en marcha.

## Conclusión final

En mi opinión, ningún lenguaje es 100% invulnerable, pero usar Python facilita mucho crear un código robusto. Me ha permitido centrarme en los errores del
usuario (el manejo de excepciones) sin tener que preocuparme por fallos complejos del sistema operativo.

Sin embargo, lo más importante que nos enseña esta práctica es que la seguridad debe ir por capas. Aunque usemos un lenguaje seguro como Python, es necesario usar 
herramientas extras como, por ejemplo, alguna Sandbox. La combinación de un lenguaje con gestión automática de memoria y un entorno aislado por contenedores es lo
que realmente nos ha garantizado una puesta en producción segura en esta práctica.

