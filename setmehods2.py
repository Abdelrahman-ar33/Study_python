#  set mrthods 
#  diffrence ()
# تحفظ الاختلاف في Set جديدة، وفي نفس الوقت المشترك لا يظهر في الـSet الجديدة
a={1,2,3,4}
b={1,2,"osama","Ahmed"}
print(b.difference(a))
print (b)
#  a - b   syntax 2
print("="*40)
#  diffrance update 
# difference_update() تعمل حاجتين:
# 
# تشيل العناصر المشتركة بين الـ Setين.
# تحتفظ بالعناصر المختلفة في الـSet الأصلية.
d={1,2,3,4}
c={1,2,"osama","Ahmed"}
d.difference_update(c)
print (d)
print ("="*40)
# intersection()   e & f
#  بتشوف الحاجات الي الحاجات  موجوده في الاتنين  
e={1,2,3,"osama","x"}
f={7,"osama","x",2,1}
print (f.intersection(e))
print("="*40)
# intersection_update ()   e & f
g={1,2,3,"osama","x"}
h={7,"osama","x",2,1}
g.intersection_update(h)
# same differance update 
print(g)
print ("="*40)
# Symmetric_diffrance()
#  بتطلع الحاجات الي مش موجوده مابين الاتنين 
#  i ^ j
i={1,2,3,4,5,"x"}
j={"osama","zero",1,2,3,4,"x"}
print (i.symmetric_difference(j))
print ("="*40)
k={1,2,3,4,5,"x"}
l={"osama","zero",1,2,3,4,"x"}
k.symmetric_difference_update(l)
print (k)
#  same_diffrance 
