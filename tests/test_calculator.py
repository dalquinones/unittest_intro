import unittest

class TestCalculadora(unittest.TestCase):

    def test_suma_sin_decimales(self):
        '''Prueba el método sumar para verificar si la operación es correcta.'''
        calc = Calculadora(permitir_decimales=False)
        self.assertEqual(calc.sumar(10, 3.7), 13)  
    
    # TODO: Crear los test de todas las operaciones