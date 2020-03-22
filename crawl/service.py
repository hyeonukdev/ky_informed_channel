from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\Users\yejiPark\chromedriver_win32\chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.fsb.or.kr/bank/finding_bank.do')
path=['//*[@id="subContents"]/div[5]/dl[1]/dd/ul/li[',']/a']
path_index=[2,3,4,5,6,7]
end=[282,239,212,189,197,190]
loc=[162,163,164,165,166,167]

bis_list=[]
for per in range(0,6):
    xpath=path[0]+str(path_index[per])+path[1]
    driver.find_element_by_xpath(xpath).click()

    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')
    bises=soup.find_all('a')
    if(per==5):
        driver.close()
        
    # 가져온 내용을 list에 저장
    i=0
    for bis in bises:
        if(i==loc[per]):
            t=bis.get_text().strip()
        if(i>167):
            if(i>end[per]):
                break
            else:
                bis_list.append(t)
                bis_list.append('*')
                bis_list.append(bis.get_text().strip())
                bis_list.append('**')
        i=i+1


# 파일을 만들고 그안에 리스트 내용 저장
bis_list=",".join(map(str,bis_list))
bis_list=bis_list.replace("\n","")
bis_list=bis_list.replace(",","")
bis_list=bis_list.replace("]","")
bis_list=bis_list.replace("[",",")
bis_list=bis_list.replace("선택됨","")
bis_list=bis_list.replace("**","\n")
bis_list=bis_list.replace("*",",")
file=open('service1.csv','w',encoding='ANSI')
for bis in bis_list:
    file.write(bis)
file.close()

#------------------------------------------------------------------------------
driver = webdriver.Chrome(r'C:\Users\yejiPark\chromedriver_win32\chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.fsb.or.kr/bank/finding_bank.do')
path1=['//*[@id="subContents"]/div[5]/dl[1]/dd/ul/li[',']/a']
path1_index=[2,3,4,5,6,7]
end=[286,243,216,193,201,194]
loc=[166,167,168,169,170,171]
path2=['//*[@id="subContents"]/div[5]/dl[2]/dd/ul/li[',']/a']
path2_n=[115,72,45,22,30,23]

bis_list=[]
s1=[]
s2=[]
s3=[]
for per1 in range(0,6):
    xpath=path1[0]+str(path1_index[per1])+path1[1]
    driver.find_element_by_xpath(xpath).click()
    
    for per2 in range(0,path2_n[per1]):
        xpath=path2[0]+str(per2+1)+path2[1]
        driver.find_element_by_xpath(xpath).click()
        html=driver.page_source
        soup=BeautifulSoup(html,'lxml')
        bises=soup.find_all('dd')
    
        # 가져온 내용을 list에 저장
        i=0
        for bis in bises:
            if(i==9):
                s1=bis.get_text().split('도로명주소 : ')
                s2=s1[0].split('지번주소 : ')
                bis_list.append(s2[1])
                bis_list.append("*")
                s3=s1[1].split('\n')
                bis_list.append(s3[0])
                bis_list.append("*")
            elif(i>11):
                if(i>13):
                    bis_list.append("*")
                    break
                else:
                    bis_list.append(bis.get_text().strip())
                    bis_list.append("*")
            i=i+1
            if((per1==1 and (per2+1==56 or per2+1==57))or(per1==4 and(per2+1==21 or per2+1==22))):
                xpath=path1[0]+str(path1_index[per1])+path1[1]
                driver.find_element_by_xpath(xpath).click()

driver.close()

# 파일을 만들고 그안에 리스트 내용 저장
bis_list=",".join(map(str,bis_list))
bis_list=bis_list.replace("\n","")
bis_list=bis_list.replace(",","")
bis_list=bis_list.replace("**","\n")
bis_list=bis_list.replace("*",",")
file=open('service2.csv','w',encoding='ANSI')
for bis in bis_list:
    file.write(bis)
file.close()

#--------------------------------------------------------------------------------
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome(r'C:\Users\yejiPark\chromedriver_win32\chromedriver')
driver.implicitly_wait(3)
driver.get('http://f.goodkiss.co.kr/naver/naverMap.html')
file=open('service2.csv')
csv_reader=csv.reader(file)
lines=list(csv_reader)
file.close()

bis_list=[]
for per in range(0,307):
    line=lines[per][0]
    if(per==22 or per==26 or per==27 or per==55 or per==144 or per==253 or per==269 or per==272):
        line=line[:-3]
    elif(per==39):
        line=line[:-14]
    elif(per==305):
        line=line[:-16]
    elif(per==156 or per==273):
        line=line[:-5]
    elif(per==130):
        line=line[:-8]
    elif(per==286):
        line=line[:-9]
    elif(per==220):
        line=lines[per][1]
        line=line[:-8]
    driver.find_element_by_name('addr').send_keys(line)
    driver.find_element_by_xpath('/html/body/form/span/input[2]').click()
    html=driver.page_source
    soup=BeautifulSoup(html,'lxml')
    bises=soup.find_all('tbody')
        
    # 가져온 내용을 list에 저장
    for bis in bises:
        s1=bis.get_text().split('\n')
        bis_list.append(s1[7])
        bis_list.append(",")
        bis_list.append(s1[8])
        bis_list.append("\n")

    driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/input').click()

driver.close()
file.close()

# 파일을 만들고 그안에 리스트 내용 저장
file=open('service3.csv','w',encoding='ANSI')
for bis in bis_list:
    file.write(bis)
file.close()

