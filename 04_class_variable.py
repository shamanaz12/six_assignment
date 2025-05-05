class Bank:
    bank_name = "My Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show(self):
        print("Bank name is", Bank.bank_name)

a = Bank()
a.show()
Bank.change_bank_name("New Bank")
b = Bank()
b.show()
