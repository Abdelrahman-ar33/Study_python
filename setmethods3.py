#  set methods 
#  issuperset()
# Are all the elements present?
a= {1,2,3}
b= {1,2}
# هل أنا أحتوي التانية بالكامل؟
print (a.issuperset(b))
#  false 
print ("="*40)
# issubset()
d={1,2,3,4}
n={1,2,3}
f={1,2,3,4}
# هل أنا موجود بالكامل جوه التانية؟
print (d.issubset(n))
print (d.issubset(f))
#  isdisjoint ()
print ("="*40)
g={1,2,3}
h= {1,2,5,7}
i={10,20,40}
#  يعني مفيش حاجات مختلفه مابينهم 
print (g.isdisjoint(i))