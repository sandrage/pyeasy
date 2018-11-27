from wormhole import *
accounts = {
    11: Account(11, 'Sandra'),
    12: Account(12, 'Gergawi'),
    13: Account(13, 'SGergawi')
}
class ATM:
    def __init__(self, idn):
        self.idn = idn
    def deposit(self, accnumber, amount):
        accounts[accnumber].deposit(amount)
    def withdraw(self, accnumber, amount):
        accounts[accnumber].withdraw(amount)
    def balance(self, accnumber):
        return accounts[accnumber].balance()
