def sign_up():
    personal_data = []
    email = input("e-mail address: ")
    password = input("password: ")
    print("Thanks for signing up! Please confirm your e-mail via clicking the link in your inbox.")
    first_name = input("First Name: ")
    personal_data.append(first_name)
    last_name = input("Last Name: ")
    personal_data.append(last_name)
    birthdate = []
    print("Date of Birth")
    birth_day = input("Day: ")
    birth_month = input("Month: ")
    birth_year = input("Year: ")
    birthdate = (f'{birth_day}''/'f'{birth_month}''/'f'{birth_year}')
    personal_data.append(birthdate)
    address = []
    street = input("Street: ")
    address.append(street)
    house_number = input("House Number: ")
    if type(house_number) != int:
        print("Error")
    #das klappt irgendwie nicht
    address.append(house_number)
    zipcode = input("Zipcode: ")
    if type(zipcode) != int:
        print("Error")
    #das auch nicht
    address.append(zipcode)
    city = input("City: ")
    address.append(city)
    personal_data.append(address)
    return personal_data
    print ("Is everything correct?")
    if input("yes"):
        print ("Thanks!")
    if input("no"):
        print("Let's try again.")

#import pickle

#f = open('personal_data.pickle','wb')
#with open('personal_data.pickle', 'wb') as f:
#    pickle.dump(personal_data)


def log_in():
    email = input("e-mail address: ")
    password = input("password: ")
    print("Logged in successfully!")
