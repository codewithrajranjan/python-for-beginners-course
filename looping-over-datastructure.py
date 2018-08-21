#############################################
# Looping on a list
#############################################
print("Looping over list")

programmingLanguages = ["nodejs","python","php","c","java"]


for eachData in programmingLanguages:
    print("Do you want to learn : {}".format(eachData))



#####################################################
# Looping over tuples
####################################################
print("Looping over tuples")

programmingLanguages = ("nodejs","python","php","c","java")

for eachData in programmingLanguages:
    print("Do you want to learn : {}".format(eachData))



####################################################
# Looping over dictionary
###################################################
print("Looping over dictionary")

programmingLanguages = {
            
        "nodejs" : "I am used at netflix",
        "python": "I am used at Quora",
        "php": "I am used at facebook",
        "c": "I am used every where",
        "java": "I am used in Amazon"
    }


for key in programmingLanguages:
    print("Lanuage : {} Description : {} ".format(key,programmingLanguages[key]))







