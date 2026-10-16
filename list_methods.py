# --------------------------------
# -- List Methods --
# --------------------------------
#  append() to add data ("str",bool,int,float,list)
mylist=["Osama","Ahmed","Sayed"]
mylist2= ["c++","python","ccna","mcsa"]
mylist.append("Alaa")
mylist.append(100)
mylist.append(True)
#  ass one element 
mylist.append(mylist2)
#  access second list 
# syntax (mylist[index_list][index_element]) 
print (mylist[6][0])
# extend ()
#  add full list 
#  output -> [1, 2, 3, 4, 'a', 'b', 'c', 'one', 'two']
a=[1,2,3,4]
b=["a","b","c"]
c=["one","two"]
a.extend(b)
a.extend(c)
print(a)
print ("=====================================================")
#  remove ()
#  remove (element ) 
x=[1,2,3,4,5,"osama"]
x.remove("osama")
print (x)
print ("=====================================================")
#  sort ()
y=[1,3,2,4,6,5,0,-1]
#  option reverse by default -> false , reverse -> true 
y.sort()
#  will reverse element sequance  (sort ) only numbers
y.sort(reverse=True)
print(y)
print ("=====================================================") 
# z=[10,1,9,80,100,"Osama",102]
# y.sort(reverse=True)
#  output error not sort only string & only numbers 
#  reverse  not sequance .
print ("=====================================================") 
z=[10,1,9,80,100,"Osama",102]
z.reverse()
print (z)
print ("=====================================================")
v=[1,3,2,4,6,5,0,-1]
v.reverse()
print (v)
print ("=====================================================")
v.sort(reverse=True)
print(v)
print ("=====================================================")