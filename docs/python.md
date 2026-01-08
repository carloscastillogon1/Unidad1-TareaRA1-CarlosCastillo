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

    # ==============================
    # CONSTANTES DE FASES
    # ==============================

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
        self.__ingresos = 0.0
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
        self.terminar()

    # ==============================
    # PROPIEDADES (GETTERS)
    # ==============================

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

    # ==============================
    # CONTROL DEL CICLO DE LAVADO
    # ==============================

    def terminar(self):
        """
        Finaliza el ciclo de lavado y deja el lavadero disponible.
        """
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False

    def hacerLavado(self, prelavado_a_mano, secado_a_mano, encerado):
        """
        Inicia un nuevo lavado validando las reglas de negocio.
        """
        if self.__ocupado:
            raise RuntimeError(
                "No se puede iniciar un nuevo lavado mientras el lavadero está ocupado"
            )

        if not secado_a_mano and encerado:
            raise ValueError(
                "No se puede encerar el coche sin secado a mano"
            )

        self.__fase = self.FASE_INACTIVO
        self.__ocupado = True
        self.__prelavado_a_mano = prelavado_a_mano
        self.__secado_a_mano = secado_a_mano
        self.__encerado = encerado

    # ==============================
    # COBRO DEL SERVICIO
    # ==============================

    def _cobrar(self):
        """
        Calcula el coste del lavado y lo suma a los ingresos.
        """
        coste_lavado = 5.00

        if self.__prelavado_a_mano:
            coste_lavado += 1.50

        if self.__secado_a_mano:
            coste_lavado += 1.20

        if self.__encerado:
            coste_lavado += 1.00

        self.__ingresos += coste_lavado
        return coste_lavado

    # ==============================
    # MÁQUINA DE ESTADOS
    # ==============================

    def avanzarFase(self):
        """
        Avanza el lavadero a la siguiente fase.
        """
        if not self.__ocupado:
            return

        if self.__fase == self.FASE_INACTIVO:
            coste = self._cobrar()
            self.__fase = self.FASE_COBRANDO
            print(f"(COBRADO: {coste:.2f} €)", end="")

        elif self.__fase == self.FASE_COBRANDO:
            self.__fase = (
                self.FASE_PRELAVADO_MANO
                if self.__prelavado_a_mano
                else self.FASE_ECHANDO_AGUA
            )

        elif self.__fase == self.FASE_PRELAVADO_MANO:
            self.__fase = self.FASE_ECHANDO_AGUA

        elif self.__fase == self.FASE_ECHANDO_AGUA:
            self.__fase = self.FASE_ENJABONANDO

        elif self.__fase == self.FASE_ENJABONANDO:
            self.__fase = self.FASE_RODILLOS

        elif self.__fase == self.FASE_RODILLOS:
            self.__fase = (
                self.FASE_SECADO_AUTOMATICO
                if self.__secado_a_mano
                else self.FASE_SECADO_MANO
            )

        elif self.__fase in (
            self.FASE_SECADO_AUTOMATICO,
            self.FASE_SECADO_MANO,
            self.FASE_ENCERADO
        ):
            self.terminar()

        else:
            raise RuntimeError(f"Estado no válido: Fase {self.__fase}")

    # ==============================
    # SALIDA POR PANTALLA
    # ==============================

    def imprimir_fase(self):
        """Muestra la fase actual."""
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


