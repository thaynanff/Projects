from random import randint


def dice_face(dice): # function that prints out the dice face
    switch = {
        1: '[       ]\n|   *   |\n[       ]\n',
        2: '[*      ]\n|       |\n[      *]\n',
        3: '[*      ]\n|   *   |\n[      *]\n',
        4: '[*     *]\n|       |\n[*     *]\n',
        5: '[*     *]\n|   *   |\n[*     *]\n',
        6: '[ *   * ]\n| *   * |\n[ *   * ]\n'
    }
    return switch.get(dice)


while True:
    dice = randint(1, 6) # generates a ramdom number bettween 1 and 6
    print(dice_face(dice)) # it calls the function  
    ans = str(input('Would you like to roll the dice again? (Y/N): ').upper()).split()[0]
    while ans not in 'YN':
        ans = str(input('Invalid answer! Would you like to roll the dice again? (Y/N): ').upper()).split()[0]
    if ans == 'N': # it terminates the loop if the user types 'N'
        break
