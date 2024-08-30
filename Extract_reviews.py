from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

path = "/Users/Wany/Downloads/chromedriver-mac-x64/chromedriver"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

#defining the fonction to scrap the reviews
def scrap_reviews(link, csvname, nbr_page):
    #set the page number on 1
    pageNumber = 1
    # open the the website
    driver.get(link)
    driver.maximize_window()
    time.sleep(5)
    #creating a loop to scrap the amount of page decided
    while(pageNumber < nbr_page):
        print("Scraping page number : ", pageNumber)

        #find the main element of the page and loop through it to find the dates of the reviews
        reviewsCard = driver.find_elements(By.XPATH, "//*[contains(@class, 'styles_reviewContent__0Q2Tg')]")
        dates = []
        for card in reviewsCard:
            cardChilds = card.find_elements(By.XPATH, ("./child::*"))
            for child in cardChilds:
                if child.text[:4] == "Date":
                    dates.append(child.text[20:])

        # finding all the reviews of the page
        reviews_list = driver.find_elements(By.XPATH, "//*[contains(@class, 'typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn')]")
        #finding all the location of the reviews in the page
        place_list = driver.find_elements(By.XPATH, "//*[contains(@class, 'typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_detailsIcon__Fo_ua')]")
        
        # adding all the reviews in a list
        reviews = [i.text for i in reviews_list]
        # adding all the location to a list
        places = [i.text for i in place_list]
        print(reviews)
        print(dates)
        print(places)

        #write all the elements collected on the page in a csv file
        with open(f"{csvname}.csv", "a", newline= "", encoding="utf8") as csv_file:
            fieldnames = ["Reviews", "Date", "Place"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            for i in range(0, len(reviews_list)):
                writer.writerow({"Reviews" : reviews[i],
                                "Date" : dates[i],
                                "Place" : places[i]})
        csv_file.close()

        #navigate to the next page
        pageNumber += 1
        driver.get(f"https://www.trustpilot.com/review/hostinger.com?page={pageNumber}&stars=1&stars=2")
        time.sleep(3)
    driver.quit()

scrap_reviews("https://www.trustpilot.com/review/hostinger.com?stars=1&stars=2", "Hostinger2", 30)
scrap_reviews("https://www.trustpilot.com/review/www.bluehost.com?stars=1&stars=2", "Bluehost2", 30)
