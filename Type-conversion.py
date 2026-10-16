#  str()
a=10
print (type(a))
print (type(str(a)))
print ("="*40)
#  tuple()
#  element iteration 
#  must iterable 
c="Osama"
d=[1,2,3,4,5]
e={"A","b","c"}
f={"a":1,"B":2}
print (tuple(d))
print (tuple(c))
print (tuple(e))
print (tuple(f))
print ("="*40)
#list ()
g="Osama"
h=[1,2,3,4,5]
n={"A","b","c"}
o={"a":1,"B":2}
print (list(g))
print (list(h))
print (list(n))
print (list(o))
print ("="*40)
#set()
x="Osama"
y=[1,2,3,4,5]
z={"A","b","c"}
w={"a":1,"B":2}
print (set(x))
print (set(y))
print (set(z))
print (set(w))
print ("="*40)
#  dict ()
#  key,value 
aa=[("A",1),("b",2),("c",3),("d",4)]   # list 
bb=(("A",3),("b",4),("c",5))  # tuple 
print (dict(aa))
print (dict(bb))