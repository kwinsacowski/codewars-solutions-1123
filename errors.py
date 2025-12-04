account_balance = 1500.0

try:
    num1 = float(input("How much would you like to withdraw? "))
    
    if num1 < 0:
        raise ValueError("Withdrawal amount cannot be negative.")
    if num1 > account_balance:
        raise ValueError("Insufficient funds for this withdrawal.")
    
    account_balance -= num1
    print(f"Withdrawal successful.")

except ValueError as e:
    print(e)

finally:
    print(f"Current Account Balance: ${account_balance:.2f}")
