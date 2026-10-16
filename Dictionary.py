# ----------------------------------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# --------------------------------------------------------
user = {
"name" : "Osama",
"age ":"22",
"country":"egypt",
1:"teat",
"Skills" : ["ccna","mcsa","firewall"],
"rating":10.5
}
print (user)
#  access element 
#  syntax (name dict [key])
print (user ['country'])
print (user.get("country"))
#  print keys 
print (user.keys())
#  print keys
print (user.values())
print ("="*40)
#  2d dict  or nested 
language = {
    "one": {
        "name" : "html",
        "progress":"80%"
    },
    "Two" : {
      "name"  : "css",
      "progress" :"90%"
    }
}
print (language["one"])
print (language["Two"]["progress"])
print (len(language["one"]))
print ("="*40)

FrameWorkOne={
    "name": "reactjs",
    "progress":"80%"
}
FrameWorktwo={
    "name": "ANgular",
    "progress":"90%"
}
# Create Dictionary from varible 
allframeWOrk={
    "one":FrameWorkOne,
    "two":FrameWorktwo
}
print (allframeWOrk.values())
