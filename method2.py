#####################################################
########             Methods2   string          #######
#####################################################
#  split () rsplit 
a="i-love-python-&-php "
print (a.split('-'))
b="i love python & php "
print (b.split())
# convert strig list ['i', 'love', 'python', '&', 'php'] must be space 
# can control  number split 
c="i-love-python-&-php "
print (a.split('-',2))
# split 2 element 
print('============rsplit===============')
d="i-love-ccna-mcsa-ceh-it"
print (d.rsplit('-',3))

print('============center===============')
# center () number letter
e="Osama"
# must add 1 argument .
print(e.center(15,"#")) # if you dont add character add by default space
print('============count===============')
# count text exsample "abdo" 
# letter case sensetive 
f="i love ccna because ccna is easy"
print(f.count('ccna'))
# star end print(f.count('ccna',star,end))
print(f.count('ccna',0,))
print('============ swap case ===============')
# (text) -> (capital letter) -> "small" ; (letter)-> , small -> "capital" 
g="i LoVe pyThoN"
print (g.swapcase())
print('============ star with  ===============')
# s=
h="i love python"
print (h.startswith('i'))
# start , end 
print (h.startswith('p',7,10))
print('============ end  with  ===============')
n="i love python"
print (n.endswith('n'))
# start , end 
print (n.endswith('e',2,6)) 
# letter case sensetive 
print('============ this function return bool vlaue   ===============')