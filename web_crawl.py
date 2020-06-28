import os.path
import time
import shutil
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('headless')
options.add_experimental_option("prefs", {
    "download.default_directory": r"E:\College NSF",
    "download.prompt_for_download": False,
    "download.directroy_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)

headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/83.0.4103.97 Safari/537.36',
             'X-Amzn-Trace-Id': 'Root=1-5ee7b614-d1d9a6e8106184eb3d66b108'
        }

states = {'Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California',
          'Colorado', 'Connecticut', 'Delaware', 'Florida',
          'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
          'Minnesota', 'Mississippi', 'Missouri', 'Montana',
          'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
          'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma',
          'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina',
          'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
          'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'}


def download_nsf(state):
    with open(r'E:\College NSF\\' + state + '\\' + state + '.txt') as file:
        colleges = file.readlines()
        for college in colleges:
            college = college.rstrip()
            link = 'https://www.nsf.gov/awardsearch/advancedSearchResult?PIId=&PIFirstName=&PILastName=&PIOrganization=' + \
                   college.replace(' ', '+') + '&PIState=&PIZip=&PICountry=&ProgOrganization=&ProgEleCode=&BooleanElement=' \
                   'All&ProgRefCode=&BooleanRef=All&Program=&ProgOfficer=&Keyword=&AwardNumberOperator=&AwardAmount=&' \
                   'AwardInstrument=&ActiveAwards=true&ExpiredAwards=true&OriginalAwardDateOperator=&StartDateOperator=&' \
                   'ExpDateOperator='
            print(link)
            driver.get(link)
            time.sleep(20)

            college_file = r'E:\College NSF\\' + state + '\\' + college + '.csv'
            if os.path.exists(college_file):
                os.remove(college_file)

            try:
                driver.find_element_by_id('x-auto-33').click()
                file_path = r'E:\College NSF\Awards.csv'
                while not os.path.exists(file_path):
                    time.sleep(1)

                os.rename(r'E:\College NSF\Awards.csv', r'E:\College NSF\\' + college + '.csv')
                shutil.move(r'E:\College NSF\\' + college + '.csv', r'E:\College NSF\\' + state)
            except NoSuchElementException as e:
                with open(r'E:\College NSF\\' + state + '\\' + state + 'NotFound.txt', 'a') as f:
                    f.write(college + '\n')


def download_nsf_college(state, college):
        link = 'https://www.nsf.gov/awardsearch/advancedSearchResult?PIId=&PIFirstName=&PILastName=&PIOrganization=' + \
               college.replace(' ', '+') + '&PIState=&PIZip=&PICountry=&ProgOrganization=&ProgEleCode=&BooleanElement=' \
               'All&ProgRefCode=&BooleanRef=All&Program=&ProgOfficer=&Keyword=&AwardNumberOperator=&AwardAmount=&' \
               'AwardInstrument=&ActiveAwards=true&ExpiredAwards=true&OriginalAwardDateOperator=&StartDateOperator=&' \
               'ExpDateOperator='
        print(link)
        driver.get(link)
        time.sleep(20)

        college_file = r'E:\College NSF\\' + state + '\\' + college + '.csv'
        if os.path.exists(college_file):
            os.remove(college_file)

        try:
            driver.find_element_by_id('x-auto-33').click()
            file_path = r'E:\College NSF\Awards.csv'
            while not os.path.exists(file_path):
                time.sleep(1)

            os.rename(r'E:\College NSF\Awards.csv', r'E:\College NSF\\' + college + '.csv')
            shutil.move(r'E:\College NSF\\' + college + '.csv', r'E:\College NSF\\' + state)
        except NoSuchElementException as e:
            with open(r'E:\College NSF\\' + state + '\\' + state + 'NotFound.txt', 'a') as f:
                f.write(college + '\n')


for state in states:
    if not os.path.exists(r'E:\College NSF\\' + state):
        os.makedirs(r'E:\College NSF\\' + state)

    # f = open(r'E:\College NSF\\' + state + '\\' + state + '.txt', 'a')
    # g = open(r'E:\College NSF\\' + state + '\\' + state + 'NotFound.txt', 'a')
    # f.close()
    # g.close()

download_nsf_college('Alabama', 'Wallace State Community College')

