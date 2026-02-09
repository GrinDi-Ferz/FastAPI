import requests

# data = requests.post(
#     "http://127.0.0.1:8002/advertisement", json={"title": "phone", "price": "20000", "description": "newdewsc", "author": "Author_Name"}
# )
# print(data.status_code)
# print(data.json())

# data = requests.get("http://127.0.0.1:8002/advertisement/5")
# print(data.status_code)
# print(data.json())

# data = requests.patch("http://127.0.0.1:8002/advertisement/5", json={"title": "phone", "price": "220000", "description": "advertisment", "author": "User1"})
# print(data.status_code)
# print(data.json())

data = requests.get("http://127.0.0.1:8002/advertisement", params={"title": "phone"})
print(data.status_code)
print(data.json())

# # data = requests.delete("http://127.0.0.1:8002/advertisement/2")
# # print(data.status_code)
# # print(data.json())

# data = requests.get("http://127.0.0.1:8002/advertisement/5")
# print(data.status_code)
# print(data.json())

# data = requests.get(
#     "http://127.0.0.1:8002/advertisement/2"
# )
# print(data.status_code)
# print(data.json())