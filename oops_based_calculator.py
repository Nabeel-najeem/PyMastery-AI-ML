class calculator_function:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def add(self):
        r=self.x+self.y
        return r
    
    def sub(self):
        r=self.x-self.y
        return r
    
    def mult(self):
        r=self.x*self.y
        return r
    def div(self):
        r=self.x/self.y
        return r
    
#prob=calculator_function(5,6)
#print(prob.add())

while True:
    print("1 : addition\t2 : substraction\t3 : multiplication\t4 : division\t5 : exit")
    opt=int(input("select the option from below : "))
    if opt == 5:
        print("exiting..")
        break
    elif opt == 1 or opt == 2 or opt == 3 or opt == 4 :   
        num1=float(input("enter the first number : "))
        num2=float(input("enter the second number : "))
        prob=calculator_function(num1,num2)
        if opt == 1 :
            print(prob.add())
        elif opt == 2 :
            print(prob.sub())
        elif opt == 3 :
            print(prob.mult())
        elif opt == 4 :
            print(prob.div())
    else :
        print("Error invalid input..")
        