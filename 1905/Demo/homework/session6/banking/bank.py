"""
Bank class for managing customer accounts and transactions.
"""

from typing import Dict, Optional, List
from accounts import Account, CheckingAccount, SavingsAccount, MoneyMarketAccount


class Bank:
    """Class representing a bank that manages customer accounts and transactions."""
    
    def __init__(self, bank_name: str):
        """
        Initialize a bank.
        
        Args:
            bank_name: Name of the bank
        """
        self.bank_name = bank_name
        self.accounts: Dict[str, Account] = {}
        self.account_counter = 1000  # Starting account number
    
    def create_account(self, account_type: str, customer_name: str, 
                      initial_balance: float = 0.0, **kwargs) -> Optional[str]:
        """
        Create a new account for a customer.
        
        Args:
            account_type: Type of account ('checking', 'savings', or 'moneymarket')
            customer_name: Name of the customer
            initial_balance: Initial deposit amount
            **kwargs: Additional parameters for specific account types
                     (e.g., interest_rate, minimum_balance, withdrawal_limit)
        
        Returns:
            Account number if successful, None otherwise
        """
        account_number = str(self.account_counter)
        self.account_counter += 1
        
        account_type_lower = account_type.lower()
        
        try:
            if account_type_lower == 'checking':
                account = CheckingAccount(account_number, customer_name, initial_balance)
            elif account_type_lower == 'savings':
                interest_rate = kwargs.get('interest_rate', 0.02)
                minimum_balance = kwargs.get('minimum_balance', 100.0)
                account = SavingsAccount(account_number, customer_name, initial_balance,
                                       interest_rate, minimum_balance)
            elif account_type_lower == 'moneymarket':
                interest_rate = kwargs.get('interest_rate', 0.035)
                minimum_balance = kwargs.get('minimum_balance', 1000.0)
                withdrawal_limit = kwargs.get('withdrawal_limit', 6)
                account = MoneyMarketAccount(account_number, customer_name, initial_balance,
                                           interest_rate, minimum_balance, withdrawal_limit)
            else:
                print(f"Error: Unknown account type '{account_type}'. Valid types: checking, savings, moneymarket")
                return None
            
            # Validate initial balance meets minimum requirements
            if hasattr(account, 'minimum_balance') and initial_balance < account.minimum_balance:
                print(f"Error: Initial balance ${initial_balance:.2f} is below minimum balance requirement of ${account.minimum_balance:.2f}")
                return None
            
            self.accounts[account_number] = account
            print(f"Created {account.account_type} account {account_number} for {customer_name} with initial balance ${initial_balance:.2f}")
            return account_number
        
        except Exception as e:
            print(f"Error creating account: {e}")
            return None
    
    def get_account(self, account_number: str) -> Optional[Account]:
        """
        Get an account by account number.
        
        Args:
            account_number: Account number to retrieve
        
        Returns:
            Account object if found, None otherwise
        """
        return self.accounts.get(account_number)
    
    def deposit(self, account_number: str, amount: float) -> bool:
        """
        Deposit money into an account.
        
        Args:
            account_number: Account number
            amount: Amount to deposit
        
        Returns:
            True if successful, False otherwise
        """
        account = self.get_account(account_number)
        if account is None:
            print(f"Error: Account {account_number} not found.")
            return False
        return account.deposit(amount)
    
    def withdraw(self, account_number: str, amount: float) -> bool:
        """
        Withdraw money from an account.
        
        Args:
            account_number: Account number
            amount: Amount to withdraw
        
        Returns:
            True if successful, False otherwise
        """
        account = self.get_account(account_number)
        if account is None:
            print(f"Error: Account {account_number} not found.")
            return False
        return account.withdraw(amount)
    
    def transfer(self, from_account: str, to_account: str, amount: float) -> bool:
        """
        Transfer money between two accounts.
        
        Args:
            from_account: Source account number
            to_account: Destination account number
            amount: Amount to transfer
        
        Returns:
            True if successful, False otherwise
        """
        from_acc = self.get_account(from_account)
        to_acc = self.get_account(to_account)
        
        if from_acc is None:
            print(f"Error: Source account {from_account} not found.")
            return False
        
        if to_acc is None:
            print(f"Error: Destination account {to_account} not found.")
            return False
        
        if from_account == to_account:
            print("Error: Cannot transfer to the same account.")
            return False
        
        # Withdraw from source account
        if from_acc.withdraw(amount):
            # Deposit to destination account
            if to_acc.deposit(amount):
                print(f"Transferred ${amount:.2f} from account {from_account} to account {to_account}")
                return True
            else:
                # Rollback: deposit back to source account if destination deposit fails
                from_acc.deposit(amount)
                print(f"Error: Transfer failed. Rolled back withdrawal from account {from_account}")
                return False
        
        return False
    
    def get_balance(self, account_number: str) -> Optional[float]:
        """
        Get the balance of an account.
        
        Args:
            account_number: Account number
        
        Returns:
            Account balance if found, None otherwise
        """
        account = self.get_account(account_number)
        if account is None:
            print(f"Error: Account {account_number} not found.")
            return None
        return account.get_balance()
    
    def process_interest(self, account_number: str) -> Optional[float]:
        """
        Process and apply interest for an account.
        
        Args:
            account_number: Account number
        
        Returns:
            Interest amount applied if successful, None otherwise
        """
        account = self.get_account(account_number)
        if account is None:
            print(f"Error: Account {account_number} not found.")
            return None
        
        interest = account.apply_interest()
        return interest
    
    def process_interest_all(self) -> Dict[str, float]:
        """
        Process interest for all accounts that earn interest.
        
        Returns:
            Dictionary mapping account numbers to interest amounts applied
        """
        results = {}
        for account_number, account in self.accounts.items():
            interest = account.apply_interest()
            if interest > 0:
                results[account_number] = interest
        return results
    
    def get_account_info(self, account_number: str) -> Optional[Dict]:
        """
        Get detailed information about an account.
        
        Args:
            account_number: Account number
        
        Returns:
            Dictionary with account information if found, None otherwise
        """
        account = self.get_account(account_number)
        if account is None:
            print(f"Error: Account {account_number} not found.")
            return None
        
        info = {
            "account_number": account.account_number,
            "customer_name": account.customer_name,
            "account_type": account.account_type,
            "balance": account.balance,
            "created_date": account.created_date.strftime("%Y-%m-%d %H:%M:%S"),
            "transaction_count": len(account.transactions)
        }
        
        if hasattr(account, 'interest_rate'):
            info["interest_rate"] = f"{account.interest_rate * 100:.2f}%"
        
        if hasattr(account, 'minimum_balance'):
            info["minimum_balance"] = account.minimum_balance
        
        if isinstance(account, MoneyMarketAccount):
            info["remaining_withdrawals"] = account.get_remaining_withdrawals()
            info["withdrawal_limit"] = account.withdrawal_limit
        
        return info
    
    def list_all_accounts(self) -> List[Dict]:
        """
        Get information about all accounts.
        
        Returns:
            List of dictionaries containing account information
        """
        accounts_list = []
        for account_number in sorted(self.accounts.keys()):
            info = self.get_account_info(account_number)
            if info:
                accounts_list.append(info)
        return accounts_list
    
    def get_transaction_history(self, account_number: str) -> Optional[List]:
        """
        Get transaction history for an account.
        
        Args:
            account_number: Account number
        
        Returns:
            List of transactions if found, None otherwise
        """
        account = self.get_account(account_number)
        if account is None:
            print(f"Error: Account {account_number} not found.")
            return None
        return account.get_transaction_history()
    
    def __str__(self) -> str:
        """String representation of the bank."""
        return f"Bank(name='{self.bank_name}', accounts={len(self.accounts)})"
    
    def __repr__(self) -> str:
        """Detailed representation of the bank."""
        return f"Bank(bank_name='{self.bank_name}', account_count={len(self.accounts)})"

