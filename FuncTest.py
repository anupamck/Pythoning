n = 0
while n < 5:
    for a in range (0,100):
        print("Hello fellow")
        print("Exit loop?")
        value = input().lower()
        if value == 'y':
            break
    print("Do I get printed or not?")
    n+=1

print("What about me?")
