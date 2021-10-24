from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


"""
Welcome To FindMeADoctor, this bot scrapes google(using selenium) and prepares a convenient list
of doctors around you
"""

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

def dictionary_input(): #function to validate the input for dictionary key input
    while(True):
        inp = input("My Choice is: ")
        if inp.isdigit() and int(inp)>=0 and int(inp)<10:
            return inp
        else:
            print("Please Choose an Option From 0-9, and Hit Enter")
        
def token_input():
    while(True):
        tokens=input("My Keyword/s is/are: ")
        if tokens.isascii():
            return tokens
        else:
            print("Please Enter A Valid Input");


print("What Kind of Doctor Are you Looking for?\nChoose From The List Below!\n")
docdict = {0:"NeuroSurgeon",1:"Dentist",2:"Orthopaedic",3:"Physician",4:"Cardiologist",5:"",7:"",8:"",9:"Something Else"}
intake = dictionary_input()
if int(intake)==9:
    print("You chose Others")
    print("Enter Keywords Separated By Commas (,)");
    intake = (token_input()+' near me').replace(',','%2C').replace(' ','+')
    driver.get('https://www.google.com/search?q='+intake)
    driver.find_element(By.CLASS_NAME,"wUrVib").click()
    items = driver.find_elements_by_xpath("//*[contains(@id, 'tsuid')]")
    for item in items:
        print(item.text)
        print("\n")
    
print(intake)



