import sys

print("Enter the character for the box")
character = input()

print("Enter box width")
width = int(input())

print("Enter box height")
height = int(input())
      
def boxPrintO(character, width, height):
    print((character + '-'*(width-2)))
    sys.stdout.write((character + ' '*(width-2)*len(character) + character +'\n')*(height-2)+ (character*width) + '\n')

def boxPrintB(character, width, height):
    print(character + '-'*(width-2))                                                                        #top line
    sys.stdout.write(   (character + ' '*(width-2)*len(character) + character +'\n')*((height)//2 -1)       #top hole
           + (character*width + '\n')                                                                       #mid line
           + (character + ' '*(width-2)*len(character) + character +'\n')*((height)//2 + height%2 - 2)      #bottom hole
           + (character + '-'*(width-2)) +'\n')                                                                       #bottom line
                    
boxPrintB(character, width, height)
boxPrintO(character, width, height)
boxPrintO(character, width, height)
boxPrintB(character, width, height)    

    
    
