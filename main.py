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

from flask import Flask, render_template, request
app = Flask(__name__)


# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)

# wait = WebDriverWait(driver, 10)

# class Stats:
#     """Class that aggregates all of the stats for a movie."""
#     def __init__(self):
#         self.count = 0
#         self.rotten = 0
#         self.fresh = 0

#     def addCount(self):
#         self.count += 1
    
#     def addRotten(self):
#         self.rotten += 1
    
#     def addFresh (self):
#         self.fresh += 1

#     def showScore(self):
#         return self.fresh / self.count

# women = Stats()
# men = Stats()
# unknown = Stats()
# total = Stats()

# def find_gender_breakdown(url):
#     driver.get(url)
#     next_class = '.js-prev-next-paging-next.btn.prev-next-paging__button.prev-next-paging__button-right'
#     next_button = driver.find_element(By.CSS_SELECTOR, next_class)

#     review_class = '.row.review_table_row'
#     name_class = '.critic_name'
#     review_icon_class = '.review_icon'


#     reviews = {}

#     while(next_button):
#         time.sleep(3)
#         reviews_on_page = driver.find_elements(By.CSS_SELECTOR, review_class)
    
#         for review in reviews_on_page:
#             name_element = review.find_element(By.CSS_SELECTOR, name_class)
#             name_link = name_element.find_element(By.TAG_NAME, 'a')
#             name = name_link.get_attribute('innerHTML')

#             review_icon_element = review.find_element(By.CSS_SELECTOR, review_icon_class)
#             review_icon_all_classes = review_icon_element.get_attribute("class")
#             tomatometer = ''

#             if 'rotten' in review_icon_all_classes:
#                 tomatometer = 'rotten'
#             else:
#                 tomatometer = 'fresh'

#             reviews[name] = {
#                 'tomatometer': tomatometer
#             }

#         for name in reviews:
#             name_list = name.split(' ')
#             first_name = name_list[0]
#             response = requests.get('https://api.genderize.io?name={}&apikey={}'.format(first_name,API_KEY))
#             json = response.json()
#             print(json)
#             reviews[name]['gender'] = json['gender']

#         try:
#             next_button.click()
#         except: 
#             print('End reached')
#             next_button = False

#     for name in reviews:
#         gender = reviews[name]['gender']
#         tomatometer = reviews[name]['tomatometer']

#         total.addCount()

#         if gender == 'female':
#            women.addCount()
#            if tomatometer == 'fresh':
#                women.addFresh()
#                total.addFresh()
#            if tomatometer == 'rotten':
#                women.addRotten()
#                total.addRotten()

#         if gender == 'male':
#            men.addCount()
#            if tomatometer == 'fresh':
#                men.addFresh()
#                total.addFresh()
#            if tomatometer == 'rotten':
#                men.addRotten()
#                total.addRotten()
        
#         if gender == None:
#             unknown.addCount()
#             if tomatometer == 'fresh':
#                unknown.addFresh()
#                total.addFresh()

#             if tomatometer == 'rotten':
#                unknown.addRotten()
#                total.addRotten()

        
#     print(url)
#     print('Total Women: {}'.format(women.count))
#     print('Women % to Total: {}'.format(round((women.count/total.count)*100)))
#     print('Women Rotten: {}'.format(women.rotten))
#     print('Women Fresh: {}'.format(women.fresh))
#     print('Women Tomatometer: {}'.format(round((women.fresh/women.count)*100)))
#     print(' ')
#     print('Total Men: {}'.format(men.count))
#     print('Men % to Total: {}'.format(round((men.count/total.count)*100)))
#     print('Men Rotten: {}'.format(men.rotten))
#     print('Men Fresh: {}'.format(men.fresh))
#     print('Men Tomatometer: {}'.format(round((men.fresh/men.count)*100)))
#     print(' ')
#     print('Total Unknown: {}'.format(unknown.count))
#     print('Unknown % to Total: {}'.format(round((unknown.count/total.count)*100)))
#     print('Unknown Rotten: {}'.format(unknown.rotten))
#     print('Unknown Fresh: {}'.format(unknown.fresh))
#     print('Unknown Tomatometer: {}'.format(round((unknown.fresh/unknown.count)*100)))
#     print(' ')
#     print('Total: {}'.format(total.count))
#     print('Total Rotten: {}'.format(total.rotten))
#     print('Total Fresh: {}'.format(total.fresh))
#     print('Total Tomatometer: {}'.format(round((total.fresh/total.count)*100)))

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/users/<username>')
# def show_username(username):
#     return f'Hello {username}'
    
# @app.route('/getmovie', methods=['GET', 'POST'])
# def get_movie():
#     if request.method == 'POST':
#         form_data = request.form
#         return render_template('data.html', form_data = form_data)
#     return render_template('getmovie.html')

# app.run(host='localhost', port=5000)