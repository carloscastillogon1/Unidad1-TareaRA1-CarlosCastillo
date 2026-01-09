# En este apartado, lo que vamos a realizar es una serie de test basándonos en el enunciado de la tarea, el cual nos menciona una serie de 14 pruebas.

En la carpeta proporcionada en la tarea, se nos proporciona un ejemplo de test, pero este no nos servirá de mucho, simplemente para fijarnos en como desarrollar
más o menos las pruebas.

Se nos menciona que el código contiene errores, pero estos errores ya los hemos solucionado previamente, lo cual quiere decir que las pruebas no deberían arrojar
ni un solo error, por lo que dichas pruebas nos van a servir para comprobar que el código está perfectamente estructurado.


----

## 14 test basándonos en los enunciados

**1. Cuando se crea un lavadero, éste no tiene ingresos, no está ocupado, está en fase 0 y todas las opciones de lavado
   (prelavado a mano, secado a mano y encerado) están puestas a false.**

   ![Test1](images/test1.png)


**2. Cuando se intenta comprar un lavado con encerado pero sin secado a mano, se produce una ValueError.**

   ![Test2](images/test2.png)

**3. Cuando se intenta hacer un lavado mientras que otro ya está en marcha, se produce una ValueError.**

   ![Test3](images/test3.png)

**4.Si seleccionamos un lavado con prelavado a mano, los ingresos de lavadero son 6,50€.**

   ![Test4](images/test4.png)

**5.Si seleccionamos un lavado con secado a mano, los ingresos son 6,00€.**

   ![Test5](images/test5.png)

**6.Si seleccionamos un lavado con secado a mano y encerado, los ingresos son 7,20€.**

   ![Test6](images/test6.png)

**7.Si seleccionamos un lavado con prelavado a mano y secado a mano, los ingresos son 7,50€.**

   ![Test7](images/test7.png)

**8.Si seleccionamos un lavado con prelavado a mano, secado a mano y encerado, los ingresos son 8,70€.**

   ![Test8](images/test8.png)

**9.Si seleccionamos un lavado sin extras y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 3, 4, 5, 6, 0.**

   ![Test9](images/test9.png)

**10.Si seleccionamos un lavado con prelavado a mano y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 6, 0.**

   ![Test10](images/test10.png)

**11.Si seleccionamos un lavado con secado a mano y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 3, 4, 5, 7, 0.**

   ![Test11](images/test11.png)

**12.Si seleccionamos un lavado con secado a mano y encerado y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 3, 4, 5, 7, 8, 0.**

   ![Test12](images/test12.png)

**13.Si seleccionamos un lavado con prelavado a mano y secado a mano y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 7, 0.**

   ![Test13](images/test13.png)

**14.Si seleccionamos un lavado con prelavado a mano, secado a mano y encerado y vamos avanzando fases, el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 7, 8, 0.**

   ![Test14](images/test14.png)

----
## Ejecución del test

Como he mencionado antes, vamos a ejecutar el test para verificar que todas las corrwcciones que hemos realizado con anterioridad dan solución a todos los problemas.

Para ejecutarlo, abriremos la consola, y escribiremos ***py test_lavadero_unittest.py -v***:

   ![pruebas](images/pruebas.png)

   

