import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        w, h, r = input().split()
        w = int(w)
        h = int(h)
        r = int(r)
        if w > r * 2 and h > r * 2:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break