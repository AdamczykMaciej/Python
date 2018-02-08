def string_length(mystring):
    # try:
    #     return len(mystring)
    # except:
    #     return("Sorry integers don't have length.")
    if type(mystring) == int:
        return "Sorry integers don't have length."
    elif type(mystring) == float:
        return "Sorry floats don't have length"
    else:
        return len(mystring)
print(string_length(10.0))

emails = ["madadamczyk22@gmail.com", "adamczyk.maciej01@gmail.com", "maciejadamczyk.official@gmail.com", "maciejadamczyk7@wp.pl", "madadamczyk@gmail.com", "s15170@pjwstk.edu.pl"]

for email in emails:
    if 'gmail' in email:
        print(email)

mylist = [1,2,3,4,5]
print(mylist[0:-1])

for item in mylist:
    if item > 2:
        print(item)

password = ''
while password != 'python123':
    password = input("Type Your password:")
    if(password == 'python123'):
        print("You are logged in!")
    else:
        print("Sorry, please try again.")

name=['maciek','pablo','kris']
email_domain=['yahoo', 'gmail', 'hotmail']

for i,j in zip(name, email_domain):
    print(i,j)
a="ma"
print(a[0])
