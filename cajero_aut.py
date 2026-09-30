
nombre_usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

if nombre_usuario == "felipe" and contrasena == "1234":
    print("Bienvenido al sistema, ", nombre_usuario)
else:
    print("Usuario o contraseña incorrectos. Acceso denegado.")
    exit()

saldo = 500000 

while True:

      print("---------CAJERO AUTOMÁTICO---------")
      print("1. Consultar Saldo")
      print("2. Retirar Dinero")
      print("3. Depositar Dinero")
      print("4. Salir")
      opcion = int(input("Seleccione una opción: "))

      if opcion == 1:
        print("Su saldo actual es: $", saldo)
      elif opcion == 2:
        monto_retirar = float(input("ingrese el monto a retirar: "))
        if monto_retirar <= saldo:
            saldo -= monto_retirar
            print("Retiro exitoso. Su nuevo saldo es: $", saldo)
        else:
            print("Saldo insuficiente para realizar el retiro.")

      elif opcion == 3:
        monto_depositar = float(input("Ingrese el monto a depositar: "))
        saldo = monto_depositar + saldo
        print("Depósito exitoso. Su nuevo saldo es: $", saldo)  

      elif opcion == 4:
        print("Gracias por usar el cajero automático. ¡Hasta luego!") 
        break     
    

