# ATM con python

## Descripción

Este código es un programa de consola que simula un sistema bancario. Crea una lista de usuarios y asigna cuentas bancarias a algunos de ellos. Los usuarios pueden acceder a sus cuentas y realizar operaciones bancarias como depósitos, retiros y consultas de saldo.

El código define dos clases, la clase **User** y la clase **Account**. La clase **User** tiene una lista de cuentas bancarias que el usuario posee y métodos para agregar cuentas a la lista y obtener una cuenta de la lista. La clase **Account** tiene un identificador de cuenta, un saldo y una lista de operaciones bancarias que el usuario ha realizado.

El programa le pide al usuario que ingrese su nombre de usuario y contraseña, y luego le presenta un menú con opciones para realizar operaciones bancarias en una cuenta específica. Si el usuario es "**admin**", se le pide una contraseña adicional y se le muestra una lista de todos los usuarios y contraseñas.

El código utiliza la función `clear()` para borrar la pantalla de la consola y la función `sleep()` para introducir pausas en la ejecución del programa. También utiliza la biblioteca os para determinar el sistema operativo y limpiar la pantalla adecuadamente.

### Usuarios y cuentas

| Usuarios | Contraseñas | Num. Cuentas | Balance |
| :------: | :---------: | :----------: | :-----: |
| Darlin | 1234 | 00 | $ 10000.00 |
| | | 01 | $ 1500.00 |
| Yeiser | 4321 | 02 | $ 0.00 |
| | | 03 | $ 100.00 |
| Jannovi | 0000 | 04 | $ 12500.00 |
| | | 05 | $ 265.50

