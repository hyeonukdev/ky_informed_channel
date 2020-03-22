import json
from collections import OrderedDict

file_data = OrderedDict()

file_data["name"] = "room_address"
file_data["number"] = 8
file_data["data"] = {
    '간호학사': '대전광역시 서구 관저동로 158 간호학사',
    '담곡학사': '대전광역시 서구 관저동로 158 담곡학사',
    '청림학사': '대전광역시 서구 관저동로 158 청림학사',
    '봉사학사': '대전광역시 서구 관저동로 158 봉소학사',
    '현암학사': '대전광역시 서구 관저동로 158 현암학사',
    '선행화학사': '대전광역시 서구 관저동로 158 선행화학사',
    '반야학사': '대전광역시 서구 관저동로 158 반야학사',
    '구연학사': '대전광역시 서구 관저동로 158 구연학사'
}

print(json.dumps(file_data, ensure_ascii=False))

with open('../json/room_address.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False)
