def emailslicer():
    print("Welcome to the email slicer")
    email=input("Enter your email adress: ")
    (username,domain)=email.split("@")
    (domain,extension)=domain.split(".")
    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
    