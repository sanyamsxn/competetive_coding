n=int(input())


def rish_fn(n):
    if ( n%2==0):
        if (n>=2 and n<=5):
            print('Not Weird')
        elif (n>=6 and n<=20):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")

def rish_fn2(n):
    flag=0

    if ( n%2==0):
        if ((n>=2 and n<=5) or (n>=20)):
            flag=1

            
    if flag==0:
        print('Weird')
    else:
        print("not Weird")

rish_fn2(n)
