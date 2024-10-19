# import unittest
# import os
# from src.calculator import Calculadora  

# class TestCalculadora(unittest.TestCase):

#     def setUp(self):
#         '''
#         Este método se ejecuta antes de cada prueba. Aquí se inicializa una
#         instancia de Calculadora y se especifica el archivo de log temporal.
#         '''
#         self.archivo_log_test = "test_calculadora_logs.txt"
#         self.calc = Calculadora(permitir_decimales=True, archivo_log=self.archivo_log_test)

#     def tearDown(self):
#         '''
#         Este método se ejecuta después de cada prueba. Aquí se limpia el archivo
#         de log usado en las pruebas si existe.
#         '''
#         if os.path.exists(self.archivo_log_test):
#             os.remove(self.archivo_log_test)

#     def test_suma(self):
#         '''Prueba el método sumar para verificar si la operación es correcta.'''
#         resultado = self.calc.sumar(5, 3)
#         self.assertEqual(resultado, 8.0)
        
#     def test_resta(self):
#         '''Prueba el método restar para verificar si la operación es correcta.'''
#         resultado = self.calc.restar(10, 4)
#         self.assertEqual(resultado, 6.0)
        
#     def test_multiplicacion(self):
#         '''Prueba el método multiplicar para verificar si la operación es correcta.'''
#         resultado = self.calc.multiplicar(3, 7)
#         self.assertEqual(resultado, 21.0)

#     def test_division(self):
#         '''Prueba el método dividir para verificar si la operación es correcta.'''
#         resultado = self.calc.dividir(15, 3)
#         self.assertEqual(resultado, 5.0)

#     def test_division_por_cero(self):
#         '''Prueba que la división entre cero lanza una excepción ValueError.'''
#         with self.assertRaises(ValueError):
#             self.calc.dividir(10, 0)

#     def test_log_suma(self):
#         '''Verifica que se guarde un log al realizar una suma.'''
#         self.calc.sumar(5, 3)
#         self.assertTrue(os.path.exists(self.archivo_log_test))

#         with open(self.archivo_log_test, "r") as archivo:
#             log_contenido = archivo.read()
#             self.assertIn("Suma: 5 y 3 = 8.0", log_contenido)

#     def test_log_no_creado_para_resta(self):
#         '''Verifica que no se guarde un log al realizar una resta (ya que la función restar no lo tiene implementado).'''
#         self.calc.restar(5, 3)
#         self.assertFalse(os.path.exists(self.archivo_log_test))


# if __name__ == '__main__':
#     unittest.main()