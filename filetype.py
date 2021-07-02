file = str(input("Input the File Name :"))
exe = file.split(".")
if (exe[1]) == "py":
    print("The extension of the file is : python")
elif (exe[1]) == "java":
    print("The extension of the file is : java")
elif (exe[1]) == "cpp":
    print("The extension of the file is : c++")
elif (exe[1]) == "js":
    print("The extension of the file is : javascript")

