# requests

`pip install requests`

```py
>>> import requests
>>> req = requests.request('GET', 'http://github.com')
<Response [200]>

req = requests.post('http://github.com', data = {'key':'value'})
```

## 请求内容为json

```py
import requests

req = requests.post('http://github.com', json = {'key':'value'})
```



## 返回内容

**r.text**

```py
>>> import requests

>>> r = requests.get('https://api.github.com/events')
>>> r.text
u'[{"repository":{"open_issues":0,"url":"https://github.com/...
```

**r.content**
You can also access the response body as bytes, for non-text requests:
```py
>>> r.content
b'[{"repository":{"open_issues":0,"url":"https://github.com/...
```

**r.json()**

```py
>>> import requests

>>> r = requests.get('https://api.github.com/events')
>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
```

**r.raw()**

In the rare case that you’d like to get the raw socket response from the server, you can access r.raw. If you want to do this, make sure you set stream=True in your initial request. Once you do, you can do this:

```py
>>> r = requests.get('https://api.github.com/events', stream=True)

>>> r.raw
<urllib3.response.HTTPResponse object at 0x101194810>

>>> r.raw.read(10)
'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
```

## 传递url参数 GET请求
```py
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get("http://httpbin.org/get", params=payload)


>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
```

## POST发送数据,参数的data或者json

data发送的时候

:param data: (optional) Dictionary or list of tuples ``[(key, value)]`` (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
:param json: (optional) json data to send in the body of the :class:`Request`.

- 响应状态 `r.status_code`
- 响应内容 `r.text`
- 响应头 `r.headers`
- 请求地址 `r.url`

返回内容

- r.text
- r.json()
- r.raw


请求头

```py
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)
```

## Custom Headers

```py
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)
```

## post application/json
For example, the GitHub API v3 accepts JSON-Encoded POST/PATCH data:

```py
>>> import json

>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, data=json.dumps(payload))
```

Instead of encoding the dict yourself, you can also pass it directly using the json parameter (added in version 2.4.2) and it will be encoded automatically:

```py
>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, json=payload)
```

Note, the json parameter is ignored if either data or files is passed.

Using the json parameter in the request will change the Content-Type in the header to application/json.

## sessoin

```py
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'
```

```py
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
```
