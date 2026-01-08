# lavadero.py

class Lavadero:
    """
    Clase encargada de gestionar el ciclo de vida y la lógica de negocio de un túnel de lavado.
    Implementa el control de estados, la gestión de ingresos y la validación de servicios.
    """

    # Definición de constantes para representar los estados del sistema.
    # El uso de constantes facilita el mantenimiento y evita errores por tipos de datos mágicos.
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
        Constructor de la clase. Inicializa los atributos privados y asegura que
        el sistema comience en un estado consistente (Inactivo y sin ingresos).
        """
        self.__ingresos = 0.0
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
        self.terminar() 

    # Implementación de decoradores @property para garantizar el encapsulamiento.
    # Permiten el acceso de solo lectura a los atributos privados desde el exterior.
    @property
    def fase(self):
        return self.__fase

    @property
    def ingresos(self):
        return self.__ingresos

    @property
    def ocupado(self):
        return self.__ocupado
    
    @property
    def prelavado_a_mano(self):
        return self.__prelavado_a_mano

    @property
    def secado_a_mano(self):
        return self.__secado_a_mano

    @property
    def encerado(self):
        return self.__encerado

    def terminar(self):
        """
        Restablece todos los parámetros operativos del lavadero a sus valores por defecto,
        finalizando cualquier proceso activo.
        """
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
    
    def hacerLavado(self, prelavado_a_mano, secado_a_mano, encerado):
        """
        Configura e inicia un nuevo proceso de lavado tras validar las reglas de negocio.
        
        :raises RuntimeError: Si se intenta iniciar un servicio estando el sistema ocupado.
        :raises ValueError: Si la combinación de servicios seleccionada es incompatible.
        """
        # Validación de disponibilidad del sistema (Requisito 3).
        if self.__ocupado:
            raise RuntimeError("No se puede iniciar un nuevo lavado mientras el lavadero está ocupado")
        
        # Validación de dependencia de servicios (Requisito 2: Encerado requiere secado manual).
        if not secado_a_mano and encerado:
            raise ValueError("No se puede encerar el coche sin secado a mano")
        
        self.__fase = self.FASE_INACTIVO  
        self.__ocupado = True
        self.__prelavado_a_mano = prelavado_a_mano
        self.__secado_a_mano = secado_a_mano
        self.__encerado = encerado
        

    def _cobrar(self):
        """
        Método interno para el cálculo de tarifas según los servicios adicionales contratados.
        Aplica los costes estipulados y actualiza el acumulado de ingresos globales.
        """
        coste_lavado = 5.00 # Tarifa base estándar.
        
        if self.__prelavado_a_mano:
            coste_lavado += 1.50 # Suplemento por prelavado manual.
        
        if self.__secado_a_mano:
            coste_lavado += 1.20 # Suplemento por secado manual.
            
        if self.__encerado:
            coste_lavado += 1.00 # Suplemento por encerado.
            
        self.__ingresos += coste_lavado
        return coste_lavado

    def avanzarFase(self):
        """
        Gestiona la transición de estados dentro del flujo de trabajo del lavadero.
        Controla la secuencia lógica del proceso en función de la configuración inicial.
        """
        if not self.__ocupado:
            return

        # Inicio del flujo: Transición de inactividad a facturación.
        if self.__fase == self.FASE_INACTIVO:
            coste_cobrado = self._cobrar()
            self.__fase = self.FASE_COBRANDO
            print(f" (COBRADO: {coste_cobrado:.2f} €) ", end="")

        # Determinación de la siguiente etapa tras el cobro.
        elif self.__fase == self.FASE_COBRANDO:
            if self.__prelavado_a_mano:
                self.__fase = self.FASE_PRELAVADO_MANO
            else:
                self.__fase = self.FASE_ECHANDO_AGUA 
        
        elif self.__fase == self.FASE_PRELAVADO_MANO:
            self.__fase = self.FASE_ECHANDO_AGUA
        
        elif self.__fase == self.FASE_ECHANDO_AGUA:
            self.__fase = self.FASE_ENJABONANDO

        elif self.__fase == self.FASE_ENJABONANDO:
            self.__fase = self.FASE_RODILLOS
        
        # Bifurcación del flujo según el tipo de secado seleccionado.
        elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_AUTOMATICO 
            else:
                self.__fase = self.FASE_SECADO_MANO
        
        # Estados finales que conllevan la liberación de los recursos del sistema.
        elif self.__fase == self.FASE_SECADO_AUTOMATICO:
            self.terminar()
        
        elif self.__fase == self.FASE_SECADO_MANO:
            self.terminar() 
        
        elif self.__fase == self.FASE_ENCERADO:
            self.terminar() 
        
        else:
            raise RuntimeError(f"Estado no válido: Fase {self.__fase}.")


    def imprimir_fase(self):
        """Mapea el valor numérico del estado actual a su descripción textual correspondiente."""
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
        print(fases_map.get(self.__fase, f"{self.__fase} - En estado no válido"), end="")


    def imprimir_estado(self):
        """Genera un informe visual por consola detallando los parámetros actuales del objeto."""
        print("----------------------------------------")
        print(f"Ingresos Acumulados: {self.ingresos:.2f} €")
        print(f"Ocupado: {self.ocupado}")
        print(f"Prelavado a mano: {self.prelavado_a_mano}")
        print(f"Secado a mano: {self.secado_a_mano}")
        print(f"Encerado: {self.encerado}")
        print("Fase: ", end="")
        self.imprimir_fase()
        print("\n----------------------------------------")
