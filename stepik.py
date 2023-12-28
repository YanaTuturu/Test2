numer = input().split('-')
if ''.join(numer).isdigit():
    if numer[0] == '7':
        del numer[0]
    if len(numer[0]) == 3 and len(numer[1]) == 3 and len(numer[2]) == 4:
        print("YES")
else:
     print("NO")

