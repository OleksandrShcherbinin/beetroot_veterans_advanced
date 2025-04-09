# import httpx
#
#
# response = httpx.get(
#     'https://developer.mozilla.org/',
#     headers={'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1'}
# )
# print(response.status_code)
# print(response.headers)
# print(response.cookies)
# print(response.request.headers)
import json

import requests
from lxml import etree

qop = 'auth'
user = 'user'
password = 'passwd'
number = 100
url = f'https://httpbin.org/stream/{number}'

# with requests.Session() as session:
#     response = session.get(url, timeout=5, stream=True)
#     print(response.status_code)
#     with open('files/data_new.json', 'wb') as file:
#         for chunk in response.iter_lines():
#             if chunk:
#                 data = json.loads(chunk.decode('utf-8'))
#                 file.write(chunk)


# with requests.Session() as session:
#     response = session.get(url, timeout=5, stream=True)
#     print(response.status_code)
#     with open('files/data_new', 'wb') as file:
#         for chunk in response.iter_content(chunk_size=10):
#             if chunk:
#                 file.write(chunk)

url = 'https://dummyjson.com/auth/me'
# data = {'username': 'emilys', 'password': 'emilyspass', 'expiresInMins': 30}
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJlbWlseXMiLCJlbWFpbCI6ImVtaWx5LmpvaG5zb25AeC5kdW1teWpzb24uY29tIiwiZmlyc3ROYW1lIjoiRW1pbHkiLCJsYXN0TmFtZSI6IkpvaG5zb24iLCJnZW5kZXIiOiJmZW1hbGUiLCJpbWFnZSI6Imh0dHBzOi8vZHVtbXlqc29uLmNvbS9pY29uL2VtaWx5cy8xMjgiLCJpYXQiOjE3NDQyMjEzODAsImV4cCI6MTc0NDIyMzE4MH0.7HYrmBqp8vaCUuXWLo3JM4ILfjmmmrmHYIFEeZ6MxKw', 'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJlbWlseXMiLCJlbWFpbCI6ImVtaWx5LmpvaG5zb25AeC5kdW1teWpzb24uY29tIiwiZmlyc3ROYW1lIjoiRW1pbHkiLCJsYXN0TmFtZSI6IkpvaG5zb24iLCJnZW5kZXIiOiJmZW1hbGUiLCJpbWFnZSI6Imh0dHBzOi8vZHVtbXlqc29uLmNvbS9pY29uL2VtaWx5cy8xMjgiLCJpYXQiOjE3NDQyMjEzODAsImV4cCI6MTc0NjgxMzM4MH0.u2CII9cHgPt9AxO7DO95ULXGrZ9W9GQwZOkfQri2C5k"

with requests.Session() as session:
    response = session.get(url, timeout=5, headers={'Authorization': 'Bearer ' +access_token})
    print(response.status_code)
    data = response.json()
    print(data)

