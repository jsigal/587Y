"""
Pytest test file for the bank module.
Tests the Bank class and all its methods.
"""

import pytest
from bank import Bank
from accounts import CheckingAccount, SavingsAccount, MoneyMarketAccount


class TestBankInitialization:
    """Test Bank class initialization."""
    
    def test_bank_creation(self):
        """Test creating a bank."""
        bank = Bank("Test Bank")
        assert bank.bank_name == "Test Bank"
        assert isinstance(bank.accounts, dict)
        assert len(bank.accounts) == 0
        assert bank.account_counter == 1000
    
    def test_bank_string_representation(self):
        """Test string representation of bank."""
        bank = Bank("My Bank")
        str_repr = str(bank)
        assert "Bank" in str_repr
        assert "My Bank" in str_repr
    
    def test_bank_repr(self):
        """Test detailed representation of bank."""
        bank = Bank("My Bank")
        repr_str = repr(bank)
        assert "Bank" in repr_str
        assert "My Bank" in repr_str


class TestBankAccountCreation:
    """Test account creation methods."""
    
    def test_create_checking_account(self):
        """Test creating a checking account."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John Doe", 500.0)
        assert account_num == "1000"
        assert account_num in bank.accounts
        account = bank.accounts[account_num]
        assert isinstance(account, CheckingAccount)
        assert account.customer_name == "John Doe"
        assert account.balance == 500.0
    
    def test_create_savings_account(self):
        """Test creating a savings account."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("savings", "Jane Smith", 1000.0)
        assert account_num == "1000"
        account = bank.accounts[account_num]
        assert isinstance(account, SavingsAccount)
        assert account.balance == 1000.0
    
    def test_create_money_market_account(self):
        """Test creating a money market account."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("moneymarket", "Bob Johnson", 5000.0)
        assert account_num == "1000"
        account = bank.accounts[account_num]
        assert isinstance(account, MoneyMarketAccount)
        assert account.balance == 5000.0
    
    def test_create_account_case_insensitive(self):
        """Test that account type is case insensitive."""
        bank = Bank("Test Bank")
        account_num1 = bank.create_account("CHECKING", "Test", 100.0)
        account_num2 = bank.create_account("Savings", "Test", 200.0)
        account_num3 = bank.create_account("MoneyMarket", "Test", 1000.0)
        assert account_num1 == "1000"
        assert account_num2 == "1001"
        assert account_num3 == "1002"
    
    def test_create_account_invalid_type(self):
        """Test creating account with invalid type."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("invalid", "Test", 100.0)
        assert account_num is None
        assert len(bank.accounts) == 0
    
    def test_create_account_insufficient_initial_balance(self):
        """Test creating account with insufficient initial balance."""
        bank = Bank("Test Bank")
        # Savings requires minimum $100
        account_num = bank.create_account("savings", "Test", 50.0)
        assert account_num is None
        assert len(bank.accounts) == 0
    
    def test_create_account_with_custom_parameters(self):
        """Test creating account with custom parameters."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("savings", "Test", 500.0,
                                         interest_rate=0.03, minimum_balance=200.0)
        assert account_num is not None
        account = bank.accounts[account_num]
        assert account.interest_rate == 0.03
        assert account.minimum_balance == 200.0
    
    def test_account_counter_increments(self):
        """Test that account counter increments correctly."""
        bank = Bank("Test Bank")
        acc1 = bank.create_account("checking", "Test1", 100.0)
        acc2 = bank.create_account("checking", "Test2", 100.0)
        acc3 = bank.create_account("checking", "Test3", 100.0)
        assert acc1 == "1000"
        assert acc2 == "1001"
        assert acc3 == "1002"


class TestBankAccountRetrieval:
    """Test account retrieval methods."""
    
    def test_get_account_existing(self):
        """Test getting an existing account."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John", 100.0)
        account = bank.get_account(account_num)
        assert account is not None
        assert isinstance(account, CheckingAccount)
        assert account.account_number == account_num
    
    def test_get_account_nonexistent(self):
        """Test getting a non-existent account."""
        bank = Bank("Test Bank")
        account = bank.get_account("9999")
        assert account is None
    
    def test_get_balance_existing(self):
        """Test getting balance of existing account."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John", 500.0)
        balance = bank.get_balance(account_num)
        assert balance == 500.0
    
    def test_get_balance_nonexistent(self):
        """Test getting balance of non-existent account."""
        bank = Bank("Test Bank")
        balance = bank.get_balance("9999")
        assert balance is None


class TestBankDeposits:
    """Test deposit operations."""
    
    def test_deposit_valid(self):
        """Test valid deposit."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John", 100.0)
        result = bank.deposit(account_num, 50.0)
        assert result is True
        assert bank.get_balance(account_num) == 150.0
    
    def test_deposit_invalid_account(self):
        """Test deposit to non-existent account."""
        bank = Bank("Test Bank")
        result = bank.deposit("9999", 50.0)
        assert result is False
    
    def test_deposit_negative_amount(self):
        """Test deposit with negative amount."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John", 100.0)
        result = bank.deposit(account_num, -50.0)
        assert result is False
        assert bank.get_balance(account_num) == 100.0
    
    def test_deposit_zero(self):
        """Test deposit with zero amount."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John", 100.0)
        result = bank.deposit(account_num, 0.0)
        assert result is False
        assert bank.get_balance(account_num) == 100.0


