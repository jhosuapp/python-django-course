class BankAccount:
    
    def __init__(self, username, initial_balance):
        self.username = username
        self.__invalid_movements = 0
        self.__balance = initial_balance
        self.is_account_blocked = False
        
    def deposit(self, amount):
        if self.is_account_blocked: return f'Su cuenta se encuentra bloqueda por exceso de intentos fallidos'
        if(amount > 0):
            self.__balance += amount
            return self.__balance
        else:
            self.__invalid_movements += 1;
            if(self.__invalid_movements >= 3):
                self.is_account_blocked = True
            return f'El valor ingresado es inválido, si haces más de 3 movimientos invalidos se bloqueara tu cuenta {self.__invalid_movements}/3'
        
    def withdraw(self, amount):
        if self.is_account_blocked: return f'Su cuenta se encuentra bloqueda por exceso de intentos fallidos'
        if(amount > 0 and self.__balance > amount):
            self.__balance -= amount
            return self.__balance
        else:
            if(self.__invalid_movements >= 3):
                self.is_account_blocked = True
            self.__invalid_movements += 1;
            return f'El valor ingresado es inválido, si haces más de 3 movimientos invalidos se bloqueara tu cuenta {self.__invalid_movements}/3'
            
    def see_balance(self):
        return f'Su saldo es {self.__balance}'
    

account = BankAccount("Jhosua", 2000)
account.deposit(1000)


print(account.deposit(-1000))