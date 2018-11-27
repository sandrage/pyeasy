from account import Account
import types
import inspect

def decorate_me(func):
    def wrapper(*args):
        accountnumber = args[0].number
        owner = args[0].owner
        balance = args[1]
        atmcaller = inspect.currentframe().f_back.f_locals['self']
        print("# At the ATM{0} Has been requested a <<{1}>> on the account {4} owned by {2} for {3}".format(atmcaller.idn,func.__name__,owner, balance, accountnumber))
        return func(*args)
    return wrapper

class LoggerMetaclass(type):
    def __new__(metac,clsname,subs,dct):
        for key,val in dct.items():
            if type(val) is types.FunctionType and (key=='deposit' or key=='withdraw'):
                dct[key]=decorate_me(val)
        return type.__new__(metac,clsname,subs,dct)

Account = LoggerMetaclass('Account',(),dict(Account.__dict__))
