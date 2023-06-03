import datetime # Imports the datetime module
import os # Imports the os module

# Dynamically obtain the date and time of the local computer where the script is running
now = datetime.datetime.now() 
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Clear interface command line for neater appearance
clear = lambda: os.system('cls')  
clear() 

# The available services are being stored in services {} dictionary
services = {
    1: {'name': 'Firewall Service', 'price': 1.2},
    2: {'name': 'Security Ops Centre', 'price': 4.2},
    3: {'name': 'Hot Site', 'price': 8.5},
    4: {'name': 'Data Protection', 'price': 10.0}
}

# Subscriptions {} dictionary is being externally defined which will be used later on
subscriptions = {}

# This function prompts the user to input their name which will then be greeted accordingly once the main menu of the application shows up
def getUserDetails():
    print("[*] ELECTRONIC SERVICES & PROTECTION [*]\n")
    name = input("Please enter your name: ")
    print("")
    return name

# This is the main function of the ELECTRONIC SERVICES & PROTECTION application
def main():
    user_name = getUserDetails() 
    user_input = '0' 
    subscribed_services = [] 

    # Since user_input has been defined as '0' and while loop condition is != '7', the main menu will be printed everytime
    while user_input != '7':
        print("=" * 53)
        print("[**] WELCOME TO ELECTRONIC SERVICES & PROTECTION [**]")
        print("=" * 53)
        print(formatted_time) # Printing the date and time which was stored in the formatted_time variable
        print(f"\nHello, {user_name}! You are currently viewing the main menu.\n") 
        print("1. Display our list of services")
        print("2. Search for a service")
        print("3. Display added services")
        print("4. Add service(s)")
        print("5. Remove service(s)")
        print("6. Payment")
        print("7. Exit Electronic Services & Protection\n")

        # user_input variable will now be updated to whichever option the user selects
        user_input = input("Please input your choice of action or select 7 to exit: ") 

        if user_input == '1':
            displayServices() 
        elif user_input == '2':
            searchService(services) 
        elif user_input == '3':
            displaySubscribedServices(subscribed_services, subscriptions)
        elif user_input == '4':
            subscribeService(services, subscribed_services, subscriptions) 
        elif user_input == '5':
            removeService(subscribed_services) 
        elif user_input == '6':
            calculatePayment(subscribed_services, services) 
        elif user_input == '7':
            print("\nThank you for using Electronic Services & Protection. It has been a pleasure serving you!\n") 
        else:
            print("\n[INVALID CHOICE. PLEASE ENTER A VALID OPTION!]\n") 

# This function dislpays the available services of the application. The details are manually listed in order to present uniformity
def displayServices():
    print("\nThank you for selecting this option. Yes, we have the following service(s): ")
    print("1. Firewall Service     :        $1.2k/year")
    print("2. Security Ops Centre  :        $4.2k/year")
    print("3. Hot Site             :        $8.5k/year")
    print("4. Data Protection      :        $10.0k/year")

# This function allows the user to search for services available within the application using keyword search. It is coded in away that keyword case sensitivity does not apply
def searchService(services):
    keyword = input("Enter the keyword to search for a service: \n") 
    found = False 
    for service_id, service_details in services.items(): # Using for loops to call the service_id and service_details variables in the services dictionary items
        if keyword.lower() in service_details['name'].lower(): 
            print(f"Service ID: {service_id}\tService Name: {service_details['name']} : ${service_details['price']}k/year\t")
            found = True # Updates the boolean expression to true

    if not found:
        print("\n[NO SERVICE FOUND MATCHING THE KEYWORD!]\n") 

# This function displays the subscribed services of the user
def displaySubscribedServices(subscribed_services, subscriptions): 
    if len(subscribed_services) == 0: # The script will check the subscribed_services[] array if there are stored input, if there is none, the script will notify the user they have not subscribed to any services yet
        print("\n[YOU HAVE NOT SUBSCRIBE TO ANY SERVICES YET!]\n") 
    else:
        print("\nYour subscribed services:") 
        for index, service_id in enumerate(subscribed_services): 
            service_details = services[service_id] 
            expiry_date = subscriptions[service_id] 
            print(f"{index + 1}. Service ID: {service_id}\tService Name: {service_details['name']} : ${service_details['price']}k/year\tExpiry Date: {expiry_date}") 

