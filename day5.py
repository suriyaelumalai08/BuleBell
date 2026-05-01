# a=int(input('enter a value:'))
# b=int(input('enter b value:'))
# c=int(input('enter c value:'))

# # print(f'For +b method: {-b+((b**2)-(4*a*c))**0.5/2*a}')
# # print(f'For -b method: {-b-((b**2)-(4*a*c))**0.5/2*a}')


# print(int(a<b)<c and int(b>a)<c and int(a>c)<b and int(c<a)<b and int(b>c)<a and int(c<b)<a)


# print(a>b and a>c and a or b>c and b or c)


n=int(input('enter the number:'))
flags=True
while n>0:
    r=n%10
    n//=10
    if r==0:
        flags=False
        break

if flags:
    print('non-duck number')
else:
    print('duck number')  
