num1 = int(input("Enter Num1 : "))
num2 = int(input("Enter Num2 : "))

choice = input("""
enter 1 for plus
enter 2 for minus 
enter 3 for multiply
enter 4 for divide
""")

if choice == "1":
    answer = num1 + num2
    print("ANSWER : ", answer)
elif choice == "2":
    answer = num1 - num2
    print("ANSWER : ", answer)
elif choice == "3":
    answer = num1 * num2
    print("ANSWER : ", answer)
elif choice == "4":
    answer = num1 / num2
    print("ANSWER : ", answer)
else:
    print("Something went wrong. try again")