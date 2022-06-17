# import sys
# print(sys.version)
# print(sys.stdin)
#
#
# import os
#
#
# def current_directory():
#     cwd = os.getcwd()
#     print(cwd)
while True:
    try:
        x = int(input("Please Enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")


