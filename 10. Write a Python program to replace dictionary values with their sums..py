d1={'a':[100,250,300,450]}
d2={'j':[500,500]}
for key in d1:
    d1[key]=sum(d1[key])
print(d1)
for key in d2:
    d2[key]=sum(d2[key])
print(d2)