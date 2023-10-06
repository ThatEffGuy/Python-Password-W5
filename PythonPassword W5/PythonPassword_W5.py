#Password Program

password = "" 
count = 0
correct = False

while password !="password":
    count += 1
    if count>3:
        print("3 attempts. exiting")
        break

    print ("What is your password? Attempt",count)
    password = input()
    if password =="password":
        correct = True
        break

if correct == True:
    print ("Yes, the password is", password, "you may enter")
else:
    print("password is NOT",password,"Goodbye!")