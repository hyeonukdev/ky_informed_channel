from datetime import datetime
import json
from collections import OrderedDict

with open('food_foodmenu.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

month = datetime.today().month      # 현재 월 가져오기
day = datetime.today().day      # 현재 일 가져오기
date = str(month) + "월 " + str(day) + "일"

campus1 = json_data["죽헌정보관"]
today_campus1_menu = campus1[date]
campus2 = json_data["건양회관"]
today_campus2_menu = campus2[date]

file_data = OrderedDict()
file_data["죽헌정보관"] = today_campus1_menu
file_data["건양회관"] = today_campus2_menu

with open('food_foodmenu_today.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, indent=3 ,ensure_ascii=False)