"""
Pytest test file for the accounts module.
Tests Account base class and all account subclasses.
"""

import pytest
from datetime import datetime
from accounts import Account, CheckingAccount, SavingsAccount, MoneyMarketAccount


class TestAccountBaseClass:
    """Test the abstract Account base class functionality."""
    
    def test_account_cannot_be_instantiated(self):
        """Test that Account base class cannot be instantiated directly."""
        with pytest.raises(TypeError):
            Account("123", "Test Customer", 100.0)
    
    def test_account_attributes(self):
        """Test that account subclasses have correct attributes."""
        account = CheckingAccount("123", "Test Customer", 100.0)
        assert account.account_number == "123"
        assert account.customer_name == "Test Customer"
        assert account.balance == 100.0
        assert isinstance(account.transactions, list)
        assert isinstance(account.created_date, datetime)
    
    def test_account_string_representation(self):
        """Test string representation of accounts."""
        account = CheckingAccount("123", "Test Customer", 100.0)
        str_repr = str(account)
        assert "CheckingAccount" in str_repr
        assert "123" in str_repr
        assert "Test Customer" in str_repr
        assert "100.00" in str_repr
    
    def test_account_repr(self):
        """Test detailed representation of accounts."""
        account = CheckingAccount("123", "Test Customer", 100.0)
        repr_str = repr(account)
        assert "CheckingAccount" in repr_str
        assert "account_number='123'" in repr_str
        assert "customer_name='Test Customer'" in repr_str


class TestCheckingAccount:
    """Test the CheckingAccount class."""
    
    def test_checking_account_creation(self):
        """Test creating a checking account."""
        account = CheckingAccount("1001", "John Doe", 500.0)
        assert account.account_number == "1001"
        assert account.customer_name == "John Doe"
        assert account.balance == 500.0
        assert account.account_type == "Checking"
        assert account.interest_rate == 0.0
    
    def test_checking_account_default_balance(self):
        """Test checking account with default balance."""
        account = CheckingAccount("1002", "Jane Smith")
        assert account.balance == 0.0
    
    def test_checking_deposit_positive(self):
        """Test depositing a positive amount."""
        account = CheckingAccount("1003", "Bob", 100.0)
        result = account.deposit(50.0)
        assert result is True
        assert account.balance == 150.0
        assert len(account.transactions) == 1
        assert account.transactions[0]["type"] == "deposit"
        assert account.transactions[0]["amount"] == 50.0
    
    def test_checking_deposit_zero(self):
        """Test depositing zero amount (should fail)."""
        account = CheckingAccount("1004", "Alice", 100.0)
        result = account.deposit(0.0)
        assert result is False
        assert account.balance == 100.0
        assert len(account.transactions) == 0
    
    def test_checking_deposit_negative(self):
        """Test depositing negative amount (should fail)."""
        account = CheckingAccount("1005", "Charlie", 100.0)
        result = account.deposit(-50.0)
        assert result is False
        assert account.balance == 100.0
        assert len(account.transactions) == 0
    
    def test_checking_withdraw_sufficient_funds(self):
        """Test withdrawing with sufficient funds."""
        account = CheckingAccount("1006", "David", 200.0)
        result = account.withdraw(50.0)
        assert result is True
        assert account.balance == 150.0
        assert len(account.transactions) == 1
        assert account.transactions[0]["type"] == "withdrawal"
    
    def test_checking_withdraw_insufficient_funds(self):
        """Test withdrawing with insufficient funds."""
        account = CheckingAccount("1007", "Eve", 50.0)
        result = account.withdraw(100.0)
        assert result is False
        assert account.balance == 50.0
        assert len(account.transactions) == 0
    
    def test_checking_withdraw_zero(self):
        """Test withdrawing zero amount (should fail)."""
        account = CheckingAccount("1008", "Frank", 100.0)
        result = account.withdraw(0.0)
        assert result is False
        assert account.balance == 100.0
    
    def test_checking_withdraw_negative(self):
        """Test withdrawing negative amount (should fail)."""
        account = CheckingAccount("1009", "Grace", 100.0)
        result = account.withdraw(-50.0)
        assert result is False
        assert account.balance == 100.0
    
    def test_checking_can_withdraw_to_zero(self):
        """Test that checking accounts can withdraw to zero balance."""
        account = CheckingAccount("1010", "Henry", 100.0)
        result = account.withdraw(100.0)
        assert result is True
        assert account.balance == 0.0
    
    def test_checking_calculate_interest(self):
        """Test that checking accounts return zero interest."""
        account = CheckingAccount("1011", "Iris", 1000.0)
        interest = account.calculate_interest()
        assert interest == 0.0
    
    def test_checking_apply_interest(self):
        """Test that checking accounts don't earn interest."""
        account = CheckingAccount("1012", "Jack", 1000.0)
        interest = account.apply_interest()
        assert interest == 0.0
        assert account.balance == 1000.0
    
    def test_checking_get_balance(self):
        """Test getting balance."""
        account = CheckingAccount("1013", "Kate", 250.0)
        assert account.get_balance() == 250.0
    
    def test_checking_transaction_history(self):
        """Test transaction history."""
        account = CheckingAccount("1014", "Liam", 100.0)
        account.deposit(50.0)
        account.withdraw(25.0)
        history = account.get_transaction_history()
        assert len(history) == 2
        assert history[0]["type"] == "deposit"
        assert history[1]["type"] == "withdrawal"


