print("Bienvenido al conversor de monedas \n")

def conversor(moneda_actual, valor, moneda_a_convertir):
    if moneda_actual == 1:
        if moneda_a_convertir == "1":
            print(f'{valor} dólares equivale a ₱{valor * 3750} pesos colombianos')
        elif moneda_a_convertir == "2":
            print(f'{valor} dólares equivale a ¥{valor * 6.37} yuanes')
        elif moneda_a_convertir == "3":
            print(f'{valor} dólares equivale a £{valor * 0.76} libras esterlinas')
        else:
            print("No se reconoce la moneda_a_convertir")
        
    elif moneda_actual == 2:
        if moneda_a_convertir == "1":
            print(f'{valor} euros equivale a ₱{valor * 4000} pesos colombianos')
        elif moneda_a_convertir == "2":
            print(f'{valor} euros equivale a ¥{valor * 6.93} yuanes')
        elif moneda_a_convertir == "3":
            print(f'{valor} euros equivale a £{valor * 0.83} libras esterlinas')
        else:
            print("No se reconoce la moneda_a_convertir")
                
moneda_actual = int(input("Ingrese su moneda actual \n 1. Dólar \n 2. Euro \n "))
valor = float(input("Ingrese el valor a convertir: \n"))
moneda_a_convertir = input(
    "¿A qué moneda quiere convertirlo? \n 1. Pesos colombianos"
    "\n 2. Yuanes \n 3. Libras Esterlinas \n")

conversor(moneda_actual, valor, moneda_a_convertir)
