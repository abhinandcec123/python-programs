string=input("Enter the string:")
first=string[0]
mod_str=first+string[1:].replace(first,'$')
print("modified string:",mod_str)
