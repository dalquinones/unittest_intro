from calculator import Calculadora

if __name__ == "__main__":
    calc = Calculadora(archivo_log="calculator_log.txt")

    num1 = int(input("Ingresa el primer numero "))
    num2 = int(input("Ingresa el segundo numero "))
    operation = input("Ingresa la operacion [1. suma, 2. resta, 3. multiplicacion, 4. division]")
    
    dic = {"1": calc.sumar(num1,num2),
           "2": calc.restar(num1,num2),
           "3": calc.multiplicar(num1,num2),
           "5": calc.dividir(num1,num2)}

    print(dic[operation])