from selenium import webdriver
from bs4 import BeautifulSoup as bs
import json
from collections import OrderedDict

driver = webdriver.Chrome('chromedriver')
URL = "https://www.konyang.ac.kr/kor/sub06_07_01.do"

driver.get(URL)
driver.implicitly_wait(3)

file_data = OrderedDict()

# 대캠->논캠 =============================================================================================================
xpath = '//*[@id="txt"]/div[1]/ul/li[1]/a'
driver.find_element_by_xpath(xpath).click()

html = driver.page_source
soup = bs(html, 'lxml')

# 캠퍼스 정보
title = soup.select('h3.mt_40')[0].text

menu_list = [[], [], [], [], [], [], []]
# thead 정보
thead = driver.find_element_by_xpath('//*[@id="dep_01"]/table/thead')
thead_tr = thead.find_elements_by_tag_name("tr")
for tr in thead_tr:
    ths = tr.find_elements_by_tag_name('th')
    for th in ths:
        coin_list = []
        coin_row = th.text
        coin_list.append(coin_row)
        menu_list[0].append(coin_list)

# tbody 정보
tbody = driver.find_element_by_xpath('//*[@id="dep_01"]/table/tbody')
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

# dict 만들기
data = OrderedDict()
for col in range(1, 12):
    if col != 11:
        data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]): menu_list[1][col], ''.join(menu_list[2][0]): menu_list[2][col], ''.join(
            menu_list[3][0]): menu_list[3][col], ''.join(menu_list[4][0]): menu_list[4][col], ''.join(menu_list[5][0]): menu_list[5][col], ''.join(menu_list[6][0]): menu_list[6][col]}
    else:
        data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]): menu_list[1][col], ''.join(menu_list[2][0]): menu_list[2][col], ''.join(
            menu_list[3][0]): menu_list[2][col], ''.join(menu_list[4][0]): menu_list[2][col], ''.join(menu_list[5][0]): menu_list[2][col], ''.join(menu_list[6][0]): menu_list[6][col]}
file_data[title] = data

# 논캠->대캠 =============================================================================================================
xpath = '//*[@id="txt"]/div[1]/ul/li[2]/a'
driver.find_element_by_xpath(xpath).click()

html = driver.page_source
soup = bs(html, 'lxml')

# 캠퍼스 정보
title = soup.select('h3.mt_40')[1].text

menu_list = [[], [], [], [], []]
# thead 정보
thead = driver.find_element_by_xpath('//*[@id="dep_02"]/table/thead')
thead_tr = thead.find_elements_by_tag_name("tr")
for tr in thead_tr:
    ths = tr.find_elements_by_tag_name('th')
    for th in ths:
        coin_list = []
        coin_row = th.text
        coin_list.append(coin_row)
        menu_list[0].append(coin_list)

# tbody 정보
tbody = driver.find_element_by_xpath('//*[@id="dep_02"]/table/tbody')
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

# dict 만들기
data = OrderedDict()
for col in range(1, 13):
    data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]): menu_list[1][col], ''.join(
        menu_list[2][0]): menu_list[2][col], ''.join(menu_list[3][0]): menu_list[3][col], ''.join(menu_list[4][0]): menu_list[4][col]}
file_data[title] = data

# 유성온천역(대캠->논캠) =============================================================================================================
xpath = '//*[@id="txt"]/div[1]/ul/li[3]/a'
driver.find_element_by_xpath(xpath).click()

html = driver.page_source
soup = bs(html, 'lxml')

# 캠퍼스 정보
title = soup.select('h3.mt_40')[2].text

menu_list = [[], [], [], [], [], [], [], [], [], [], [], [], []]
# thead 정보
thead = driver.find_element_by_xpath('//*[@id="dep_24"]/table/thead')
thead_tr = thead.find_elements_by_tag_name("tr")
for tr in thead_tr:
    ths = tr.find_elements_by_tag_name('th')
    for th in ths:
        coin_list = []
        coin_row = th.text
        coin_list.append(coin_row)
        menu_list[0].append(coin_list)

