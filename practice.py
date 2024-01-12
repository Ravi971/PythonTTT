# a = bin(15)
# print(a)
#
# print(bin(0o123))
#
# print(bin(0xfab))

def sum_of_digits(n):
 sum = 0
while n> 0:
digit = n % 10
sum += digit
n = n // 10
return sum

n = int(input("Enter a sum of  number: "))
print(sum_of_digits(sum))


