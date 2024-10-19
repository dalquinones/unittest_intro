import unittest
import os
from src.calculator import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
         self.archivo_log_test = 'test_logs.txt'
         self.calc = Calculadora(permitir_decimales=False, archivo_log=self.archivo_log_test)

    def tearDown(self):
        if os.path.exists(self.archivo_log_test):
            os.remove(self.archivo_log_test)

    def test_suma_sin_decimales(self):
        '''Prueba el método sumar para verificar si la operación es correcta.'''
        self.assertEqual(self.calc.sumar(10, 3.7), 13)  
    
    def test_resta_sin_decimales(self):
        self.assertEqual(self.calc.restar(10, 3), 7)  
        self.assertEqual(self.calc.restar(10, 3.1), 6)  
        self.assertEqual(self.calc.restar(-10, 3), -13)  

    def test_multiplicacion_sin_decimales(self):
        self.assertEqual(self.calc.multiplicar(10, 3), 30)  

    def test_division_sin_decimales(self):
        with self.assertRaises(ValueError) as context:
                    self.calc.dividir(10, 0)
        self.assertEqual(str(context.exception), "No se puede dividir entre 0")


    # TODO: Crear los test de todas las operaciones