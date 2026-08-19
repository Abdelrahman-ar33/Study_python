a="i love python"
# print lenght string 
print(len(a))
print ("=============================================\n")
b="       i love python         "
# strip () == rstrip () == lstrip () remove --> space 
#  a. strip ()
# this function accept parameter # or symbol
print (b.strip())
print (b.rstrip())
print (b.lstrip())
print ("=====================strip========================\n")
c="######################i love python######################"
print (c.strip('#'))
print (c.rstrip('#'))
print (c.lstrip('#'))
print 
print ("===================function title==========================\n")
# d.tile ()
# convert frist letter in sentence  capital &  after nubmer exsample -> 3d-> 3D
d="i love 2d graphics and 5g technology and python 9k 88hh"
print(d.title())

print ("===================capitalize==========================\n")
# convert frist letter capital 
e="hello my major bis"
print (e.capitalize())
print ("=======================zero fill ===========================")
#zfill exsample 001 ,002,009,010
# afill()->parameter width 
f,g,i="1","11","111"
print(f.zfill(4))
print(g.zfill(4))
print(i.zfill(4))
# upper 
print ("=======================upper===========================")
h="osama"
print(h.upper())
# 13 video