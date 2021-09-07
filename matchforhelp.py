import datetime

def sign_up():
    email = input("e-mail address: ")
    password = input("password: ")
    print("Thanks for signing up! Please confirm your e-mail via clicking the link in your inbox.")
    create_profile()

def log_in():
    user_email = "melaniegneuer@gmail.com"
    user_password = "password123"
    email = input("e-mail address: ")
    password = input("password: ")
    if user_email == email and user_password == password:
        print("Logged in successfully!")
        create_profile()
    elif user_email == email and user_password != password:
        print("Incorrect password. Please try again.")
    else:
        print("User not found.")
        sign_up()

def create_profile():
    personal_data = []
    first_name = input("First Name: ")
    personal_data.append(first_name)
    last_name = input("Last Name: ")
    personal_data.append(last_name)
    birthdate = []
    print("Date of Birth")
    birth_day = int(input("Day: "))
    birth_month = int(input("Month: "))
    birth_year = int(input("Year: "))
    birthdate = datetime.datetime(birth_year, birth_month, birth_day)
    personal_data.append(birthdate.strftime("%x"))
    address = []
    street = input("Street: ")
    address.append(street)
    house_number = input("House Number: ")
    address.append(house_number)
    zipcode = input("Zipcode: ")
    address.append(zipcode)
    city = input("City: ")
    address.append(city)
    personal_data.append(address)
    print(personal_data)
    profile_varification()

def profile_varification():
    answer = input("Is everything correct? ")
    if answer == "yes":
        print("Thanks!")
    elif answer == "no":
        print("Let's try again.")
        sign_up()
    else:
        print("Please type yes or no.")