# tbody 정보
tbody = driver.find_element_by_xpath('//*[@id="dep_24"]/table/tbody')
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

# dict 만들기
data = OrderedDict()
for col in range(1, 2):
    data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]): menu_list[1][col], ''.join(menu_list[2][0]): menu_list[2][col], ''.join(menu_list[3][0]): menu_list[3][col], ''.join(menu_list[4][0]): menu_list[4][col],
                                        ''.join(menu_list[5][0]): menu_list[5][col], ''.join(menu_list[6][0]): menu_list[6][col], ''.join(menu_list[7][0]): menu_list[7][col], ''.join(menu_list[8][0]): menu_list[8][col],
                                        ''.join(menu_list[9][0]): menu_list[9][col], ''.join(menu_list[10][0]): menu_list[10][col], ''.join(menu_list[11][0]): menu_list[11][col], ''.join(menu_list[12][0]): menu_list[12][col]}
file_data[title] = data

# 삼성동(대캠) =============================================================================================================
xpath = '//*[@id="txt"]/div[1]/ul/li[4]/a'
driver.find_element_by_xpath(xpath).click()

html = driver.page_source
soup = bs(html, 'lxml')

# 캠퍼스 정보
title = soup.select('h3.mt_40')[3].text

menu_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
# thead 정보
thead = driver.find_element_by_xpath('//*[@id="dep_03"]/table/thead')
thead_tr = thead.find_elements_by_tag_name("tr")
for tr in thead_tr:
    ths = tr.find_elements_by_tag_name('th')
    for th in ths:
        coin_list = []
        coin_row = th.text
        coin_list.append(coin_row)
        menu_list[0].append(coin_list)

# tbody 정보
tbody = driver.find_element_by_xpath('//*[@id="dep_03"]/table/tbody')
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

# dict 만들기
data = OrderedDict()
for col in range(1, 2):
    data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]): menu_list[1][col], ''.join(menu_list[2][0]): menu_list[2][col], ''.join(menu_list[3][0]): menu_list[3][col], ''.join(menu_list[4][0]): menu_list[4][col],
                                        ''.join(menu_list[5][0]): menu_list[5][col], ''.join(menu_list[6][0]): menu_list[6][col], ''.join(menu_list[7][0]): menu_list[7][col], ''.join(menu_list[8][0]): menu_list[8][col], ''.join(menu_list[9][0]): menu_list[9][col],
                                        ''.join(menu_list[10][0]): menu_list[10][col], ''.join(menu_list[11][0]): menu_list[11][col], ''.join(menu_list[12][0]): menu_list[12][col], ''.join(menu_list[13][0]): menu_list[13][col]}
file_data[title] = data

# 선사(유성온천역)출발 (대캠->논캠) =============================================================================================================
xpath = '//*[@id="txt"]/div[1]/ul/li[5]/a'
driver.find_element_by_xpath(xpath).click()

html = driver.page_source
soup = bs(html, 'lxml')

# 캠퍼스 정보
title = soup.select('h3.mt_40')[4].text

menu_list = [[], [], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [], [], []]
# thead 정보
thead = driver.find_element_by_xpath('//*[@id="dep_04"]/table/thead')
thead_tr = thead.find_elements_by_tag_name("tr")
for tr in thead_tr:
    ths = tr.find_elements_by_tag_name('th')
    for th in ths:
        coin_list = []
        coin_row = th.text
        coin_list.append(coin_row)
        menu_list[0].append(coin_list)

# tbody 정보
tbody = driver.find_element_by_xpath('//*[@id="dep_04"]/table/tbody')
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

