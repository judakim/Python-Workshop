from time import time
from sys import argv

class Jphone:

    def isInContacts(self, contact):
        with open('contacts.csv', 'r') as fHandle:
            for line in fHandle:
                if contact in line:
                    return True
            return False

    def add(self, contact="", num=""):
        if not(self.isInContacts(contact)):
            try:
                with open('contacts.csv', 'a') as fHandle:
                    fHandle.write(contact + ',' + num + '\n')
            except ExceptionError:
                print("File opening failed")
        else:
            print("The contct alrady exist")

    def call(self, contact=""):
        if contact.isnumeric() or self.isInContacts(contact):
            t0 = time()
            input("Calling " + contact + "...")
            t = time() - t0
            with open('call_logs.csv', 'a') as fHandle:
                fHandle.write(contact + ',' + str(t) + '\n')
        else:
            raise Exception("Enter a valid contact..")


jphone = Jphone()

if argv[1] == "add":
    jphone.add(argv[2], argv[3])
elif argv[1] == "call":
    jphone.call(argv[2])
else:
    raise Exception("invalid argument. Enter only add or call as parameters!")
