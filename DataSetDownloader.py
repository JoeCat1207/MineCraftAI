import minerl
import main

print("Download dataset? y or n")
x = input()
userInput = x.lower()
if userInput == "y" :
    print("What is the install location: ")
    install = input()
    minerl.data.download(directory=install)
else :
    main.main()