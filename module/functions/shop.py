import sys

def buy_item():
    print('Buy item!')

def show_info():
    print('shop module')


if __name__ == '__main__':
    buy_item()
    print(__name__)
    print(sys.argv) 