class TestSavingsAccount:
    """Test the SavingsAccount class."""
    
    def test_savings_account_creation_default(self):
        """Test creating a savings account with default parameters."""
        account = SavingsAccount("2001", "John Doe", 500.0)
        assert account.account_number == "2001"
        assert account.customer_name == "John Doe"
        assert account.balance == 500.0
        assert account.account_type == "Savings"
        assert account.interest_rate == 0.02
        assert account.minimum_balance == 100.0
    
    def test_savings_account_creation_custom(self):
        """Test creating a savings account with custom parameters."""
        account = SavingsAccount("2002", "Jane", 1000.0, interest_rate=0.03, minimum_balance=200.0)
        assert account.interest_rate == 0.03
        assert account.minimum_balance == 200.0
    
    def test_savings_deposit(self):
        """Test depositing to savings account."""
        account = SavingsAccount("2003", "Bob", 500.0)
        result = account.deposit(100.0)
        assert result is True
        assert account.balance == 600.0
    
    def test_savings_withdraw_above_minimum(self):
        """Test withdrawing while maintaining minimum balance."""
        account = SavingsAccount("2004", "Alice", 500.0, minimum_balance=100.0)
        result = account.withdraw(300.0)
        assert result is True
        assert account.balance == 200.0
        assert account.balance >= account.minimum_balance
    
    def test_savings_withdraw_below_minimum(self):
        """Test withdrawing that would violate minimum balance."""
        account = SavingsAccount("2005", "Charlie", 500.0, minimum_balance=100.0)
        result = account.withdraw(450.0)  # Would leave 50, below minimum of 100
        assert result is False
        assert account.balance == 500.0
    
    def test_savings_withdraw_to_minimum(self):
        """Test withdrawing to exactly minimum balance."""
        account = SavingsAccount("2006", "David", 500.0, minimum_balance=100.0)
        result = account.withdraw(400.0)  # Leaves exactly 100
        assert result is True
        assert account.balance == 100.0
    
    def test_savings_calculate_interest(self):
        """Test interest calculation for savings account."""
        account = SavingsAccount("2007", "Eve", 1000.0, interest_rate=0.02)
        # Monthly interest = 1000 * (0.02 / 12) = 1000 * 0.001666... ≈ 1.67
        interest = account.calculate_interest()
        expected = 1000.0 * (0.02 / 12)
        assert abs(interest - expected) < 0.01
    
    def test_savings_apply_interest(self):
        """Test applying interest to savings account."""
        account = SavingsAccount("2008", "Frank", 1000.0, interest_rate=0.02)
        initial_balance = account.balance
        interest = account.apply_interest()
        assert interest > 0
        assert account.balance == initial_balance + interest
        assert len(account.transactions) == 1
        assert account.transactions[0]["type"] == "interest"
    
    def test_savings_apply_interest_zero_balance(self):
        """Test applying interest to account with zero balance."""
        account = SavingsAccount("2009", "Grace", 0.0)
        interest = account.apply_interest()
        assert interest == 0.0
        assert account.balance == 0.0
    
    def test_savings_multiple_transactions(self):
        """Test multiple transactions on savings account."""
        account = SavingsAccount("2010", "Henry", 1000.0, minimum_balance=100.0)
        account.deposit(200.0)
        account.withdraw(100.0)
        account.apply_interest()
        assert len(account.transactions) == 3
        assert account.balance > 1100.0  # Should have interest applied


