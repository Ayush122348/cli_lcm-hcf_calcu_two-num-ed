#Showpiece Values:
mid_dash_sep = "---------------------------"
long_dash_sep = "-------------------------------------------------------------"
short_dash_sep = "----"

#Intro Body:
print(long_dash_sep)
print("LCM & HCF Calculator")
print(short_dash_sep)
print("[Author -> Ayush Kumar Kurrey | Edition Name -> Two Num Ed.]")
print(long_dash_sep,"\n")

#Input Management Loop:
while(True):
    try:
        num1 = int(input("Enter the first number (integer only): "))
        num2 = int(input("Enter the second number (integer only): "))
    except(ValueError):
        print(mid_dash_sep)
        print("NOTE: Please enter only the valid and acceptable values.")
        print(short_dash_sep,"\n")
    else:
        break

#Group/Class of important functions:
class main_calculator:
    #Initialization of main parameters:
    def __init__(self, number1:int, number2:int):
        self.number1 = number1
        self.number2 = number2
    
    #Method to prime factorise numbers:
    def prime_factorise(self):
        prime_factors:dict = {}
        
        #Prime Factorisation Algorithm:
        def factorise(num):
            factor_list = []
            divisor:int = 2
            while True:
                num_remainder = (num)%(divisor)
                if num_remainder != 0:
                    divisor += 1
                else:
                    if num == divisor:
                        factor_list.append(divisor)
                        return factor_list
                    else:
                        num = (num//divisor)
                        factor_list.append(divisor)
        
        prime_factors["num1"] = factorise(self.number1)
        prime_factors["num2"] = factorise(self.number2)

        return prime_factors
    
    #Method to find LCM from prime factor lists - To Do!:
    def find_lcm(self):
        pass
        