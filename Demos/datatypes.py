print("what is your name?")
name = input()
print("what is your age?")
age = int(input())
print(type(age))
print("what is your bank balance?")
balance = float(input())

print("welcome {}. You are set to be {}years old. Your bank balance is {}.".format(name, age, balance))