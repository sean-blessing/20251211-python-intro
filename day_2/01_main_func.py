#import my_console
#from my_console import prompt_string
import my_console as mc

def main():
    print('Hello')
    print(f'main() function __name__=', __name__)
    # call another module (that we create) - my-console.py

    # get username from user
    username = mc.prompt_string('Username? ')
    print(f'username = {username}')

    print('Bye')

if __name__ == '__main__':
    main()
