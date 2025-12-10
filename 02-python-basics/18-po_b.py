from abc import ABC, abstractmethod

class BankAccount(ABC):
    
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
        
    def _set_balance(self, amount):
        self.__balance = amount
        return self.__balance
    
    def _get_balance(self):
        return self.__balance
    
    def _set_invalid_movements(self, movements):
        self.__invalid_movements = movements
        return self.__invalid_movements
        
    def _get_invalid_movements(self):
        return self.__invalid_movements
    
    def _set_is_account_blocked(self, is_blocked):
        self.is_account_blocked = is_blocked
        return self.is_account_blocked
        
    def _get_is_account_blocked(self):
        return self.is_account_blocked
        
    @abstractmethod
    def withdraw(self, amount):
        pass
            
    def see_balance(self):
        return f'Su saldo es {self.__balance}'
    

class SavingAccount(BankAccount):
    
    def withdraw(self, amount):
        if self.is_account_blocked: return f'Su cuenta se encuentra bloqueda por exceso de intentos fallidos'
        
        penalty = amount * 0.05
        total = amount + penalty
        
        if(total > 0 and total < self._get_balance()):
            self._set_balance(self._get_balance() - total)
            return self._get_balance()
        else:
            if(self._get_invalid_movements() >= 3):
                self._set_is_account_blocked(True)
            else: 
                self._set_invalid_movements(self._get_invalid_movements() + 1);
                return f'El valor ingresado es inválido, si haces más de 3 movimientos invalidos se bloqueara tu cuenta {self._get_invalid_movements()}/3'
            
class PayrollAccount(BankAccount):
    
    def withdraw(self, amount):
        if self.is_account_blocked: return f'Su cuenta se encuentra bloqueda por exceso de intentos fallidos'
        
        penalty = amount * 0
        total = amount + penalty
        
        if(total > 0 and total < self._get_balance()):
            self._set_balance(self._get_balance() - total)
            return self._get_balance()
        else:
            if(self._get_invalid_movements() >= 3):
                self._set_is_account_blocked(True)
            else: 
                self._set_invalid_movements(self._get_invalid_movements() + 1);
                return f'El valor ingresado es inválido, si haces más de 3 movimientos invalidos se bloqueara tu cuenta {self._get_invalid_movements()}/3'
            
savings = SavingAccount("Jhosua", 100)
payroll = PayrollAccount("Jhosua", 10000)

savings.withdraw(50)
payroll.withdraw(4000)

print("Cuenta de ahorro: ", savings.see_balance())
print("Cuenta de nomina: ", payroll.see_balance())