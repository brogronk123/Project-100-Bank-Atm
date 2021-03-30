class Atm:
    def __init__(self,cardNumber,Pin,Cash):
        self.cardNumber = cardNumber
        self.Pin = Pin
        self.Cash = Cash

    def check_balance(self):
        print("Your balance is "+str(self.Cash))

    def Withdrawl(self,amount):
        new_amount = self.Cash - amount
        self.Cash = self.Cash - amount
        print("You have withdrawn "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
    Card_number = input("Card Number: ")
    pin_number  = input("Pin Number: ")

    new_user =  Atm(Card_number ,pin_number,50000)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("Enter activity number : "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("Enter the amount: "))
        new_user.Withdrawl(amount)
    else:
        print("Enter a valid number")


if __name__ == "__main__":
    main()