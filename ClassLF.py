import time
class validae:
    def __init__(self):
        self.user = None
        self.password = None

    def signup(self):
        def register():
            while True:
                if self.signup_cond():
                    time.sleep(1)
                    print(f"The username '{self.user}' has already been taken.\n")
                    self.user = input('Create a new username: ').title()
                    self.password = input('Create a new password: ')
                    
                else:
                    with open('Logins.txt', mode="a") as file:
                        file.write(f"{self.user} {self.password}\n")
                        time.sleep
                        print("You have successfully signed up")
                        break
        register()
        
    def signup_details(self):
        if self.user == None and self.password == None:
            self.user = input('Create your username: ').title()
            self.password = input('Create your password: ')

    def signup_cond(self):
        return validae.userexists(self.user)
    
    def cmd_check():
        while True:
            try:
                check_string = input("Input command: ")
                check = int(check_string)
                commands = [1, 2, 3]
                print("Command check in progress...\n")
                time.sleep(1)
                if check in commands:
                    return check
                else:
                     print(f'{check} is not part of the commands. Try again!\n')
            except ValueError:
                print("Command check in progress...")
                time.sleep(3)
                print(f'{check_string} is not part of the commands. Try again!\n')
            
    def readfile():
        with open('Logins.txt', mode='r') as file:
            filelist = file.readlines()
            data = [element.split() for element in filelist]
            return data  

    def filelines():
        with open('Logins.txt', mode='r') as file:
            filelist = file.readlines()
            return filelist

    def writelines(updateline):
        with open('Logins.txt', mode='w') as file:
            file.writelines(updateline)
    
    def userexists(username):
        data = validae.readfile()
        listscan = [[data.index(sublist), data[data.index(sublist)].index(username)]
                for sublist in data for item in sublist if item == username]
        return listscan
    
    def login_details():
        signin_username = input('Input your username: ').title()
        signin_password = input('Input your password: ')
        list = [signin_username, signin_password]
        return list
    
    def log_in():
        while True:
            data = validae.readfile()
            list = validae.login_details()
            if list in data:
                index = data.index(list)
                print("Verifying credentials...")
                time.sleep(1)
                print("You have successfully signed in")
                print(f"Welcome, {list[0]}!")
                break

            elif list not in data:
                lue_text = "Username exists but password does not correspond."
                listuserex = [lue_text for element in data if list[0] == element[0] and list[1] != element[1]]
                print("Verifying user details...")
                time.sleep(1)
                if listuserex:
                    print("".join(listuserex) + '\n')
                else:
                     print("Credentials doesn't exist, pls verify your inputs.\n")
                
    def change_passkey():
        while True:
            username = input('Input your username: ').title()
            data = validae.readfile()
            listscan = validae.userexists(username)
            print(f"Checking username '{username}' if it exists...")
            time.sleep(3)
            if listscan:
                listupdate = listscan[0][0]
                listspread = [item for data in listscan for item in data]
                system_user = data[listspread[0]][listspread[1]]

                if username == system_user:
                        print("Usernmae exists in DataBase.\n")
                        file_list = validae.filelines()
                        new_password = input('Input your new password: ')
                        file_list[listupdate] = f"{username} {new_password}\n"
                        validae.writelines(file_list)
                        time.sleep(1)
                        print(f"{username}, your new password is {new_password}")
                        break
            else:
                    print("Account doesn't exist, input correct details\n")
