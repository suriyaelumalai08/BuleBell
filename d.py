# def task_4(n):
#     rev=0
#     while n>0:
#         i=n%10
#         rev=rev*10+i
#         n=n//10
#     return rev

# def task_3(n):
#     odd=0
#     even=0
#     while n>0:
#         if (n%2)==0:
#             even+=n
#         else:
#             odd+=n
#     return f"odd count: {odd},even count: {even}"

# print(task_3(n=3))

# # print(task_4(345))


# no_std=int(input("enter the number of studen:"))
# data=[[i for i in input().split()] for i in range(no_std)]
# for i  in data:
#     print(i[0],end=',')

        
n=int(input('enter the number:'))
flags=False
while n>0:
    r=0
    r=r*10+n%10
    n//=10
    if r==0:
        flags=True
if flags:
    print('Duck Number')
else:
    print('Not Duck Number')

    



    
