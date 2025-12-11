class multipleFunctions():
     def list_subfields():
        subfields = (
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        )

        print("Sub-fields in AI are:")
        for field in subfields:
            print(field)
     def oddEven():
            num = int(input("Enter a number: "))
            if((num % 2) == 0):
                print(num, "is Even number")
                message="is Even number"
            else:
                print(num, "is Odd number")
                message="is Odd nmber"
            return message
     def EligibilityForMarriage():
            gender = input("Your Gender:")
            age = int(input("Your Age:"))
            if gender == "male" and age >= 21:
                print("ELIGIBLE")
                message ="is ELIGIBLE"
            elif gender == "female" and age >= 18:
                print("ELIGIBLE")
                message =("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
                message=("NOT ELIGIBLE")
                return message      
     def Percentage():
            marks1=int(input("Subject1 : "))
            marks2=int(input("Subject2 : "))
            marks3=int(input("Subject3 : "))
            marks4=int(input("Subject4 : "))
            marks5=int(input("Subject5 : "))
            total=(marks1+marks2+marks3+marks4+marks5)
            print("Total : ",total)
            per=(total/5)
            print("Percentage : ", per)
            return per
     def triangle():
            Height=float(input("Height : "))
            Breadth=float(input("Breadth : "))
            area=(Height*Breadth)/2
            Height1=float(input("Height1 : "))
            Height2=float(input("Height2 : "))
            Breadth=float(input("Breadth : "))
            peri=(Height1+Height2+Breadth)
            print("Perimeter of Triangle : ",peri)
            return (area,peri)