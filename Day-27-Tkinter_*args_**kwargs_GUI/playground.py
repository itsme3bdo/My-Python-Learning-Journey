def add(*args):
    ans=0
    for n in args:
        ans+=n
    return ans
add(1,2,3,4,5)

def calculate(**kwargs):
    print(kwargs)

calculate(add=3,multiply=5)