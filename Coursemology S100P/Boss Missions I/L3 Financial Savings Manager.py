import pickle
import os

class FinancialSavingsManager:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Error: Cannot deposit a negative amount.")
        else:
            self.balance += amount
            print(f"Deposited ${amount:.2f} successfully. New balance: ${self.balance:.2f}")
            self.save_data()

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Cannot withdraw a negative amount.")
        elif amount > self.balance:
            print("Error: Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} successfully. New balance: ${self.balance:.2f}")
            self.save_data()

    def simulate_interest(self, years):
        if years < 0:
            print("Error: Cannot simulate a negative number of years.")
        else:
            interest_rate = 0.01
            future_balance = self.balance * (1 + interest_rate) ** years
            print(f"Simulating {years} years at 1% interest. Projected balance: ${future_balance:.2f}")

    def view_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def save_data(self):
        with open("savings_data.pkl", "wb") as file:
            pickle.dump(self.balance, file)

    def load_data(self):
        try:
            with open("savings_data.pkl", "rb") as file:
                self.balance = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.balance = 0.0

def main():
    savings_manager = FinancialSavingsManager()
    savings_manager.load_data()

    while True:
        print("\nFinancial Savings Manager Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Simulate Interest")
        print("4. View Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            os.system('cls')
            try:
                amount = float(input("Enter the amount to deposit: "))
                savings_manager.deposit(amount)
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")

        elif choice == "2":
            os.system('cls')
            try:
                amount = float(input("Enter the amount to withdraw: "))
                savings_manager.withdraw(amount)
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")

        elif choice == "3":
            os.system('cls')
            try:
                years = int(input("Enter the number of years to simulate: "))
                savings_manager.simulate_interest(years)
            except ValueError:
                print("Error: Invalid input. Please enter a valid number of years.")

        elif choice == "4":
            os.system('cls')
            savings_manager.view_balance()
            
        elif choice == "5":
            print("Exiting Financial Savings Manager.\n")
            break
        else:
            print("Invalid choice. Please try again.")

main()