# This function prompts the user to select from the available services they would like to subscribe
def subscribeService(services, subscribed_services, subscriptions):
    displayServices() 
    while True: # Using while loop, the script runs without any conditions until the break is executed in the loop
        service_id = input("Enter the service 1-4 that you would like to add, 0 to stop: ") 
        if service_id == '0': # If the selected option is '0', the argument states to break the loop
            break
        try:
            service_id = int(service_id) 
            if service_id not in services:
                raise ValueError("Please enter a valid service ID.") 
            subscribed_services.append(service_id) 
            expiry_date = calculateExpiryDate() 
            subscriptions[service_id] = expiry_date
            print(f"[Service option {service_id}] subscribed successfully! Expiry Date: {expiry_date}\n") # The subscribed service(s) is presented to the user which includes its expiry date (1year)
        except ValueError:
            print("[Invalid choice! Please enter 1-4 or 0 to stop.]\n") 

# This function allows the user to remove any services they have added into their cart
def removeService(subscribed_services):
    if len(subscribed_services) == 0: # The script will check the subscribed_services[] array if there are stored input, if there is none, the script will notify the user they have not subscribed to any services yet
        print("\n[YOU HAVE NOT SUBSCRIBE TO ANY SERVICES YET!]\n") 
        return

    print("Your subscribed services:") 
    for index, service_id in enumerate(subscribed_services):
        service_details = services[service_id]
        print(f"{index + 1}. Service ID: {service_id}\tService Name: {service_details['name']}") 

    while True: # Using while loop, the script runs without any conditions until the break is executed in the loop
        service_index = input("Enter the index number of the service you want to remove, 0 to cancel: ") 
        if service_index == '0': # If the selected option is '0', the argument states to break the loop
            break 
        try: 
            service_index = int(service_index) 
            if service_index < 1 or service_index > len(subscribed_services):
                raise ValueError("INVALID INDEX. PLEASE ENTER A VALID INDEX NUMBER!\n") 

            removed_service_id = subscribed_services.pop(service_index - 1) # Using .pop(), it allows to returns the item present in the given index from subscribed_services and subtracts from service_index as per the defined condition
            removed_service_name = services[removed_service_id]['name']
            del subscriptions[removed_service_id]
            print(f"Service '{removed_service_name}' (ID: {removed_service_id}) removed successfully!\n") 
            break # Breaks the while loop
        except ValueError:
            print("[INVALID CHOICE! PLEASE ENTER A VALID INDEX NUMBER!\n") 

# This function tabulates the total amount of the services subscribed
def calculatePayment(subscribed_services, services):
    if len(subscribed_services) == 0:  # The script will check the subscribed_services[] array if there are stored input, if there is none, the script will notify the user they have not subscribed to any services yet
        print("\n[YOU HAVE NOT SUBSCRIBE TO ANY SERVICES YET!]\n") 
    else:
        total_price = 0 
        for service_id in subscribed_services: # Using for loops, it obtains the service_id from the subscribed_services[] array
            service_details = services[service_id] 
            total_price += service_details['price'] 
        if len(subscribed_services) == len(services):
            discount = 0.1  # Gives 10% discount if user selects all services (1-4 only). Any additional service will not trigger the discounted price
            discounted_price = total_price * (1 - discount)
            discounted_price = round(discounted_price, 2)  # Round the results to 2 decimal places
            print(f"\nTotal payment amount: ${discounted_price:.2f}k/year") 
            print("\nCongratulations! You have selected all subscriptions and received a 10% discount.")
        else:
            total_price = round(total_price, 2)  # Round to 2 decimal places
            print(f"\nTotal payment amount: ${total_price:.2f}k/year\n")

# This function calculates the expiry date of the subscribed services
def calculateExpiryDate():
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    expiry_date = current_date + datetime.timedelta(days=365)
    return expiry_date

# Calling out the main function in order for the application to run
main()

#################### Credits and References ####################

# https://www.w3schools.com/python/default.asp
# https://www.tutorialsteacher.com/python/os-module
# https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
# https://www.programiz.com/python-programming/if-elif-else
# https://datagy.io/python-enumerate/
# https://stackoverflow.com/questions/7118276/how-to-remove-specific-element-from-an-array-using-python
# https://code2care.org/q/calculate-discount-amount-python-code
# https://www.sitepoint.com/community/t/calculating-a-20-discount/203412
# https://www.freecodecamp.org/news/how-to-round-to-2-decimal-places-in-python/
# https://pythonguides.com/python-print-2-decimal-places/#:~:text=In%20Python%2C%20to%20print%202,float%20with%202%20decimal%20places.
# https://stackoverflow.com/questions/31885821/code-to-check-for-expiration-date-from-one-python-scripts-output