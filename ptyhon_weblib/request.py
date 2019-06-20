from urllib.parse import urlencode
from urllib.request import urlopen, Request

# Get
httpresponse = urlopen('http://www.example.com?a=123&key=keyiskey')
body = httpresponse.read()
print(type(httpresponse))
print(body)


# Post
data = {
    'email': 'lucy@gmail.com',
    'password': '1234',
    'name': '조부광'
}
# post로 보내면 body 부분에 data붙어서 보내짐
# data = urlencode(data)
data = urlencode(data).encode('utf-8')
# b' => binary ? byte ?

# Request객체는 Post방식으로 보낼때 꼭 필요
# Get은 urlopen만으로도 ok
request = Request('http://www.example.com', data)
httpresponse = urlopen(request)
print(httpresponse.read())

# Cookie 등 줄 때 header add 가능
request.add_header('Content-Type', 'text/html')
# request.add_header('cookies:jsessionid=54f64ds8f423sefd')

httpresponse