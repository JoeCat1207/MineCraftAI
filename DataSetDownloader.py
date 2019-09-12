import minerl
import main

print("Download dataset? y or n")
x = input()
userInput = x.lower()
if userInput == "y" :
    print("What is the install location: ")
    install = raw_input()
    minerl.data.download(install)
else :
    main.main()