# -----------------
#  -- Tuple --
# -----------------
# Tuple With One Element add -> ,
mytuple1=("Osama",)
mytuple2="osama"
print(len(mytuple1))
# Tuple Concatenation
a=(1,2,34)
b=(90,70)
c=a+(True,False,"i")+b
print(len(c))
# Tuple , list ,string repeat (*)
mystring="osama"
print(a*4)
print("================================================")
#  methods 
#  count ()
z=("osama","zero","ahmed","momo","momo")
print(z.count("momo"))
#  index ()
print(f"the position index of str :  {z.index("momo")}{z}")
#  Tuple Destruct 
#  to assign varible 
#  _ to ignore 
s=(1,2,3,0)
n,m,o,_=s 
print(n)
print(m)
print(o)