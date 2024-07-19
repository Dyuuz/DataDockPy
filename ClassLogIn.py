from ClassLF import *
import time
time.sleep(1)
print("""Welcome to DataDocks App. To proceed:
Input 1 to sign up a fresh account.
Input 2 to sign in if have a registered accont.
Input 3 to change password.\n""")


check = validae.cmd_check()
time.sleep(4)
if check == 1:
    validae_self = validae()
    validae_self.signup_details()
    validae_self.signup()
    print("Processing login request...\n")
    time.sleep(4)

    if check:
        validae.log_in()

elif check == 2:
    
    validae.log_in()

elif check == 3:
    
    validae.change_passkey()