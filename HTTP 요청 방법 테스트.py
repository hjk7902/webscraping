import requests

response = requests.post("https://httpbin.org/post", json={'key':'value'})
# response = requests.post("https://httpbin.org/post", data=[('key','value')])
print(response.stat기us_code)
# print(response.text)
json_response = response.json()
print(json_response)
print(json_response['data'])
print(json_response['headers']['Content-Type'])