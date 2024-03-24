from selenium import webdriver
import time
from time import sleep
import requests
import sys
import math
from datetime import date
import  os 
import datetime
import time 
import sched
import webbrowser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class MyWebdriver:

    def __init__(self, webdriverval):
        driver = webdriverval


    def remove_quotes(self):  # not in use   # possibly take in list, return string?
        data = ""
        with open("new_info.csv") as file:
            data = file.read().replace('"', "'").replace('[', '').replace(']', '').replace("'", '').replace('.', '').replace(' ,', '')

        with open("new_info_mod.csv", 'a') as file:
            file.write(data)

    def toBinary(a):
          l,m=[],[]
          # print("''Hello world'' in binary is ") 
          # print(toBinary("Hello world"))
          for i in a:
            l.append(ord(i))
          for i in l:
            m.append(int(bin(i)[2:]))
          return m


    def table_scrape(self, race_date):
        num_tables = driver.find_elements('tag name', 'table')
        race_count = len(num_tables) / 3
        tables = driver.find_elements('xpath', "//table[@class='table table-sm table-hrn table-entries']")
        scratched = driver.find_elements('xpath', "//*[@class='scratched']")
        col_headers = driver.find_elements('tag name', 'thead')
        payouts = driver.find_elements('xpath', "//table[@class='table table-hrn table-payouts']")
        race_info = driver.find_elements('xpath', "//*[@class='col-lg-auto flex-grow-1 race-distance']")
        race_purse = driver.find_elements('xpath', "//*[@class='col-lg-auto race-purse']")

        path = 'data/aqueduct-test/' + str(race_date.strip("\n")) + '/'

        os.makedirs(path, exist_ok=True)

        race = 0
        # sleep(5)
        for money, x in zip(race_purse, race_info):
            race = race + 1
            np = path + "race" + str(race) + "/"
            os.makedirs(np, exist_ok=True)
            price = money.text
            price = price.replace('[', '').replace(']', '')
            price = price.replace('Purse: ', '').replace(',', '')
            price = price.replace('$', '')
            rinfo = [x.text]
            rinfo = [item.replace('[', '') for item in rinfo]
            rinfo = [item.replace(']', '') for item in rinfo]
            rinfo = [item.replace(',000', '000') for item in rinfo]
            rinfo = [item.replace(',500', '500') for item in rinfo]
            rinfo = [item.replace('$', '') for item in rinfo]
            rinfo = [item.replace('-', '') for item in rinfo]
            rinfo = [item.replace('Dirt', '0') for item in rinfo]
            rinfo = [item.replace('Turf', '1') for item in rinfo]
            # race_date = race_date.replace('-', '')
            # race_date = race_date.replace('\n', '').replace('-', '') # adds date
            print(type(race_date))
            race_date = int(race_date)
            rinfo.insert(0, race_date)

            rinfo.insert(1, str(race)) # adds race_num
            rinfo.insert(2, price) # add purse
            # if rinfo == "Dirt":
            #     rinfo.replace("Dirt", int(0))
            # if rinfo == "Turf":
            #     rinfo.replace("Turf", int(1))
            rinfo = str(rinfo) # date, race, purse, dist, dirt/turf, type
            rinfo = rinfo.replace('"', "'").replace('[', '').replace(']', '').replace("'", '').replace('.', '').replace(' ,', '').replace('/', '')

            new_path = np + 'new_info.csv'
            sys.stdout = open(new_path, 'a')
            print(rinfo)

        # print('starting "for table in payouts: " ')
        ra = 0
        # sleep(5)
        for table in payouts:
            ra = ra + 1
            #winner_stats = []
            #new_stats = []
            for row in table.find_elements('tag name', 'tr'):
                winner_stats = []
                new_stats = []
                for cell in row.find_elements('tag name', 'td'):
                    cell = cell.text
                    winner_stats.append(cell)
                if winner_stats == []:
                    # print('winner_stats == []')
                    pass
                else:
                    # print('payout checkpoint')
                    winner_stats.pop(1)
                    winner_stats_str = str(winner_stats)
                    winner_stats_str = winner_stats_str.replace('"', "'").replace('[', '').replace(']', '').replace("'", '').replace(' ,', '')
                    nppp = path + "race" + str(ra) + "/"
                    new_path = nppp + 'payouts.csv'  
                    sys.stdout = open(new_path, 'a')
                    print(winner_stats_str)

        # sleep(5)
        n = 0
        for table in tables:
            n = n + 1
            for entry in table.find_elements('tag name', 'tr'):
                if entry not in scratched:
                    horse_stats = []
                    new_stat = []
                    for stat in entry.find_elements('tag name', 'td'):
                        stat = stat.text
                        m = stat.replace("\n", "', '").replace(", Jr.", " Jr.")
                        horse_stats.append(m)
                    if horse_stats == []:
                        pass
                    else:
                        npppp = path + "race" + str(n) + "/"
                        new_path = npppp + 'entries.csv'
                        horse_stats_str = str(horse_stats)
                        horse_stats_str = horse_stats_str.replace('"', "'").replace('[', '').replace(']', '').replace("'", '').replace('.', '').replace(' ,', '')
                        horse_stats_str = horse_stats_str[2:]
                        sys.stdout = open(new_path, 'a')
                        print(horse_stats_str)
                else:
                    pass



if __name__ == '__main__':

    start_time = time.time()
    print("entered __main__")
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument("--start-maximized")
    # chrome_options.page_load_strategy = "eager"
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.page_load_strategy = 'none'
    # chrome_options.add_argument("--headless")
    print('got here')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

file1 = open('2022-aqueduct-race-days.txt', 'r')

for item in file1:
    sleep(3)
    str_item = str(item)
    N = 11
    length = len(str_item)
    date = str_item[length - N:]
    url = item.strip()
    request = requests.head(url)
    print("checking if site exists")
    sleep(3)
    if request.status_code == 200: # maybe from here, create function below containing next steps??
        print("launching driver")
        driver.get(url)
        sleep(3)
        driver.refresh()
        obj = MyWebdriver(driver)
        sleep(3)
        obj.table_scrape(date)
        sleep(3)

    else:
        pass
