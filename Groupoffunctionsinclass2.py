class multiplefunctions():
    def oddeven():
        num=int(input("Enter a number:"))
        if (num%2==1):
            print(num, "is Odd number")
            message="odd number"
        else:
            print(num, "is Even number")
            message="Even number"
        return message


    def Eligible1():
        Gender=input("Your Gender:")
        Agelimit=int(input("Your Age:"))
        if(Agelimit>=21) and (Gender=="Male"):
                print("Eligible")
                Age="Eligible"
        elif(Agelimit>=18) and (Gender=="Female"):
                print("Eligible")
                Age="Eligible"
        else:
                print("NOT ELIGIBLE")
                Age="NOT ELIGIBLE"
        return Age    