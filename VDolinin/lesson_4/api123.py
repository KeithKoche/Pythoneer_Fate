import requests
import json


#dogapi вывести код успешного запроса
def test_api():
    responce = requests.get("https://dog.ceo/api/breeds/list/all", params={'status': 'status'})
    responce.raise_for_status()
    print(responce)
    # assert "status" == 'success'

# #получить тело запроса
def test_req():
    responce = requests.get("https://dog.ceo/api/breed/schnauzer/giant/images/random/4")
    print(responce.json()['message'])

def test_req2():
    responce = requests.get("https://dog.ceo/api/breed/hound/list")
    print(responce.json()['message'])


#openbrewery тело запроса
def test_simple():
    responce = requests.get("https://api.openbrewerydb.org/breweries")
    print(responce.json())


# пивоварни города Montgomery
def test_knox():
    responce = requests.get("https://api.openbrewerydb.org/breweries?by_city=montgomery")
    print(responce.json())


# responce = requests.get("https://api.openbrewerydb.org/breweries?by_id=10th-district-brewing-company-abington")
# print(responce.json())


# поиск по запросу search by req
def test_rq():
    url = 'https://api.openbrewerydb.org/breweries/search?query=mackinaw'
    response = requests.get(url)
    print(response.json())


# status.code
def test_brewery_status(): #status not 200
    responce = requests.get("https://api.openbrewerydb.org/ghvfgvgnh", params={'status': 'status'})
    if responce.status_code == 200:
        print('success 200 ok')
    else:
        print('error not 200')


def test_brewery_status200(): #status 200
    responce = requests.get("https://api.openbrewerydb.org/breweries", params={'status': 'status'})
    if responce.status_code == 200:
        print('success 200 ok')
    else:
        print('status not 200')


# json placeholder body
def test_placeholder():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response.json())


def test_placerq(): # json headers
    responce = requests.get("https://jsonplaceholder.typicode.com/users")
    print(responce.headers)


def test_yandex_is_available():
    response = requests.get("https://ya.ru")
    assert response.ok


def test_page_unavailable():
    response = requests.get("https://ya.ru/sfhfhfhfhfhfhfhfh")
    assert response.status_code == 404






