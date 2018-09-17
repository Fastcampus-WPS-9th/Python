import game
import shop


def turn_on():
    print('= Turn on game =')
    
    while True:
        choice = input(
            'What would you like to do?\n'
            ' 1: Go to Shop\n'
            ' 2: Play Game\n'
            ' 0: Exit\n'
            'Input: '
        )
        if choice == '1':
            shop.buy_item()
        elif choice == '2':
            game.play_game()
        elif choice == '0':
            break
        else:
            print('Choice not exist')
        print('--------------------------')
    print('= Turn off game =')

if __name__ == '__main__':
    turn_on()

