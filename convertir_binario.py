def binario(decimal):
    binario = ""
    
    # Realiza la división con resultado de número entero (x // y = z)
    while ((decimal // 2) != 0): # !Ojo Si quitamos la operación de division, el programa no funciona!
        binario = str(decimal % 2) + binario;
        # Realiza la división con resultado de número entero (x // y = z)
        decimal = decimal // 2;

    return str(decimal) + binario;


if __name__ == "__main__":
    
    numero = int(input("Introduzca el número que quieres convertir a binario: "));
    print(binario(numero));

    input("\nPulsa una tecla para salir...");