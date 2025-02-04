''' d1 = 0a 0 :
100, 0 b 0 : 200, 0 c 0 : 300 d2 = 0a 0 : 300, 0 b 0 : 200, 0 d 0 : 400 Sample output: Counter( 0a 0 :
400, 0 b 0 : 400, 0 d 0 : 400, 0 c 0 : 300) '''

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
#print(d1)
result={}
for key,value in d1.items():
    result[key] = value

for key,value in d2.items():
    if key in result:
        result[key]+=value
    else:
        result[key]=value
print(result)