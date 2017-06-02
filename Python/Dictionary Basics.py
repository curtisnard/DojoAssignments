Me = {}
Me["name"] = "Curtis"
Me["age"] = "25"
Me["Country of Birth"] = "Germany"
Me["Favorite Language"] = "Python"

You={}
You["name"]="Yolanda"
You["age"]="25"
You["Country of Birth"]="USA"
You["Favorite Language"]="None"


def Dictionary(x):
    for key,data in x.iteritems():
            print "My",key,"is",data
Dictionary(Me)