class TestBankWithdrawals:
    """Test withdrawal operations."""
    
    def test_withdraw_valid(self):
        """Test valid withdrawal."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John", 200.0)
        result = bank.withdraw(account_num, 50.0)
        assert result is True
        assert bank.get_balance(account_num) == 150.0
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John", 100.0)
        result = bank.withdraw(account_num, 200.0)
        assert result is False
        assert bank.get_balance(account_num) == 100.0
    
    def test_withdraw_invalid_account(self):
        """Test withdrawal from non-existent account."""
        bank = Bank("Test Bank")
        result = bank.withdraw("9999", 50.0)
        assert result is False
    
    def test_withdraw_minimum_balance_violation(self):
        """Test withdrawal that violates minimum balance."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("savings", "John", 500.0, minimum_balance=100.0)
        result = bank.withdraw(account_num, 450.0)  # Would leave 50, below minimum
        assert result is False
        assert bank.get_balance(account_num) == 500.0


class TestBankTransfers:
    """Test transfer operations."""
    
    def test_transfer_valid(self):
        """Test valid transfer between accounts."""
        bank = Bank("Test Bank")
        acc1 = bank.create_account("checking", "John", 500.0)
        acc2 = bank.create_account("checking", "Jane", 200.0)
        result = bank.transfer(acc1, acc2, 100.0)
        assert result is True
        assert bank.get_balance(acc1) == 400.0
        assert bank.get_balance(acc2) == 300.0
    
    def test_transfer_insufficient_funds(self):
        """Test transfer with insufficient funds."""
        bank = Bank("Test Bank")
        acc1 = bank.create_account("checking", "John", 100.0)
        acc2 = bank.create_account("checking", "Jane", 200.0)
        result = bank.transfer(acc1, acc2, 200.0)
        assert result is False
        assert bank.get_balance(acc1) == 100.0
        assert bank.get_balance(acc2) == 200.0
    
    def test_transfer_same_account(self):
        """Test transfer to same account (should fail)."""
        bank = Bank("Test Bank")
        acc1 = bank.create_account("checking", "John", 500.0)
        result = bank.transfer(acc1, acc1, 100.0)
        assert result is False
        assert bank.get_balance(acc1) == 500.0
    
    def test_transfer_invalid_source_account(self):
        """Test transfer with invalid source account."""
        bank = Bank("Test Bank")
        acc2 = bank.create_account("checking", "Jane", 200.0)
        result = bank.transfer("9999", acc2, 100.0)
        assert result is False
        assert bank.get_balance(acc2) == 200.0
    
    def test_transfer_invalid_destination_account(self):
        """Test transfer with invalid destination account."""
        bank = Bank("Test Bank")
        acc1 = bank.create_account("checking", "John", 500.0)
        result = bank.transfer(acc1, "9999", 100.0)
        assert result is False
        assert bank.get_balance(acc1) == 500.0
    
    def test_transfer_rollback_on_deposit_failure(self):
        """Test that transfer rolls back if deposit fails."""
        bank = Bank("Test Bank")
        acc1 = bank.create_account("checking", "John", 500.0)
        acc2 = bank.create_account("savings", "Jane", 200.0, minimum_balance=100.0)
        # Try to transfer amount that would violate minimum balance
        # This should fail and rollback
        initial_balance = bank.get_balance(acc1)
        result = bank.transfer(acc2, acc1, 150.0)  # Would leave savings at 50, below minimum
        assert result is False
        assert bank.get_balance(acc1) == initial_balance  # Should be rolled back


