
from flask import Flask
app = Flask(__name__)

@app.route("/")
def cat_say(x):
    
    print('             {}'.format('-'*len(x)))
    print('             <{}>'.format(x))
    print('             {}'.format('-'*len(x)))
    print('            /')
    print('          /')
    print(' /\_/\  /')
    print('( o.o )')
    print(' > ^ <')
def sum(x,y):
    print(x+y)

def main():
    inp=input('what you want the cat to say')
    cat_say(inp)
if __name__ == '__main__':
    main()

    print("end of cat say 1")
z=100
