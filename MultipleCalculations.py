class multiplecalculations():
    def Subfields():
        print("Subfields in AI are")
        list=["Machine learning","Neural Network","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for i in list:
            print(i)
    def OddEven():
        number = int(input("enter the number:"))
        if(number%2 ==0):
            print(number,"is even number")
            message=number,"is even number"
        else:
            print(number,"is odd number")
            message=number, "is odd number"
            return message
    def Eligible(gender,age):
        print("Your Gender:",gender)
        print("Your age:",age)
        if((gender=="Male")and(age>=21)):
            print("ELIGIBLE")
            message="ELIGIBLE"
        elif((gender=="Female")and(age>=18)):
            print("ELIGIBLE")
            message="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
        return message
    def percentage(sub1,sub2,sub3,sub4,sub5):
        Total=sub1+sub2+sub3+sub4+sub5
        percentage=(Total/500) * 100
        print("Subject1=",sub1)
        print("Subject2=",sub2)
        print("Subject3=",sub3)
        print("Subject4=",sub4)
        print("Subject5=",sub5)
        print("Total:",Total)
        print("Percentage:",percentage)
        return percentage
    def area_triangle(height,breadth):
        Area = (height*breadth)/2
        print("Height:",height)
        print("Breadth:",breadth)
        print("Area formula:(Height*Breadth)/2")
        print("Area of triangle:",Area)
        return Area
    def perimeter_triangle(height1,height2,breadth):
        Perimeter=height1+height2+breadth
        print("Height1:",height1)
        print("Height2:",height2)
        print("Breadth:",breadth)
        print("Perimeter formula:Height1+Height2+Breadth")
        print("Perimeter of triangle:",Perimeter)
        return Perimeter
    def triangle(height,breadth,Height1,Height2,Breadth):
        Area = (height*breadth)/2
        print("Height:",height)
        print("Breadth:",breadth)
        print("Area formula:(Height*Breadth)/2")
        print("Area of triangle:",Area)
        Perimeter=Height1+Height2+Breadth
        print("Height1:",Height1)
        print("Height2:",Height2)
        print("Breadth:",Breadth)
        print("Perimeter formula:Height1+Height2+Breadth")
        print("Perimeter of triangle:",Perimeter)
        return Area,Perimeter
                    
                        
        
        

    