# dict 만들기
data = OrderedDict()
for col in range(1, 2):
    data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]): menu_list[1][col], ''.join(menu_list[2][0]): menu_list[2][col], ''.join(menu_list[3][0]): menu_list[3][col], ''.join(menu_list[4][0]): menu_list[4][col],
                                        ''.join(menu_list[5][0]): menu_list[5][col], ''.join(menu_list[6][0]): menu_list[6][col], ''.join(menu_list[7][0]): menu_list[7][col], ''.join(menu_list[8][0]): menu_list[8][col], ''.join(menu_list[9][0]): menu_list[9][col],
                                        ''.join(menu_list[10][0]): menu_list[10][col], ''.join(menu_list[11][0]): menu_list[11][col], ''.join(menu_list[12][0]): menu_list[12][col], ''.join(menu_list[13][0]): menu_list[13][col],
                                        ''.join(menu_list[14][0]): menu_list[14][col], ''.join(menu_list[15][0]): menu_list[15][col], ''.join(menu_list[16][0]): menu_list[16][col], ''.join(menu_list[17][0]): menu_list[17][col]}
file_data[title] = data

# 삼천중학교(대캠->논캠) =============================================================================================================
xpath = '//*[@id="txt"]/div[1]/ul/li[6]/a'
driver.find_element_by_xpath(xpath).click()

html = driver.page_source
soup = bs(html, 'lxml')

# 캠퍼스 정보
title = soup.select('h3.mt_40')[6].text

menu_list = [[], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [], [], []]
# thead 정보
thead = driver.find_element_by_xpath('//*[@id="dep_06"]/table/thead')
thead_tr = thead.find_elements_by_tag_name("tr")
for tr in thead_tr:
    ths = tr.find_elements_by_tag_name('th')
    for th in ths:
        coin_list = []
        coin_row = th.text
        coin_list.append(coin_row)
        menu_list[0].append(coin_list)

# tbody 정보
tbody = driver.find_element_by_xpath('//*[@id="dep_06"]/table/tbody')
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

# dict 만들기
data = OrderedDict()
for col in range(1, 2):
    data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]): menu_list[1][col], ''.join(menu_list[2][0]): menu_list[2][col], ''.join(menu_list[3][0]): menu_list[3][col], ''.join(menu_list[4][0]): menu_list[4][col],
                                        ''.join(menu_list[5][0]): menu_list[5][col], ''.join(menu_list[6][0]): menu_list[6][col], ''.join(menu_list[7][0]): menu_list[7][col], ''.join(menu_list[8][0]): menu_list[8][col], ''.join(menu_list[9][0]): menu_list[9][col],
                                        ''.join(menu_list[10][0]): menu_list[10][col], ''.join(menu_list[11][0]): menu_list[11][col], ''.join(menu_list[12][0]): menu_list[12][col], ''.join(menu_list[13][0]): menu_list[13][col],
                                        ''.join(menu_list[14][0]): menu_list[14][col], ''.join(menu_list[15][0]): menu_list[15][col], ''.join(menu_list[16][0]): menu_list[16][col]}
file_data[title] = data

# 서대전(대캠->논캠) =============================================================================================================
xpath = '//*[@id="txt"]/div[1]/ul/li[7]/a'
driver.find_element_by_xpath(xpath).click()

html = driver.page_source
soup = bs(html, 'lxml')

# 캠퍼스 정보
title = soup.select('h3.mt_40')[5].text

menu_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
# thead 정보
thead = driver.find_element_by_xpath('//*[@id="dep_05"]/table/thead')
thead_tr = thead.find_elements_by_tag_name("tr")
for tr in thead_tr:
    ths = tr.find_elements_by_tag_name('th')
    for th in ths:
        coin_list = []
        coin_row = th.text
        coin_list.append(coin_row)
        menu_list[0].append(coin_list)

# tbody 정보
tbody = driver.find_element_by_xpath('//*[@id="dep_05"]/table/tbody')
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

