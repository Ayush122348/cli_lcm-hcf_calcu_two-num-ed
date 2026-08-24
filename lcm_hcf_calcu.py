# Showpiece Values:
mid_dash_sep = "---------------------------"
long_dash_sep = "-------------------------------------------------------------"
short_dash_sep = "----"

# Intro Body:
print(long_dash_sep)
print("LCM & HCF Calculator")
print(short_dash_sep)
print("[Author -> Ayush Kumar Kurrey | Edition -> Two Num Ed.]")
print(long_dash_sep)

# Simple Input Management Loop:
while(True):
    try:
        num1 = int(input("Enter the 1st number (integer only): "))
        num2 = int(input("Enter the 2nd number (integer only): "))
        orig_usr_inputs = {"num1": num1, "num2": num2}
    except(ValueError):
        print(mid_dash_sep)
        print("NOTE: Please enter only the valid and acceptable values.")
        print(short_dash_sep,"\n")
    else:
        #Getting absolute values of inputs:
        num1 = abs(num1)
        num2 = abs(num2)
        break

# Group/Class of important functions:
class Main_Calculator:
    """
    ### A class containing methods to calculate HCF and LCM of and
    ### also to Prime-Factorise two given numbers.
    
    Things to keep in mind before use:
    * Pass/Give two integer numbers as arguments.
    * Keywords for accepted arguments are, 
    'number1' and 'number2' respectively.
    * Arguments are explicitly converted to integers.
    """
    # Initialization of main parameters:
    def __init__(self, number1:int, number2:int):
        self.number1 = int(number1)
        self.number2 = int(number2)
        
    def prime_factorise(self) -> dict:
        """_Method to prime-factorise both numbers._"""
        
        prime_factors:dict = {}
        
        def factorise(num):
            """
            _Prime Factorisation Algorithm (Internal Nested Function)_
            """
            # Some Prerequisite Values:
            factor_list = []
            divisor:int = 2
            
            # 0 and 1 has no prime divisors:
            if num == 0 or num == 1:
                return factor_list
            
            # Main Prime-Factorisation Loop:
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
        
        # Neutral Integer Value Handling
        # (HCF is always positive and non-zero):
        if (num1 == 0 and num2 != 0) or (num2 == 0 and num1 != 0):
            return max([num1,num2])
        elif num1 == 0 and num2 == 0:
            raise Exception(f"HCF({num1},{num2}) undefined.")
        else:
            # Some Prerequisite Values:
            prime_factors:dict = self.prime_factorise()
            hcf:int = 1
            
            # HCF Calculating Algorithm:
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
        # Neutral Integer Value Handling
        # (LCM is always non-negative.):
        if (num1 == 0 and num2 != 0) or (num2 == 0 and num1 != 0):
            return min([num1,num2])
        elif num1 == 0 and num2 == 0:
            return 0
        else:
            #LCM Formula:
            return (self.number1*self.number2)//self.find_hcf()

# An important class object:
calcu = Main_Calculator(num1,num2)

# Some Prerequisite Values:
prime_factors_dict:dict = calcu.prime_factorise()
final_lcm:int = calcu.find_lcm()
final_prime_factors_dict:dict = {"num1": "", "num2": ""}
txt_for_undefined_val = "UNDEFINED"

# A For-Loop family for creating string values representing
# prime-factors of the numbers in a neat/presentable way:
for factors_key in prime_factors_dict:
    current_factor_list = prime_factors_dict[factors_key]
    to_called_none_vals = (1,-1)
    if (len(current_factor_list) == 0) and (orig_usr_inputs[factors_key] not in 
                                            to_called_none_vals):
        final_prime_factors_dict[factors_key] = txt_for_undefined_val
        continue
    elif (len(current_factor_list) == 0 and (orig_usr_inputs[factors_key] in 
                                             to_called_none_vals)):
        final_prime_factors_dict[factors_key] = "NONE"
        continue
    else:
        if orig_usr_inputs[factors_key] < 0:
            final_prime_factors_dict[factors_key] = "-1"
        for factor in current_factor_list[:]:
            factor_count = current_factor_list.count(factor)
            if factor_count == 0:
                continue
            if len(final_prime_factors_dict[factors_key]) == 0:
                    final_prime_factors_dict[factors_key] = (f"{factor}^"
                                                            f"{factor_count}")
                    current_factor_list[:] = [x for x in current_factor_list 
                                            if x != factor]
            else:
                final_prime_factors_dict[factors_key] += (f" * {factor}^"
                                                            f"{factor_count}")
                current_factor_list[:] = [x for x in current_factor_list 
                                        if x != factor]

# Work-related user entertainment:
print(long_dash_sep)
print(f"- Prime Factors of The 1st Number: {final_prime_factors_dict["num1"]}")
print(f"- Prime Factors of The 2nd Number: {final_prime_factors_dict["num2"]}")
print(f"  {short_dash_sep}")
print(f"- LCM({orig_usr_inputs["num1"]},{orig_usr_inputs['num2']}): "
      f"{final_lcm}")
# Special treatment for HCF Value output, as it can be 
# 'Undefined':
try:
    print(f"- HCF({orig_usr_inputs['num1']},{orig_usr_inputs['num2']}): ", 
          end="")
    final_hcf:int = calcu.find_hcf()
except(Exception):
    print(txt_for_undefined_val)
else:
    print(final_hcf)
print(long_dash_sep)
# Formality for exiting program:
print("[Press Enter Twice to Exit...]")
for i in range(2):
    input("")