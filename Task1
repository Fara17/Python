import random
def per(a):
    b = []
    while(len(b) != len(a)*(len(a)-1)):
        while(True):
            s = ''
            for i in range(len(a)):
                d = a[random.randint(0,len(a)-1)]
                while(d in s):
                    d = a[random.randint(0,len(a)-1)]
                s = s + d
            if(s not in b):
                break;
        b.append(s)
    return b
print(per(['a','b','c','d']))
