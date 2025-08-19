import requests
url = "http://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print(response.json())

url ="https://jsonplaceholder.typicode.com/posts"
post ={"title":"ddd" ,"body":555,'anas':False}
response =requests.post(url , json=post)

print (response.status_code)
print (response.headers["content-type"])
print(response.json())


url="https://jsonplaceholder.typicode.com/posts/15"
response =requests.get(url)
print(response.status_code)
print(response.json())

post ={"userid" : 1 ,"title": "daraghmeh" ,"body" : ""}
response =requests.put(url , json =post)
print(response.status_code)
print(response.json())

url ="https://jsonplaceholder.typicode.com/posts/15"
response=requests.get(url)
print (response.status_code)
print(response.json())

update ={'body':"good moring"}
response =requests.patch(url ,json=update)
print (response.status_code)
print (response.json())

url="http://jsonplaceholder.typicode.com/posts/15"
response=requests.delete(url)
print(response.status_code)
print(response.json())

