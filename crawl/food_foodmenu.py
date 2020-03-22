from selenium import webdriver
from bs4 import BeautifulSoup as bs
import json
from collections import OrderedDict

# 유의: chromedriver를 위에서 받아준 
# chromdriver(windows는 chromedriver.exe)의 절대경로로 바꿔주세요!
driver = webdriver.Chrome('chromedriver')
URL = "https://www.konyang.ac.kr/prog/sikdan/kor/sub06_06_03/list.do"

driver.get(URL)
driver.implicitly_wait(3)

file_data = OrderedDict()

for i in range(1,3):
    xpath = '//*[@id="sikdang_cd"]/optgroup/option['+ str(i) +']'
    driver.find_element_by_xpath(xpath).click()

    html=driver.page_source
    soup=bs(html,'lxml')
    #print(soup)

    # 캠퍼스 정보
    campus = soup.select('h3.mb_10')[0].text

    menu_list = [[],[],[],[]]
    # 날짜 정보
    thead = driver.find_element_by_xpath('//*[@id="sikdan"]/table/thead')
    thead_tr = thead.find_elements_by_tag_name("tr")
    for tr in thead_tr:
        ths = tr.find_elements_by_tag_name('th')
        i = 0
        for th in ths:
            coin_list = []
            coin_row = th.text
            coin_row = coin_row[8:]
            coin_row = coin_row.replace('.','월')
            coin_row = coin_row.replace(')','일')
            if i != 0 and i != 6:
                if coin_row[0] == '0':
                    coin_row = coin_row[1:]
                if coin_row[-3] == '0':
                    coin_row = coin_row[:-3]+coin_row[-2:]
            i = i+1
            coin_list.append(coin_row)
            menu_list[0].append(coin_list)

    # 메뉴 정보
    tbody = driver.find_element_by_xpath('//*[@id="sikdan"]/table/tbody')
    tbody_tr = tbody.find_elements_by_tag_name("tr")
    i = 1
    for tr in tbody_tr:
        tds = tr.find_elements_by_tag_name('td')
        for td in tds:
            coin_list = []
            coin_row = td.text
            coin_row_list = coin_row.split("\n")
            menu_list[i].append(coin_row_list)
        i = i+1

    #for a in range(0,4):
    #    print(menu_list[a])

    # dict 만들기
    data = OrderedDict()
    for col in range(1,6):
        data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]):menu_list[1][col], ''.join(menu_list[2][0]):menu_list[2][col], ''.join(menu_list[3][0]):menu_list[3][col]}
    file_data[campus] = data

with open('food_foodmenu.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False)

driver.close()
driver.quit()