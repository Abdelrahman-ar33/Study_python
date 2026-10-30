mydict ={
"Html":"80%",
"css":"90%",
"JS":"70%"
}
# for skill in mydict:
#     print (skill)

#  loop key value
# for skill_key,skill_progress in mydict.items():
#     print (f"{skill_key}->{skill_progress}")
# -----------------------------------------------------------------------
mydict2={
    #  main key 
"Html":{
    #  main value 
    "mainjs":"80%",
    "Pugjs":"80%"
},
"css":{
    "mainjs":"90%",
    "sass":"7%"
}
}

# for mkey,mvalue in mydict2.items():
#     print (f"{mkey} progress is :")
#     for childkey,chilv in mvalue.items():
#         print (f"-{childkey} -> {chilv}")
for mkey,mvlue in mydict2.items():
    print (f"{mkey} progress is: ")
    for childkey,childv in mvlue.items():
        print (f"{childkey} -> {childv}")
# ===================================================================================
# myskills={
#     "Abdo":{
#         "ccna":"90%",
#         "mcsa":"40%",
#         "firewall":"0%"
#     },
#     "osama":{
#         "Html":"80%",
#         "css":"60%",
#         "js":"40%"
#     }
# }
# for main_key in myskills :
#     print (f"{main_key} progress is :")
#     for main_vlaue in myskills[main_key]:
#         print (f"{main_vlaue}->{myskills[main_key][main_vlaue]}")
#  revesion علي كل ما سبق 