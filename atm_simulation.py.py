class ATM:
    def __init__(self):
        # Initialize ATM with a default account
        self.balance = 1000.00  # Starting balance
        self.pin = "1234"  # Default PIN
        self.transaction_history = []  # List to store transaction history
        self.is_logged_in = False  # Flag for login status

    def login(self, entered_pin):
        """
        Attempts to log the user into the ATM system.
        If the PIN is correct, the user is logged in.
        """
        if entered_pin == self.pin:
            self.is_logged_in = True
            print("Login successful.")
        else:
            print("Invalid PIN. Please try again.")

    def logout(self):
        """Logs the user out of the ATM system."""
        self.is_logged_in = False
        print("You have been logged out.")

    def check_balance(self):
        """
        Displays the current account balance.
        """
        if self.is_logged_in:
            print(f"Your current balance is: ${self.balance:.2f}")
        else:
            print("Please login first.")

    def withdraw(self, amount):
        """
        Allows the user to withdraw a specific amount of cash from the account.
        Ensures the user has sufficient funds and is logged in.
        """
        if self.is_logged_in:
            if amount > self.balance:
                print("Insufficient funds for this transaction.")
            else:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawal: ${amount:.2f}")
                print(f"Withdrawal of ${amount:.2f} successful. Your new balance is: ${self.balance:.2f}")
        else:
            print("Please login first.")

    def deposit(self, amount):
        """
        Allows the user to deposit a specific amount into the account.
        """
        if self.is_logged_in:
            if amount <= 0:
                print("Deposit amount must be greater than zero.")
            else:
                self.balance += amount
                self.transaction_history.append(f"Deposit: ${amount:.2f}")
                print(f"Deposit of ${amount:.2f} successful. Your new balance is: ${self.balance:.2f}")
        else:
            print("Please login first.")

    def change_pin(self, old_pin, new_pin):
        """
        Allows the user to change their PIN.
        The user must enter their current PIN to proceed with changing to a new one.
        """
        if self.is_logged_in:
            if old_pin == self.pin:
                self.pin = new_pin
                print("PIN successfully changed.")
            else:
                print("Incorrect old PIN. Please try again.")
        else:
            print("Please login first.")

    def view_transaction_history(self):
        """
        Displays the transaction history.
        """
        if self.is_logged_in:
            if self.transaction_history:
                print("Transaction History:")
                for transaction in self.transaction_history:
                    print(transaction)
            else:
                print("No transactions found.")
        else:
            print("Please login first.")

    def run_atm(self):
        """
        The main method that runs the ATM simulation.
        It provides a menu for the user to choose actions.
        """
        while True:
            print("\nATM Main Menu:")
            print("1. Login")
            print("2. Check Balance")
            print("3. Withdraw")
            print("4. Deposit")
            print("5. Change PIN")
            print("6. View Transaction History")
            print("7. Logout")
            print("8. Exit")

            choice = input("Select an option (1-8): ")

            if choice == "1":
                pin = input("Enter your PIN: ")
                self.login(pin)
            elif choice == "2":
                self.check_balance()
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == "4":
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == "5":
                old_pin = input("Enter your current PIN: ")
                new_pin = input("Enter your new PIN: ")
                self.change_pin(old_pin, new_pin)
            elif choice == "6":
                self.view_transaction_history()
            elif choice == "7":
                self.logout()
            elif choice == "8":
                print("Exiting ATM. Thank you for using our service.")
                break
            else:
                print("Invalid selection. Please choose again.")

# Create an ATM object and run the ATM simulation
atm_machine = ATM()
atm_machine.run_atm()
