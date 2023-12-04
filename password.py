password = "password"
def askpasw():
    for i in range(3):
        p= input("pass")
        if p == password:
            print("rait")
            return
    print("щтказ")
askpasw()