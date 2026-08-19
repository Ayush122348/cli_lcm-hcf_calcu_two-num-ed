#Showpiece Values:
mid_dash_sep = "---------------------------"
long_dash_sep = "--------------------------------------------------"
short_dash_sep = "----"

#Intro Body:
print(long_dash_sep)
print("LCM & HCF Calculator")
print(short_dash_sep)
print("[UI -> CLI | Author -> Ayush Kumar Kurrey |"
      " Edition Name -> Two Num Ver. Ed.]")
print(long_dash_sep)

#Input Management Loop:
while(True):
    try:
        num1 = int(input("Enter the first number (integer only): "))
        num2 = int(input("Enter the second number (integer only): "))
    except(ValueError):
        print(mid_dash_sep)
        print("Please enter only the valid and acceptable values.\n")
    else:
        break
