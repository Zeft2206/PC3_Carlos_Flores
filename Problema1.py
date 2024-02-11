def fraccción():
    try:
        X = int(input("Introduce un número:"))
        Y = int(input("Introduce un número:"))
        resultado = float(X/Y) * 100
        if X == Y:
            print("F")
        else:
            print(f'{resultado}%') 
    except ValueError:
        print("Solo valores enteros")
    except ZeroDivisionError:
        return fraccción()
    except X > Y:
        return fraccción()

fraccción()
       
    