class TestBankInterestProcessing:
    """Test interest processing methods."""
    
    def test_process_interest_checking(self):
        """Test processing interest for checking account (should be zero)."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John", 1000.0)
        interest = bank.process_interest(account_num)
        assert interest == 0.0
        assert bank.get_balance(account_num) == 1000.0
    
    def test_process_interest_savings(self):
        """Test processing interest for savings account."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("savings", "John", 1000.0, interest_rate=0.02)
        initial_balance = bank.get_balance(account_num)
        interest = bank.process_interest(account_num)
        assert interest > 0
        assert bank.get_balance(account_num) == initial_balance + interest
    
    def test_process_interest_money_market(self):
        """Test processing interest for money market account."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("moneymarket", "John", 10000.0, interest_rate=0.035)
        initial_balance = bank.get_balance(account_num)
        interest = bank.process_interest(account_num)
        assert interest > 0
        assert bank.get_balance(account_num) == initial_balance + interest
    
    def test_process_interest_invalid_account(self):
        """Test processing interest for non-existent account."""
        bank = Bank("Test Bank")
        interest = bank.process_interest("9999")
        assert interest is None
    
    def test_process_interest_all(self):
        """Test processing interest for all accounts."""
        bank = Bank("Test Bank")
        acc1 = bank.create_account("checking", "John", 1000.0)
        acc2 = bank.create_account("savings", "Jane", 2000.0)
        acc3 = bank.create_account("moneymarket", "Bob", 5000.0)
        
        results = bank.process_interest_all()
        # Should only include accounts that earn interest (savings and money market)
        assert len(results) == 2
        assert acc2 in results
        assert acc3 in results
        assert acc1 not in results  # Checking doesn't earn interest


class TestBankAccountInfo:
    """Test account information methods."""
    
    def test_get_account_info_checking(self):
        """Test getting info for checking account."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John Doe", 500.0)
        bank.deposit(account_num, 500.0)
        info = bank.get_account_info(account_num)
        assert info is not None
        assert info["account_number"] == account_num
        assert info["customer_name"] == "John Doe"
        assert info["account_type"] == "Checking"
        assert info["balance"] == 1000.0
        assert "created_date" in info
        assert info["transaction_count"] == 1  # Initial deposit
    
    def test_get_account_info_savings(self):
        """Test getting info for savings account."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("savings", "Jane", 1000.0)
        info = bank.get_account_info(account_num)
        assert info is not None
        assert "interest_rate" in info
        assert "minimum_balance" in info
        assert info["minimum_balance"] == 100.0
    
    def test_get_account_info_money_market(self):
        """Test getting info for money market account."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("moneymarket", "Bob", 5000.0)
        info = bank.get_account_info(account_num)
        assert info is not None
        assert "interest_rate" in info
        assert "minimum_balance" in info
        assert "remaining_withdrawals" in info
        assert "withdrawal_limit" in info
    
    def test_get_account_info_invalid(self):
        """Test getting info for non-existent account."""
        bank = Bank("Test Bank")
        info = bank.get_account_info("9999")
        assert info is None
    
    def test_list_all_accounts(self):
        """Test listing all accounts."""
        bank = Bank("Test Bank")
        acc1 = bank.create_account("checking", "John", 100.0)
        acc2 = bank.create_account("savings", "Jane", 200.0)
        acc3 = bank.create_account("moneymarket", "Bob", 1000.0)
        
        accounts_list = bank.list_all_accounts()
        assert len(accounts_list) == 3
        account_numbers = [acc["account_number"] for acc in accounts_list]
        assert acc1 in account_numbers
        assert acc2 in account_numbers
        assert acc3 in account_numbers
    
    def test_list_all_accounts_empty(self):
        """Test listing accounts when bank is empty."""
        bank = Bank("Test Bank")
        accounts_list = bank.list_all_accounts()
        assert len(accounts_list) == 0


class TestBankTransactionHistory:
    """Test transaction history methods."""
    
    def test_get_transaction_history(self):
        """Test getting transaction history."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John", 100.0)
        bank.deposit(account_num, 50.0)
        bank.withdraw(account_num, 25.0)
        
        history = bank.get_transaction_history(account_num)
        assert history is not None
        assert len(history) == 2  #  deposit, withdrawal
        assert history[0]["type"] == "deposit"
        assert history[1]["type"] == "withdrawal"
    
    def test_get_transaction_history_invalid(self):
        """Test getting transaction history for non-existent account."""
        bank = Bank("Test Bank")
        history = bank.get_transaction_history("9999")
        assert history is None


class TestBankEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_multiple_operations_sequence(self):
        """Test a sequence of multiple operations."""
        bank = Bank("Test Bank")
        acc1 = bank.create_account("checking", "John", 1000.0)
        acc2 = bank.create_account("savings", "Jane", 2000.0)
        
        bank.deposit(acc1, 500.0)
        bank.withdraw(acc1, 200.0)
        bank.transfer(acc1, acc2, 100.0)
        bank.process_interest(acc2)
        
        assert bank.get_balance(acc1) == 1200.0
        assert bank.get_balance(acc2) > 2000.0  # Should have interest
    
    def test_account_info_after_transactions(self):
        """Test account info reflects transaction count."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("checking", "John", 100.0)
        bank.deposit(account_num, 50.0)
        bank.deposit(account_num, 25.0)
        bank.withdraw(account_num, 30.0)
        
        info = bank.get_account_info(account_num)
        assert info["transaction_count"] == 3  # 2 deposits + 1 withdrawal
    
    def test_money_market_withdrawal_tracking(self):
        """Test that money market withdrawal limits are tracked correctly."""
        bank = Bank("Test Bank")
        account_num = bank.create_account("moneymarket", "John", 10000.0, 
                                         minimum_balance=1000.0, withdrawal_limit=3)
        account = bank.get_account(account_num)
        
        # Make withdrawals up to limit
        for i in range(3):
            result = bank.withdraw(account_num, 500.0)
            assert result is True
        
        # Next withdrawal should fail
        result = bank.withdraw(account_num, 500.0)
        assert result is False
        
        info = bank.get_account_info(account_num)
        assert info["remaining_withdrawals"] == 0

