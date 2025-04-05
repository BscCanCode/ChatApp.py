print("Chat App")
print("What would you like to do?")
print("1.New Chat\n2.Delete Chat\n3.Previous Chat\n4.Show Chats\n5.Exit")
a=[] #here will consider this list as recevier
while True:
    try:
        n=int(input("Enter the choice: "))
        if n==5:
            print("Exit is success!")
            break
        if 0<n<=4:
            if n==1:
                b=input("Enter the message: ")
                a.append(b)
                print("Message Sent Successfully")
            elif n==2:
                if a:
                    a.pop()
                    print("Chat deleted")
                else:
                    print("Stack is empty")
            elif n==3:
                print("This is previous chat")
                print(b)
            elif n==4:
                print("These are chats")
                print(a)
        else:
            print("Appropriate Choice between 1-5")
    except:
        print("Enter appropriate input,See the options and try again")
