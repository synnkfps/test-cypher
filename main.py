dict = {'a':1,'b':2,'c':3, 'd':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def obfuscate(user=str):
    key = ''
    for i in user.lower():
        key += f'{dict[i]*len(user)}-'
    else:
        key = ''.join(list(key)[:-1])
        return key

def main():
    user = input('Enter your user: ')
    key = input(f'Enter the key for "{user}": ')
    if key != obfuscate(user):
        print('Wrong key!')
    else:
        print('Right key!')

main()
