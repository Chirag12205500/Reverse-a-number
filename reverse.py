a = int(input( ))
reverse = 0
#use while loop
while a != 0:
    digit = a%10
    reverse = reverse*10+digit
    a//=10
print(str(reverse))
