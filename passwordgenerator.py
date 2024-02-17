from cryptography.fernet import Fernet

def write_key():
    key =Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file= open("key.key", "rb")
    key= file.read()
    file.close()
    return key


pwd= input(" what is the master password?")
key= load_key() + pwd.encode()
fer=Fernet(key)


mode= input(" would you like to add a new passord or view exisitng ones(view,add)Press q to quit?")



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            "hello|tim"
            user,passw= ["hello", "tim"]
            print("user:", user, " |,password", fer.decrypt(passw.encode()).decode())

def add():
    name=input("account name")
    pwd=input("password:")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode= input(" would you like to add a new passord or view exisitng ones(view,add)Press q to quit?")
    if mode=="q":
        break
    if mode=="view":
      view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode.")
        continue


