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

#Simple Input Management Loop:
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
    """
    ### A class containing methods to calculate HCF and LCM of and
    ### also to Prime-Factorise two given numbers.
    
    Things to keep in mind before use:
    * Pass/Give two integer numbers as arguments.
    * Keywords for accepted arguments are, 
    'number1' and 'number2' respectively.
    * Arguments are explicitly converted to integers.
    """
    #Initialization of main parameters:
    def __init__(self, number1:int, number2:int):
        self.number1 = int(number1)
        self.number2 = int(number2)
        
    def prime_factorise(self) -> dict:
        """_Method to prime-factorise both numbers._"""
        
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
    
    def find_hcf(self) -> int:
        """
        _Method to find HCF(Highest Common Factor) of both 
        numbers._
        """
        
        prime_factors:dict = self.prime_factorise()
        hcf:int = 1
        
        for factor in prime_factors["num1"]:
            if factor in prime_factors["num2"]:
                hcf *= factor
                prime_factors["num2"].remove(factor)
            else:
                pass
        
        return hcf
    
    def find_lcm(self) -> int:
        """
        _Method to find LCM(Least/Lowest Common Factor) of both 
        numbers._
        """
        return (self.number1*self.number2)//self.find_hcf()