
def pos_neg():
    num = int(input("enter the number between (-number to + number)"))
    if num >0:
        print('Possitive')
    else:
        print('Negative')

# pos_neg()


def find_big_num():
    num1 = int(input('enter the first number:'))
    num2 = int(input('enter the second number:'))

    if num1>num2:
        print(num1)
    else:
        print(num2)

# find_big_num()

def find_big_3num():
    num1 = int(input('enter the first number:'))
    num2 = int(input('enter the second number:'))
    num3 = int(input('enter the therid number:'))

    if num1>num2 and num1>num3:
        print(num1)
    elif num2>num1 and num2> num3:
        print(num2)
    else:
        print(num3)

def find_num():
    # num1 = int(input('enter the first number:'))
    # num2 = int(input('enter the second number:'))
    # num3 = int(input('enter the therid number:'))

    # if num1 == num2 == num3:
    #     print('equal')

    # elif num1!=num2 and num2!=num3 and num1!=num3:
    #     print('differents')
    # else:
    #     print('partial equal')

    a,b,c = map(int,input().split())
    print('equal' if a==b==c else 
          "different" if len({a,b,c})==3 else 
          'partial equal')

# find_num()


def find_grade():
    score = int(input())
    print('grade A+' if 91 < score < 100 else 
          'grade A ' if 76 < score < 90 else
          'grade B ' if 51 < score < 75 else
          'grade C ' if 35 < score < 50 else
          'grade D ' if 1 < score < 34 else
          'invalid number')
    



    