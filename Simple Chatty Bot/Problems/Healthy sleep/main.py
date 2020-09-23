A = input()
B = input()
H = input()

if int(B) >= int(H) >= int(A):
    print("Normal")
else:
    if int(H) < int(A):
        print("Deficiency")
    else:
        if int(H) > int(B):
            print("Excess")
