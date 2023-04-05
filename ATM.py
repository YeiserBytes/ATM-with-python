import os
from time import sleep


def clear() -> None:
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ['ce', 'nt', 'dos']:
        os.system('cls')


class User:
    def __init__(self, name: str, passwd: str) -> None:
        self.name = name
        self.passwd = passwd
        self.accounts = []

    def add_account(self, account: object) -> None:
        self.accounts.append(account)

    def get_account(self, account_id: int):
        return next((acc for acc in self.accounts if acc.account_id == account_id), None)


class Account:
    def __init__(self, account_id: str, balance: float) -> None:
        self.account_id = account_id
        self.balance = balance
        self.operations = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.operations.append(
            f'Depósito de {amount:.2f}. Saldo actual: {self.balance:.2f}')

    def withdraw(self, amount: float) -> bool:
        if self.balance < amount:
            return False
        self.balance -= amount
        self.operations.append(
            f'Retiro de {amount:.2f}. Saldo actual: {self.balance:.2f}')
        return True

    def get_history(self):
        print(f'Historial de operaciones de la cuenta {self.account_id}: ')
        print('\n'.join(self.operations))


users = [
    User('Darlin', '1234'),
    User('Yeiser', '4321'),
    User('Jannovi', '0000')
]

users[0].add_account(Account('00', 10000))
users[0].add_account(Account('01', 1500))
users[1].add_account(Account('02', 0))
users[1].add_account(Account('03', 100))
users[2].add_account(Account('04', 12500))
users[2].add_account(Account('05', 265.5))


def menu(user):
    clear()
    print('Banco Popular')
    print(f'Bienvenido {user.name}!\n')
    print('1. Retirar \n2. Depositar \n3. Consultar Balance \n4. Salir')
    while True:
        try:
            opc = input('\nIngrese la opción deseada: ')
            if opc in ['1', '2', '3', '4']:
                return opc
            else:
                print('Opción no válida, por favor ingrese una opción válida!')
        except ValueError:
            print('Entrada no es válida, por favor ingrese una opcion correcta!')


def operations(account, operation_type):
    clear()
    while True:
        try:
            amount = float(input(f'Ingrese el monto a {operation_type}: '))
            if amount > 0:
                break
            else:
                print('El monto debe ser mayor que cero!')
        except ValueError:
            print('Entrada no válida, por favor ingrese un número!')
    confirm = input(
        f'¿Está seguro que desea {operation_type} {amount:.2f}? (S/N): ')
    if confirm.upper() == 'S':
        if operation_type == 'retirar':
            result = account.withdraw(amount)
            if result:
                print(
                    f'Retiro realizado con éxito. Saldo actual: {account.balance}')
                sleep(2)
            else:
                print('No se pudo realizar el retiro. Saldo insuficiente!')
                sleep(2)
        elif operation_type == 'depositar':
            account.deposit(amount)
            print(
                f'Depósito realizado con éxito! \nSaldo actual: {account.balance}')
            sleep(2)
    else:
        print('Operación cancelada!')


def show_users(users, user_now):
    clear()
    if user_now == 'admin':
        passwd = input('Ingrese su contraseña: ')
        if passwd == 'secreto':
            clear()
            print('Bienvenido Administrador! \n')
            print('Listado de usuarios: \n')
            for user in users:
                print(f'Usuario: {user.name} \nContraseña: {user.passwd}')
            exit()
        else:
            print('Operación cancelada!')
            sleep(2)


user_now = None

while user_now is None:
    clear()
    name_user = input('Ingrese su nombre de usuario: ')
    if name_user == 'admin':
        user_now = 'admin'
        show_users(users, user_now)
    else:
        passwd = input('Ingrese su contraseña: ')
        for user in users:
            if user.name.lower() == name_user and user.passwd == passwd:
                user_now = user
                break
        if user_now is None:
            print('Usuario o contraseña incorrecta. \n')
            sleep(2)

if user_now == 'admin':
    show_users(users)
else:
    opc = menu(user_now)
    while opc != '4':
        clear()
        num_account = input('Ingrese el número de cuenta: ')
        account = user_now.get_account(num_account)
        if account is None:
            print('Número de cuenta incorrecto.\n')
            sleep(2)
        else:
            if opc == '1':
                operations(account, 'retirar')
                sleep(1.5)
            elif opc == '2':
                operations(account, 'depositar')
                sleep(1.5)
            elif opc == '3':
                print(f"El saldo actual de la cuenta '{num_account}' es de {account.balance}")
                sleep(2)
        opc = menu(user_now)

show_users(users, user_now)
