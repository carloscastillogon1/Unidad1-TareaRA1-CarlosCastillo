import unittest
from lavadero import Lavadero

class TestLavadero(unittest.TestCase):

    def setUp(self):
        """Inicializa una instancia de Lavadero antes de cada test."""
        self.lavadero = Lavadero()

    def test1_estado_inicial_inactivo(self):
        """Test 1: Verifica el estado inicial del lavadero."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)

    def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Comprueba que encerar sin secado a mano lanza ValueError."""
        with self.assertRaises(ValueError) as cm:
            self.lavadero.hacerLavado(False, False, True)
        self.assertEqual(str(cm.exception), "No se puede encerar el coche sin secado a mano")

    def test3_excepcion_lavadero_ocupado(self):
        """Test 3: Comprueba que no se puede iniciar lavado si ya está ocupado."""
        self.lavadero.hacerLavado(False, False, False)
        with self.assertRaises(ValueError) as cm:
            self.lavadero.hacerLavado(False, False, False)
        self.assertEqual(str(cm.exception), "No se puede iniciar un nuevo lavado mientras el lavadero está ocupado")

    def test4_ingresos_prelavado_mano(self):
        """Test 4: Si seleccionamos prelavado a mano, ingresos son 6,50€."""
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=False, encerado=False)
        self.lavadero.avanzarFase() # Transición 0 -> 1 (aquí se cobra)
        self.assertEqual(self.lavadero.ingresos, 6.50)

    def test5_ingresos_secado_mano(self):
        """Test 5: Si seleccionamos secado a mano, ingresos son 6,00€."""
        self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=True, encerado=False)
        self.lavadero.avanzarFase()
        self.assertEqual(self.lavadero.ingresos, 6.00)

    def test6_ingresos_secado_y_encerado(self):
        """Test 6: Si seleccionamos secado a mano y encerado, ingresos son 7,20€."""
        self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=True, encerado=True)
        self.lavadero.avanzarFase()
        self.assertEqual(self.lavadero.ingresos, 7.20)

    def test7_ingresos_prelavado_y_secado(self):
        """Test 7: Si seleccionamos prelavado y secado a mano, ingresos son 7,50€."""
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=True, encerado=False)
        self.lavadero.avanzarFase()
        self.assertEqual(self.lavadero.ingresos, 7.50)

    def test8_ingresos_todo_incluido(self):
        """Test 8: Si seleccionamos todo, los ingresos son 8,70€."""
        self.lavadero.hacerLavado(prelavado_a_mano=True, secado_a_mano=True, encerado=True)
        self.lavadero.avanzarFase()
        self.assertEqual(self.lavadero.ingresos, 8.70)

    def test9_flujo_rapido_sin_extras(self):
        """Test 9: Simula el flujo rápido sin opciones opcionales."""
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(False, False, False)
        self.assertEqual(fases_obtenidas, fases_esperadas)

    def test10_flujo_con_prelavado(self):
        """Test 10: Flujo con prelavado a mano."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(True, False, False)
        self.assertEqual(fases_obtenidas, fases_esperadas)

    def test11_flujo_con_secado_mano(self):
        """Test 11: Flujo con secado a mano."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(False, True, False)
        self.assertEqual(fases_obtenidas, fases_esperadas)

    def test12_flujo_con_secado_y_encerado(self):
        """Test 12: Flujo con secado a mano y encerado."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 8, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(False, True, True)
        self.assertEqual(fases_obtenidas, fases_esperadas)

    def test13_flujo_con_prelavado_y_secado(self):
        """Test 13: Flujo con prelavado y secado a mano."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(True, True, False)
        self.assertEqual(fases_obtenidas, fases_esperadas)

    def test14_flujo_completo(self):
        """Test 14: Flujo completo (prelavado, secado y encerado)."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(True, True, True)
        self.assertEqual(fases_obtenidas, fases_esperadas)

if __name__ == '__main__':
    unittest.main()
