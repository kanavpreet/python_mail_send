import re
pattern = ['kanav','preet']
x="Find my name kanav"
for k in pattern:
    print (k)
if re.search(k,x):
    print("Found pattern")
else:
    print ("Not found")
