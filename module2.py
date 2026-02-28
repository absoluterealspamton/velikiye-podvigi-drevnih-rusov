import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        c, h, o = input().split()
        c = int(c)//2
        h = int(h)//6
        o = int(o)
        a = min(c, h, o)
        print(a)
    except EOFError:
        break