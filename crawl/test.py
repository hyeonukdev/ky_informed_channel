from selenium import webdriver
from bs4 import BeautifulSoup as bs
import json
from collections import OrderedDict

driver = webdriver.Chrome('chromedriver')
URL = "https://www.konyang.ac.kr/kor/sub06_07_01.do"

driver.get(URL)
driver.implicitly_wait(3)

file_data = OrderedDict()

# 송강(전민동) (대캠->논캠) =============================================================================================================
xpath = '//*[@id="txt"]/div[1]/ul/li[9]/a'
driver.find_element_by_xpath(xpath).click()

html=driver.page_source
soup=bs(html,'lxml')

# 캠퍼스 정보
title = soup.select('h3.mt_40')[11].text

menu_list = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
# thead 정보
thead = driver.find_element_by_xpath('//*[@id="dep_10"]/table[1]/thead')
thead_tr = thead.find_elements_by_tag_name("tr")
for tr in thead_tr:
    ths = tr.find_elements_by_tag_name('th')
    for th in ths:
        coin_list = []
        coin_row = th.text
        coin_list.append(coin_row)
        menu_list[0].append(coin_list)

# tbody 정보
tbody = driver.find_element_by_xpath('//*[@id="dep_10"]/table/tbody')
tbody_tr = tbody.find_elements_by_tag_name("tr")
i = 1
for tr in tbody_tr:
    ths = tr.find_elements_by_tag_name('th')
    tds = tr.find_elements_by_tag_name('td')
    for th in ths:
        coin_list = []
        coin_row = th.text
        coin_row_list = coin_row.split("\n ")
        menu_list[i].append(coin_row_list)
    for td in tds:
        coin_row = td.text
        coin_row_list = coin_row.split("\n")
        menu_list[i].append(coin_row_list)
    i = i+1

#for a in range(0,13):
#    print(menu_list[a])

# dict 만들기
data = OrderedDict()
for col in range(1,2):
    data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]):menu_list[1][col], ''.join(menu_list[2][0]):menu_list[2][col], ''.join(menu_list[3][0]):menu_list[3][col], ''.join(menu_list[4][0]):menu_list[4][col],
    ''.join(menu_list[5][0]):menu_list[5][col], ''.join(menu_list[6][0]):menu_list[6][col], ''.join(menu_list[7][0]):menu_list[7][col], ''.join(menu_list[8][0]):menu_list[8][col], ''.join(menu_list[9][0]):menu_list[9][col], 
    ''.join(menu_list[10][0]):menu_list[10][col], ''.join(menu_list[11][0]):menu_list[11][col], ''.join(menu_list[12][0]):menu_list[12][col], ''.join(menu_list[13][0]):menu_list[13][col], ''.join(menu_list[14][0]):menu_list[14][col], ''.join(menu_list[15][0]):menu_list[15][col],}
file_data[title] = data

with open('busgoschool1.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False)

driver.close()
driver.quit()