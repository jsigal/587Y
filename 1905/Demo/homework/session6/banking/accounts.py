"""
Account classes for the banking application.
Includes base Account class and subclasses for different account types.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional


class Account(ABC):
    """Base class for all bank accounts."""
    
    def __init__(self, account_number: str, customer_name: str, initial_balance: float = 0.0):
        """
        Initialize an account.
        
        Args:
            account_number: Unique account identifier
            customer_name: Name of the account holder
            initial_balance: Starting balance (default: 0.0)
        """
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.transactions = []
        self.created_date = datetime.now()
    
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account.
        
        Args:
            amount: Amount to deposit (must be positive)
            
        Returns:
            True if successful, False otherwise
        """
        if amount <= 0:
            print(f"Error: Deposit amount must be positive. Attempted: ${amount:.2f}")
            return False
        
        self.balance += amount
        self._record_transaction("deposit", amount)
        print(f"Deposited ${amount:.2f} into account {self.account_number}. New balance: ${self.balance:.2f}")
        return True
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw (must be positive)
            
        Returns:
            True if successful, False otherwise
        """
        if amount <= 0:
            print(f"Error: Withdrawal amount must be positive. Attempted: ${amount:.2f}")
            return False
        
        if not self._can_withdraw(amount):
            print(f"Error: Insufficient funds or withdrawal limit exceeded. Balance: ${self.balance:.2f}, Requested: ${amount:.2f}")
            return False
        
        self.balance -= amount
        self._record_transaction("withdrawal", amount)
        print(f"Withdrew ${amount:.2f} from account {self.account_number}. New balance: ${self.balance:.2f}")
        return True
    
    def get_balance(self) -> float:
        """Get the current account balance."""
        return self.balance
    
    def _record_transaction(self, transaction_type: str, amount: float):
        """Record a transaction in the account history."""
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance_after": self.balance,
            "timestamp": datetime.now()
        }
        self.transactions.append(transaction)
    
    def get_transaction_history(self) -> list:
        """Get the transaction history for this account."""
        return self.transactions.copy()
    
    @abstractmethod
    def _can_withdraw(self, amount: float) -> bool:
        """
        Check if a withdrawal is allowed.
        Must be implemented by subclasses.
        
        Args:
            amount: Amount to withdraw
            
        Returns:
            True if withdrawal is allowed, False otherwise
        """
        pass
    
    @abstractmethod
    def calculate_interest(self) -> float:
        """
        Calculate interest for the account.
        Must be implemented by subclasses.
        
        Returns:
            Interest amount
        """
        pass
    
    @abstractmethod
    def apply_interest(self) -> float:
        """
        Apply interest to the account balance.
        Must be implemented by subclasses.
        
        Returns:
            Interest amount applied
        """
        pass
    
    def __str__(self) -> str:
        """String representation of the account."""
        return f"{self.__class__.__name__}(Account: {self.account_number}, Customer: {self.customer_name}, Balance: ${self.balance:.2f})"
    
    def __repr__(self) -> str:
        """Detailed representation of the account."""
        return (f"{self.__class__.__name__}(account_number='{self.account_number}', "
                f"customer_name='{self.customer_name}', balance={self.balance:.2f})")


class CheckingAccount(Account):
    """Checking account with no interest and no minimum balance requirement."""
    
    def __init__(self, account_number: str, customer_name: str, initial_balance: float = 0.0):
        super().__init__(account_number, customer_name, initial_balance)
        self.account_type = "Checking"
        self.interest_rate = 0.0  # No interest on checking accounts
    
    def _can_withdraw(self, amount: float) -> bool:
        """Checking accounts can withdraw up to the available balance."""
        return self.balance >= amount
    
    def calculate_interest(self) -> float:
        """Checking accounts do not earn interest."""
        return 0.0
    
    def apply_interest(self) -> float:
        """Checking accounts do not earn interest."""
        return 0.0


class SavingsAccount(Account):
    """Savings account with interest and minimum balance requirement."""
    
    def __init__(self, account_number: str, customer_name: str, initial_balance: float = 0.0,
                 interest_rate: float = 0.02, minimum_balance: float = 100.0):
        """
        Initialize a savings account.
        
        Args:
            account_number: Unique account identifier
            customer_name: Name of the account holder
            initial_balance: Starting balance
            interest_rate: Annual interest rate (default: 2% = 0.02)
            minimum_balance: Minimum required balance (default: $100.00)
        """
        super().__init__(account_number, customer_name, initial_balance)
        self.account_type = "Savings"
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance
        self.last_interest_date = datetime.now()
    
    def _can_withdraw(self, amount: float) -> bool:
        """Savings accounts must maintain minimum balance after withdrawal."""
        return (self.balance >= amount) and (self.balance - amount >= self.minimum_balance)
    
    def calculate_interest(self) -> float:
        """
        Calculate monthly interest based on current balance.
        Assumes monthly compounding.
        """
        monthly_rate = self.interest_rate / 12
        return self.balance * monthly_rate
    
    def apply_interest(self) -> float:
        """
        Apply monthly interest to the account.
        
        Returns:
            Interest amount applied
        """
        interest = self.calculate_interest()
        if interest > 0:
            self.balance += interest
            self._record_transaction("interest", interest)
            self.last_interest_date = datetime.now()
            print(f"Applied interest of ${interest:.2f} to account {self.account_number}. New balance: ${self.balance:.2f}")
        return interest


class MoneyMarketAccount(Account):
    """Money market account with higher interest rate and higher minimum balance."""
    
    def __init__(self, account_number: str, customer_name: str, initial_balance: float = 0.0,
                 interest_rate: float = 0.035, minimum_balance: float = 1000.0,
                 withdrawal_limit: int = 6):
        """
        Initialize a money market account.
        
        Args:
            account_number: Unique account identifier
            customer_name: Name of the account holder
            initial_balance: Starting balance
            interest_rate: Annual interest rate (default: 3.5% = 0.035)
            minimum_balance: Minimum required balance (default: $1000.00)
            withdrawal_limit: Maximum number of withdrawals per month (default: 6)
        """
        super().__init__(account_number, customer_name, initial_balance)
        self.account_type = "Money Market"
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance
        self.withdrawal_limit = withdrawal_limit
        self.withdrawals_this_month = 0
        self.last_interest_date = datetime.now()
        self.month_start = datetime.now().month
    
    def _can_withdraw(self, amount: float) -> bool:
        """Money market accounts have withdrawal limits and minimum balance requirements."""
        # Check if we've exceeded monthly withdrawal limit
        current_month = datetime.now().month
        if current_month != self.month_start:
            # New month, reset counter
            self.withdrawals_this_month = 0
            self.month_start = current_month
        
        if self.withdrawals_this_month >= self.withdrawal_limit:
            print(f"Error: Monthly withdrawal limit ({self.withdrawal_limit}) exceeded.")
            return False
        
        # Check balance and minimum balance requirement
        if self.balance < amount:
            return False
        
        if self.balance - amount < self.minimum_balance:
            print(f"Error: Withdrawal would violate minimum balance requirement of ${self.minimum_balance:.2f}")
            return False
        
        return True
    
    def withdraw(self, amount: float) -> bool:
        """Override withdraw to track monthly withdrawal count."""
        if super().withdraw(amount):
            self.withdrawals_this_month += 1
            return True
        return False
    
    def calculate_interest(self) -> float:
        """
        Calculate monthly interest based on current balance.
        Assumes monthly compounding.
        """
        monthly_rate = self.interest_rate / 12
        return self.balance * monthly_rate
    
    def apply_interest(self) -> float:
        """
        Apply monthly interest to the account.
        
        Returns:
            Interest amount applied
        """
        interest = self.calculate_interest()
        if interest > 0:
            self.balance += interest
            self._record_transaction("interest", interest)
            self.last_interest_date = datetime.now()
            print(f"Applied interest of ${interest:.2f} to account {self.account_number}. New balance: ${self.balance:.2f}")
        return interest
    
    def get_remaining_withdrawals(self) -> int:
        """Get the number of remaining withdrawals for the current month."""
        current_month = datetime.now().month
        if current_month != self.month_start:
            return self.withdrawal_limit
        return max(0, self.withdrawal_limit - self.withdrawals_this_month)

