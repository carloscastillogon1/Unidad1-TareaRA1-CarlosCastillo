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
class Lavadero:
    """
    Clase que representa un túnel de lavado de coches.

    Se encarga de:
    - Controlar el estado interno del lavadero
    - Gestionar las fases del lavado
    - Validar reglas de negocio
    - Calcular y acumular los ingresos

    El flujo del lavado se controla mediante una máquina de estados.
    """

    # CONSTANTES DE FASES, cada constante representa una fase del proceso de lavado.


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
        Constructor de la clase Lavadero.

        Inicializa todas las variables internas del sistema.
        El lavadero comienza sin coches y sin ingresos.
        """

        # Dinero total acumulado por los lavados realizados
        self.__ingresos = 0.0

        # Fase actual del lavadero
        self.__fase = self.FASE_INACTIVO

        # Indica si el lavadero está ocupado por un coche
        self.__ocupado = False

        # Opciones del lavado actual
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False

        # Se fuerza el estado inicial correcto
        self.terminar()

    # PROPIEDADES: Permiten consultar el estado del lavadero sin permitir modificaciones externas.

    @property
    def fase(self):
        """Devuelve la fase actual del lavadero."""
        return self.__fase

    @property
    def ingresos(self):
        """Devuelve los ingresos acumulados."""
        return self.__ingresos

    @property
    def ocupado(self):
        """Indica si el lavadero está ocupado."""
        return self.__ocupado

    @property
    def prelavado_a_mano(self):
        """Indica si el lavado incluye prelavado a mano."""
        return self.__prelavado_a_mano

    @property
    def secado_a_mano(self):
        """Indica si el lavado incluye secado a mano."""
        return self.__secado_a_mano

    @property
    def encerado(self):
        """Indica si el lavado incluye encerado."""
        return self.__encerado

    # CONTROL DEL CICLO DE LAVADO

    def terminar(self):
        """
        Finaliza el ciclo de lavado.

        Se usa cuando el coche ha terminado todas las fases.
        El lavadero vuelve a quedar disponible.
        """
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False

    def hacerLavado(self, prelavado_a_mano, secado_a_mano, encerado):
        """
        Inicia un nuevo ciclo de lavado.

        Parámetros:
        - prelavado_a_mano
        - secado_a_mano
        - encerado

        Reglas de negocio:
        - No se puede iniciar un lavado si el lavadero está ocupado
        - No se puede encerar sin secado a mano
        """

        # Regla 1: solo un coche a la vez
        if self.__ocupado:
            raise RuntimeError(
                "No se puede iniciar un nuevo lavado mientras el lavadero está ocupado"
            )

        # Regla 2: no se permite encerado sin secado a mano
        if not secado_a_mano and encerado:
            raise ValueError(
                "No se puede encerar el coche sin secado a mano"
            )

        # Se inicia el ciclo de lavado
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = True
        self.__prelavado_a_mano = prelavado_a_mano
        self.__secado_a_mano = secado_a_mano
        self.__encerado = encerado

    # COBRO DEL SERVICIO

    def _cobrar(self):
        """
        Calcula el coste del lavado según los servicios seleccionados.

        Precio base: 5.00 €
        Extras:
        - Prelavado a mano: +1.50 €
        - Secado a mano: +1.20 €
        - Encerado: +1.00 €

        Devuelve el importe cobrado.
        """
        coste_lavado = 5.00

        if self.__prelavado_a_mano:
            coste_lavado += 1.50

        if self.__secado_a_mano:
            coste_lavado += 1.20

        if self.__encerado:
            coste_lavado += 1.00

        # Se suman los ingresos al total
        self.__ingresos += coste_lavado
        return coste_lavado

    # MÁQUINA DE ESTADOS

    def avanzarFase(self):
        """
        Avanza el lavadero a la siguiente fase del proceso.

        Este método debe llamarse repetidamente para simular
        el avance del coche dentro del túnel de lavado.
        """

        # Si no hay coche, no se hace nada
        if not self.__ocupado:
            return

        # Fase 0: Cobro
        if self.__fase == self.FASE_INACTIVO:
            coste = self._cobrar()
            self.__fase = self.FASE_COBRANDO
            print(f"(COBRADO: {coste:.2f} €)", end="")

        # Fase 1: Prelavado o agua
        elif self.__fase == self.FASE_COBRANDO:
            if self.__prelavado_a_mano:
                self.__fase = self.FASE_PRELAVADO_MANO
            else:
                self.__fase = self.FASE_ECHANDO_AGUA

        # Fase 2: Agua
        elif self.__fase == self.FASE_PRELAVADO_MANO:
            self.__fase = self.FASE_ECHANDO_AGUA

        # Fase 3: Jabón
        elif self.__fase == self.FASE_ECHANDO_AGUA:
            self.__fase = self.FASE_ENJABONANDO

        # Fase 4: Rodillos
        elif self.__fase == self.FASE_ENJABONANDO:
            self.__fase = self.FASE_RODILLOS

        # Fase 5: Secado
        elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_AUTOMATICO
            else:
                self.__fase = self.FASE_SECADO_MANO

        # Fases finales: Terminar
        elif self.__fase in (
            self.FASE_SECADO_AUTOMATICO,
            self.FASE_SECADO_MANO,
            self.FASE_ENCERADO
        ):
            self.terminar()

        else:
            raise RuntimeError(f"Estado no válido: Fase {self.__fase}")

    # MÉTODOS DE SALIDA

    def imprimir_fase(self):
        """Muestra por pantalla la fase actual."""
        fases_map = {
            self.FASE_INACTIVO: "0 - Inactivo",
            self.FASE_COBRANDO: "1 - Cobrando",
            self.FASE_PRELAVADO_MANO: "2 - Prelavado a mano",
            self.FASE_ECHANDO_AGUA: "3 - Echando agua",
            self.FASE_ENJABONANDO: "4 - Enjabonando",
            self.FASE_RODILLOS: "5 - Rodillos",
            self.FASE_SECADO_AUTOMATICO: "6 - Secado automático",
            self.FASE_SECADO_MANO: "7 - Secado a mano",
            self.FASE_ENCERADO: "8 - Encerado",
        }
        print(fases_map.get(self.__fase, "Estado no válido"), end="")

    def imprimir_estado(self):
        """Imprime el estado completo del lavadero."""
        print("----------------------------------------")
        print(f"Ingresos acumulados: {self.ingresos:.2f} €")
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




