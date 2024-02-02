str = "Python"
str2 = "Restrart"

#concatenation
final_str= str+" "+str2
print(final_str)

#lenght of string
len(final_str)

#Indexing access 
print(str[2])  

#Slicing 
print(str[1:4],str[:4])
print(str[:len(str)], str[::])

# Negative Index - Last Index is -1 , -2 , ... Slicing
print(str[0:-3])
print(str[:3])

# String functions
str1 = "welcome all and happy coding all"

print(str1.endswith("ll")) # Returns True or false 
print(str1.capitalize())   # Temporary changes
print(str1.replace('all','team')) # Replace all occurance
print(str1.find("happy"))  #Returns 1st Index at 1st occurance . Else if not exit returns -- -1 (Invalid Index)
print(str1.count("w"))   # Counts char or word

# 1. WAP to input user's first name and print its lenght

word = input("Enter the word or sentence")
print(word,len(word))

# 2. WAP to find occurance of "$" in a string
name = "$komal $kka $jk $jjan"
print(name.count("$"))
