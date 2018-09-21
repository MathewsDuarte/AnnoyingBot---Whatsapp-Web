from selenium import webdriver
import sys

driver = webdriver.Chrome(executable_path="YOUR PATH/DIR/chromedriver")
driver.get("https://web.whatsapp.com/")

while True:
    print ("Welcome to Annoying Bot, take a sit, please.")
    print ("--------------------------------------------")
    print("# \n # \n # \n # MADE TO ANNOYING YOU # \n # \n # \n # \n")

    userName = input("What's the group or username? : \n")
    messageText = input("\n Type your message for annoy someone : \n")
    count = int(input("Enter the number of times you will repeat the message : \n"))

    print ("Scan with your phone the QR Code.")
    print ("Type any shit to proceed.")
    print ("Loading...")

    user = driver.find_element_by_xpath('//span[@title ="{}"]'.format(userName))
    user.click()

    msg_box = driver.find_element_by_class_name('_1Plpp')

    for i in range(count):
        msg_box.send_keys(messageText)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()


    option = input("Will continue? \n")

    if (option == '0'):
        sys.exit(0)
    if (option == '1'):
        continue
