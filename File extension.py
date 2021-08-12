a=input("Input the Filename:")
b=a.split('.')
c=b[-1]
if c=='py':
    print("The extension of file is :'python'")
else:
    print("The extension of the file is :",c)
