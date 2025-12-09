"""
Test driver for the banking application.
Exercises all classes and methods.
"""

from bank import Bank
from accounts import CheckingAccount, SavingsAccount, MoneyMarketAccount


def print_separator(title: str = ""):
    """Print a visual separator for test sections."""
    if title:
        print(f"\n{'=' * 70}")
        print(f"  {title}")
        print(f"{'=' * 70}\n")
    else:
        print(f"\n{'-' * 70}\n")


def test_account_creation():
    """Test creating different types of accounts."""
    print_separator("TEST 1: Account Creation")
    
    bank = Bank("Test Bank")
    
    # Create checking account
    acc1 = bank.create_account("checking", "John Doe", 500.0)
    print(f"Created checking account: {acc1}")
    
    # Create savings account
    acc2 = bank.create_account("savings", "Jane Smith", 1000.0)
    print(f"Created savings account: {acc2}")
    
    # Create money market account
    acc3 = bank.create_account("moneymarket", "Bob Johnson", 5000.0)
    print(f"Created money market account: {acc3}")
    
    # Try to create account with insufficient initial balance
    acc4 = bank.create_account("savings", "Alice Brown", 50.0)
    print(f"Attempted to create savings account with $50 (should fail): {acc4}")
    
    # List all accounts
    print("\nAll accounts in bank:")
    accounts = bank.list_all_accounts()
    for acc_info in accounts:
        print(f"  {acc_info}")
    
    return bank, acc1, acc2, acc3


def test_deposits_and_withdrawals(bank, checking_acc, savings_acc, mm_acc):
    """Test deposit and withdrawal operations."""
    print_separator("TEST 2: Deposits and Withdrawals")
    
    # Test deposits
    print("--- Testing Deposits ---")
    bank.deposit(checking_acc, 200.0)
    bank.deposit(savings_acc, 500.0)
    bank.deposit(mm_acc, 1000.0)
    
    # Test invalid deposit
    bank.deposit(checking_acc, -50.0)
    
    # Test withdrawals
    print("\n--- Testing Withdrawals ---")
    bank.withdraw(checking_acc, 100.0)
    bank.withdraw(savings_acc, 200.0)
    bank.withdraw(mm_acc, 500.0)
    
    # Test insufficient funds
    print("\n--- Testing Insufficient Funds ---")
    bank.withdraw(checking_acc, 10000.0)
    
    # Test minimum balance violation (savings)
    print("\n--- Testing Minimum Balance Requirements ---")
    bank.withdraw(savings_acc, 900.0)  # Should fail - would go below minimum
    
    # Check balances
    print("\n--- Current Balances ---")
    print(f"Checking account {checking_acc}: ${bank.get_balance(checking_acc):.2f}")
    print(f"Savings account {savings_acc}: ${bank.get_balance(savings_acc):.2f}")
    print(f"Money Market account {mm_acc}: ${bank.get_balance(mm_acc):.2f}")


def test_transfers(bank, checking_acc, savings_acc, mm_acc):
    """Test transfer operations."""
    print_separator("TEST 3: Transfers")
    
    print("--- Testing Valid Transfers ---")
    bank.transfer(checking_acc, savings_acc, 50.0)
    bank.transfer(savings_acc, mm_acc, 100.0)
    
    print("\n--- Testing Invalid Transfers ---")
    bank.transfer(checking_acc, savings_acc, 10000.0)  # Insufficient funds
    bank.transfer(checking_acc, "9999", 50.0)  # Invalid account
    bank.transfer(checking_acc, checking_acc, 50.0)  # Same account
    
    print("\n--- Balances After Transfers ---")
    print(f"Checking account {checking_acc}: ${bank.get_balance(checking_acc):.2f}")
    print(f"Savings account {savings_acc}: ${bank.get_balance(savings_acc):.2f}")
    print(f"Money Market account {mm_acc}: ${bank.get_balance(mm_acc):.2f}")


def test_interest_processing(bank, checking_acc, savings_acc, mm_acc):
    """Test interest calculation and processing."""
    print_separator("TEST 4: Interest Processing")
    
    # Get account info before interest
    print("--- Account Balances Before Interest ---")
    print(f"Checking: ${bank.get_balance(checking_acc):.2f}")
    print(f"Savings: ${bank.get_balance(savings_acc):.2f}")
    print(f"Money Market: ${bank.get_balance(mm_acc):.2f}")
    
    # Process interest for individual accounts
    print("\n--- Processing Interest for Individual Accounts ---")
    interest1 = bank.process_interest(checking_acc)
    print(f"Interest applied to checking account: ${interest1:.2f}")
    
    interest2 = bank.process_interest(savings_acc)
    print(f"Interest applied to savings account: ${interest2:.2f}")
    
    interest3 = bank.process_interest(mm_acc)
    print(f"Interest applied to money market account: ${interest3:.2f}")
    
    # Process interest for all accounts
    print("\n--- Processing Interest for All Accounts ---")
    all_interest = bank.process_interest_all()
    print(f"Interest applied to {len(all_interest)} accounts:")
    for acc_num, interest in all_interest.items():
        print(f"  Account {acc_num}: ${interest:.2f}")
    
    # Show balances after interest
    print("\n--- Account Balances After Interest ---")
    print(f"Checking: ${bank.get_balance(checking_acc):.2f}")
    print(f"Savings: ${bank.get_balance(savings_acc):.2f}")
    print(f"Money Market: ${bank.get_balance(mm_acc):.2f}")


