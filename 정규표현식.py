import re

pattern = re.compile(r'\d+')
match = pattern.match('123abc')
if match:
    print(match.group())  # 123


import re

pattern = re.compile(r'\d+')
match = pattern.search('abc123')
if match:
    print(match.group())  # 123


import re

pattern = re.compile(r'\d+')
matches = pattern.findall('abc123def456')
print(matches)  # ['123', '456']

import re

pattern = re.compile(r'\d+')
result = pattern.sub('NUMBER', 'abc123def456')
# result = re.sub(pattern, 'NUMBER', 'abc123def456')
print(result)  # abcNUMBERdefNUMBER
