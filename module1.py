import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        a = int(input())
        if a < 3 and a > 0 or a == 12:
            print("Winter")
        elif a < 6 and a > 2:
            print("Spring")
        elif a < 9 and a > 5:
            print("Summer")
        elif a < 12 and a > 8:
            print("Autumn")
        else:
            print("Error")
    except EOFError:
        break