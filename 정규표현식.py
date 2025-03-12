import re

string = 'hello hjk790@gmail.com 010-222-3333 world 02-5678-9988'

phone_pattern = re.compile(r'\d{2,3}-\d{3,4}-\d{4}') # raw, 위의 예에서 전화번호를 찾는 패턴

phone_list = phone_pattern.findall(string)
print(phone_list)
print(re.findall(phone_pattern, string))

email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
email_list = re.findall(email_pattern, string)
print(email_list)
