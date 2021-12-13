import operator
d={1:2,3:4,4:3,2:1,3:1}
print("ORIGINAL DICTIONARY",d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print("DICTIONARY IN ASCENDING ORDER : ",sorted_d)
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print('DICTIONARY IN DESCENDING ORDER : ',sorted_d)
