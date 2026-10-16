# email="osama@zero.org"
# print (email[0:email.index("@")])
thename=input ('What\'s your name ?').strip().capitalize()
themails=input ('What\'s your Email ?').capitalize()
theusername=themails[:themails.index("@")]
thewebsite=themails[themails.index("@")+1:]
print (f"Hello {thename}\n Your email is {themails}")
print (f"The web site {thewebsite}")
print (theusername)
 