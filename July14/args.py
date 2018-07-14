def function(*args):
    print(type(args))


function(1,2,3,5,6,7,7)

"""sum =0
def function1(*args):   #variable length argument
    for each in args:
        sum += each
"""

#function1(1,2,3,5,6,7,7)


def function3(**kwargs):
    print(type(kwargs))

function3(a=1,b=2,c=4)


def function4(**kwargs):
    sum=0
    for k,v in kwargs.items():
        sum+=v
    print sum

function4(a=1,b=2,c=4)