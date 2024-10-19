import datetime

class Calculadora:
    '''
    Clase que representa una calculadora básica capaz de realizar operaciones
    aritméticas como suma, resta, multiplicación y división. Además, guarda un
    registro (log) de las operaciones realizadas.

    Atributos:
    -----------
    permitir_decimales : bool
        Indica si los resultados deben incluir decimales o no.
    archivo_log : str
        Nombre del archivo donde se guardarán los logs de las operaciones.
    '''
    
    def __init__(self, permitir_decimales=True, archivo_log="calculadora_logs.txt"):
        self.permitir_decimales = permitir_decimales
        self.archivo_log = archivo_log

    def _validar_resultado(self, resultado):
        '''
        Valida el resultado según si los decimales están permitidos o no.

        Parámetros:
        -----------
        resultado : float/int
            El resultado de la operación que debe ser validado.

        Retorna:
        --------
        float/int:
            El resultado en formato float si se permiten decimales, o como int si no se permiten.
        '''
        if self.permitir_decimales:
            return float(resultado)
        else:
            return int(resultado)
        
    def _guardar_log(self, operacion, a, b, resultado):
        '''
        Guarda un log de la operación realizada en el archivo especificado.

        Parámetros:
        -----------
        operacion : str
            El nombre de la operación realizada (e.g., "Suma", "Resta").
        a : int/float
            El primer número de la operación.
        b : int/float
            El segundo número de la operación.
        resultado : int/float
            El resultado de la operación.
        '''
        with open(self.archivo_log, "a") as archivo:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log = f"{timestamp} - {operacion}: {a} y {b} = {resultado}\n"
            archivo.write(log)
            
    def sumar(self, a, b):
        '''
        Suma dos números y guarda la operación en el archivo de logs.

        Parámetros:
        -----------
        a : int/float
            El primer número a sumar.
        b : int/float
            El segundo número a sumar.

        Retorna:
        --------
        float/int:
            El resultado validado de la suma.
        '''
        resultado = a + b
        resultado_validado = self._validar_resultado(resultado)
        self._guardar_log("Suma", a, b, resultado_validado)
        return resultado_validado

    def restar(self, a, b):
        '''
        Resta dos números.

        Parámetros:
        -----------
        a : int/float
            El primer número de la resta.
        b : int/float
            El segundo número de la resta.

        Retorna:
        --------
        float/int:
            El resultado validado de la resta.
        '''
        resultado = a - b
        resultado_validado = self._validar_resultado(resultado)
        self._guardar_log("Resta", a, b, resultado_validado)
        return resultado_validado

    def multiplicar(self, a, b):
        '''
        Multiplica dos números.

        Parámetros:
        -----------
        a : int/float
            El primer número a multiplicar.
        b : int/float
            El segundo número a multiplicar.

        Retorna:
        --------
        float/int:
            El resultado validado de la multiplicación.
        '''
        resultado = a * b
        resultado_validado = self._validar_resultado(resultado)
        self._guardar_log("Multiplicar", a, b, resultado_validado)
        return resultado_validado

    def dividir(self, a, b):
        '''
        Divide dos números, siempre que el divisor no sea cero.

        Parámetros:
        -----------
        a : int/float
            El numerador.
        b : int/float
            El denominador, debe ser distinto de cero.

        Retorna:
        --------
        float/int:
            El resultado validado de la división.

        Excepciones:
        ------------
        ValueError:
            Se lanza cuando el denominador es cero.
        '''
        if b == 0:
            self._guardar_log("Dividir [ERRROR]",a,b, 0)
            raise ValueError("No se puede dividir entre 0")
        resultado = a / b
        resultado_validado = self._validar_resultado(resultado)
        self._guardar_log("Dividir", a, b, resultado_validado)
        return resultado_validado
