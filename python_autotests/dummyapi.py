import requests

host = "https://dummyapi.io/data/v1"
token = "64f71ad23fb07a9205d09849"
randomFirstName = "nika"
randomLastName = "petrova"
email = "test6969@email.com"
id = "64f7232fa9de561d5f59c1f7"

# создание юзера

userCreate = requests.post(f'{host}/user/create', data = {
    'lastName': 'vereshagin',
    'firstName': 'kolya',
    'email': email
},
headers = {
    "app-id": token
})

print(userCreate.text)

# изменение юзера

userUpdate = requests.put(f'{host}/user/{id}', data = {
    'lastName': randomLastName,
    'firstName': randomFirstName
},
headers = {
    "app-id": token
})

print(userUpdate.text)
print(userUpdate.status_code)

if userUpdate.status_code == 200:
    print('OK!')
else:
    print('Not OK!')


# загрузка листа постов юзеров с лимитом выдачи 5

postsList = requests.get(f'{host}/post', headers = {
    "app-id": token
}, params={
    'limit': 5
})

print(postsList.json())