woods = '*'*10+'\n'+'*'*10 + '\n     :(\n' + '*'*10+'\n'+'*'*10
print(woods)
n = input("You're in the lost woods! Will you go left, or right? ")
while n == "right":
    print(woods)
    n = input("You're in the lost woods! Will you go left, or right? ")
print("You left the lost woods!")