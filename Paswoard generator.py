import random
lower="abcdegghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
charecters="<>!@$%^&*+"
string=lower+upper+number+charecters
length=9
pasword="".join(random.sample(string,length))
print("Your password is: ",pasword)
