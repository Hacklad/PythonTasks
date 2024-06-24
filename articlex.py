# write a program that will tell a user to write an article. The program will have the ffg functionalities: 
# Ask user if he/she wants to replace a word from the article
# Ask the user to supply the word to be replcaed and the word to be replaced with
# Append the changes to the article

print("~Welcome to Bloggerz~")
blog = input("Type your Article here: ")
print(f" Your Article: {blog}")
prompt = input("Press '1' to replace any word, any other key to cancel: ")
if prompt == '1':
    replaced = input("Enter a word you want to replace: ")
    if replaced in blog: 
        replacer = input("Enter the replaced word here: ")
        edited = blog.replace(replaced, replacer)
        print(f"Changes succesfully made: {edited}")
    else: 
        print(f"Sorry we can't find {replaced}")
else:
    print('Article Received')