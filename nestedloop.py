#  nested loop 
# people=["osama","ali","ziko","ahmed"]
# skills=['Html','css','js']
# for name in people : # outer loop
#     print (f"{name} skills is :")
#     for skill in skills : # inner loop 
#       print (f"-{skill}")
people ={
    "osama":{
        "ccna":"10%",
        "ccnp":"20%",
        "mcsa":"30%"
    },
    "Ahmed":{
        "html":"110%",
        "css":"40%",
        "js":"50%"
    }
   
}

# ---------------------------------------------------------------------
for name in people:
    print (f"skills & progress {name}")
    for skill in people[name] :
        print(f"is :{skill.upper()} =>{people[name][skill]}")

# print (people["Ahmed"])
# ------------------------------------------------------------
#  print key & value
# print (people["osama"])
#  access 2d list 
# print (people["osama"]["mcsa"])