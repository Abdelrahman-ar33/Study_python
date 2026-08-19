#  function index (substring ,start ,end)
a="i love python"
# print (a.index('i',2,7)) #" error " , if this can't find letter -> error 
print (a.index('z')) #" error "
print ("=============== find ==================")
#  function find  (substring ,start ,end)
# if dont find letter  return -1 
print (a.find('o',7,13)) 
print ("===============  rjust(), ljust()  ===============")
#  same function ()-> center ()
#  by default space 
b="Osama"
print (b.rjust(10,"l"))
print ("=============== splitline ()  ===============")
#  return string list  """""";

e="""Frist line 
second line 
Third line 
"""
print (e.splitlines())
d= "frist line\n second line\n thirdline"
print (d.splitlines())
print ("=============== expandtabs()  ===============")
#  can you control tabs 
# Must add tabs 
g="Hello\tworld\tilove\tpython"
print (g.expandtabs(10))
print ("=============== istitle()  ===============")

k="I Love Python & Ccna 3D"
print(k.istitle()) 
print ("=============== isspace ()  ===============")
# return boolean value 
l="   "
print(l.isspace())
print ("=============== islower ()  ===============")
#  return boolean value 
mo="I pove python & ccna 3d"
print(mo.islower()) 
print ("=============== isindentifier ()  ===============")
#  is allow write varible
# #  return boolean value  
x="osama_elzero"
jj="osama-elzero"
nn="osama/elzero"
vv="osama/elzero"
print (x.isidentifier())
print (jj.isidentifier())
print (vv.isidentifier())
print (nn.isidentifier())
print ("=============== isalpha ()  ===============")
# if find space return false 
#  is alphapetic 
uo="Alisistany"
print (uo.isalpha())
print ("=============== isalnum ()  ===============")
#  letters & num 
uoo="io66"
print (uoo.isalnum())
print ("======================== methods string (replace ) ======================")
#  replace (old vlaue ,new vlaue ,count)
rep="Hello,one,two,one,two"
print(rep.replace("one","1",2))
print(rep.replace("two","2",2)) # Hello,one,2 ,one,2
print ("=============== join () ====================")
# join 
# insert any  symbol in list 
#  syntax print ("-".join(namelist))
mylist =["osama","mohamed","elsayed"]
print("_".join(mylist))
print (type("_".join(mylist)))
# done methods string .