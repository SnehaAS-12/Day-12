#Create a file 30 days 30 hour operations
#Write data in it I have completed 10 days successfully.
#Append the data your name in to it.
#Close the file.

file=open("30 days 30 hour operations.txt","w+")
file.write("I have completed 10 days successfully")
file.close()

file1 =open("30 days 30 hour operations.txt","a+") 
file1.writelines("\nSneha")
file1 =open("30 days 30 hour operations.txt","r") 
print(file1.read())
file1.close()