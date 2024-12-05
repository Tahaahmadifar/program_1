import random
import math
from gooey import Gooey,GooeyParser
@Gooey(program_name='multi tab')

def main():
    parser = GooeyParser()
    sp = parser.add_subparsers(dest = 'forfunc')
    ap = sp.add_parser('intro')
    ag = ap.add_argument_group('introduction')
    ag.add_argument('description', widget='Textarea', gooey_options ={'intial_value': 'my first program include gusse random nubmer game,even & odd,calculator,registration,search in DB ','height':400 , 'readonly':True})
    
    ap1 = sp.add_parser('random')
    ap1.add_argument('gusse_number', help='plz enter your gusse')
    
    ap2 = sp.add_parser('Even_Odd')
    ap2.add_argument('number1', help='plz enter your number')
    ap2.add_argument('number2', help='plz enter your number')
    ap2.add_argument('number3', help='plz enter your number')
    ap2.add_argument('number4', help='plz enter your number')
    ap2.add_argument('number5', help='plz enter your number')

    ap3 = sp.add_parser('Calculator')
    ap3.add_argument('number1', help='plz enter your number')
    ap3.add_argument('number2', help='plz enter your number')
    ap3.add_argument('operation', choices=['+','-','*','/','sqrt'] , help='plz select operation')

    ap4 = sp.add_parser('Registration')
    ap4.add_argument('username1',help='plz enter your username')
    ap4.add_argument('password1',help='plz enter your password')
    ap4.add_argument('username2',help='plz enter your username')
    ap4.add_argument('password2',help='plz enter your password')
    ap4.add_argument('username3',help='plz enter your username')
    ap4.add_argument('password3',help='plz enter your password')
    ap4.add_argument('username4',help='plz enter your username')
    ap4.add_argument('password4',help='plz enter your password')
    ap4.add_argument('username5',help='plz enter your username')
    ap4.add_argument('password5',help='plz enter your password')
    
    args = parser.parse_args()
    return args

def subparsers2(gusse_number):
    random_number = random.randint(1,2)
    if random_number == int(gusse_number):
        print("correct")
        print(f"random number is {random_number} and gusse number is {int(gusse_number)}")
    else:
        print("incorrect")
        print(f"random number is {random_number} and gusse number is {int(gusse_number)}")

def subparsers3(number1,number2,number3,number4,number5):
    lst_Even = []
    lst_Odd = []
    if int(number1) % 2 == int(0):
        lst_Even.append(int(number1))
        print("zoj")
    else:
        lst_Odd.append(int(number1))
        print("fard")
    if int(number2) % 2 == int(0):
        lst_Even.append(int(number2))
        print("zoj")
    else:
        lst_Odd.append(int(number2))
        print("fard")
    if int(number3) % 2 == int(0):
        lst_Even.append(int(number3))
        print("zoj")
    else:
        lst_Odd.append(int(number3))
        print("fard")
    if int(number4) % 2 == int(0):
        lst_Even.append(int(number4))
        print("zoj")
    else:
        lst_Odd.append(int(number4))
        print("fard") 
    if int(number5) % 2 == int(0):
        lst_Even.append(int(number5))
        print("zoj")
    else:
        lst_Odd.append(int(number5))
        print("fard")
        print(sum(lst_Even))
        print(sum(lst_Odd))

def subparsers4(number1,number2,operation):
    if operation == "+":
        print(int(number1)+int(number2))
    elif operation == "-":
        print(int(number1)-int(number2))
    elif operation == "*":
        print(int(number1)*int(number2))
    elif operation == "/":
        print(int(number1)/int(number2))
    elif operation == "sqrt":
        print(math.sqrt(int(number1)))
        print(math.sqrt(int(number2)))
    else:
        print('Error') 

def subparsers5(username1,password1,username2,password2,username3,password3,username4,password4,username5,password5):
        with open("test.txt","a") as f:
            f.write('{}'.format(username1))
            f.write("\n")
            f.write('{}'.format(password1))
            f.write("\n")
            f.write('{}'.format(username2))
            f.write("\n")
            f.write('{}'.format(password2))
            f.write("\n")
            f.write('{}'.format(username3))
            f.write("\n")
            f.write('{}'.format(password3))
            f.write("\n")
            f.write('{}'.format(username4))
            f.write("\n")
            f.write('{}'.format(password4))
            f.write("\n")
            f.write('{}'.format(username5))
            f.write("\n")
            f.write('{}'.format(password5))
            f.write("\n")

def subparsers6():
    pass

complexity = main()
if complexity.forfunc == 'random':
    subparsers2(complexity.gusse_number)
if complexity.forfunc == 'Even_Odd':
    subparsers3(complexity.number1,complexity.number2,complexity.number3,complexity.number4,complexity.number5)
if complexity.forfunc == 'Calculator':
    subparsers4(complexity.number1,complexity.number2,complexity.operation)
if complexity.forfunc == 'Registration':
    subparsers5(complexity.username1,complexity.password1,complexity.username2,complexity.password2,complexity.username3,complexity.password3,complexity.username4,complexity.password4,complexity.username5,complexity.password5)