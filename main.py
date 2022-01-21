import time
import requests
from config import API_KEY
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

wait = WebDriverWait(driver, 10)

def find_gender_breakdown(url):
    driver.get(url)
    next_class = '.js-prev-next-paging-next.btn.prev-next-paging__button.prev-next-paging__button-right'
    next_button = driver.find_element(By.CSS_SELECTOR, next_class)

    review_class = '.row.review_table_row'
    name_class = '.critic_name'
    review_icon_class = '.review_icon'


    reviews = {}

    female_count = 0
    female_rotten = 0
    female_fresh = 0

    male_count = 0
    male_rotten = 0
    male_fresh = 0

    unknown_count = 0
    unknown_rotten = 0
    unknown_fresh = 0

    total_count = 0
    total_rotten = 0
    total_fresh = 0

    while(next_button):
        time.sleep(3)
        reviews_on_page = driver.find_elements(By.CSS_SELECTOR, review_class)
    
        for review in reviews_on_page:
            name_element = review.find_element(By.CSS_SELECTOR, name_class)
            name_link = name_element.find_element(By.TAG_NAME, 'a')
            name = name_link.get_attribute('innerHTML')

            review_icon_element = review.find_element(By.CSS_SELECTOR, review_icon_class)
            review_icon_all_classes = review_icon_element.get_attribute("class")
            tomatometer = ''

            if 'rotten' in review_icon_all_classes:
                tomatometer = 'rotten'
            else:
                tomatometer = 'fresh'

            reviews[name] = {
                'tomatometer': tomatometer
            }

        for name in reviews:
            name_list = name.split(' ')
            first_name = name_list[0]
            response = requests.get('https://api.genderize.io?name={}&apikey={}'.format(first_name,API_KEY))
            json = response.json()
            print(json)
            reviews[name]['gender'] = json['gender']

        try:
            next_button.click()
        except: 
            print('End reached')
            next_button = False

    for name in reviews:
        gender = reviews[name]['gender']
        tomatometer = reviews[name]['tomatometer']

        total_count += 1

        if gender == 'female':
           female_count += 1
           if tomatometer == 'fresh':
               female_fresh += 1
               total_fresh += 1
           if tomatometer == 'rotten':
               female_rotten += 1
               total_rotten += 1

        if gender == 'male':
           male_count += 1
           if tomatometer == 'fresh':
               male_fresh += 1
               total_fresh += 1
           if tomatometer == 'rotten':
               male_rotten += 1
               total_rotten += 1
        
        if gender == None:
            unknown_count += 1
            if tomatometer == 'fresh':
               unknown_fresh += 1
               total_fresh += 1

            if tomatometer == 'rotten':
               unknown_rotten += 1
               total_rotten += 1

        
    print(url)
    print('Total Women: {}'.format(female_count))
    print('Women % to Total: {}'.format(female_count/total_count))
    print('Women Rotten: {}'.format(female_rotten))
    print('Women Fresh: {}'.format(female_fresh))
    print('Women Tomatometer: {}'.format(female_fresh/female_count))
    print(' ')
    print('Total Men: {}'.format(male_count))
    print('Men % to Total: {}'.format(male_count/total_count))
    print('Men Rotten: {}'.format(male_rotten))
    print('Men Fresh: {}'.format(male_fresh))
    print('Men Tomatometer: {}'.format(male_fresh/male_count))
    print(' ')
    print('Total Unknown: {}'.format(unknown_count))
    print('Unknown % to Total: {}'.format(unknown_count/total_count))
    print('Unknown Rotten: {}'.format(unknown_rotten))
    print('Unknown Fresh: {}'.format(unknown_fresh))
    print('Unknown Tomatometer: {}'.format(unknown_fresh/unknown_count))
    print(' ')
    print('Total: {}'.format(total_count))
    print('Total Rotten: {}'.format(total_rotten))
    print('Total Fresh: {}'.format(total_fresh))
    print('Total Tomatometer: {}'.format(total_fresh/total_count))


find_gender_breakdown('https://www.rottentomatoes.com/m/oceans_8/reviews?intcmp=rt-scorecard_tomatometer-reviews')