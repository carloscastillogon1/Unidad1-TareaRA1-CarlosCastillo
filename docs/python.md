# Código Python – Simulación de un Lavadero de Coches

## Introducción
Este documento muestra el código comentado del archivo `lavadero.py`.  
El objetivo del programa es **simular el comportamiento de un túnel de lavado de coches**, controlando:

- El estado del lavadero
- Las fases del lavado
- Las reglas de negocio
- El cálculo de ingresos

---

## Conceptos clave del diseño

Antes de analizar el código, es importante comprender los siguientes conceptos:

- El lavadero **solo puede atender a un coche a la vez**
- Cada lavado sigue una **secuencia fija de fases**
- Algunas fases son **opcionales**
- El precio final depende de los servicios seleccionados

---

## Aquí está el Código Comentado

A continuación se muestra el código completo del lavadero, acompañado de
comentarios detallados que explican el funcionamiento de cada parte.

```python
# lavadero.py
class Lavadero:
    """
    Clase que representa un lavadero de coches.
    Controla el estado del lavado, las fases y los ingresos.
    """

    # Constantes de clase que representan las distintas fases del lavado
    FASE_INACTIVO = 0
    FASE_COBRANDO = 1
    FASE_PRELAVADO_MANO = 2
    FASE_ECHANDO_AGUA = 3
    FASE_ENJABONANDO = 4
    FASE_RODILLOS = 5
    FASE_SECADO_AUTOMATICO = 6
    FASE_SECADO_MANO = 7
    FASE_ENCERADO = 8

    def __init__(self):
        """
        Constructor de la clase.
        Se ejecuta automáticamente al crear un objeto Lavadero.
        Inicializa los atributos del objeto.
        """

        # Atributo privado que guarda el total de ingresos del lavadero
        self.__ingresos = 0.0

        # Atributo privado que indica la fase actual del lavado
        self.__fase = self.FASE_INACTIVO

        # Indica si el lavadero está ocupado o no
        self.__ocupado = False

        # Opciones del lavado (todas empiezan desactivadas)
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False

        # Se asegura de que el lavadero empieza en estado inactivo
        self.terminar()

    # Propiedad que permite consultar la fase actual sin modificarla
    @property
    def fase(self):
        return self.__fase

    # Propiedad que devuelve los ingresos acumulados
    @property
    def ingresos(self):
        return self.__ingresos

    # Propiedad que indica si el lavadero está ocupado
    @property
    def ocupado(self):
        return self.__ocupado
    
    # Propiedad que indica si se ha elegido prelavado a mano
    @property
    def prelavado_a_mano(self):
        return self.__prelavado_a_mano

    # Propiedad que indica si se ha elegido secado a mano
    @property
    def secado_a_mano(self):
        return self.__secado_a_mano

    # Propiedad que indica si se ha elegido encerado
    @property
    def encerado(self):
        return self.__encerado

    def terminar(self):
        """
        Método que finaliza el lavado y reinicia el estado del lavadero.
        """

        # Se vuelve a la fase inactiva
        self.__fase = self.FASE_INACTIVO

        # El lavadero deja de estar ocupado
        self.__ocupado = False

        # Se desactivan todas las opciones del lavado
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
    
    def hacerLavado(self, prelavado_a_mano, secado_a_mano, encerado):
        """
        Inicia un nuevo lavado.
        Comprueba que se cumplan las reglas del negocio antes de empezar.
        """

        # Si el lavadero ya está ocupado, no se puede iniciar otro lavado
        if self.__ocupado:
            raise RuntimeError("No se puede iniciar un nuevo lavado mientras el lavadero está ocupado")
        
        # No se permite encerar si no se ha seleccionado secado a mano
        if not secado_a_mano and encerado:
            raise ValueError("No se puede encerar el coche sin secado a mano")
        
        # Se inicia el lavado poniendo el lavadero como ocupado
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = True

        # Se guardan las opciones elegidas para este lavado
        self.__prelavado_a_mano = prelavado_a_mano
        self.__secado_a_mano = secado_a_mano
        self.__encerado = encerado

    def _cobrar(self):
        """
        Método interno que calcula el precio del lavado
        y suma el importe a los ingresos del lavadero.
        """

        # Precio base del lavado
        coste_lavado = 5.00
        
        # Si se ha elegido prelavado a mano, se suma su coste
        if self.__prelavado_a_mano:
            coste_lavado += 1.50 
        
        # Si se ha elegido secado a mano, se suma su coste
        if self.__secado_a_mano:
            coste_lavado += 1.20 
            
        # Si se ha elegido encerado, se suma su coste
        if self.__encerado:
            coste_lavado += 1.00 
        
        # Se añade el coste total a los ingresos acumulados
        self.__ingresos += coste_lavado

        # Se devuelve el coste del lavado actual
        return coste_lavado

    def avanzarFase(self):
        """
        Avanza el lavado a la siguiente fase según el estado actual.
        """

        # Si el lavadero no está ocupado, no se hace nada
        if not self.__ocupado:
            return

        # Fase inicial: se cobra el lavado
        if self.__fase == self.FASE_INACTIVO:
            coste_cobrado = self._cobrar()
            self.__fase = self.FASE_COBRANDO
            print(f" (COBRADO: {coste_cobrado:.2f} €) ", end="")

        # Después de cobrar, se decide si hay prelavado a mano
        elif self.__fase == self.FASE_COBRANDO:
            if self.__prelavado_a_mano:
                self.__fase = self.FASE_PRELAVADO_MANO
            else:
                self.__fase = self.FASE_ECHANDO_AGUA 
        
        # Transiciones entre fases del lavado
        elif self.__fase == self.FASE_PRELAVADO_MANO:
            self.__fase = self.FASE_ECHANDO_AGUA
        
        elif self.__fase == self.FASE_ECHANDO_AGUA:
            self.__fase = self.FASE_ENJABONANDO

        elif self.__fase == self.FASE_ENJABONANDO:
            self.__fase = self.FASE_RODILLOS
        
        elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_AUTOMATICO
            else:
                self.__fase = self.FASE_SECADO_MANO
        
        # Al terminar el secado, el lavado finaliza
        elif self.__fase == self.FASE_SECADO_AUTOMATICO:
            self.terminar()
        
        elif self.__fase == self.FASE_SECADO_MANO:
            self.terminar()
        
        elif self.__fase == self.FASE_ENCERADO:
            self.terminar()
        
        # Control de errores por si aparece un estado no válido
        else:
            raise RuntimeError(f"Estado no válido: Fase {self.__fase}")

    def imprimir_fase(self):
        """
        Muestra por pantalla el nombre de la fase actual.
        """

        # Diccionario que relaciona cada fase con un texto descriptivo
        fases_map = {
            self.FASE_INACTIVO: "0 - Inactivo",
            self.FASE_COBRANDO: "1 - Cobrando",
            self.FASE_PRELAVADO_MANO: "2 - Haciendo prelavado a mano",
            self.FASE_ECHANDO_AGUA: "3 - Echándole agua",
            self.FASE_ENJABONANDO: "4 - Enjabonando",
            self.FASE_RODILLOS: "5 - Pasando rodillos",
            self.FASE_SECADO_AUTOMATICO: "6 - Haciendo secado automático",
            self.FASE_SECADO_MANO: "7 - Haciendo secado a mano",
            self.FASE_ENCERADO: "8 - Encerando a mano",
        }

        # Se imprime la fase actual
        print(fases_map.get(self.__fase, "Estado no válido"), end="")

    def imprimir_estado(self):
        """
        Imprime por pantalla el estado completo del lavadero.
        """

        print("----------------------------------------")
        print(f"Ingresos Acumulados: {self.ingresos:.2f} €")
        print(f"Ocupado: {self.ocupado}")
        print(f"Prelavado a mano: {self.prelavado_a_mano}")
        print(f"Secado a mano: {self.secado_a_mano}")
        print(f"Encerado: {self.encerado}")
        print("Fase: ", end="")
        self.imprimir_fase()
        print("\n----------------------------------------")


    # MÉTODO AUXILIAR PARA PRUEBAS / TESTS: Este método NO forma parte del funcionamiento real del lavadero. Su único propósito es facilitar pruebas unitarias y
    # comprobaciones automáticas del flujo de estados del sistema.

    def ejecutar_y_obtener_fases(self, prelavado, secado, encerado):
        """
        Ejecuta un ciclo completo de lavado y devuelve
        una lista con todas las fases visitadas.

        Este método es muy útil para:
        - Verificar que el flujo de estados es correcto
        - Detectar errores en la máquina de estados
        - Realizar pruebas unitarias automatizadas

        Parámetros:
        - prelavado: indica si hay prelavado a mano
        - secado: indica si hay secado a mano
        - encerado: indica si hay encerado

        Retorna:
        - Lista de enteros con las fases visitadas
        """

        # Se inicia el lavado con las opciones indicadas
        self.hacerLavado(prelavado, secado, encerado)

        # Se guarda la fase inicial
        fases_visitadas = [self.fase]

        # Mientras el lavadero esté ocupado, seguimos avanzando fases
        while self.ocupado:

            # Medida de seguridad para evitar bucles infinitos
            # en caso de que exista un error en la lógica
            if len(fases_visitadas) > 15:
                raise Exception(
                    "Bucle infinito detectado en la simulación de fases."
                )

            # Avanzamos a la siguiente fase
            self.avanzarFase()

            # Guardamos la nueva fase alcanzada
            fases_visitadas.append(self.fase)

        # Devolvemos la lista completa de fases recorridas
        return fases_visitadas





