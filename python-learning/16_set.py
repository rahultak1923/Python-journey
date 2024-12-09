s= set() # this is a empty set 

print(type(s))

e= {1,5,5,4,6} # do no show the repeted value "element"
print(e)

# union operastion 

s1 = {1,2,5,98}
s2 = {5,6,1,25}

print(s1.union(s2))
print(s1.intersection(s2))