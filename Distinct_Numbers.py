s = int (input ( ))
numbers = input()
numbers = list(map(int, numbers.split()))
# print(numbers)
a = set(numbers)
unique_values = len(a)
print(unique_values)

# def distinct(arr,num):
#     arr1=[]
#     for i in range(0,num):
#         d=0
#         for j in range(0,i):
#             if (arr[i] == arr[j]):
#                 d=1
#                 break
#         if (d==0):
#             arr1.append(arr[i])
#     print(len(arr1))
#
# a = int(input())
# numbers = input()
# numbers = list(map(int, numbers.split()))
# distinct(numbers,a)