# dict 만들기
data = OrderedDict()
for col in range(1, 3):
    data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]): menu_list[1][col], ''.join(menu_list[2][0]): menu_list[2][col], ''.join(menu_list[3][0]): menu_list[3][col], ''.join(menu_list[4][0]): menu_list[4][col],
                                        ''.join(menu_list[5][0]): menu_list[5][col], ''.join(menu_list[6][0]): menu_list[6][col], ''.join(menu_list[7][0]): menu_list[7][col], ''.join(menu_list[8][0]): menu_list[8][col], ''.join(menu_list[9][0]): menu_list[9][col],
                                        ''.join(menu_list[10][0]): menu_list[10][col], ''.join(menu_list[11][0]): menu_list[11][col], ''.join(menu_list[12][0]): menu_list[12][col], ''.join(menu_list[13][0]): menu_list[13][col],
                                        ''.join(menu_list[14][0]): menu_list[14][col], ''.join(menu_list[15][0]): menu_list[15][col]}
file_data[title] = data

# 대전복합터미널(논캠) =============================================================================================================
xpath = '//*[@id="txt"]/div[1]/ul/li[8]/a'
driver.find_element_by_xpath(xpath).click()

html = driver.page_source
soup = bs(html, 'lxml')

# 캠퍼스 정보
title = soup.select('h3.mt_40')[7].text

menu_list = [[], [], [], [], [], [], [], [], [], [], []]
# thead 정보
thead = driver.find_element_by_xpath('//*[@id="dep_07"]/table[1]/thead')
thead_tr = thead.find_elements_by_tag_name("tr")
for tr in thead_tr:
    ths = tr.find_elements_by_tag_name('th')
    for th in ths:
        coin_list = []
        coin_row = th.text
        coin_list.append(coin_row)
        menu_list[0].append(coin_list)

# tbody 정보
tbody = driver.find_element_by_xpath('//*[@id="dep_07"]/table/tbody')
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

# dict 만들기
data = OrderedDict()
for col in range(1, 2):
    data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]): menu_list[1][col], ''.join(menu_list[2][0]): menu_list[2][col], ''.join(menu_list[3][0]): menu_list[3][col], ''.join(menu_list[4][0]): menu_list[4][col],
                                        ''.join(menu_list[5][0]): menu_list[5][col], ''.join(menu_list[6][0]): menu_list[6][col], ''.join(menu_list[7][0]): menu_list[7][col], ''.join(menu_list[8][0]): menu_list[8][col], ''.join(menu_list[9][0]): menu_list[9][col],
                                        ''.join(menu_list[10][0]): menu_list[10][col]}
file_data[title] = data

# 송강(전민동) (대캠->논캠) =============================================================================================================
xpath = '//*[@id="txt"]/div[1]/ul/li[9]/a'
driver.find_element_by_xpath(xpath).click()

html = driver.page_source
soup = bs(html, 'lxml')

# 캠퍼스 정보
title = soup.select('h3.mt_40')[11].text

menu_list = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
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

# dict 만들기
data = OrderedDict()
for col in range(1, 2):
    data[''.join(menu_list[0][col])] = {''.join(menu_list[1][0]): menu_list[1][col], ''.join(menu_list[2][0]): menu_list[2][col], ''.join(menu_list[3][0]): menu_list[3][col], ''.join(menu_list[4][0]): menu_list[4][col],
                                        ''.join(menu_list[5][0]): menu_list[5][col], ''.join(menu_list[6][0]): menu_list[6][col], ''.join(menu_list[7][0]): menu_list[7][col], ''.join(menu_list[8][0]): menu_list[8][col], ''.join(menu_list[9][0]): menu_list[9][col],
                                        ''.join(menu_list[10][0]): menu_list[10][col], ''.join(menu_list[11][0]): menu_list[11][col], ''.join(menu_list[12][0]): menu_list[12][col], ''.join(menu_list[13][0]): menu_list[13][col], ''.join(menu_list[14][0]): menu_list[14][col], ''.join(menu_list[15][0]): menu_list[15][col], }
file_data[title] = data
# ===========================================================================================================
with open('busgoschool.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False)

driver.close()
driver.quit()
