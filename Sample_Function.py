print("What is your name?")
name = input()
def hello(name):
    print('Howdy!' + name)
    print('Howdy!!!')
    print('Hello there, ' + name)
hello(name)

print("And who is along with you?")
friend = input()
hello(friend)

print("How does the weather look like outside?")
weather = input().lower()

def commentweather(answer):
    if answer == 'sunny':
        return 1
    if answer == 'rainy':
        return 2

print(commentweather(weather))
