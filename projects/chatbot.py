while True:
    user=input("ask u r quetion:")
    if user.lower():
        if user in ['hello','hi']:
            print("bot: hi, how can i help you?")
        elif user == "courses":
            print("bot: MITS offered mca,mba,b.tech,m.tech")
        elif user=="hostel":
            print("bot: separate hostels is there for girls and boys")
        elif user == "bye":
            print("thak u ")
            break
        else:
            print("i dont understand")
            break
