print("Welcome to the email slicer \n")

def main():
    while True:
        email_input = input("Input your email address: ")
        if email_input == 'end':
            print("GoodBye")
            break

        (username, domain) = email_input.split("@")  # ჭრის @-მდე მონაცემს
        (domain, extension) = domain.split(".")  # ჭრის .-მდე მონაცემს

        print("Username: ", username)
        print("Domain: ", domain)
        print("Extension: ", extension)
        #print("\n")
main()






