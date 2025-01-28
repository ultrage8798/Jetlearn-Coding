array=list(map(int,input("Enter the Numbers: ").split()))
key=int(input())
for number in array:
    if number==key:
        print("Key Exists")
    else:
        print("Key Does not Exist")

