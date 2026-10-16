# clear()
a=[1,2,3,4,5]
a.clear()
print(a)
#  copy ()
b=[1,2,3,4,5]
b.append(7)
c=b.copy()
print (b)
print (c)
#  count (element)
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print (d.count(1))
#  index ()
e =["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Sayed"))   
#  insert(index,object) Add before element 
f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(-1,"pop")
print(f)
#  pop (index_element) get element index ()
g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(3))
