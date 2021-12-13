d1={'a':100,'b':200}
d2={'x':300,'y':400}
print("DICTIONARY 1 :",d1 )
print("DICTIONARY 2 : ",d2)
d=d1.copy()
d.update(d2)
print("DICTIONARY MERGE : ",d)