def test_money_market_withdrawal_limits(bank, mm_acc):
    """Test money market account withdrawal limits."""
    print_separator("TEST 5: Money Market Withdrawal Limits")
    
    account = bank.get_account(mm_acc)
    if isinstance(account, MoneyMarketAccount):
        print(f"Money Market account withdrawal limit: {account.withdrawal_limit} per month")
        print(f"Remaining withdrawals: {account.get_remaining_withdrawals()}")
        
        print("\n--- Testing Multiple Withdrawals ---")
        for i in range(account.withdrawal_limit + 2):
            amount = 100.0
            print(f"\nWithdrawal attempt {i + 1}:")
            success = bank.withdraw(mm_acc, amount)
            if success:
                print(f"  Success! Remaining withdrawals: {account.get_remaining_withdrawals()}")
            else:
                print(f"  Failed - limit exceeded or other issue")


def test_transaction_history(bank, checking_acc, savings_acc):
    """Test transaction history retrieval."""
    print_separator("TEST 6: Transaction History")
    
    print(f"--- Transaction History for Checking Account {checking_acc} ---")
    history = bank.get_transaction_history(checking_acc)
    if history:
        for i, trans in enumerate(history, 1):
            print(f"  {i}. {trans['type'].upper()}: ${trans['amount']:.2f} "
                  f"at {trans['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} "
                  f"(Balance after: ${trans['balance_after']:.2f})")
    
    print(f"\n--- Transaction History for Savings Account {savings_acc} ---")
    history = bank.get_transaction_history(savings_acc)
    if history:
        for i, trans in enumerate(history, 1):
            print(f"  {i}. {trans['type'].upper()}: ${trans['amount']:.2f} "
                  f"at {trans['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} "
                  f"(Balance after: ${trans['balance_after']:.2f})")


def test_account_info(bank):
    """Test account information retrieval."""
    print_separator("TEST 7: Account Information")
    
    accounts = bank.list_all_accounts()
    for acc_info in accounts:
        print(f"\nAccount {acc_info['account_number']}:")
        print(f"  Customer: {acc_info['customer_name']}")
        print(f"  Type: {acc_info['account_type']}")
        print(f"  Balance: ${acc_info['balance']:.2f}")
        print(f"  Created: {acc_info['created_date']}")
        print(f"  Transactions: {acc_info['transaction_count']}")
        if 'interest_rate' in acc_info:
            print(f"  Interest Rate: {acc_info['interest_rate']}")
        if 'minimum_balance' in acc_info:
            print(f"  Minimum Balance: ${acc_info['minimum_balance']:.2f}")
        if 'remaining_withdrawals' in acc_info:
            print(f"  Remaining Withdrawals: {acc_info['remaining_withdrawals']}/{acc_info['withdrawal_limit']}")


def test_edge_cases(bank):
    """Test edge cases and error handling."""
    print_separator("TEST 8: Edge Cases and Error Handling")
    
    # Test operations on non-existent account
    print("--- Testing Non-Existent Account ---")
    bank.deposit("9999", 100.0)
    bank.withdraw("9999", 100.0)
    bank.get_balance("9999")
    bank.process_interest("9999")
    
    # Test invalid amounts
    print("\n--- Testing Invalid Amounts ---")
    accounts = bank.list_all_accounts()
    if accounts:
        test_acc = accounts[0]['account_number']
        bank.deposit(test_acc, 0.0)
        bank.deposit(test_acc, -10.0)
        bank.withdraw(test_acc, 0.0)
        bank.withdraw(test_acc, -10.0)
    
    # Test account creation with custom parameters
    print("\n--- Testing Custom Account Parameters ---")
    acc1 = bank.create_account("savings", "Custom Customer", 500.0,
                               interest_rate=0.03, minimum_balance=200.0)
    if acc1:
        info = bank.get_account_info(acc1)
        if info:
            print(f"Created account with custom interest rate: {info.get('interest_rate')}")
            print(f"Custom minimum balance: ${info.get('minimum_balance'):.2f}")


def main():
    """Main test driver function."""
    print("\n" + "=" * 70)
    print(" " * 20 + "BANKING APPLICATION TEST DRIVER")
    print("=" * 70)
    
    # Run all tests
    bank, checking_acc, savings_acc, mm_acc = test_account_creation()
    test_deposits_and_withdrawals(bank, checking_acc, savings_acc, mm_acc)
    test_transfers(bank, checking_acc, savings_acc, mm_acc)
    test_interest_processing(bank, checking_acc, savings_acc, mm_acc)
    test_money_market_withdrawal_limits(bank, mm_acc)
    test_transaction_history(bank, checking_acc, savings_acc)
    test_account_info(bank)
    test_edge_cases(bank)
    
    print_separator("TEST SUMMARY")
    print(f"Bank: {bank}")
    print(f"Total accounts: {len(bank.list_all_accounts())}")
    print("\nAll tests completed!")


if __name__ == "__main__":
    main()