class TestMoneyMarketAccount:
    """Test the MoneyMarketAccount class."""
    
    def test_money_market_account_creation_default(self):
        """Test creating a money market account with default parameters."""
        account = MoneyMarketAccount("3001", "John Doe", 5000.0)
        assert account.account_number == "3001"
        assert account.customer_name == "John Doe"
        assert account.balance == 5000.0
        assert account.account_type == "Money Market"
        assert account.interest_rate == 0.035
        assert account.minimum_balance == 1000.0
        assert account.withdrawal_limit == 6
        assert account.withdrawals_this_month == 0
    
    def test_money_market_account_creation_custom(self):
        """Test creating a money market account with custom parameters."""
        account = MoneyMarketAccount("3002", "Jane", 5000.0, 
                                    interest_rate=0.04, 
                                    minimum_balance=2000.0,
                                    withdrawal_limit=10)
        assert account.interest_rate == 0.04
        assert account.minimum_balance == 2000.0
        assert account.withdrawal_limit == 10
    
    def test_money_market_deposit(self):
        """Test depositing to money market account."""
        account = MoneyMarketAccount("3003", "Bob", 5000.0)
        result = account.deposit(1000.0)
        assert result is True
        assert account.balance == 6000.0
    
    def test_money_market_withdraw_within_limit(self):
        """Test withdrawing within monthly limit."""
        account = MoneyMarketAccount("3004", "Alice", 5000.0, minimum_balance=1000.0)
        result = account.withdraw(500.0)
        assert result is True
        assert account.balance == 4500.0
        assert account.withdrawals_this_month == 1
    
    def test_money_market_withdraw_exceeds_limit(self):
        """Test withdrawing that exceeds monthly limit."""
        account = MoneyMarketAccount("3005", "Charlie", 5000.0, 
                                    minimum_balance=1000.0, withdrawal_limit=2)
        # Make 2 successful withdrawals
        account.withdraw(500.0)
        account.withdraw(500.0)
        # Third withdrawal should fail
        result = account.withdraw(500.0)
        assert result is False
        assert account.withdrawals_this_month == 2
    
    def test_money_market_withdraw_below_minimum(self):
        """Test withdrawing that would violate minimum balance."""
        account = MoneyMarketAccount("3006", "David", 5000.0, minimum_balance=1000.0)
        result = account.withdraw(4500.0)  # Would leave 500, below minimum
        assert result is False
        assert account.balance == 5000.0
    
    def test_money_market_get_remaining_withdrawals(self):
        """Test getting remaining withdrawals."""
        account = MoneyMarketAccount("3007", "Eve", 5000.0, withdrawal_limit=6)
        assert account.get_remaining_withdrawals() == 6
        account.withdraw(500.0)
        assert account.get_remaining_withdrawals() == 5
        account.withdraw(500.0)
        assert account.get_remaining_withdrawals() == 4
    
    def test_money_market_calculate_interest(self):
        """Test interest calculation for money market account."""
        account = MoneyMarketAccount("3008", "Frank", 10000.0, interest_rate=0.035)
        interest = account.calculate_interest()
        expected = 10000.0 * (0.035 / 12)
        assert abs(interest - expected) < 0.01
    
    def test_money_market_apply_interest(self):
        """Test applying interest to money market account."""
        account = MoneyMarketAccount("3009", "Grace", 10000.0, interest_rate=0.035)
        initial_balance = account.balance
        interest = account.apply_interest()
        assert interest > 0
        assert account.balance == initial_balance + interest
        assert len(account.transactions) == 1
        assert account.transactions[0]["type"] == "interest"
    
    def test_money_market_multiple_withdrawals(self):
        """Test multiple withdrawals tracking."""
        account = MoneyMarketAccount("3010", "Henry", 10000.0, 
                                    minimum_balance=1000.0, withdrawal_limit=5)
        for i in range(5):
            result = account.withdraw(500.0)
            assert result is True
            assert account.withdrawals_this_month == i + 1
        
        # Sixth withdrawal should fail
        result = account.withdraw(500.0)
        assert result is False
        assert account.withdrawals_this_month == 5


class TestAccountEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_large_deposit(self):
        """Test depositing a very large amount."""
        account = CheckingAccount("4001", "Test", 0.0)
        result = account.deposit(1000000.0)
        assert result is True
        assert account.balance == 1000000.0
    
    def test_small_deposit(self):
        """Test depositing a very small amount."""
        account = CheckingAccount("4002", "Test", 0.0)
        result = account.deposit(0.01)
        assert result is True
        assert account.balance == 0.01
    
    def test_precision_handling(self):
        """Test handling of floating point precision."""
        account = CheckingAccount("4003", "Test", 100.0)
        account.deposit(0.1)
        account.deposit(0.2)
        # Should handle floating point arithmetic
        assert abs(account.balance - 100.3) < 0.0001
    
    def test_transaction_timestamps(self):
        """Test that transactions have timestamps."""
        account = CheckingAccount("4004", "Test", 100.0)
        account.deposit(50.0)
        transaction = account.transactions[0]
        assert "timestamp" in transaction
        assert isinstance(transaction["timestamp"], datetime)
    
    def test_transaction_history_copy(self):
        """Test that transaction history returns a copy."""
        account = CheckingAccount("4005", "Test", 100.0)
        account.deposit(50.0)
        history1 = account.get_transaction_history()
        history2 = account.get_transaction_history()
        # Should be different objects
        assert history1 is not history2
        # But should have same content
        assert len(history1) == len(history2) == 1

