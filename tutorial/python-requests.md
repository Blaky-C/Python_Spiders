
# Requests

### 实例引入

```python
import requests

response = requests.get('https://www.baidu.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
```

    <class 'requests.models.Response'>
    200
    <class 'str'>
    <!DOCTYPE html>
    <!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css><title>ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus=autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=ç¾åº¦ä¸ä¸ class="bg s_btn" autofocus></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>æ°é»</a> <a href=https://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>å°å¾</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>è§é¢</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>è´´å§</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>ç»å½</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">ç»å½</a>');
                    </script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">æ´å¤äº§å</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>å³äºç¾åº¦</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>ä½¿ç¨ç¾åº¦åå¿è¯»</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>æè§åé¦</a>&nbsp;äº¬ICPè¯030173å·&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>
    
    <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
    

### 各种请求方式


```python
import requests

requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')
```

---
# 请求

## 基本GET请求

### 基本写法


```python
import requests

response = requests.get('http://httpbin.org/get')
print(response.text)
```

    {
      "args": {}, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.22.0"
      }, 
      "origin": "210.32.145.58, 210.32.145.58", 
      "url": "https://httpbin.org/get"
    }
    
    

### 带参数GET请求


```python
import requests

response = requests.get('http://httpbin.org/get?name=germey&age=22')
print(response.text)
```

    {
      "args": {
        "age": "22", 
        "name": "germey"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.22.0"
      }, 
      "origin": "210.32.145.58, 210.32.145.58", 
      "url": "https://httpbin.org/get?name=germey&age=22"
    }
    
    


```python
import requests

data = {
    'name': 'germey',
    'age': 22
}

response = requests.get('http://httpbin.org/get', params=data)
print(response.text)
```

    {
      "args": {
        "age": "22", 
        "name": "germey"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.22.0"
      }, 
      "origin": "210.32.145.58, 210.32.145.58", 
      "url": "https://httpbin.org/get?name=germey&age=22"
    }
    
    

### 解析json


```python
import requests
import json

response = requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
```

    <class 'str'>
    {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0'}, 'origin': '210.32.145.58, 210.32.145.58', 'url': 'https://httpbin.org/get'}
    {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0'}, 'origin': '210.32.145.58, 210.32.145.58', 'url': 'https://httpbin.org/get'}
    <class 'dict'>
    

### 获得二进制数据


```python
import requests

response = requests.get('https://github.com/favicon.ico')
print(type(response.text), type(response.content))
print(response.content)
print(response.text)
```

    <class 'str'> <class 'bytes'>
    b'\x00\x00\x01\x00\x02\x00\x10\x10\x00\x00\x01\x00 \x00(\x05\x00\x00&\x00\x00\x00  \x00\x00\x01\x00 \x00(\x14\x00\x00N\x05\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00 \x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x11\x13v\x13\x13\x13\xc5\x0e\x0e\x0e\x12\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x11\x11\x11\x14\xb1\x13\x13\x13i\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x14\x14\x96\x13\x13\x14\xfc\x13\x13\x14\xed\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x15\x15\x17\xff\x15\x15\x17\xff\x11\x11\x13\x85\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x11\x12\xc1\x13\x13\x14\xee\x11\x11\x11\x1e\x10\x10\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x13\x13\x14\xf5\x15\x15\x17\xff\x15\x15\x17\xff\x11\x11\x14\xaf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x14\x14\x99\x15\x15\x17\xff\x06\x06\x11,\x0e\x0e\x0e\\\x0f\x0f\x0f\xc1\x0f\x0f\x0f"\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f4\x10\x10\x10\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x14\x14\x14\x8f\x00\x00\x00\x00\x10\x10\x100\x0f\r\x0f\xff\x00\x00\x00\xf9\x01\x01\x01\xed\x02\x02\x02\xff\x02\x02\x02\xf6\x0e\x0e\x0e8\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x08@\x02\x02\x02\xeb\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x11\x11\x11-\x14\x14\x15\x9c\x14\x14\x15\xff\x01\x01\x01\xfc\x0f\x0f\x11\xfb\r\r\x11;\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\r\x12:\x13\x13\x14\xe7\x15\x15\x17\xff\x15\x15\x17\xff\x12\x12\x12\x9a\x13\x13\x13\xd9\x15\x15\x17\xff\x15\x15\x17\xff\x13\x13\x13O\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x11\x11L\x15\x15\x17\xff\x15\x15\x17\xff\x13\x13\x13\xda\x13\x13\x14\xf6\x15\x15\x17\xff\x14\x14\x14\xf0\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x13\x13\x14\xf1\x15\x15\x17\xff\x13\x13\x14\xf6\x13\x13\x14\xf7\x15\x15\x17\xff\x14\x14\x14\xe1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x14\x14\xe1\x15\x15\x17\xff\x13\x13\x14\xf7\x14\x14\x14\xde\x15\x15\x17\xff\x13\x13\x14\xf9\x0f\x0f\x0f!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x10\x10\x1f\x13\x13\x14\xf8\x15\x15\x17\xff\x14\x14\x14\xde\x11\x11\x14\xa2\x15\x15\x17\xff\x15\x15\x17\xff\x0f\x0f\x0f4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x10\x10@\x15\x15\x17\xff\x15\x15\x17\xff\x11\x11\x14\xa2\x0e\x0e\x0e8\x15\x15\x17\xff\x15\x15\x17\xff\x12\x12\x12\x98\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x01\x00\x00\x00\x00\x12\x12\x12\x98\x15\x15\x17\xff\x15\x15\x17\xff\x0e\x0e\x0e8\x00\x00\x00\x00\x11\x11\x14\xa4\x15\x15\x17\xff\x11\x11\x12\xc1\x0e\x0e\x0e6\x00\x00\x00\x81\r\r\r\xdc\x12\x12\x14\xd8\x12\x12\x14\xd8\x13\x13\x14\xf7\x00\x00\x00t\x05\x05\x057\x11\x11\x12\xc1\x15\x15\x17\xff\x11\x11\x14\xa4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x13\x13\x13\xc6\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x13\x13\x13\xc6\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x11\x11\x14\xa2\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x11\x11\x14\xa2\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x10\x10>\x13\x13\x13\x97\x13\x13\x13\xd9\x12\x12\x14\xf2\x12\x12\x14\xf2\x13\x13\x13\xd9\x13\x13\x13\x97\x10\x10\x10>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00 \x00\x00\x00@\x00\x00\x00\x01\x00 \x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15+\x0c\x1e\x1e\x1e\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x1b\x1b\x1c$$$\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x1d#\x17\x17\x18\x92\x15\x15\x17\xf1\x16\x16\x17\xf3@@@\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x18\xed\x16\x16\x17\xf3\x16\x16\x18\x95\x1c\x1c\x1c%\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$$$\x07\x16\x16\x18\x80\x16\x16\x18\xf8\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff   \x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15\x17\xfe\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xf9\x16\x16\x18\x82   \x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x1b\x1b\x1c\x16\x16\x17\xd0\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff+++\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15\x17\xfd\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x17\xd2\x1a\x1a\x1a\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x1b/\x15\x15\x17\xe6\x15\x15\x17\xff\x15\x15\x17\xfc\x16\x16\x18\xb8\x16\x16\x18t\x16\x16\x19g\x16\x16\x18~UUU\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15\x17\xfc\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xe6\x16\x16\x1b/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x1a\x1a\x1d\x15\x15\x17\xe6\x15\x15\x17\xff\x15\x15\x17\xfc\x18\x18\x18I\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15\x17\xfb\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xe6\x1a\x1a\x1a\x1d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$$$\x07\x16\x16\x17\xd1\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x18\x9d\x00\x00\x00\x00\x15\x15 \x18\x16\x16\x18s\x15\x15\x17\x90\x17\x17\x19f$$$\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c\x1c\x12\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x17\xd1$$$\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x18\x81\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xf1\x1b\x1b\x1b\x1c\x1c\x1c\x1c%\x16\x16\x18\xeb\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x17\x17\x1aN\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x18\x18@\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15\x1c$\x16\x16\x18\xf9\x15\x15\x17\xff\x15\x15\x18\xee\x16\x16\x1aE\x15\x15+\x0c\x16\x16\x17\xcf\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x17\xc4\x80\x80\x80\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15\x18\xbf\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xf8\x16\x16\x1d#\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x18\x94\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x17\x8e\x17\x17\x1aZ\x16\x16\x17\xd1\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x18\xe2\x16\x16\x18\x80\x16\x16\x1aE\x1c\x1c\x1c\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"""\x0f\x17\x17\x17B\x17\x17\x19{\x16\x16\x17\xdb\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x17\x17\x18\x93\x00\x00\x00\x00\'\'\'\r\x15\x15\x17\xf2\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xfe\x16\x16\x18\x82333\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x02\x16\x16\x18t\x15\x15\x17\xfc\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xf2\x15\x15+\x0c\x16\x16\x19R\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15\x18`\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x19R\x15\x15\x19\x91\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x18\xca\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x18\xb7\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x19\x91\x16\x16\x18\xc9\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x19\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x19G\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xc8\x16\x16\x18\xe1\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x17\x17\x17\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00   \x08\x16\x16\x18\xf8\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xe0\x16\x16\x18\xf5\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xf2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x18\xde\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xf5\x16\x16\x17\xf3\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xde\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15\x18\xca\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x17\xf3\x15\x15\x18\xd9\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xf4\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x18\xe1\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x18\xd9\x15\x15\x18\xbf\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x1c\x1c\x1c%\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00   \x10\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x18\xbf\x16\x16\x18\x95\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18v\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15\x18a\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\x95\x16\x16\x19G\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xf4\x19\x19\x19\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x1b\x1b\x13\x16\x16\x18\xeb\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x19G+++\x06\x15\x15\x17\xf1\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x19]\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x18\x18I\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xf1+++\x06\x00\x00\x00\x00\x16\x16\x18\x97\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x19\x19\x193\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x1a\x1a\x1e\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\x97\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15 \x18\x16\x16\x18\xf4\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x18\x18\x185\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15+\x0c\x18\x18\x18*\x80\x80\x80\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x01\x1b\x1b\x1b&\x1e\x1e\x1e\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x17\x17!\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xf4\x15\x15 \x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x18\x82\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x17\x17\x19f\x00\x00\x00\x00@@@\x04\x17\x17\x17b\x16\x16\x17\xe7\x15\x15\x17\xff\x16\x16\x17\xf3\x16\x16\x17\xd2\x15\x15\x18\xc1\x15\x15\x18\xc0\x16\x16\x17\xd1\x15\x15\x17\xf0\x15\x15\x17\xff\x16\x16\x18\xed\x15\x15\x18l+++\x06\x00\x00\x00\x00\x16\x16\x19R\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\x82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$$$\x07\x16\x16\x18\xc8\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x18\xd6\x15\x15\x18\xa8\x16\x16\x18\xec\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xef\x15\x15\x18\xaa\x15\x15\x18\xcd\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xc8$$$\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15 \x18\x15\x15\x18\xe3\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x18\xe3\x15\x15 \x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x16\x1c.\x15\x15\x18\xe3\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x18\xe3\x16\x16\x1c.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15 \x18\x16\x16\x18\xc8\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xc8\x15\x15 \x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$$$\x07\x16\x16\x18\x82\x16\x16\x18\xf4\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x16\x16\x18\xf4\x16\x16\x18\x82$$$\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x15 \x18\x16\x16\x18\x97\x15\x15\x17\xf1\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xff\x15\x15\x17\xf1\x16\x16\x18\x97\x15\x15 \x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00+++\x06\x16\x16\x19G\x16\x16\x18\x95\x15\x15\x18\xbf\x15\x15\x18\xd9\x16\x16\x17\xf3\x16\x16\x17\xf3\x15\x15\x18\xd9\x15\x15\x18\xbf\x16\x16\x18\x95\x16\x16\x19G+++\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    :�������OL������������������!������4@���8���
    ��������333���t�������+R������t`������R�����������������������\G������������   ���������������������������������������������������%   ������������va������G������������G+++������]I������+++������3������ �����5+*������&!����� �����f@@@b����������l+++R�����$$$��������������������������$$$ ������������������������ .����������������������. �������������������� $$$������������������$$$ �������������� +++G��������G+++
    


```python
import requests

response = requests.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(response.content)
    f.close()
```

### 添加headers


```python
import requests

response = requests.get('https://www.zhihu.com/explore')
print(response.text)
```

    <html>
    <head><title>400 Bad Request</title></head>
    <body bgcolor="white">
    <center><h1>400 Bad Request</h1></center>
    <hr><center>openresty</center>
    </body>
    </html>
    
    


```python
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
response = requests.get('https://www.zhihu.com/explore', headers = headers)
print(response.text)
```

    <!doctype html>
    <html lang="zh" data-hairline="true" data-theme="light"><head><meta charSet="utf-8"/><title data-react-helmet="true">发现 - 知乎</title><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1"/><meta name="renderer" content="webkit"/><meta name="force-rendering" content="webkit"/><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/><meta name="google-site-verification" content="FTeR0c8arOPKh8c5DYh_9uu98_zJbaWw53J-Sch9MTg"/><meta name="description" property="og:description" content="有问题，上知乎。知乎，可信赖的问答社区，以让每个人高效获得可信赖的解答为使命。知乎凭借认真、专业和友善的社区氛围，结构化、易获得的优质内容，基于问答的内容生产方式和独特的社区机制，吸引、聚集了各行各业中大量的亲历者、内行人、领域专家、领域爱好者，将高质量的内容透过人的节点来成规模地生产和分享。用户通过问答等交流方式建立信任和连接，打造和提升个人影响力，并发现、获得新机会。"/><link data-react-helmet="true" rel="apple-touch-icon" href="https://static.zhihu.com/heifetz/assets/apple-touch-icon-152.67c7b278.png"/><link data-react-helmet="true" rel="apple-touch-icon" href="https://static.zhihu.com/heifetz/assets/apple-touch-icon-152.67c7b278.png" sizes="152x152"/><link data-react-helmet="true" rel="apple-touch-icon" href="https://static.zhihu.com/heifetz/assets/apple-touch-icon-120.b3e6278d.png" sizes="120x120"/><link data-react-helmet="true" rel="apple-touch-icon" href="https://static.zhihu.com/heifetz/assets/apple-touch-icon-76.7a750095.png" sizes="76x76"/><link data-react-helmet="true" rel="apple-touch-icon" href="https://static.zhihu.com/heifetz/assets/apple-touch-icon-60.a4a761d4.png" sizes="60x60"/><link rel="shortcut icon" type="image/x-icon" href="https://static.zhihu.com/static/favicon.ico"/><link rel="search" type="application/opensearchdescription+xml" href="https://static.zhihu.com/static/search.xml" title="知乎"/><link rel="dns-prefetch" href="//static.zhimg.com"/><link rel="dns-prefetch" href="//pic1.zhimg.com"/><link rel="dns-prefetch" href="//pic2.zhimg.com"/><link rel="dns-prefetch" href="//pic3.zhimg.com"/><link rel="dns-prefetch" href="//pic4.zhimg.com"/><style>
    .u-safeAreaInset-top {
      height: constant(safe-area-inset-top) !important;
      height: env(safe-area-inset-top) !important;
      
    }
    .u-safeAreaInset-bottom {
      height: constant(safe-area-inset-bottom) !important;
      height: env(safe-area-inset-bottom) !important;
      
    }
    </style><link href="https://static.zhihu.com/heifetz/app.a22669dfd7d242a5985f.css" rel="stylesheet"/><link href="https://static.zhihu.com/heifetz/explore-routes.40a0e3bdf731f044d393.css" rel="stylesheet"/><script defer="" crossorigin="anonymous" src="https://unpkg.zhimg.com/@cfe/sentry-script@latest/dist/init.js" data-sentry-config="{&quot;dsn&quot;:&quot;https://65e244586890460588f00f2987137aa8@crash2.zhihu.com/193&quot;,&quot;sampleRate&quot;:0.1,&quot;release&quot;:&quot;2345-4dd5661d&quot;,&quot;ignoreErrorNames&quot;:[&quot;NetworkError&quot;,&quot;SecurityError&quot;],&quot;ignoreErrors&quot;:[&quot;origin message&quot;,&quot;Network request failed&quot;,&quot;Loading chunk&quot;,&quot;这个系统不支持该功能。&quot;,&quot;Can&#x27;t find variable: webkit&quot;,&quot;Can&#x27;t find variable: $&quot;,&quot;内存不足&quot;,&quot;out of memory&quot;,&quot;DOM Exception 18&quot;,&quot;The operation is insecure&quot;,&quot;[object Event]&quot;,&quot;[object FileError]&quot;,&quot;[object DOMError]&quot;,&quot;[object Object]&quot;,&quot;拒绝访问。&quot;,&quot;Maximum call stack size exceeded&quot;,&quot;UploadError&quot;,&quot;无法 fetch&quot;,&quot;draft-js&quot;,&quot;缺少 JavaScript 对象&quot;,&quot;componentWillEnter&quot;,&quot;componentWillLeave&quot;,&quot;componentWillAppear&quot;,&quot;getInlineStyleAt&quot;,&quot;getCharacterList&quot;],&quot;whitelistUrls&quot;:[&quot;static.zhihu.com&quot;]}"></script></head><body class="Entry-body"><div id="root"><div><div class="LoadingBar"></div><div><header role="banner" class="Sticky AppHeader" data-za-module="TopNavBar"><div class="AppHeader-inner"><a href="//www.zhihu.com" aria-label="知乎"><svg viewBox="0 0 200 91" class="Icon ZhihuLogo ZhihuLogo--blue Icon--logo" style="height:30px;width:64px" width="64" height="30" aria-hidden="true"><title></title><g><path d="M53.29 80.035l7.32.002 2.41 8.24 13.128-8.24h15.477v-67.98H53.29v67.978zm7.79-60.598h22.756v53.22h-8.73l-8.718 5.473-1.587-5.46-3.72-.012v-53.22zM46.818 43.162h-16.35c.545-8.467.687-16.12.687-22.955h15.987s.615-7.05-2.68-6.97H16.807c1.09-4.1 2.46-8.332 4.1-12.708 0 0-7.523 0-10.085 6.74-1.06 2.78-4.128 13.48-9.592 24.41 1.84-.2 7.927-.37 11.512-6.94.66-1.84.785-2.08 1.605-4.54h9.02c0 3.28-.374 20.9-.526 22.95H6.51c-3.67 0-4.863 7.38-4.863 7.38H22.14C20.765 66.11 13.385 79.24 0 89.62c6.403 1.828 12.784-.29 15.937-3.094 0 0 7.182-6.53 11.12-21.64L43.92 85.18s2.473-8.402-.388-12.496c-2.37-2.788-8.768-10.33-11.496-13.064l-4.57 3.627c1.363-4.368 2.183-8.61 2.46-12.71H49.19s-.027-7.38-2.372-7.38zm128.752-.502c6.51-8.013 14.054-18.302 14.054-18.302s-5.827-4.625-8.556-1.27c-1.874 2.548-11.51 15.063-11.51 15.063l6.012 4.51zm-46.903-18.462c-2.814-2.577-8.096.667-8.096.667s12.35 17.2 12.85 17.953l6.08-4.29s-8.02-11.752-10.83-14.33zM199.99 46.5c-6.18 0-40.908.292-40.953.292v-31.56c1.503 0 3.882-.124 7.14-.376 12.773-.753 21.914-1.25 27.427-1.504 0 0 3.817-8.496-.185-10.45-.96-.37-7.24 1.43-7.24 1.43s-51.63 5.153-72.61 5.64c.5 2.756 2.38 5.336 4.93 6.11 4.16 1.087 7.09.53 15.36.277 7.76-.5 13.65-.76 17.66-.76v31.19h-41.71s.88 6.97 7.97 7.14h33.73v22.16c0 4.364-3.498 6.87-7.65 6.6-4.4.034-8.15-.36-13.027-.566.623 1.24 1.977 4.496 6.035 6.824 3.087 1.502 5.054 2.053 8.13 2.053 9.237 0 14.27-5.4 14.027-14.16V53.93h38.235c3.026 0 2.72-7.432 2.72-7.432z" fill-rule="evenodd"/></g></svg></a><ul role="navigation" class="Tabs AppHeader-Tabs"><li role="tab" class="Tabs-item AppHeader-Tab Tabs-item--noMeta"><a class="Tabs-link AppHeader-TabsLink" href="//www.zhihu.com/" data-za-not-track-link="true">首页</a></li><li role="tab" class="Tabs-item AppHeader-Tab Tabs-item--noMeta"><a class="Tabs-link AppHeader-TabsLink is-active" href="//www.zhihu.com/explore" data-za-not-track-link="true">发现</a></li><li role="tab" class="Tabs-item AppHeader-Tab Tabs-item--noMeta"><a class="Tabs-link AppHeader-TabsLink" href="//www.zhihu.com/question/waiting" data-za-not-track-link="true">等你来答</a></li></ul><div class="SearchBar" role="search" data-za-module="PresetWordItem"><div class="SearchBar-toolWrapper"><form class="SearchBar-tool"><div><div class="Popover"><div class="SearchBar-input Input-wrapper Input-wrapper--grey"><input type="text" maxLength="100" value="" autoComplete="off" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-activedescendant="null--1" id="null-toggle" aria-haspopup="true" aria-owns="null-content" class="Input" placeholder=""/><div class="Input-after"><button aria-label="搜索" type="button" class="Button SearchBar-searchIcon Button--primary"><span style="display:inline-flex;align-items:center">​<svg class="Zi Zi--Search" fill="currentColor" viewBox="0 0 24 24" width="18" height="18"><path d="M17.068 15.58a8.377 8.377 0 0 0 1.774-5.159 8.421 8.421 0 1 0-8.42 8.421 8.38 8.38 0 0 0 5.158-1.774l3.879 3.88c.957.573 2.131-.464 1.488-1.49l-3.879-3.878zm-6.647 1.157a6.323 6.323 0 0 1-6.316-6.316 6.323 6.323 0 0 1 6.316-6.316 6.323 6.323 0 0 1 6.316 6.316 6.323 6.323 0 0 1-6.316 6.316z" fill-rule="evenodd"></path></svg></span></button></div></div></div></div></form></div></div><div class="AppHeader-userInfo"><div class="AppHeader-profile"><div><button type="button" class="Button AppHeader-login Button--blue">登录</button><button type="button" class="Button Button--primary Button--blue">加入知乎</button></div></div></div></div><div></div></header></div><main role="main" class="App-main"><div><div class="Sticky"></div></div><div class="ExploreHomePage"><div class="ExploreHomePage-ContentSection ExploreHomePage-section" id="special"><div class="ExploreHomePage-ContentSection-header"><svg class="Zi Zi--LabelSpecial" fill="currentColor" viewBox="0 0 24 24" width="36" height="36"><path d="M7.667 3.667h11.466a1.2 1.2 0 0 1 1.2 1.2v13.066a2.4 2.4 0 0 1-2.4 2.4H6.467V4.867a1.2 1.2 0 0 1 1.2-1.2zM4.2 9.619h1.689v10.714H5.4a2.4 2.4 0 0 1-2.4-2.4V10.82a1.2 1.2 0 0 1 1.2-1.2zm5.178-2.38a.6.6 0 0 0-.6.6v.585a.6.6 0 0 0 .6.6h8.044a.6.6 0 0 0 .6-.6v-.586a.6.6 0 0 0-.6-.6H9.378zm0 3.57a.6.6 0 0 0-.6.6v.586a.6.6 0 0 0 .6.6h8.044a.6.6 0 0 0 .6-.6v-.585a.6.6 0 0 0-.6-.6H9.378zm0 3.572a.6.6 0 0 0-.6.6v.586a.6.6 0 0 0 .6.6h4.578a.6.6 0 0 0 .6-.6v-.586a.6.6 0 0 0-.6-.6H9.378z" fill-rule="evenodd"></path></svg><span>最新专题</span></div><div class="ExploreHomePage-ContentSection-body"><div class="ExploreHomePage-specials"><div class="ExploreSpecialCard ExploreHomePage-specialCard"><a class="ExploreSpecialCard-banner" href="/special/19560438" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5792"><img src="https://pic3.zhimg.com/50/v2-0999111303457fb6e0a0503873700f72_hd.jpg"/></a><div class="ExploreSpecialCard-header"><div class="ExploreSpecialCard-info"><a class="ExploreSpecialCard-title" href="/special/19560438" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5792">夏日将尽，二刷走起</a><div class="ExploreSpecialCard-count"><span>1 天前<!-- -->更新</span><span>3,287,939<!-- --> 浏览</span></div></div><div class="ExploreSpecialCard-followButton"><button class="ExploreFollowButton">关注专题</button></div></div><div class="ExploreSpecialCard-contentList"><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19560438#NewsSpecial-SubModule-1150456401133383680" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">夏日爆款</a><a class="ExploreSpecialCard-contentTitle" href="/question/333300489" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">影视综全集 | 又一个暑假过去了，你错过了啥？</a></div><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19560438#NewsSpecial-SubModule-1150457329399959552" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">热映国片</a><a class="ExploreSpecialCard-contentTitle" href="/answer/754343925" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">哪吒 | 我命由我，不由天！</a></div><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19560438#NewsSpecial-SubModule-1150458272401281024" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">海外佳片</a><a class="ExploreSpecialCard-contentTitle" href="/answer/792589563" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794"> 骡子 | 两种价值观的拉扯</a></div></div></div><div class="ExploreSpecialCard ExploreHomePage-specialCard"><a class="ExploreSpecialCard-banner" href="/special/19605346" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5792"><img src="https://pic2.zhimg.com/50/v2-394d7e36df41d99a5e9f94398cff138d_hd.jpg"/></a><div class="ExploreSpecialCard-header"><div class="ExploreSpecialCard-info"><a class="ExploreSpecialCard-title" href="/special/19605346" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5792">聚焦 LPL 季后赛，「3G 时代」要终结了吗？</a><div class="ExploreSpecialCard-count"><span>1 天前<!-- -->更新</span><span>1,515,139<!-- --> 浏览</span></div></div><div class="ExploreSpecialCard-followButton"><button class="ExploreFollowButton">关注专题</button></div></div><div class="ExploreSpecialCard-contentList"><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19605346#NewsSpecial-SubModule-1150460288724742144" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">EDG 建队首次无缘季后赛</a><a class="ExploreSpecialCard-contentTitle" href="/answer/801489100" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">EDG 建队首次无缘世界赛</a></div><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19605346#NewsSpecial-SubModule-1150460491200720896" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">iG 能否出线仅剩冒泡赛机会</a><a class="ExploreSpecialCard-contentTitle" href="/answer/800016020" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">iG 冠军教练的「遗产」消耗殆尽了</a></div><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19605346#NewsSpecial-SubModule-1150460604530626560" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">RNG 的「生死战」</a><a class="ExploreSpecialCard-contentTitle" href="/answer/802338479" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">距离世界赛更近，但却无法让人放心</a></div></div></div><div class="ExploreSpecialCard ExploreHomePage-specialCard"><a class="ExploreSpecialCard-banner" href="/special/19638453" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5792"><img src="https://pic4.zhimg.com/50/v2-cb51d035dc3ffb20bd6ffc16034186f7_hd.jpg"/></a><div class="ExploreSpecialCard-header"><div class="ExploreSpecialCard-info"><a class="ExploreSpecialCard-title" href="/special/19638453" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5792">Ti9 折戟沉沙，CN DOTA 出了什么问题？</a><div class="ExploreSpecialCard-count"><span>2 天前<!-- -->更新</span><span>2,693,780<!-- --> 浏览</span></div></div><div class="ExploreSpecialCard-followButton"><button class="ExploreFollowButton">关注专题</button></div></div><div class="ExploreSpecialCard-contentList"><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19638453#NewsSpecial-SubModule-1149746248029483008" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">Ti9 赛事回顾</a><a class="ExploreSpecialCard-contentTitle" href="/question/342463513" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">Ti9「全村最后的希望」跌落败者组</a></div><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19638453#NewsSpecial-SubModule-1149746584882376704" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">三年无冠，CN DOTA 怎么了？</a><a class="ExploreSpecialCard-contentTitle" href="/answer/793474632" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">不复当年</a></div><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/19638453#NewsSpecial-SubModule-1149747914640441344" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">人们为什么怀念 Wings？</a><a class="ExploreSpecialCard-contentTitle" href="/answer/648090914" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">最「传奇」的战队</a></div></div></div><div class="ExploreSpecialCard ExploreHomePage-specialCard"><a class="ExploreSpecialCard-banner" href="/special/20011001" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5792"><img src="https://pic4.zhimg.com/50/v2-ce8c59b61f71b2a5c9324946bda00dc3_hd.jpg"/></a><div class="ExploreSpecialCard-header"><div class="ExploreSpecialCard-info"><a class="ExploreSpecialCard-title" href="/special/20011001" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5792">知新车 · 2019 汽车下半局</a><div class="ExploreSpecialCard-count"><span>22 小时前<!-- -->更新</span><span>3,545,365<!-- --> 浏览</span></div></div><div class="ExploreSpecialCard-followButton"><button class="ExploreFollowButton">关注专题</button></div></div><div class="ExploreSpecialCard-contentList"><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/20011001#NewsSpecial-SubModule-1150450968071110656" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">新车之惑</a><a class="ExploreSpecialCard-contentTitle" href="/question/337599789" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">2019 成都车展有哪些值得关注的新车？</a></div><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/20011001#NewsSpecial-SubModule-1150451002414002176" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">经济之选</a><a class="ExploreSpecialCard-contentTitle" href="/question/338797096" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">丰田 · 第 12 代卡罗拉</a></div><div class="ExploreSpecialCard-contentItem"><a class="ExploreSpecialCard-contentTag" href="/special/20011001#NewsSpecial-SubModule-1150451038237728768" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5793">德系豪华</a><a class="ExploreSpecialCard-contentTitle" href="/question/330701118" target="blank" rel="noopener noreferrer" data-za-detail-view-id="5794">宝马 · 全新 3 系 G20/G28</a></div></div></div></div></div><div class="ExploreHomePage-ContentSection-moreButton"><a href="/special/all" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5796">查看更多专题<svg class="Zi Zi--ArrowRight" fill="currentColor" viewBox="0 0 24 24" width="25" height="25"><path d="M9.218 16.78a.737.737 0 0 0 1.052 0l4.512-4.249a.758.758 0 0 0 0-1.063L10.27 7.22a.737.737 0 0 0-1.052 0 .759.759 0 0 0-.001 1.063L13 12l-3.782 3.716a.758.758 0 0 0 0 1.063z" fill-rule="evenodd"></path></svg></a></div></div><div class="ExploreHomePage-ContentSection ExploreHomePage-section" id="roundtable"><div class="ExploreHomePage-ContentSection-header"><svg class="Zi Zi--LabelRoundtable" fill="currentColor" viewBox="0 0 24 24" width="36" height="36"><path d="M12 21.333a9.333 9.333 0 1 1 0-18.666 9.333 9.333 0 0 1 0 18.666zm-.66-11.287c.332.385.609.77.775 1.21.055-.054.665-.99.72-1.706.055-.385.126-1.616-.443-2.367-.443-.496-1.219-.77-1.884-.55a1.788 1.788 0 0 0-1.33 2.036c.887.276 1.607.771 2.161 1.377zm-1.33 1.541c.443-.055.941-.11 1.44 0 0-.055-.484-.936-1.108-1.486-.665-.496-1.33-.973-2.216-.771-.72.11-1.723.77-1.55 2.092.11.606.553 1.101 1.162 1.321.61-.605 1.44-1.046 2.272-1.156zm2.714.165c.056 0 1.164.055 1.828-.165.72-.275 1.412-.68 1.773-1.541.11-.276.23-1.248-.443-1.872-.72-.716-1.717-.716-2.438-.165.222.825.063 1.966-.11 2.532-.103.348-.333.88-.61 1.211zm-1.44.55c-.056 0-1.33.056-1.828.221-.72.275-1.447.668-1.773 1.541-.11.276-.21 1.26.443 1.872.665.661 1.718.661 2.438.11-.295-.811-.166-1.761.055-2.477.166-.495.388-.936.665-1.266zm5.041-.99c-.665.605-1.44.99-2.327 1.211-.443.055-.941.11-1.44 0 0 .055.554.991 1.108 1.431.665.496 1.385.771 2.216.771.72-.11 1.678-.692 1.551-2.092-.055-.605-.554-1.101-1.108-1.321zm-3.656 2.642a3.475 3.475 0 0 1-.776-1.156c-.055.055-.665.991-.72 1.707-.055.385-.101 1.506.499 2.312.443.496 1.218.77 1.883.55.887-.275 1.496-1.1 1.33-2.036a5.38 5.38 0 0 1-2.216-1.377z" fill-rule="evenodd"></path></svg><span>圆桌讨论</span></div><div class="ExploreHomePage-ContentSection-body"><div class="ExploreHomePage-roundtables"><div class="ExploreRoundtableCard ExploreHomePage-roundtableCard"><div class="ExploreRoundtableCard-headerContainer" style="background-color:#14003D"><div class="ExploreRoundtableCard-headerBackgrounds"><div style="background-image:url(https://pic4.zhimg.com/50/v2-f46dad73ac3a8060062ec5d96934c0de_hd.jpg);background-position:center"></div><div style="background:linear-gradient(to right, rgba(20, 0, 61, 1) 0%, rgba(20, 0, 61, 0) 100%"></div><div style="background:linear-gradient(to right, rgba(20, 0, 61, 0.5) 0%, rgba(20, 0, 61, 0) 100%"></div></div><div class="ExploreRoundtableCard-header"><a class="ExploreRoundtableCard-title" href="/roundtable/basketballworldcup" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5799">男篮世界杯，中国队能否突围？</a><a class="ExploreRoundtableCard-intro" href="/roundtable/basketballworldcup" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5799">2019 年的篮球世界杯将在中国举办，中国队面对「史上最佳分组」，能否在家门口取得好成绩？美国队多名 NBA 球员退赛，梦之队能否捍卫荣誉？塞尔维亚、希腊等豪强并起，篮球世界杯冠军最终会落入谁手？本次圆桌，就让我们一起来围观。
    </a><div class="ExploreRoundtableCard-info"><div class="ExploreRoundtableCard-guests"><img src="https://pic3.zhimg.com/50/v2-c2a7f309662683907f17bcccee7c2454_hd.jpg"/><img src="https://pic3.zhimg.com/50/v2-2c9428ee55620cab25bbbf72dc53a9dd_hd.jpg"/><img src="https://pic2.zhimg.com/50/v2-56b591ecfd7c66676752b9a9f2adc56f_hd.jpg"/><span>10<!-- --> 位嘉宾参与</span></div><div class="ExploreRoundtableCard-count"><span>106<!-- --> 人关注</span></div></div></div><div class="ExploreRoundtableCard-followButton"><button class="ExploreFollowButton ExploreFollowButton--colored" style="color:rgba(20, 0, 61, 1)">关注圆桌</button></div></div><div class="ExploreRoundtableCard-questionList"><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/316195740" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">如何评价 2019 男篮世界杯的抽签分组结果？</a><div class="ExploreRoundtableCard-questionCounts"><span>135<!-- --> 个回答</span></div></div><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/343677646" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">男篮世界杯中国队首战对阵科特迪瓦，有多少胜算？</a><div class="ExploreRoundtableCard-questionCounts"><span>6<!-- --> 个回答</span></div></div><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/336925927" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">国际篮协要怎样做，才能让篮球世界杯跟足球世界杯一样，其地位大于职业联赛?</a><div class="ExploreRoundtableCard-questionCounts"><span>14<!-- --> 个回答</span></div></div></div></div><div class="ExploreRoundtableCard ExploreHomePage-roundtableCard"><div class="ExploreRoundtableCard-headerContainer" style="background-color:#343382"><div class="ExploreRoundtableCard-headerBackgrounds"><div style="background-image:url(https://pic4.zhimg.com/50/v2-1604ae1189fd42f69d6a255551b49e03_hd.jpg);background-position:center"></div><div style="background:linear-gradient(to right, rgba(52, 51, 130, 1) 0%, rgba(52, 51, 130, 0) 100%"></div><div style="background:linear-gradient(to right, rgba(52, 51, 130, 0.5) 0%, rgba(52, 51, 130, 0) 100%"></div></div><div class="ExploreRoundtableCard-header"><a class="ExploreRoundtableCard-title" href="/roundtable/lol8years" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5799">英雄联盟，无限热爱</a><a class="ExploreRoundtableCard-intro" href="/roundtable/lol8years" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5799">英雄联盟与我们相伴八年了，踏峡谷，登云顶，一路走来，大家找到了各自的段位成为了英雄。在召唤师峡谷中，你留下了哪些故事和回忆？今年的夏季总决赛和全球总决赛又会上演怎样的精彩对决？因为无限热爱，才有无限可能。本次圆桌，就让我们一同探寻未来，共话热爱！</a><div class="ExploreRoundtableCard-info"><div class="ExploreRoundtableCard-guests"><img src="https://pic1.zhimg.com/50/v2-7486a4246242f1d69f13bfc3a37655dd_hd.jpg"/><img src="https://pic2.zhimg.com/50/v2-06734a92e6fd35ce9d4df76af0cd1cce_hd.jpg"/><img src="https://pic3.zhimg.com/50/v2-06463e9377c7ff434dd456d396668f14_hd.jpg"/><span>5<!-- --> 位嘉宾参与</span></div><div class="ExploreRoundtableCard-count"><span>40<!-- --> 人关注</span></div></div></div><div class="ExploreRoundtableCard-followButton"><button class="ExploreFollowButton ExploreFollowButton--colored" style="color:rgba(52, 51, 130, 1)">关注圆桌</button></div></div><div class="ExploreRoundtableCard-questionList"><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/340349232" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">《英雄联盟》有哪些实用的翻盘技巧（经验）？</a><div class="ExploreRoundtableCard-questionCounts"><span>35<!-- --> 个回答</span></div></div><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/329620324" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">如果穿越到《英雄联盟》，你要怎么活下去，并成为一名英雄？</a><div class="ExploreRoundtableCard-questionCounts"><span>291<!-- --> 个回答</span></div></div><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/328805878" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">《英雄联盟》里，谁能最快清完100个聚集在一起的小兵？</a><div class="ExploreRoundtableCard-questionCounts"><span>158<!-- --> 个回答</span></div></div></div></div><div class="ExploreRoundtableCard ExploreHomePage-roundtableCard"><div class="ExploreRoundtableCard-headerContainer" style="background-color:#91aed6"><div class="ExploreRoundtableCard-headerBackgrounds"><div style="background-image:url(https://pic2.zhimg.com/50/v2-d28e4712150515bcfd9780c171177437_hd.jpg);background-position:center"></div><div style="background:linear-gradient(to right, rgba(145, 174, 214, 1) 0%, rgba(145, 174, 214, 0) 100%"></div><div style="background:linear-gradient(to right, rgba(145, 174, 214, 0.5) 0%, rgba(145, 174, 214, 0) 100%"></div></div><div class="ExploreRoundtableCard-header"><a class="ExploreRoundtableCard-title" href="/roundtable/xiaoyuanxinshengjinj" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5799">校园新生进阶之道</a><a class="ExploreRoundtableCard-intro" href="/roundtable/xiaoyuanxinshengjinj" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5799">对不少离家求学的学子们来说，陌生的人、陌生的环境最让人感到不安。该如果与新同学沟通？该怎么规划学习目标？该怎么融入校园生活？遇到困难该如何靠自己化解？本期圆桌，我们邀请了心理界、法律界、人事界及社工界多位大咖，运用各行各业的知识与技巧，帮你缓解焦虑，融入校园新生活。</a><div class="ExploreRoundtableCard-info"><div class="ExploreRoundtableCard-guests"><img src="https://pic3.zhimg.com/50/df4318a7d28d27d3b27c0ab320fa203a_hd.jpg"/><img src="https://pic3.zhimg.com/50/b28a4217a763ea990563f33fb40a5ce9_hd.jpg"/><img src="https://pic2.zhimg.com/50/v2-474464c34921bb480f933b36361133c1_hd.jpg"/><span>10<!-- --> 位嘉宾参与</span></div><div class="ExploreRoundtableCard-count"><span>104<!-- --> 人关注</span></div></div></div><div class="ExploreRoundtableCard-followButton"><button class="ExploreFollowButton ExploreFollowButton--colored" style="color:rgba(145, 174, 214, 1)">关注圆桌</button></div></div><div class="ExploreRoundtableCard-questionList"><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/265597918" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">如何有效地劝刚上大学的儿子远离校园贷？</a><div class="ExploreRoundtableCard-questionCounts"><span>716<!-- --> 个回答</span></div></div><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/20052781" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">内向、不善社交的人如何建立人脉？</a><div class="ExploreRoundtableCard-questionCounts"><span>663<!-- --> 个回答</span></div></div><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/27177500" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">大一学生很迷茫，觉得人生浑浑噩噩的，怎么调整状态?</a><div class="ExploreRoundtableCard-questionCounts"><span>108<!-- --> 个回答</span></div></div></div></div><div class="ExploreRoundtableCard ExploreHomePage-roundtableCard"><div class="ExploreRoundtableCard-headerContainer" style="background-color:#203673"><div class="ExploreRoundtableCard-headerBackgrounds"><div style="background-image:url(https://pic1.zhimg.com/50/v2-1c8bcd921173b9ad823ec0efed296bc8_hd.jpg);background-position:center"></div><div style="background:linear-gradient(to right, rgba(32, 54, 115, 1) 0%, rgba(32, 54, 115, 0) 100%"></div><div style="background:linear-gradient(to right, rgba(32, 54, 115, 0.5) 0%, rgba(32, 54, 115, 0) 100%"></div></div><div class="ExploreRoundtableCard-header"><a class="ExploreRoundtableCard-title" href="/roundtable/fushe" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5799">辐射可怕吗 | 非常想问</a><a class="ExploreRoundtableCard-intro" href="/roundtable/fushe" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5799">1901 年，因为对 X 光的发现，威廉·伦琴获得了第一届诺贝尔物理学奖。随后的百年里，辐射被应用到了人类生活的方方面面。然而，时至今日，人们依然会谈「辐」色变。辐射到底是什么？人类对辐射的应用都有哪些？辐射真的可怕吗？本期圆桌，就让我们一起来重新认识辐射。</a><div class="ExploreRoundtableCard-info"><div class="ExploreRoundtableCard-guests"><img src="https://pic4.zhimg.com/50/1eb9b8c7e7ddc53f26db62a3ecd99dd7_hd.jpg"/><img src="https://pic1.zhimg.com/50/v2-76ee781bcc0e2225461419e564c67a88_hd.jpg"/><img src="https://pic3.zhimg.com/50/v2-7af3fdbdf67525f431e69689917b9f61_hd.jpg"/><span>9<!-- --> 位嘉宾参与</span></div><div class="ExploreRoundtableCard-count"><span>1,162<!-- --> 人关注</span></div></div></div><div class="ExploreRoundtableCard-followButton"><button class="ExploreFollowButton ExploreFollowButton--colored" style="color:rgba(32, 54, 115, 1)">关注圆桌</button></div></div><div class="ExploreRoundtableCard-questionList"><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/55352779" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">如何看待福岛核电站二号机组近日被发现压力容器已被烧穿？</a><div class="ExploreRoundtableCard-questionCounts"><span>153<!-- --> 个回答</span></div></div><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/22952334" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">辐照杀菌是安全的吗？</a><div class="ExploreRoundtableCard-questionCounts"><span>4<!-- --> 个回答</span></div></div><div class="ExploreRoundtableCard-questionItem"><a class="ExploreRoundtableCard-questionTitle" href="/question/66256527" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5800">地铁安检机频繁开门瞬间辐射会侧漏吗？</a><div class="ExploreRoundtableCard-questionCounts"><span>10<!-- --> 个回答</span></div></div></div></div></div></div><div class="ExploreHomePage-ContentSection-moreButton"><a href="/roundtable" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5802">查看更多圆桌<svg class="Zi Zi--ArrowRight" fill="currentColor" viewBox="0 0 24 24" width="25" height="25"><path d="M9.218 16.78a.737.737 0 0 0 1.052 0l4.512-4.249a.758.758 0 0 0 0-1.063L10.27 7.22a.737.737 0 0 0-1.052 0 .759.759 0 0 0-.001 1.063L13 12l-3.782 3.716a.758.758 0 0 0 0 1.063z" fill-rule="evenodd"></path></svg></a></div></div><div class="ExploreHomePage-ContentSection ExploreHomePage-section" id="collection"><div class="ExploreHomePage-ContentSection-header"><svg class="Zi Zi--Star" fill="currentColor" viewBox="0 0 24 24" width="36" height="36"><path d="M5.515 19.64l.918-5.355-3.89-3.792c-.926-.902-.639-1.784.64-1.97L8.56 7.74l2.404-4.871c.572-1.16 1.5-1.16 2.072 0L15.44 7.74l5.377.782c1.28.186 1.566 1.068.64 1.97l-3.89 3.793.918 5.354c.219 1.274-.532 1.82-1.676 1.218L12 18.33l-4.808 2.528c-1.145.602-1.896.056-1.677-1.218z" fill-rule="evenodd"></path></svg><span>热门收藏夹</span></div><div class="ExploreHomePage-ContentSection-body"><div class="ExploreHomePage-collections"><div class="ExploreCollectionCard ExploreHomePage-collectionCard"><div class="ExploreCollectionCard-header"><div class="ExploreCollectionCard-info"><a class="ExploreCollectionCard-title" href="/collection/60058588" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5804" data-za-detail-view-name="标题点击">经济，政治，社会热点</a><div class="ExploreCollectionCard-relatedMembers"><div class="ExploreCollectionCard-creator"><span class="UserLink ExploreCollectionCard-creatorAvatar"><div class="Popover"><div id="null-toggle" aria-haspopup="true" aria-expanded="false" aria-owns="null-content"><a class="UserLink-link" data-za-detail-view-element_name="User" target="_blank" data-za-detail-view-id="5806" href="//www.zhihu.com/people/fan-yan-yu-50"><img class="Avatar UserLink-avatar" width="28" height="28" src="https://pic3.zhimg.com/f101169c7db45793bf74a5da3dff174a_is.jpg" srcSet="https://pic3.zhimg.com/f101169c7db45793bf74a5da3dff174a_im.jpg 2x" alt="落雨1994"/></a></div></div></span><a class="ExploreCollectionCard-creatorName" href="/people/fan-yan-yu-50" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5806">落雨1994</a><span class="ExploreCollectionCard-creatorSuffix">创建</span></div><div class="ExploreCollectionCard-followers">509<!-- --> 人关注</div></div></div><div class="ExploreCollectionCard-followButton"><button class="ExploreFollowButton">关注收藏夹</button></div></div><div class="ExploreCollectionCard-contentList"><div class="ExploreCollectionCard-contentItem"><a class="ExploreCollectionCard-contentTitle" href="https://www.zhihu.com/answer/797170522" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5807">为什么当今社会对大龄剩男没有这么苛责?</a><div class="ExploreCollectionCard-contentExcerpt">空白：看到一位兄弟说“宽容NMB”，简直要笑疯。本来准备直接跳过的，突然想吐槽一下男人从来不会喊冤哭悲惨，而你们妹子屁大点事就这啊那的，知道你们妹子是弱势群体了好吧！没钱的大龄剩男都不算人了，自然没有权力说什么。而你们妹子花点钱把自己包装一下就觉…</div><div class="ExploreCollectionCard-contentTags"><span class="ExploreCollectionCard-contentTypeTag">回答</span><span class="ExploreCollectionCard-contentCountTag">2,017 赞同</span><span class="ExploreCollectionCard-contentCountTag">304 评论</span></div></div><div class="ExploreCollectionCard-contentItem"><a class="ExploreCollectionCard-contentTitle" href="https://www.zhihu.com/answer/798313573" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5807">李毅是谁？为什么称李毅吧为帝吧？</a><div class="ExploreCollectionCard-contentExcerpt">唐芊芊：2003年，贴吧成立，其灵感来源于李彦宏一个不成熟的想法：结合搜索引擎建立一个在线兴趣交流平台。靠着这个想法，贴吧日后发展成为了全球最大的中文社区。贴吧上线一年后，足球运动员李毅的个人主题贴吧李毅吧正式建立，李毅当年因自恃“护球像亨利”，而被…</div><div class="ExploreCollectionCard-contentTags"><span class="ExploreCollectionCard-contentTypeTag">回答</span><span class="ExploreCollectionCard-contentCountTag">39,938 赞同</span><span class="ExploreCollectionCard-contentCountTag">1,537 评论</span></div></div></div><a class="ExploreCollectionCard-collectedContentCount" href="/collection/60058588" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5804" data-za-detail-view-name="已收藏点击">已收藏 <!-- -->725<!-- --> 条内容<svg class="Zi Zi--ArrowRight" fill="currentColor" viewBox="0 0 24 24" width="24" height="24"><path d="M9.218 16.78a.737.737 0 0 0 1.052 0l4.512-4.249a.758.758 0 0 0 0-1.063L10.27 7.22a.737.737 0 0 0-1.052 0 .759.759 0 0 0-.001 1.063L13 12l-3.782 3.716a.758.758 0 0 0 0 1.063z" fill-rule="evenodd"></path></svg></a></div><div class="ExploreCollectionCard ExploreHomePage-collectionCard"><div class="ExploreCollectionCard-header"><div class="ExploreCollectionCard-info"><a class="ExploreCollectionCard-title" href="/collection/72037720" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5804" data-za-detail-view-name="标题点击">我的收藏</a><div class="ExploreCollectionCard-relatedMembers"><div class="ExploreCollectionCard-creator"><span class="UserLink ExploreCollectionCard-creatorAvatar"><div class="Popover"><div id="null-toggle" aria-haspopup="true" aria-expanded="false" aria-owns="null-content"><a class="UserLink-link" data-za-detail-view-element_name="User" target="_blank" data-za-detail-view-id="5806" href="//www.zhihu.com/people/mi-gan-79-20"><img class="Avatar UserLink-avatar" width="28" height="28" src="https://pic4.zhimg.com/v2-7d70724f8340e8172fd5b8d3496b9d62_is.jpg" srcSet="https://pic4.zhimg.com/v2-7d70724f8340e8172fd5b8d3496b9d62_im.jpg 2x" alt="曼雪莉公主"/></a></div></div></span><a class="ExploreCollectionCard-creatorName" href="/people/mi-gan-79-20" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5806">曼雪莉公主</a><span class="ExploreCollectionCard-creatorSuffix">创建</span></div><div class="ExploreCollectionCard-followers">43<!-- --> 人关注</div></div></div><div class="ExploreCollectionCard-followButton"><button class="ExploreFollowButton">关注收藏夹</button></div></div><div class="ExploreCollectionCard-contentList"><div class="ExploreCollectionCard-contentItem"><a class="ExploreCollectionCard-contentTitle" href="https://www.zhihu.com/answer/403461471" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5807">你在养宠物的时候是更偏向于养猫还是养狗？</a><div class="ExploreCollectionCard-contentExcerpt">瑞宝：同时在养着。先说猫：从小特别喜欢狗，讨厌猫。工作后因为老公经常讲他小时候，养的猫如何如何聪明，可以叫回来，还会安慰它。就养了一只小猫，才发觉原来猫这么可爱，挑食。整天就是睡觉，岁月静好。还会自己在猫砂盆里，解决大小便。每天清理就好了。长大…</div><div class="ExploreCollectionCard-contentTags"><span class="ExploreCollectionCard-contentTypeTag">回答</span><span class="ExploreCollectionCard-contentCountTag">3 赞同</span><span class="ExploreCollectionCard-contentCountTag">3 评论</span></div></div><div class="ExploreCollectionCard-contentItem"><a class="ExploreCollectionCard-contentTitle" href="https://www.zhihu.com/answer/130736857" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5807">养猫幸福感强 还是 养狗幸福感强？养过的答？</a><div class="ExploreCollectionCard-contentExcerpt">桃夭：养猫的幸福感相当于女神/男神住你家...</div><div class="ExploreCollectionCard-contentTags"><span class="ExploreCollectionCard-contentTypeTag">回答</span><span class="ExploreCollectionCard-contentCountTag">2 赞同</span><span class="ExploreCollectionCard-contentCountTag">1 评论</span></div></div></div><a class="ExploreCollectionCard-collectedContentCount" href="/collection/72037720" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5804" data-za-detail-view-name="已收藏点击">已收藏 <!-- -->504<!-- --> 条内容<svg class="Zi Zi--ArrowRight" fill="currentColor" viewBox="0 0 24 24" width="24" height="24"><path d="M9.218 16.78a.737.737 0 0 0 1.052 0l4.512-4.249a.758.758 0 0 0 0-1.063L10.27 7.22a.737.737 0 0 0-1.052 0 .759.759 0 0 0-.001 1.063L13 12l-3.782 3.716a.758.758 0 0 0 0 1.063z" fill-rule="evenodd"></path></svg></a></div><div class="ExploreCollectionCard ExploreHomePage-collectionCard"><div class="ExploreCollectionCard-header"><div class="ExploreCollectionCard-info"><a class="ExploreCollectionCard-title" href="/collection/95922523" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5804" data-za-detail-view-name="标题点击">节操呢？！木有！你造吗？！</a><div class="ExploreCollectionCard-relatedMembers"><div class="ExploreCollectionCard-creator"><span class="UserLink ExploreCollectionCard-creatorAvatar"><div class="Popover"><div id="null-toggle" aria-haspopup="true" aria-expanded="false" aria-owns="null-content"><a class="UserLink-link" data-za-detail-view-element_name="User" target="_blank" data-za-detail-view-id="5806" href="//www.zhihu.com/people/zhangletao"><img class="Avatar UserLink-avatar" width="28" height="28" src="https://pic1.zhimg.com/7d0b1d40c_is.jpg" srcSet="https://pic1.zhimg.com/7d0b1d40c_im.jpg 2x" alt="张乐陶"/></a></div></div></span><a class="ExploreCollectionCard-creatorName" href="/people/zhangletao" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5806">张乐陶</a><span class="ExploreCollectionCard-creatorSuffix">创建</span></div><div class="ExploreCollectionCard-followers">33<!-- --> 人关注</div></div></div><div class="ExploreCollectionCard-followButton"><button class="ExploreFollowButton">关注收藏夹</button></div></div><div class="ExploreCollectionCard-contentList"><div class="ExploreCollectionCard-contentItem"><a class="ExploreCollectionCard-contentTitle" href="https://www.zhihu.com/answer/809101662" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5807">是什么情况下你才发现你在婆家是个外人的？</a><div class="ExploreCollectionCard-contentExcerpt">爱生气的小河豚：一直都知道自己是个外人啊，毕竟我也不是他们亲生的不是？！举个例子吧，偶尔假期在婆家小住，他们一家三口不论喝水还是刷牙的杯子都是一套，看着很温馨，而我的就是家里闲置的杯子拿来用，很明显地差距是不是？再比如，我妈会记得我生日，不记得我先生的生…</div><div class="ExploreCollectionCard-contentTags"><span class="ExploreCollectionCard-contentTypeTag">回答</span><span class="ExploreCollectionCard-contentCountTag">1 赞同</span><span class="ExploreCollectionCard-contentCountTag">0 评论</span></div></div><div class="ExploreCollectionCard-contentItem"><a class="ExploreCollectionCard-contentTitle" href="https://www.zhihu.com/answer/777911744" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5807">你见识过的婆婆可以坏到变态到哪种程度？</a><div class="ExploreCollectionCard-contentExcerpt">匿名用户：<b>禁止转载~~~~</b><b>禁止转载~~~~</b><b>禁止转载~~~~</b><b>知道一个真事，当事人我后来认识，开始是医院的医生是我一朋友，恶婆婆送去医院的时候，我医生朋友全程聆听这事。。</b><b>这件事情全程下来，我唯一感觉就是：</b><b><i>女人一定要有经济实力。这世界父母可以背叛你 丈夫可以算计你，…</i></b></div><div class="ExploreCollectionCard-contentTags"><span class="ExploreCollectionCard-contentTypeTag">回答</span><span class="ExploreCollectionCard-contentCountTag">8,661 赞同</span><span class="ExploreCollectionCard-contentCountTag">1,732 评论</span></div></div></div><a class="ExploreCollectionCard-collectedContentCount" href="/collection/95922523" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5804" data-za-detail-view-name="已收藏点击">已收藏 <!-- -->711<!-- --> 条内容<svg class="Zi Zi--ArrowRight" fill="currentColor" viewBox="0 0 24 24" width="24" height="24"><path d="M9.218 16.78a.737.737 0 0 0 1.052 0l4.512-4.249a.758.758 0 0 0 0-1.063L10.27 7.22a.737.737 0 0 0-1.052 0 .759.759 0 0 0-.001 1.063L13 12l-3.782 3.716a.758.758 0 0 0 0 1.063z" fill-rule="evenodd"></path></svg></a></div><div class="ExploreCollectionCard ExploreHomePage-collectionCard"><div class="ExploreCollectionCard-header"><div class="ExploreCollectionCard-info"><a class="ExploreCollectionCard-title" href="/collection/145417966" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5804" data-za-detail-view-name="标题点击">行业研究</a><div class="ExploreCollectionCard-relatedMembers"><div class="ExploreCollectionCard-creator"><span class="UserLink ExploreCollectionCard-creatorAvatar"><div class="Popover"><div id="null-toggle" aria-haspopup="true" aria-expanded="false" aria-owns="null-content"><a class="UserLink-link" data-za-detail-view-element_name="User" target="_blank" data-za-detail-view-id="5806" href="//www.zhihu.com/people/fan-xue-gang"><img class="Avatar UserLink-avatar" width="28" height="28" src="https://pic3.zhimg.com/408d9c256_is.jpg" srcSet="https://pic3.zhimg.com/408d9c256_im.jpg 2x" alt="樊雪刚"/></a></div></div></span><a class="ExploreCollectionCard-creatorName" href="/people/fan-xue-gang" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5806">樊雪刚</a><span class="ExploreCollectionCard-creatorSuffix">创建</span></div><div class="ExploreCollectionCard-followers">224<!-- --> 人关注</div></div></div><div class="ExploreCollectionCard-followButton"><button class="ExploreFollowButton">关注收藏夹</button></div></div><div class="ExploreCollectionCard-contentList"><div class="ExploreCollectionCard-contentItem"><a class="ExploreCollectionCard-contentTitle" href="https://zhuanlan.zhihu.com/p/33078736" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5807">别笑话日本，我们的少子化将来得更惨烈</a><div class="ExploreCollectionCard-contentExcerpt">塞冬：半个月前，一个新闻蛮火——日本年出生人口创下新低，一年只出生了94万人。 <a href="https://link.zhihu.com/?target=http%3A//news.sina.com.cn/o/2017-12-25/doc-ifypwzxq6584030.shtml" data-draft-node="block" data-draft-type="link-card" data-image="https://pic4.zhimg.com/v2-f78901e72ebcba511e7fbcf7dccd8397_180x120.jpg" data-image-width="600" data-image-height="333" class=" wrap external" target="_blank" rel="nofollow noreferrer">日本今年新生人口数创新低 空房子如瘟疫般蔓延</a> 当时微信里不少朋友在转发这条新闻，许多评论都说，日本药丸了。 今天的一条新闻也比较火——2017年，中国出生了<b>1723万</b>人。 <a href="https://link.zhihu.com/?target=http%3A//news.sina.com.cn/o/2018-01-18/doc-ifyquixe4003553.shtml" data-draft-node="block" data-draft-type="link-card" class=" wrap external" target="_blank" rel="nofollow noreferrer">2017年…</a></div><div class="ExploreCollectionCard-contentTags"><span class="ExploreCollectionCard-contentTypeTag">文章</span><span class="ExploreCollectionCard-contentCountTag">9,936 赞同</span><span class="ExploreCollectionCard-contentCountTag">1,978 评论</span></div></div><div class="ExploreCollectionCard-contentItem"><a class="ExploreCollectionCard-contentTitle" href="https://www.zhihu.com/answer/126341256" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5807">印度将来会人口过剩还是成为人口红利？这会在今后造成什么后果？</a><div class="ExploreCollectionCard-contentExcerpt">图灵Don：印度现在已有13.3亿人口，几年内就将超过中国。上图还是保守了。 <b>看印度人口问题，你看看中国就行</b>。很多人说中国人口拐点，劳动力拐点，其实不管怎么拐，中国劳动力数量还是超过9亿人。 9亿人什么概念？美国总人口的3倍，日本8倍，德国韩国的十几倍。<b>9亿人…</b></div><div class="ExploreCollectionCard-contentTags"><span class="ExploreCollectionCard-contentTypeTag">回答</span><span class="ExploreCollectionCard-contentCountTag">365 赞同</span><span class="ExploreCollectionCard-contentCountTag">76 评论</span></div></div></div><a class="ExploreCollectionCard-collectedContentCount" href="/collection/145417966" target="_blank" rel="noopener noreferrer" data-za-detail-view-id="5804" data-za-detail-view-name="已收藏点击">已收藏 <!-- -->24,689<!-- --> 条内容<svg class="Zi Zi--ArrowRight" fill="currentColor" viewBox="0 0 24 24" width="24" height="24"><path d="M9.218 16.78a.737.737 0 0 0 1.052 0l4.512-4.249a.758.758 0 0 0 0-1.063L10.27 7.22a.737.737 0 0 0-1.052 0 .759.759 0 0 0-.001 1.063L13 12l-3.782 3.716a.758.758 0 0 0 0 1.063z" fill-rule="evenodd"></path></svg></a></div></div></div><div class="ExploreHomePage-ContentSection-moreButton"><a href="/collection/hot" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5808">查看更多收藏夹<svg class="Zi Zi--ArrowRight" fill="currentColor" viewBox="0 0 24 24" width="25" height="25"><path d="M9.218 16.78a.737.737 0 0 0 1.052 0l4.512-4.249a.758.758 0 0 0 0-1.063L10.27 7.22a.737.737 0 0 0-1.052 0 .759.759 0 0 0-.001 1.063L13 12l-3.782 3.716a.758.758 0 0 0 0 1.063z" fill-rule="evenodd"></path></svg></a></div></div><div class="ExploreHomePage-ContentSection ExploreHomePage-section" id="column"><div class="ExploreHomePage-ContentSection-header"><svg class="Zi Zi--EditCircle" fill="currentColor" viewBox="0 0 24 24" width="36" height="36"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm4.043-15.524a.745.745 0 0 0-1.053.017l-6.857 7.071 2.237 2.17 6.857-7.071a.743.743 0 0 0-.016-1.052l-1.168-1.135zm-9.028 9.476l-.348 1.381 1.37-.39 1.274-.36-1.973-1.916-.323 1.285z" fill-rule="evenodd"></path></svg><span>专栏</span></div><div class="ExploreHomePage-ContentSection-body"><div class="ExploreHomePage-columns"><div class="ExploreColumnCard ExploreHomePage-columnCard"><a class="ExploreColumnCard-avatar" href="https://zhuanlan.zhihu.com/c_201557035" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5810" data-za-detail-view-name="专栏头像点击"><img src="https://pic1.zhimg.com/v2-ff5f252b658b6574c0284f8269c462d5_xl.jpg"/></a><a class="ExploreColumnCard-title" href="https://zhuanlan.zhihu.com/c_201557035" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5810" data-za-detail-view-name="专栏名称点击">电竞GO</a><div class="ExploreColumnCard-count"><span>16,924<!-- --> 关注</span><span>1,294<!-- --> 文章</span></div><div class="ExploreColumnCard-intro">DOTA2赛事比分、数据资讯：esgo.com</div><button class="ExploreColumnCard-entryButton">进入专栏</button></div><div class="ExploreColumnCard ExploreHomePage-columnCard"><a class="ExploreColumnCard-avatar" href="https://zhuanlan.zhihu.com/c_136968229" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5810" data-za-detail-view-name="专栏头像点击"><img src="https://pic3.zhimg.com/4b70deef7_xl.jpg"/></a><a class="ExploreColumnCard-title" href="https://zhuanlan.zhihu.com/c_136968229" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5810" data-za-detail-view-name="专栏名称点击">牙白白白的电影时光</a><div class="ExploreColumnCard-count"><span>197<!-- --> 关注</span><span>121<!-- --> 文章</span></div><div class="ExploreColumnCard-intro">公众号:牙白白白，有关电影的有趣的无趣的及其他</div><button class="ExploreColumnCard-entryButton">进入专栏</button></div><div class="ExploreColumnCard ExploreHomePage-columnCard"><a class="ExploreColumnCard-avatar" href="https://zhuanlan.zhihu.com/touyanbang88" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5810" data-za-detail-view-name="专栏头像点击"><img src="https://pic1.zhimg.com/v2-be8a4427259695fc9745f4f259a85ddb_xl.jpg"/></a><a class="ExploreColumnCard-title" href="https://zhuanlan.zhihu.com/touyanbang88" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5810" data-za-detail-view-name="专栏名称点击">闲话投资</a><div class="ExploreColumnCard-count"><span>9,713<!-- --> 关注</span><span>268<!-- --> 文章</span></div><div class="ExploreColumnCard-intro">各式各样的投资idea，只用大白话说</div><button class="ExploreColumnCard-entryButton">进入专栏</button></div><div class="ExploreColumnCard ExploreHomePage-columnCard"><a class="ExploreColumnCard-avatar" href="https://zhuanlan.zhihu.com/investmentclub" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5810" data-za-detail-view-name="专栏头像点击"><img src="https://pic4.zhimg.com/v2-e11f6dd8eeee14d452cf4129eaf7ce36_xl.jpg"/></a><a class="ExploreColumnCard-title" href="https://zhuanlan.zhihu.com/investmentclub" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5810" data-za-detail-view-name="专栏名称点击">交易法门</a><div class="ExploreColumnCard-count"><span>8,629<!-- --> 关注</span><span>303<!-- --> 文章</span></div><div class="ExploreColumnCard-intro">公众号：交易法门（ID：JMtrader）</div><button class="ExploreColumnCard-entryButton">进入专栏</button></div></div></div><div class="ExploreHomePage-ContentSection-moreButton"><a href="https://zhuanlan.zhihu.com" target="_blank" rel="noreferrer noopener" data-za-detail-view-id="5811">查看更多专栏<svg class="Zi Zi--ArrowRight" fill="currentColor" viewBox="0 0 24 24" width="25" height="25"><path d="M9.218 16.78a.737.737 0 0 0 1.052 0l4.512-4.249a.758.758 0 0 0 0-1.063L10.27 7.22a.737.737 0 0 0-1.052 0 .759.759 0 0 0-.001 1.063L13 12l-3.782 3.716a.758.758 0 0 0 0 1.063z" fill-rule="evenodd"></path></svg></a></div></div><footer class="PageBottomFooter ExploreHomePage-footer"><a href="https://liukanshan.zhihu.com" target="_blank" rel="noopener noreferrer">刘看山</a><a href="https://www.zhihu.com/question/19581624" target="_blank" rel="noopener noreferrer">知乎指南</a><a href="https://www.zhihu.com/terms" target="_blank" rel="noopener noreferrer">知乎协议</a><a href="https://www.zhihu.com/app" target="_blank" rel="noopener noreferrer">应用</a><a href="https://app.mokahr.com/apply/zhihu/3819" target="_blank" rel="noopener noreferrer">工作</a><a href="https://www.zhihu.com/contact" target="_blank" rel="noopener noreferrer">联系我们</a><span>© <!-- -->2019<!-- --> 知乎</span></footer></div></main><div data-zop-usertoken="{}"></div></div></div><script id="js-clientConfig" type="text/json">{"host":"zhihu.com","protocol":"https:","wwwHost":"www.zhihu.com","zhuanlanHost":"zhuanlan.zhihu.com","apiHost":"api.zhihu.com"}</script><script id="js-initialData" type="text/json">{"initialState":{"common":{"ask":{}},"loading":{"global":{"count":0},"local":{"explore\u002FgetLatestSpecials\u002F":false,"explore\u002FgetLatestRoundtables\u002F":false,"explore\u002FgetHotCollections\u002F":false,"explore\u002FgetRecommendColumns\u002F":false}},"entities":{"users":{},"questions":{},"answers":{},"articles":{},"columns":{},"topics":{},"roundtables":{},"favlists":{},"comments":{},"notifications":{},"ebooks":{},"activities":{},"feeds":{},"pins":{},"promotions":{},"drafts":{},"chats":{},"posts":{},"clubs":{}},"currentUser":"","account":{"lockLevel":{},"unlockTicketStatus":false,"unlockTicket":null,"challenge":[],"errorStatus":false,"message":"","isFetching":false,"accountInfo":{},"urlToken":{"loading":false}},"settings":{"socialBind":null,"inboxMsg":null,"notification":{},"email":{},"privacyFlag":null,"blockedUsers":{"isFetching":false,"paging":{"pageNo":1,"pageSize":6},"data":[]},"blockedFollowees":{"isFetching":false,"paging":{"pageNo":1,"pageSize":6},"data":[]},"ignoredTopics":{"isFetching":false,"paging":{"pageNo":1,"pageSize":6},"data":[]},"restrictedTopics":null,"laboratory":{}},"notification":{},"people":{"profileStatus":{},"activitiesByUser":{},"answersByUser":{},"answersSortByVotesByUser":{},"answersIncludedByUser":{},"votedAnswersByUser":{},"thankedAnswersByUser":{},"voteAnswersByUser":{},"thankAnswersByUser":{},"topicAnswersByUser":{},"articlesByUser":{},"articlesSortByVotesByUser":{},"articlesIncludedByUser":{},"pinsByUser":{},"questionsByUser":{},"commercialQuestionsByUser":{},"favlistsByUser":{},"followingByUser":{},"followersByUser":{},"mutualsByUser":{},"followingColumnsByUser":{},"followingQuestionsByUser":{},"followingFavlistsByUser":{},"followingTopicsByUser":{},"publicationsByUser":{},"columnsByUser":{},"allFavlistsByUser":{},"brands":null,"creationsByUser":{},"creationsSortByVotesByUser":{}},"env":{"ab":{"config":{"experiments":[{"expId":"launch-us_foltopic_user-10","expPrefix":"us_foltopic_user","isDynamicallyUpdated":true,"isRuntime":false,"includeTriggerInfo":false}],"params":[{"id":"zr_answer_rec_cp","type":"String","value":"open","chainId":"_all_"},{"id":"se_topiclabel","type":"String","value":"1","chainId":"_all_"},{"id":"se_whitelist","type":"String","value":"0","chainId":"_all_"},{"id":"tp_qa_toast","type":"String","value":"1","chainId":"_all_"},{"id":"ls_fmp4","type":"String","value":"0","chainId":"_all_"},{"id":"se_dnn_muli_task","type":"String","value":"0","chainId":"_all_"},{"id":"se_mclick1","type":"String","value":"0","chainId":"_all_"},{"id":"se_topicdirect","type":"String","value":"2","chainId":"_all_"},{"id":"se_backsearch","type":"String","value":"0","chainId":"_all_"},{"id":"tsp_vote","type":"String","value":"1","chainId":"_all_"},{"id":"pf_foltopic_usernum","type":"String","value":"50","chainId":"_all_"},{"id":"li_se_album_card","type":"String","value":"0","chainId":"_all_"},{"id":"zr_km_prerank","type":"String","value":"old","chainId":"_all_"},{"id":"zr_video_rank","type":"String","value":"new_rank","chainId":"_all_"},{"id":"se_rr","type":"String","value":"0","chainId":"_all_"},{"id":"tp_qa_metacard_top","type":"String","value":"top","chainId":"_all_"},{"id":"zw_sameq_sorce","type":"String","value":"999","chainId":"_all_"},{"id":"zr_video_rank_nn","type":"String","value":"new_rank","chainId":"_all_"},{"id":"zr_km_style","type":"String","value":"base","chainId":"_all_"},{"id":"se_mobileweb","type":"String","value":"1","chainId":"_all_"},{"id":"se_lottery","type":"String","value":"0","chainId":"_all_"},{"id":"se_time_threshold","type":"String","value":"0","chainId":"_all_"},{"id":"sem_up_growth","type":"String","value":"in_app","chainId":"_all_"},{"id":"zr_km_item_cf","type":"String","value":"close","chainId":"_all_"},{"id":"se_wannasearch","type":"String","value":"0","chainId":"_all_"},{"id":"se_subtext","type":"String","value":"0","chainId":"_all_"},{"id":"tsp_hotctr","type":"String","value":"1","chainId":"_all_"},{"id":"gue_new_special_page","type":"String","value":"0"},{"id":"zr_art_rec","type":"String","value":"base","chainId":"_all_"},{"id":"zr_intervene","type":"String","value":"0","chainId":"_all_"},{"id":"se_college_cm","type":"String","value":"0","chainId":"_all_"},{"id":"top_new_feed","type":"String","value":"5","chainId":"_all_"},{"id":"ug_follow_topic_1","type":"String","value":"2","chainId":"_all_"},{"id":"li_se_xgb","type":"String","value":"0","chainId":"_all_"},{"id":"se_zu_recommend","type":"String","value":"0","chainId":"_all_"},{"id":"top_ebook","type":"String","value":"0","chainId":"_all_"},{"id":"top_vipconsume","type":"String","value":"1","chainId":"_all_"},{"id":"ug_zero_follow","type":"String","value":"0","chainId":"_all_"},{"id":"li_back","type":"String","value":"1","chainId":"_all_"},{"id":"li_qa_cover","type":"String","value":"old","chainId":"_all_"},{"id":"zr_infinity_small","type":"String","value":"64","chainId":"_all_"},{"id":"zr_km_xgb_model","type":"String","value":"new_xgb","chainId":"_all_"},{"id":"se_search_feed","type":"String","value":"N","chainId":"_all_"},{"id":"se_hot_timebox","type":"String","value":"0","chainId":"_all_"},{"id":"soc_update","type":"String","value":"1","chainId":"_all_"},{"id":"pf_creator_card","type":"String","value":"1","chainId":"_all_"},{"id":"se_ri","type":"String","value":"0","chainId":"_all_"},{"id":"se_dnn_slabel","type":"String","value":"0","chainId":"_all_"},{"id":"se_websearch","type":"String","value":"3","chainId":"_all_"},{"id":"se_ltr_topic","type":"String","value":"0","chainId":"_all_"},{"id":"li_pay_banner_type","type":"String","value":"0","chainId":"_all_"},{"id":"zr_test_aa1","type":"String","value":"0","chainId":"_all_"},{"id":"se_hotsearch","type":"String","value":"0","chainId":"_all_"},{"id":"top_v_album","type":"String","value":"1","chainId":"_all_"},{"id":"top_universalebook","type":"String","value":"1","chainId":"_all_"},{"id":"top_gr_ab","type":"String","value":"0","chainId":"_all_"},{"id":"se_billboardsearch","type":"String","value":"0","chainId":"_all_"},{"id":"soc_bigone","type":"String","value":"0","chainId":"_all_"},{"id":"zr_km_slot_style","type":"String","value":"event_card","chainId":"_all_"},{"id":"se_cardrank_1","type":"String","value":"0","chainId":"_all_"},{"id":"se_go_ztext","type":"String","value":"0","chainId":"_all_"},{"id":"se_col_boost","type":"String","value":"0","chainId":"_all_"},{"id":"se_preset_tech","type":"String","value":"0","chainId":"_all_"},{"id":"tp_sft","type":"String","value":"a","chainId":"_all_"},{"id":"pf_noti_entry_num","type":"String","value":"0","chainId":"_all_"},{"id":"web_heifetz_grow_ad","type":"String","value":"1"},{"id":"li_price_test","type":"String","value":"1","chainId":"_all_"},{"id":"gue_zhuantikapian","type":"String","value":"0"},{"id":"zr_search_xgb","type":"String","value":"1","chainId":"_all_"},{"id":"se_mclick","type":"String","value":"0","chainId":"_all_"},{"id":"tp_sticky_android","type":"String","value":"0","chainId":"_all_"},{"id":"top_rank","type":"String","value":"0","chainId":"_all_"},{"id":"top_recall_exp_v2","type":"String","value":"1","chainId":"_all_"},{"id":"tsp_lastread","type":"String","value":"0","chainId":"_all_"},{"id":"li_android_vip","type":"String","value":"0","chainId":"_all_"},{"id":"zr_km_recall","type":"String","value":"default","chainId":"_all_"},{"id":"se_dnn_cpyramid","type":"String","value":"0","chainId":"_all_"},{"id":"se_new_topic","type":"String","value":"0","chainId":"_all_"},{"id":"top_hotcommerce","type":"String","value":"1","chainId":"_all_"},{"id":"li_search_answer","type":"String","value":"0","chainId":"_all_"},{"id":"se_ltr_payconsult","type":"String","value":"0","chainId":"_all_"},{"id":"tp_qa_metacard","type":"String","value":"1","chainId":"_all_"},{"id":"tsp_childbillboard","type":"String","value":"1","chainId":"_all_"},{"id":"soc_bignew","type":"String","value":"1","chainId":"_all_"},{"id":"li_qa_new_cover","type":"String","value":"0","chainId":"_all_"},{"id":"li_se_paid_answer","type":"String","value":"0","chainId":"_all_"},{"id":"zr_km_answer","type":"String","value":"open_cvr","chainId":"_all_"},{"id":"se_webmajorob","type":"String","value":"0","chainId":"_all_"},{"id":"se_agency","type":"String","value":" 0","chainId":"_all_"},{"id":"tp_meta_card","type":"String","value":"0","chainId":"_all_"},{"id":"top_native_answer","type":"String","value":"1","chainId":"_all_"},{"id":"soc_special","type":"String","value":"0","chainId":"_all_"},{"id":"ug_follow_answerer","type":"String","value":"0","chainId":"_all_"},{"id":"ug_follow_answerer_0","type":"String","value":"0","chainId":"_all_"},{"id":"se_cardrank_2","type":"String","value":"0","chainId":"_all_"},{"id":"se_likebutton","type":"String","value":"0","chainId":"_all_"},{"id":"se_dnn_mt","type":"String","value":"0","chainId":"_all_"},{"id":"ug_fw_answ_aut_1","type":"String","value":"0","chainId":"_all_"},{"id":"top_ydyq","type":"String","value":"X","chainId":"_all_"},{"id":"li_hot_score_ab","type":"String","value":"0","chainId":"_all_"},{"id":"zr_rec_answer_cp","type":"String","value":"close","chainId":"_all_"},{"id":"se_expired_ob","type":"String","value":"0","chainId":"_all_"},{"id":"se_payconsult","type":"String","value":"0","chainId":"_all_"},{"id":"tp_m_intro_re_topic","type":"String","value":"1","chainId":"_all_"},{"id":"tsp_hotsheep","type":"String","value":"1","chainId":"_all_"},{"id":"web_sem_ab","type":"String","value":"0"},{"id":"li_tjys_ec_ab","type":"String","value":"0","chainId":"_all_"},{"id":"se_waterfall","type":"String","value":"0","chainId":"_all_"},{"id":"se_movietab","type":"String","value":"1","chainId":"_all_"},{"id":"se_famous","type":"String","value":"1","chainId":"_all_"},{"id":"ls_videoad","type":"String","value":"2","chainId":"_all_"},{"id":"web_question_invite","type":"String","value":"B"},{"id":"se_featured","type":"String","value":"1","chainId":"_all_"},{"id":"tp_club_qa","type":"String","value":"0","chainId":"_all_"},{"id":"top_test_4_liguangyi","type":"String","value":"1","chainId":"_all_"},{"id":"se_limit","type":"String","value":"0","chainId":"_all_"},{"id":"top_recall_exp_v1","type":"String","value":"1","chainId":"_all_"},{"id":"se_auto_syn","type":"String","value":"0","chainId":"_all_"},{"id":"ug_zero_follow_0","type":"String","value":"0","chainId":"_all_"},{"id":"zr_ans_rec","type":"String","value":"gbrank","chainId":"_all_"},{"id":"web_n_web_msg","type":"String","value":"0"},{"id":"gue_anonymous","type":"String","value":"show"},{"id":"web_answerlist_ad","type":"String","value":"0"},{"id":"web_column_auto_invite","type":"String","value":"0"},{"id":"web_answer_list_ad","type":"String","value":"1"},{"id":"zr_cold_start","type":"String","value":"0","chainId":"_all_"},{"id":"se_ad_index","type":"String","value":"10","chainId":"_all_"},{"id":"top_quality","type":"String","value":"0","chainId":"_all_"},{"id":"zr_slot_cold_start","type":"String","value":"default","chainId":"_all_"},{"id":"zr_video_recall","type":"String","value":"current_recall","chainId":"_all_"},{"id":"se_ltr_dnn_cp","type":"String","value":"0","chainId":"_all_"},{"id":"se_zu_onebox","type":"String","value":"0","chainId":"_all_"},{"id":"li_se_kv","type":"String","value":"0","chainId":"_all_"},{"id":"se_spb309","type":"String","value":"0","chainId":"_all_"},{"id":"se_p_slideshow","type":"String","value":"0","chainId":"_all_"},{"id":"soc_notification","type":"String","value":"0","chainId":"_all_"},{"id":"ls_new_upload","type":"String","value":"0","chainId":"_all_"},{"id":"se_ios_spb309","type":"String","value":"0","chainId":"_all_"},{"id":"se_webtimebox","type":"String","value":"0","chainId":"_all_"},{"id":"tp_header_style","type":"String","value":"1","chainId":"_all_"},{"id":"web_answer_update","type":"String","value":"0"},{"id":"zr_man_intervene","type":"String","value":"0","chainId":"_all_"},{"id":"se_amovietab","type":"String","value":"1","chainId":"_all_"},{"id":"tp_sft_v2","type":"String","value":"d","chainId":"_all_"},{"id":"tsp_newchild","type":"String","value":"1","chainId":"_all_"},{"id":"pf_fuceng","type":"String","value":"1","chainId":"_all_"},{"id":"li_se_vertical","type":"String","value":"0","chainId":"_all_"},{"id":"pf_newguide_vertical","type":"String","value":"0","chainId":"_all_"},{"id":"ug_goodcomment_0","type":"String","value":"1","chainId":"_all_"},{"id":"li_album_liutongab","type":"String","value":"0","chainId":"_all_"},{"id":"se_webrs","type":"String","value":"1","chainId":"_all_"},{"id":"se_college","type":"String","value":"default","chainId":"_all_"},{"id":"se_colorfultab","type":"String","value":"1","chainId":"_all_"},{"id":"tp_topic_head","type":"String","value":"1","chainId":"_all_"},{"id":"top_root","type":"String","value":"0","chainId":"_all_"},{"id":"top_recall_deep_user","type":"String","value":"1","chainId":"_all_"},{"id":"ug_newtag","type":"String","value":"0","chainId":"_all_"},{"id":"zr_rel_search","type":"String","value":"base","chainId":"_all_"},{"id":"se_site_onebox","type":"String","value":"0","chainId":"_all_"}],"chains":[{"chainId":"_all_"}]},"triggers":{}},"userAgent":{"Edge":false,"Wechat":false,"Weibo":false,"QQ":false,"MQQBrowser":false,"Qzone":false,"Mobile":false,"Android":false,"iOS":false,"isAppleDevice":false,"Zhihu":false,"ZhihuHybrid":false,"isBot":false,"Tablet":false,"UC":false,"Sogou":false,"Qihoo":false,"Baidu":false,"BaiduApp":false,"Safari":false,"GoogleBot":false,"isWebView":false,"origin":"Mozilla\u002F5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\u002F537.36 (KHTML, like Gecko) Chrome\u002F76.0.3809.132 Safari\u002F537.36"},"ctx":{"path":"\u002Fexplore"},"trafficSource":"production","edition":{"baidu":false,"sogou":false,"baiduBeijing":false,"sogouBeijing":false},"theme":"light","enableShortcut":true,"referer":"","conf":{},"ipInfo":{},"logged":false,"tdkInfo":{}},"me":{"columnContributions":[]},"label":{"recognizerLists":{}},"ecommerce":{},"comments":{"pagination":{},"collapsed":{},"reverse":{},"reviewing":{},"conversation":{},"parent":{}},"commentsV2":{"stickers":[],"commentWithPicPermission":{},"notificationsComments":{},"pagination":{},"collapsed":{},"reverse":{},"reviewing":{},"conversation":{},"conversationMore":{},"parent":{}},"pushNotifications":{"default":{"isFetching":false,"isDrained":false,"ids":[]},"follow":{"isFetching":false,"isDrained":false,"ids":[]},"vote_thank":{"isFetching":false,"isDrained":false,"ids":[]},"currentTab":"default","notificationsCount":{"default":0,"follow":0,"vote_thank":0}},"messages":{"data":{},"currentTab":"common","messageCount":0},"register":{"registerValidateSucceeded":null,"registerValidateErrors":{},"registerConfirmError":null,"sendDigitsError":null,"registerConfirmSucceeded":null},"login":{"loginUnregisteredError":false,"loginBindWechatError":false,"loginConfirmError":null,"sendDigitsError":null,"validateDigitsError":false,"loginConfirmSucceeded":null,"qrcodeLoginToken":"","qrcodeLoginScanStatus":0,"qrcodeLoginError":null,"qrcodeLoginReturnNewToken":false},"active":{"sendDigitsError":null,"activeConfirmSucceeded":null,"activeConfirmError":null},"switches":{},"captcha":{"captchaNeeded":false,"captchaValidated":false,"captchaBase64String":null,"captchaValidationMessage":null,"loginCaptchaExpires":false},"sms":{"supportedCountries":[]},"chat":{"chats":{},"inbox":{"recents":{"isFetching":false,"isDrained":false,"isPrevDrained":false,"result":[],"next":null,"key":null},"strangers":{"isFetching":false,"isDrained":false,"isPrevDrained":false,"result":[],"next":null,"key":null},"friends":{"isFetching":false,"isDrained":false,"isPrevDrained":false,"result":[],"next":null,"key":null},"search":{"isFetching":false,"isDrained":false,"isPrevDrained":false,"result":[],"next":null,"key":null},"config":{"newCount":0,"strangerMessageSwitch":false,"strangerMessageUnread":false,"friendCount":0}},"global":{"isChatMqttExisted":false}},"emoticons":{"emoticonGroupList":[],"emoticonGroupDetail":{}},"creator":{"currentCreatorUrlToken":null,"homeData":{"recommendQuestions":[]},"tools":{"question":{"invitationCount":{"questionFolloweeCount":0,"questionTotalCount":0},"goodatTopics":[]},"customPromotion":{"itemLists":{}},"recommend":{"recommendTimes":{}}},"explore":{"academy":{"tabs":[],"article":{}}},"rights":[],"rightsStatus":{},"levelUpperLimit":10,"account":{"growthLevel":{}},"applyStatus":{}},"question":{"followers":{},"concernedFollowers":{},"answers":{},"hiddenAnswers":{},"updatedAnswers":{},"collapsedAnswers":{},"notificationAnswers":{},"invitedQuestions":{"total":{"count":null,"isEnd":false,"isLoading":false,"questions":[]},"followees":{"count":null,"isEnd":false,"isLoading":false,"questions":[]}},"laterQuestions":{"count":null,"globalWriteAnimate":false,"isEnd":false,"isLoading":false,"questions":[]},"waitingQuestions":{"hot":{"isEnd":false,"isLoading":false,"questions":[]},"value":{"isEnd":false,"isLoading":false,"questions":[]},"newest":{"isEnd":false,"isLoading":false,"questions":[]},"easy":{"isEnd":false,"isLoading":false,"questions":[]}},"invitationCandidates":{},"inviters":{},"invitees":{},"similarQuestions":{},"relatedCommodities":{},"recommendReadings":{},"bio":{},"brand":{},"permission":{},"adverts":{},"advancedStyle":{},"commonAnswerCount":0,"hiddenAnswerCount":0,"meta":{},"autoInvitation":{},"simpleConcernedFollowers":{},"draftStatus":{},"disclaimers":{}},"shareTexts":{},"answers":{"voters":{},"copyrightApplicants":{},"favlists":{},"newAnswer":{},"concernedUpvoters":{},"simpleConcernedUpvoters":{},"paidContent":{},"settings":{}},"banner":{},"topic":{"bios":{},"hot":{},"newest":{},"top":{},"unanswered":{},"questions":{},"followers":{},"contributors":{},"parent":{},"children":{},"bestAnswerers":{},"wikiMeta":{},"index":{},"intro":{},"meta":{},"schema":{},"creatorWall":{},"wikiEditInfo":{},"committedWiki":{}},"explore":{"recommendations":{},"specials":{"19560438":{"viewCount":3287939,"updated":1567132333,"title":"夏日将尽，二刷走起","introduction":"👀又剧荒了吧？19 年夏天，有哪些推荐度爆表的影视综值得二刷？错过的补起来，看过的二刷起来吧~\t\t\t","contentList":[{"id":"333300489","title":"影视综全集 | 又一个暑假过去了，你错过了啥？","type":"question","sectionId":"1150456401133383680","sectionTitle":"夏日爆款"},{"id":"754343925","title":"哪吒 | 我命由我，不由天！","type":"answer","sectionId":"1150457329399959552","sectionTitle":"热映国片"},{"id":"792589563","title":" 骡子 | 两种价值观的拉扯","type":"answer","sectionId":"1150458272401281024","sectionTitle":"海外佳片"}],"isFollowing":false,"banner":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-0999111303457fb6e0a0503873700f72_hd.jpg","id":"19560438"},"19605346":{"viewCount":1515139,"updated":1567140117,"title":"聚焦 LPL 季后赛，「3G 时代」要终结了吗？","introduction":"今年的 LPL 新王层出不穷，世界赛名额扑朔迷离。「昔日霸主」季后赛四强阶段仅剩 RNG，「3G 时代」要宣告结束了吗？\u003E\u003E\u003E","contentList":[{"id":"801489100","title":"EDG 建队首次无缘世界赛","type":"answer","sectionId":"1150460288724742144","sectionTitle":"EDG 建队首次无缘季后赛"},{"id":"800016020","title":"iG 冠军教练的「遗产」消耗殆尽了","type":"answer","sectionId":"1150460491200720896","sectionTitle":"iG 能否出线仅剩冒泡赛机会"},{"id":"802338479","title":"距离世界赛更近，但却无法让人放心","type":"answer","sectionId":"1150460604530626560","sectionTitle":"RNG 的「生死战」"}],"isFollowing":false,"banner":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Fv2-394d7e36df41d99a5e9f94398cff138d_hd.jpg","id":"19605346"},"19638453":{"viewCount":2693780,"updated":1567066988,"title":"Ti9 折戟沉沙，CN DOTA 出了什么问题？","introduction":"随着 OG 战队问鼎冠军 DOTA2 第九届国际邀请赛开创了多项新记录。 Ti 历史上首支双冠王诞生，自 Ti3 开始从未缺席决赛的 CN DOTA 无缘本次决赛。「全村人的希望」LGD 倒在了「奇迹」面前。玩家们内心五味陈杂，人们不禁反思，CN DOTA 三年无冠背后的原因到底是什么？","contentList":[{"id":"342463513","title":"Ti9「全村最后的希望」跌落败者组","type":"question","sectionId":"1149746248029483008","sectionTitle":"Ti9 赛事回顾"},{"id":"793474632","title":"不复当年","type":"answer","sectionId":"1149746584882376704","sectionTitle":"三年无冠，CN DOTA 怎么了？"},{"id":"648090914","title":"最「传奇」的战队","type":"answer","sectionId":"1149747914640441344","sectionTitle":"人们为什么怀念 Wings？"}],"isFollowing":false,"banner":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002Fv2-cb51d035dc3ffb20bd6ffc16034186f7_hd.jpg","id":"19638453"},"20011001":{"viewCount":3545365,"updated":1567160070,"title":"知新车 · 2019 汽车下半局","introduction":"在这里，将盘点下半年即将或已上市新车，与知友一起种草、吐槽。本专题持续更新，敬请关注 \u003E\u003E\u003E","contentList":[{"id":"337599789","title":"2019 成都车展有哪些值得关注的新车？","type":"question","sectionId":"1150450968071110656","sectionTitle":"新车之惑"},{"id":"338797096","title":"丰田 · 第 12 代卡罗拉","type":"question","sectionId":"1150451002414002176","sectionTitle":"经济之选"},{"id":"330701118","title":"宝马 · 全新 3 系 G20\u002FG28","type":"question","sectionId":"1150451038237728768","sectionTitle":"德系豪华"}],"isFollowing":false,"banner":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002Fv2-ce8c59b61f71b2a5c9324946bda00dc3_hd.jpg","id":"20011001"}},"roundtables":{"basketballworldcup":{"startAt":1567209036,"name":"男篮世界杯，中国队能否突围？","title":"男篮世界杯，中国队能否突围？","color":"#14003D","banner":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002Fv2-5308ab3eb21424f0a027af5928d3bd90_hd.jpg","tinyBanner":"https:\u002F\u002Fpic1.zhimg.com\u002F50\u002Fv2-e3ada036c144da0b10dd38f8df6ddebc_hd.jpg","endAt":1568710250,"url":"\u002Froundtables\u002Fexplore\u002Fcards\u002Froundtable\u002Fbasketballworldcup","followersCount":106,"intro":"2019 年的篮球世界杯将在中国举办，中国队面对「史上最佳分组」，能否在家门口取得好成绩？美国队多名 NBA 球员退赛，梦之队能否捍卫荣誉？塞尔维亚、希腊等豪强并起，篮球世界杯冠军最终会落入谁手？本次圆桌，就让我们一起来围观。\n","isFollowing":false,"guests":[{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-c2a7f309662683907f17bcccee7c2454_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-2c9428ee55620cab25bbbf72dc53a9dd_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Fv2-56b591ecfd7c66676752b9a9f2adc56f_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002Fv2-79caf5f9eaa7d52a866d14fe69e179a6_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-e25f2a01779b031d1cb0a5352058441e_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Fv2-f79280bcbfdce9d0968c4214f5585544_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fd59df176610d56f28ad45a910f84c09f_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-71e41898beab389bb4ae7b7e8753b104_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Fv2-fe9bcdc46cc5befc27e21bb0621f0d14_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic1.zhimg.com\u002F50\u002Fv2-43902b405827a2e2a3612ce4ed98a0fd_hd.jpg"}],"questions":[{"followerCount":509,"title":"如何评价 2019 男篮世界杯的抽签分组结果？","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F316195740","type":"question","id":316195740,"answerCount":135},{"followerCount":10,"title":"男篮世界杯中国队首战对阵科特迪瓦，有多少胜算？","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F343677646","type":"question","id":343677646,"answerCount":6},{"followerCount":14,"title":"国际篮协要怎样做，才能让篮球世界杯跟足球世界杯一样，其地位大于职业联赛?","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F336925927","type":"question","id":336925927,"answerCount":14}],"logo":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002Fv2-f46dad73ac3a8060062ec5d96934c0de_hd.jpg","urlToken":"basketballworldcup"},"lol8years":{"startAt":1567293079,"name":"英雄联盟，无限热爱","title":"英雄联盟，无限热爱","color":"#343382","banner":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002Fv2-f07fefac9ae4c2cb03f1fa17887b7aa1_hd.jpg","tinyBanner":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-a2b7b6aba4dff857cf2ac8ea69a4b6e5_hd.jpg","endAt":1568041888,"url":"\u002Froundtables\u002Fexplore\u002Fcards\u002Froundtable\u002Flol8years","followersCount":40,"intro":"英雄联盟与我们相伴八年了，踏峡谷，登云顶，一路走来，大家找到了各自的段位成为了英雄。在召唤师峡谷中，你留下了哪些故事和回忆？今年的夏季总决赛和全球总决赛又会上演怎样的精彩对决？因为无限热爱，才有无限可能。本次圆桌，就让我们一同探寻未来，共话热爱！","isFollowing":false,"guests":[{"avatarUrl":"https:\u002F\u002Fpic1.zhimg.com\u002F50\u002Fv2-7486a4246242f1d69f13bfc3a37655dd_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Fv2-06734a92e6fd35ce9d4df76af0cd1cce_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-06463e9377c7ff434dd456d396668f14_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-e354b4848c773d9ec7526caac42e2a3d_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic1.zhimg.com\u002F50\u002Fv2-7d54a20ea28adc27ce34185bd3022961_hd.jpg"}],"questions":[{"followerCount":35,"title":"《英雄联盟》有哪些实用的翻盘技巧（经验）？","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F340349232","type":"question","id":340349232,"answerCount":35},{"followerCount":961,"title":"如果穿越到《英雄联盟》，你要怎么活下去，并成为一名英雄？","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F329620324","type":"question","id":329620324,"answerCount":291},{"followerCount":341,"title":"《英雄联盟》里，谁能最快清完100个聚集在一起的小兵？","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F328805878","type":"question","id":328805878,"answerCount":158}],"logo":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002Fv2-1604ae1189fd42f69d6a255551b49e03_hd.jpg","urlToken":"lol8years"},"xiaoyuanxinshengjinj":{"startAt":1567303201,"name":"校园新生进阶之道","title":"校园新生进阶之道","color":"#91aed6","banner":"https:\u002F\u002Fpic1.zhimg.com\u002F50\u002Fv2-a03ad0413a09949cab00fe6823147586_hd.jpg","tinyBanner":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002Fv2-8d4b0c4a7e353b844c586451a96910b0_hd.jpg","endAt":1567861201,"url":"\u002Froundtables\u002Fexplore\u002Fcards\u002Froundtable\u002Fxiaoyuanxinshengjinj","followersCount":104,"intro":"对不少离家求学的学子们来说，陌生的人、陌生的环境最让人感到不安。该如果与新同学沟通？该怎么规划学习目标？该怎么融入校园生活？遇到困难该如何靠自己化解？本期圆桌，我们邀请了心理界、法律界、人事界及社工界多位大咖，运用各行各业的知识与技巧，帮你缓解焦虑，融入校园新生活。","isFollowing":false,"guests":[{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fdf4318a7d28d27d3b27c0ab320fa203a_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fb28a4217a763ea990563f33fb40a5ce9_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Fv2-474464c34921bb480f933b36361133c1_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002Fv2-695fc1792dea2475b3ff7a3651329191_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-d135cfe85644870e54c4e7160d67cc74_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Fv2-18408a74f185e0532fdb9575f298341f_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002Fa93a684d9_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-0d8fae9c0958d4b83478dfc7f9fc383f_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-83b18ed0e268ff1acf204ebacb527f10_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-08b5e17cc73ca4a2934b0042452c0a89_hd.jpg"}],"questions":[{"followerCount":3727,"title":"如何有效地劝刚上大学的儿子远离校园贷？","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F265597918","type":"question","id":265597918,"answerCount":716},{"followerCount":53835,"title":"内向、不善社交的人如何建立人脉？","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F20052781","type":"question","id":20052781,"answerCount":663},{"followerCount":1850,"title":"大一学生很迷茫，觉得人生浑浑噩噩的，怎么调整状态?","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F27177500","type":"question","id":27177500,"answerCount":108}],"logo":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Fv2-d28e4712150515bcfd9780c171177437_hd.jpg","urlToken":"xiaoyuanxinshengjinj"},"fushe":{"startAt":1567382400,"name":"辐射可怕吗 | 非常想问","title":"辐射可怕吗 | 非常想问","color":"#203673","banner":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-56097fc1541cdc5f03081131d958db65_hd.jpg","tinyBanner":"https:\u002F\u002Fpic1.zhimg.com\u002F50\u002Fv2-d396e1e9e52ba02222176f19b0b7ee13_hd.jpg","endAt":1568001600,"url":"\u002Froundtables\u002Fexplore\u002Fcards\u002Froundtable\u002Ffushe","followersCount":1162,"intro":"1901 年，因为对 X 光的发现，威廉·伦琴获得了第一届诺贝尔物理学奖。随后的百年里，辐射被应用到了人类生活的方方面面。然而，时至今日，人们依然会谈「辐」色变。辐射到底是什么？人类对辐射的应用都有哪些？辐射真的可怕吗？本期圆桌，就让我们一起来重新认识辐射。","isFollowing":false,"guests":[{"avatarUrl":"https:\u002F\u002Fpic4.zhimg.com\u002F50\u002F1eb9b8c7e7ddc53f26db62a3ecd99dd7_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic1.zhimg.com\u002F50\u002Fv2-76ee781bcc0e2225461419e564c67a88_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002Fv2-7af3fdbdf67525f431e69689917b9f61_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F50\u002F5bf7478bf6570a92780afadebf0c4222_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Fv2-42236bb4c5d5f53f0161399b164aa303_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Ff82552596be14fea8bf2e7c3842eebae_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002F50\u002Fv2-7bd339e26759782e4570d1eec7c01de7_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic1.zhimg.com\u002F50\u002Fv2-2d8db89e29152e0a12131ed9335c324a_hd.jpg"},{"avatarUrl":"https:\u002F\u002Fpic1.zhimg.com\u002F50\u002F34bd51d29_hd.jpg"}],"questions":[{"followerCount":7947,"title":"如何看待福岛核电站二号机组近日被发现压力容器已被烧穿？","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F55352779","type":"question","id":55352779,"answerCount":153},{"followerCount":23,"title":"辐照杀菌是安全的吗？","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F22952334","type":"question","id":22952334,"answerCount":4},{"followerCount":66,"title":"地铁安检机频繁开门瞬间辐射会侧漏吗？","url":"https:\u002F\u002Fwww.zhihu.com\u002Fquestion\u002F66256527","type":"question","id":66256527,"answerCount":10}],"logo":"https:\u002F\u002Fpic1.zhimg.com\u002F50\u002Fv2-1c8bcd921173b9ad823ec0efed296bc8_hd.jpg","urlToken":"fushe"}},"collections":{"60058588":{"favitems":[{"content":{"isCollapsed":false,"author":{"avatarUrlTemplate":"https:\u002F\u002Fpic2.zhimg.com\u002Fv2-f9a9badcdc143a38ef52f9c4e3ef6365_{size}.jpg","name":"空白","headline":"这一路有多远，世界就有多大。","badge":[],"userType":"people","urlToken":"136839410","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002Fv2-f9a9badcdc143a38ef52f9c4e3ef6365_is.jpg","isOrg":false,"gender":1,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002F3bf818588a1f7a35f7a65785e7eb592a","type":"people","id":"3bf818588a1f7a35f7a65785e7eb592a"},"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fanswers\u002F797170522","excerpt":"看到一位兄弟说“宽容NMB”，简直要笑疯。本来准备直接跳过的，突然想吐槽一下男人从来不会喊冤哭悲惨，而你们妹子屁大点事就这啊那的，知道你们妹子是弱势群体了好吧！没钱的大龄剩男都不算人了，自然没有权力说什么。而你们妹子花点钱把自己包装一下就觉…","id":797170522,"question":{"questionType":"normal","created":1565583787,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fquestions\u002F340092385","title":"为什么当今社会对大龄剩男没有这么苛责?","type":"question","id":340092385,"updatedTime":1566951953},"updatedTime":1567093172,"commentCount":304,"extras":"","answerType":"answer","createdTime":1566373850,"isCopyable":true,"type":"answer","thumbnail":"","voteupCount":2017}},{"content":{"isCollapsed":false,"author":{"avatarUrlTemplate":"https:\u002F\u002Fpic1.zhimg.com\u002Fv2-df48c59491ef8c40c4517116a639aa76_{size}.jpg","name":"唐芊芊","headline":"女人最性感的部位是大脑","badge":[],"userType":"people","urlToken":"tang-qian-qian-91","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic1.zhimg.com\u002Fv2-df48c59491ef8c40c4517116a639aa76_is.jpg","isOrg":false,"gender":0,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002F3678682d509591c8bfced15f1a949ca7","type":"people","id":"3678682d509591c8bfced15f1a949ca7"},"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fanswers\u002F798313573","excerpt":"2003年，贴吧成立，其灵感来源于李彦宏一个不成熟的想法：结合搜索引擎建立一个在线兴趣交流平台。靠着这个想法，贴吧日后发展成为了全球最大的中文社区。贴吧上线一年后，足球运动员李毅的个人主题贴吧李毅吧正式建立，李毅当年因自恃“护球像亨利”，而被…","id":798313573,"question":{"questionType":"normal","created":1566094625,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fquestions\u002F341185812","title":"李毅是谁？为什么称李毅吧为帝吧？","type":"question","id":341185812,"updatedTime":1566094625},"updatedTime":1566452920,"commentCount":1537,"extras":"","answerType":"answer","createdTime":1566452878,"isCopyable":false,"type":"answer","thumbnail":"https:\u002F\u002Fpic4.zhimg.com\u002Fv2-d6600f246440fed5311396f7cb366dc8_200x112.jpg","voteupCount":39938}}],"title":"经济，政治，社会热点","url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fcollections\u002F60058588","totalCount":725,"creator":{"avatarUrlTemplate":"https:\u002F\u002Fpic3.zhimg.com\u002Ff101169c7db45793bf74a5da3dff174a_{size}.jpg","name":"落雨1994","headline":"在青春的道路上不断寻找自己","badge":[],"userType":"people","urlToken":"fan-yan-yu-50","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002Ff101169c7db45793bf74a5da3dff174a_is.jpg","isOrg":false,"gender":1,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002F270c6f66778531858cf33446fc9aab4f","type":"people","id":"270c6f66778531858cf33446fc9aab4f"},"isFollowing":false,"followerCount":509,"isPublic":true,"type":"collection","id":60058588},"72037720":{"favitems":[{"content":{"isCollapsed":false,"author":{"avatarUrlTemplate":"https:\u002F\u002Fpic2.zhimg.com\u002Fv2-637dad12f89f47c45cf7b73d6b0efbf0_{size}.jpg","name":"瑞宝","headline":"","badge":[],"userType":"people","urlToken":"rui-bao-33-83-18","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002Fv2-637dad12f89f47c45cf7b73d6b0efbf0_is.jpg","isOrg":false,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002Fdbd97f2ff850a2f8de1a8c33a83c72b0","type":"people","id":"dbd97f2ff850a2f8de1a8c33a83c72b0"},"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fanswers\u002F403461471","excerpt":"同时在养着。先说猫：从小特别喜欢狗，讨厌猫。工作后因为老公经常讲他小时候，养的猫如何如何聪明，可以叫回来，还会安慰它。就养了一只小猫，才发觉原来猫这么可爱，挑食。整天就是睡觉，岁月静好。还会自己在猫砂盆里，解决大小便。每天清理就好了。长大…","id":403461471,"question":{"questionType":"normal","created":1483943233,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fquestions\u002F54572422","title":"你在养宠物的时候是更偏向于养猫还是养狗？","type":"question","id":54572422,"updatedTime":1483943233},"updatedTime":1527490622,"commentCount":3,"extras":"","answerType":"answer","createdTime":1527490622,"isCopyable":true,"type":"answer","thumbnail":"","voteupCount":3}},{"content":{"isCollapsed":false,"author":{"avatarUrlTemplate":"https:\u002F\u002Fpic2.zhimg.com\u002F04d72da19d54ddb4ac87061de55693e7_{size}.jpg","name":"桃夭","headline":"泛生物行业。","badge":[],"userType":"people","urlToken":"du-juan-15-32","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002F04d72da19d54ddb4ac87061de55693e7_is.jpg","isOrg":false,"gender":0,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002Fa0aca5681a63887ad503fa1ffe8c88e1","type":"people","id":"a0aca5681a63887ad503fa1ffe8c88e1"},"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fanswers\u002F130736857","excerpt":"养猫的幸福感相当于女神\u002F男神住你家...","id":130736857,"question":{"questionType":"normal","created":1477849344,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fquestions\u002F52138505","title":"养猫幸福感强 还是 养狗幸福感强？养过的答？","type":"question","id":52138505,"updatedTime":1485109082},"updatedTime":1478774237,"commentCount":1,"extras":"","answerType":"answer","createdTime":1478774237,"isCopyable":true,"type":"answer","thumbnail":"","voteupCount":2}}],"title":"我的收藏","url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fcollections\u002F72037720","totalCount":504,"creator":{"avatarUrlTemplate":"https:\u002F\u002Fpic4.zhimg.com\u002Fv2-7d70724f8340e8172fd5b8d3496b9d62_{size}.jpg","name":"曼雪莉公主","headline":"","badge":[],"userType":"people","urlToken":"mi-gan-79-20","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic4.zhimg.com\u002Fv2-7d70724f8340e8172fd5b8d3496b9d62_is.jpg","isOrg":false,"gender":0,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002F1758533cccb003a083932fe3437f2a74","type":"people","id":"1758533cccb003a083932fe3437f2a74"},"isFollowing":false,"followerCount":43,"isPublic":true,"type":"collection","id":72037720},"95922523":{"favitems":[{"content":{"isCollapsed":false,"author":{"avatarUrlTemplate":"https:\u002F\u002Fpic4.zhimg.com\u002Fda8e974dc_{size}.jpg","name":"爱生气的小河豚","headline":"","badge":[],"userType":"people","urlToken":"xu-qian-87-15","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic4.zhimg.com\u002Fda8e974dc_is.jpg","isOrg":false,"gender":0,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002F37e8163a06c1a6491cebbed0ad8def9b","type":"people","id":"37e8163a06c1a6491cebbed0ad8def9b"},"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fanswers\u002F809101662","excerpt":"一直都知道自己是个外人啊，毕竟我也不是他们亲生的不是？！举个例子吧，偶尔假期在婆家小住，他们一家三口不论喝水还是刷牙的杯子都是一套，看着很温馨，而我的就是家里闲置的杯子拿来用，很明显地差距是不是？再比如，我妈会记得我生日，不记得我先生的生…","id":809101662,"question":{"questionType":"normal","created":1556465849,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fquestions\u002F322151072","title":"是什么情况下你才发现你在婆家是个外人的？","type":"question","id":322151072,"updatedTime":1556465849},"updatedTime":1567238726,"commentCount":0,"extras":"","answerType":"answer","createdTime":1567238726,"isCopyable":true,"type":"answer","thumbnail":"","voteupCount":1}},{"content":{"isCollapsed":false,"author":{"avatarUrlTemplate":"https:\u002F\u002Fpic4.zhimg.com\u002Faadd7b895_{size}.jpg","name":"匿名用户","headline":"","badge":[],"userType":"people","urlToken":"","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic4.zhimg.com\u002Faadd7b895_is.jpg","isOrg":false,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002F0","type":"people","id":"0"},"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fanswers\u002F777911744","excerpt":"\u003Cb\u003E禁止转载~~~~\u003C\u002Fb\u003E\u003Cb\u003E禁止转载~~~~\u003C\u002Fb\u003E\u003Cb\u003E禁止转载~~~~\u003C\u002Fb\u003E\u003Cb\u003E知道一个真事，当事人我后来认识，开始是医院的医生是我一朋友，恶婆婆送去医院的时候，我医生朋友全程聆听这事。。\u003C\u002Fb\u003E\u003Cb\u003E这件事情全程下来，我唯一感觉就是：\u003C\u002Fb\u003E\u003Cb\u003E\u003Ci\u003E女人一定要有经济实力。这世界父母可以背叛你 丈夫可以算计你，…\u003C\u002Fi\u003E\u003C\u002Fb\u003E","id":777911744,"question":{"questionType":"normal","created":1538575343,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fquestions\u002F297080993","title":"你见识过的婆婆可以坏到变态到哪种程度？","type":"question","id":297080993,"updatedTime":1562640822},"updatedTime":1566402954,"commentCount":1732,"extras":"","answerType":"answer","createdTime":1565105997,"isCopyable":false,"type":"answer","thumbnail":"","voteupCount":8661}}],"title":"节操呢？！木有！你造吗？！","url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fcollections\u002F95922523","totalCount":711,"creator":{"avatarUrlTemplate":"https:\u002F\u002Fpic1.zhimg.com\u002F7d0b1d40c_{size}.jpg","name":"张乐陶","headline":"我对愚蠢的人有耐心，除了以此为傲的那些——所谓傻×！","badge":[],"userType":"people","urlToken":"zhangletao","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic1.zhimg.com\u002F7d0b1d40c_is.jpg","isOrg":false,"gender":1,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002F1261169957a648cd9fee665962da032e","type":"people","id":"1261169957a648cd9fee665962da032e"},"isFollowing":false,"followerCount":33,"isPublic":true,"type":"collection","id":95922523},"145417966":{"favitems":[{"content":{"updated":1516337530,"author":{"avatarUrlTemplate":"https:\u002F\u002Fpic2.zhimg.com\u002Fv2-a045262a3e9e59268ae5ab6e7bd2c45c_{size}.jpg","name":"塞冬","headline":"公众号：黔财有话说，微博：北京塞冬","badge":[],"userType":"people","urlToken":"qiancai_saidong","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002Fv2-a045262a3e9e59268ae5ab6e7bd2c45c_is.jpg","isOrg":false,"gender":1,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002F9fe9fb645fe1ae399074eac8e910b667","type":"people","id":"9fe9fb645fe1ae399074eac8e910b667"},"url":"http:\u002F\u002Fzhuanlan.zhihu.com\u002Fp\u002F33078736","commentPermission":"all","title":"别笑话日本，我们的少子化将来得更惨烈","excerpt":"半个月前，一个新闻蛮火——日本年出生人口创下新低，一年只出生了94万人。 \u003Ca href=\"https:\u002F\u002Flink.zhihu.com\u002F?target=http%3A\u002F\u002Fnews.sina.com.cn\u002Fo\u002F2017-12-25\u002Fdoc-ifypwzxq6584030.shtml\" data-draft-node=\"block\" data-draft-type=\"link-card\" data-image=\"https:\u002F\u002Fpic4.zhimg.com\u002Fv2-f78901e72ebcba511e7fbcf7dccd8397_180x120.jpg\" data-image-width=\"600\" data-image-height=\"333\" class=\" wrap external\" target=\"_blank\" rel=\"nofollow noreferrer\"\u003E日本今年新生人口数创新低 空房子如瘟疫般蔓延\u003C\u002Fa\u003E 当时微信里不少朋友在转发这条新闻，许多评论都说，日本药丸了。 今天的一条新闻也比较火——2017年，中国出生了\u003Cb\u003E1723万\u003C\u002Fb\u003E人。 \u003Ca href=\"https:\u002F\u002Flink.zhihu.com\u002F?target=http%3A\u002F\u002Fnews.sina.com.cn\u002Fo\u002F2018-01-18\u002Fdoc-ifyquixe4003553.shtml\" data-draft-node=\"block\" data-draft-type=\"link-card\" class=\" wrap external\" target=\"_blank\" rel=\"nofollow noreferrer\"\u003E2017年…\u003C\u002Fa\u003E","created":1516297427,"commentCount":1978,"imageUrl":"https:\u002F\u002Fpic3.zhimg.com\u002Fv2-39e8d0e513334e746af7923bde79202f_r.jpg","excerptTitle":"","type":"article","id":33078736,"voteupCount":9936}},{"content":{"isCollapsed":false,"author":{"avatarUrlTemplate":"https:\u002F\u002Fpic2.zhimg.com\u002Fbdb7baa2d_{size}.jpg","name":"图灵Don","headline":"被收藏260000次 洞察和把握未来趋势","badge":[],"userType":"people","urlToken":"TuringDon","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic2.zhimg.com\u002Fbdb7baa2d_is.jpg","isOrg":false,"gender":1,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002F779f7b42f6798a512678c177c0290084","type":"people","id":"779f7b42f6798a512678c177c0290084"},"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fanswers\u002F126341256","excerpt":"印度现在已有13.3亿人口，几年内就将超过中国。上图还是保守了。 \u003Cb\u003E看印度人口问题，你看看中国就行\u003C\u002Fb\u003E。很多人说中国人口拐点，劳动力拐点，其实不管怎么拐，中国劳动力数量还是超过9亿人。 9亿人什么概念？美国总人口的3倍，日本8倍，德国韩国的十几倍。\u003Cb\u003E9亿人…\u003C\u002Fb\u003E","id":126341256,"question":{"questionType":"normal","created":1458402066,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fquestions\u002F41568342","title":"印度将来会人口过剩还是成为人口红利？这会在今后造成什么后果？","type":"question","id":41568342,"updatedTime":1535689043},"updatedTime":1476506321,"commentCount":76,"extras":"","answerType":"answer","createdTime":1476330003,"isCopyable":true,"type":"answer","thumbnail":"https:\u002F\u002Fpic1.zhimg.com\u002Fc91209e00a16b7764dbddbd179b633ac_200x112.jpg","voteupCount":365}}],"title":"行业研究","url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fcollections\u002F145417966","totalCount":24689,"creator":{"avatarUrlTemplate":"https:\u002F\u002Fpic3.zhimg.com\u002F408d9c256_{size}.jpg","name":"樊雪刚","headline":"知识产权法","badge":[],"userType":"people","urlToken":"fan-xue-gang","isAdvertiser":false,"avatarUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F408d9c256_is.jpg","isOrg":false,"gender":1,"url":"http:\u002F\u002Fwww.zhihu.com\u002Fapi\u002Fv4\u002Fpeople\u002F78a2df75acfee79bee47fdc5b1f417f6","type":"people","id":"78a2df75acfee79bee47fdc5b1f417f6"},"isFollowing":false,"followerCount":224,"isPublic":true,"type":"collection","id":145417966}},"columns":{"c_201557035":{"updated":1561454945,"description":"电竞GO比分情报网: www.esgo.com, 观赛2群：1025192518，水友2群：778737670（日常开黑内战聊游戏）","intro":"DOTA2赛事比分、数据资讯：esgo.com","urlToken":"c_201557035","id":"c_201557035","articlesCount":1294,"acceptSubmission":false,"title":"电竞GO","url":"https:\u002F\u002Fzhuanlan.zhihu.com\u002Fc_201557035","commentPermission":"all","created":1528791837,"imageUrl":"https:\u002F\u002Fpic1.zhimg.com\u002Fv2-ff5f252b658b6574c0284f8269c462d5_b.jpg","followers":16924,"type":"column"},"c_136968229":{"updated":1562646590,"description":"私人的，纯粹的","intro":"公众号:牙白白白，有关电影的有趣的无趣的及其他","urlToken":"c_136968229","id":"c_136968229","articlesCount":121,"acceptSubmission":true,"title":"牙白白白的电影时光","url":"https:\u002F\u002Fzhuanlan.zhihu.com\u002Fc_136968229","commentPermission":"all","created":1508986516,"imageUrl":"https:\u002F\u002Fpic3.zhimg.com\u002F4b70deef7_b.jpg","followers":197,"type":"column"},"touyanbang88":{"updated":1561693897,"description":"金融推理 | 内幕揭秘 | 独立调研 | 散户立场 | 白话解读 | 风趣幽默...这里有主流媒体上看不到的东西…最好玩的投资研究解读...","intro":"各式各样的投资idea，只用大白话说","urlToken":"touyanbang88","id":"touyanbang88","articlesCount":268,"acceptSubmission":false,"title":"闲话投资","url":"https:\u002F\u002Fzhuanlan.zhihu.com\u002Ftouyanbang88","commentPermission":"all","created":1527736905,"imageUrl":"https:\u002F\u002Fpic1.zhimg.com\u002Fv2-be8a4427259695fc9745f4f259a85ddb_b.jpg","followers":9713,"type":"column"},"investmentclub":{"updated":1563176570,"description":"入群请加助理微信：zhuliqiqi7","intro":"公众号：交易法门（ID：JMtrader）","urlToken":"investmentclub","id":"investmentclub","articlesCount":303,"acceptSubmission":false,"title":"交易法门","url":"https:\u002F\u002Fzhuanlan.zhihu.com\u002Finvestmentclub","commentPermission":"all","created":1510726895,"imageUrl":"https:\u002F\u002Fpic4.zhimg.com\u002Fv2-e11f6dd8eeee14d452cf4129eaf7ce36_b.jpg","followers":8629,"type":"column"}}},"articles":{"voters":{}},"favlists":{"relations":{}},"pins":{"voters":{}},"topstory":{"recommend":{"isFetching":false,"isDrained":false,"afterId":0,"items":[],"next":null},"follow":{"isFetching":false,"isDrained":false,"afterId":0,"items":[],"next":null},"followWonderful":{"isFetching":false,"isDrained":false,"afterId":0,"items":[],"next":null},"sidebar":null,"announcement":{},"hotListCategories":[],"hotList":[],"guestFeeds":{"isFetching":false,"isDrained":false,"afterId":0,"items":[],"next":null},"followExtra":{"isNewUser":null,"isFetched":false,"followCount":0,"followers":[]}},"upload":{},"video":{"data":{},"shareVideoDetail":{},"last":{}},"guide":{"guide":{"isFetching":false,"isShowGuide":false}},"reward":{"answer":{},"article":{},"question":{}},"search":{"recommendSearch":[],"topSearch":{},"searchValue":{},"suggestSearch":{},"attachedInfo":{},"nextOffset":{},"topicReview":{},"generalByQuery":{},"generalByQueryInADay":{},"generalByQueryInAWeek":{},"generalByQueryInThreeMonths":{},"peopleByQuery":{},"topicByQuery":{},"columnByQuery":{},"liveByQuery":{},"albumByQuery":{},"eBookByQuery":{}},"publicEditPermission":{},"readStatus":{},"draftHistory":{"history":{},"drafts":{}},"notifications":{"recent":{"isFetching":false,"isDrained":false,"isPrevDrained":false,"result":[],"next":null,"key":null},"history":{"isFetching":false,"isDrained":false,"isPrevDrained":false,"result":[],"next":null,"key":null},"notificationActors":{"isFetching":false,"isDrained":false,"isPrevDrained":false,"result":[],"next":null,"key":null},"recentNotificationEntry":"all"},"specials":{"entities":{},"all":{"data":[],"paging":{},"isLoading":false}},"collections":{"hot":{"data":[],"paging":{},"isLoading":false}},"mcn":{"bindInfo":{},"memberCategoryList":[],"categoryList":[]}},"subAppName":"main"}</script><script src="https://static.zhihu.com/heifetz/vendor.7177302d6c7d65981005.js"></script><script src="https://static.zhihu.com/heifetz/main.app.c0a62b0dd392c38e3a9e.js"></script><script src="https://static.zhihu.com/heifetz/main.explore-routes.7d178cceb955b8ce6599.js"></script></body></html>
    

---
# 基本POST请求


```python
import requests

data = {'name': 'germey', 'age': '22' }
response = requests.post('http://httpbin.org/post', data=data)
print(response.text)
```

    {
      "args": {}, 
      "data": "", 
      "files": {}, 
      "form": {
        "age": "22", 
        "name": "germey"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Content-Length": "18", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.22.0"
      }, 
      "json": null, 
      "origin": "210.32.145.58, 210.32.145.58", 
      "url": "https://httpbin.org/post"
    }
    
    


```python
import requests

data = {'name': 'germey', 'age': '22' }
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
response = requests.post('http://httpbin.org/post', data=data, headers=headers)
print(response.text)
```

    {
      "args": {}, 
      "data": "", 
      "files": {}, 
      "form": {
        "age": "22", 
        "name": "germey"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Content-Length": "18", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "Host": "httpbin.org", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
      }, 
      "json": null, 
      "origin": "210.32.145.58, 210.32.145.58", 
      "url": "https://httpbin.org/post"
    }
    
    

---
# 响应
### response属性


```python
import requests

response = requests.get('http://www.jianshu.com')
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)
```

    <class 'int'> 403
    <class 'requests.structures.CaseInsensitiveDict'> {'Server': 'Tengine', 'Content-Type': 'text/html', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Date': 'Sat, 31 Aug 2019 08:43:08 GMT', 'Vary': 'Accept-Encoding', 'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload', 'Content-Encoding': 'gzip', 'x-alicdn-da-ups-status': 'endOs,0,403', 'Via': 'cache24.l2nu16-1[4,0], cache4.cn512[25,0]', 'Timing-Allow-Origin': '*', 'EagleId': '701dc84415672409888293824e'}
    <class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[]>
    <class 'str'> https://www.jianshu.com/
    <class 'list'> [<Response [301]>]
    

### 状态码判断


```python
import requests

response = requests.get('http://www.jianshu.com')
exit() if not response.status_code == requests.codes.ok else print('Request Successfully')
```


```python
import requests

response = requests.get('http://www.jianshu.com')
exit() if not response.status_code == 200 else print('Request Successfully')
```


```python
100: { 'continus',},
101: { 'switching_protocols',},
102: { 'processing', },
103: { 'checkpoint', },
122: { 'url_too_long', 'request_url_too_long'},
200: { 'ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✔'},
201: { 'created', },
202: { 'accepted', },
203: { 'non_authoritative_info', 'non_authoritative_information'},
204: { 'no_content', },
205: { 'reset_content', 'reset'},
206: { 'partial_content', 'partial'},
207: { 'multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'},
208: { 'already_reported', },
226: { 'im_used', },

# Redirection.
300: { 'multiple_choices', },
301: { 'moved_permanently', 'moved', '\\o-'},
302: { 'found', },
303: { 'see_other', 'other' },
304: { 'not_modified', },
305: { 'use_proxy', },
306: { 'switch_proxy', },
307: { 'temporary_redirect', 'temporary_moved', 'temporary' },
308: { 'permanent_redirect', 'resume_incomplete', 'resume', },

# Client Error.
400:{ 'bad_request', 'bad'},
401:{ 'unauthorized', },
402:{ 'payment_required', 'payment'},
403:{ 'forbidden', },
404:{ 'not_found', '-o-'},
405:{ 'method_not_allowed', 'not_allowed'},
406:{ 'not_acceptable',},
407:{ 'proxy_authentication_required', 'proxy_auth', 'proxy_authentication'},
408:{ 'request_timeout', 'timeout'},
409:{ 'conflict' ,},
410:{ 'gone', },
411:{ 'length_required', },
412:{ 'precondition_failed', 'precondition'},
413:{ 'request_entity_too_large'},
414:{ 'request_url_too_large', },

# Server Error.
500: {'internal_server_error', 'server_error', '/o\\', }
501: {'not_implemented', }
502: {'bad_gateway', }
504: {'gateway_timeout'}
505: {'http_version_not_supported', 'http_version'}
```

---
# 高级操作
### 文件上传


```python
import requests

files= {'file': open('favicon.ico', 'rb')}
response = requests.post('http://httpbin.org/post', files=files)
print(response.text)
```

### 获取cookie


```python
import requests

response = requests.get('https://www.baidu.com')
print(response.cookies)
for key, value in response.cookies.items():
    print(key + '='+ value)
```

    <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
    BDORZ=27315
    

### 会话维持
#### 模拟登录


```python
import requests

requests.get('http://httpbin.org/cookies/set/number/123456789')
response = requests.get('http://httpbin.org/cookies')
print(response.text)
```

    {
      "cookies": {}
    }
    
    


```python
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)
```

    {
      "cookies": {
        "number": "123456789"
      }
    }
    
    

### 证书验证


```python
import requests

response = requests.get('https://www.12306.cn')
print(response.status_code)
```

    200
    


```python
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
```

    200
    


```python
import requests

response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)
```

### 代理设置


```python
import requests

proxies = {
    'http': 'http://127.0.0.1:9743',
    'https': 'http://127.0.0.1:9743',
}

response = requests.get('https://www.taobao.com', proxies=proxies)
print(response.status_code)
```


```python
import requests

proxies = {
    'http': 'http://user:password@127.0.0.1:9743/',
}

response = requests.get('https://www.taobao.com', proxies=proxies)
print(response.status_code)
```

    200
    


```python
pip3 install 'requests[socks]'
```


```python
import requests

proxies = {
    'http': 'socks5://127.0.0.1:9742',
    'https': 'socks://127.0.0.1:9742',
}

response = requests.get('https://www.taobao.com', proxies=proxies)
print(response.status_code)
```

### 超时设置


```python
import requests
from requests.exceptions import ReadTimeout

try:
    response = requests.get('https://httpbin.org/get', timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
```

    200
    

### 认证设置


```python
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
print(r.status_code)
```


    ---------------------------------------------------------------------------

    TimeoutError                              Traceback (most recent call last)

    D:\Anaconda3\lib\site-packages\urllib3\connection.py in _new_conn(self)
        158             conn = connection.create_connection(
    --> 159                 (self._dns_host, self.port), self.timeout, **extra_kw)
        160 
    

    D:\Anaconda3\lib\site-packages\urllib3\util\connection.py in create_connection(address, timeout, source_address, socket_options)
         79     if err is not None:
    ---> 80         raise err
         81 
    

    D:\Anaconda3\lib\site-packages\urllib3\util\connection.py in create_connection(address, timeout, source_address, socket_options)
         69                 sock.bind(source_address)
    ---> 70             sock.connect(sa)
         71             return sock
    

    TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。

    
    During handling of the above exception, another exception occurred:
    

    NewConnectionError                        Traceback (most recent call last)

    D:\Anaconda3\lib\site-packages\urllib3\connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
        599                                                   body=body, headers=headers,
    --> 600                                                   chunked=chunked)
        601 
    

    D:\Anaconda3\lib\site-packages\urllib3\connectionpool.py in _make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
        353         else:
    --> 354             conn.request(method, url, **httplib_request_kw)
        355 
    

    D:\Anaconda3\lib\http\client.py in request(self, method, url, body, headers, encode_chunked)
       1228         """Send a complete request to the server."""
    -> 1229         self._send_request(method, url, body, headers, encode_chunked)
       1230 
    

    D:\Anaconda3\lib\http\client.py in _send_request(self, method, url, body, headers, encode_chunked)
       1274             body = _encode(body, 'body')
    -> 1275         self.endheaders(body, encode_chunked=encode_chunked)
       1276 
    

    D:\Anaconda3\lib\http\client.py in endheaders(self, message_body, encode_chunked)
       1223             raise CannotSendHeader()
    -> 1224         self._send_output(message_body, encode_chunked=encode_chunked)
       1225 
    

    D:\Anaconda3\lib\http\client.py in _send_output(self, message_body, encode_chunked)
       1015         del self._buffer[:]
    -> 1016         self.send(msg)
       1017 
    

    D:\Anaconda3\lib\http\client.py in send(self, data)
        955             if self.auto_open:
    --> 956                 self.connect()
        957             else:
    

    D:\Anaconda3\lib\site-packages\urllib3\connection.py in connect(self)
        180     def connect(self):
    --> 181         conn = self._new_conn()
        182         self._prepare_conn(conn)
    

    D:\Anaconda3\lib\site-packages\urllib3\connection.py in _new_conn(self)
        167             raise NewConnectionError(
    --> 168                 self, "Failed to establish a new connection: %s" % e)
        169 
    

    NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001E5709F1F60>: Failed to establish a new connection: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。

    
    During handling of the above exception, another exception occurred:
    

    MaxRetryError                             Traceback (most recent call last)

    D:\Anaconda3\lib\site-packages\requests\adapters.py in send(self, request, stream, timeout, verify, cert, proxies)
        448                     retries=self.max_retries,
    --> 449                     timeout=timeout
        450                 )
    

    D:\Anaconda3\lib\site-packages\urllib3\connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
        637             retries = retries.increment(method, url, error=e, _pool=self,
    --> 638                                         _stacktrace=sys.exc_info()[2])
        639             retries.sleep()
    

    D:\Anaconda3\lib\site-packages\urllib3\util\retry.py in increment(self, method, url, response, error, _pool, _stacktrace)
        398         if new_retry.is_exhausted():
    --> 399             raise MaxRetryError(_pool, url, error or ResponseError(cause))
        400 
    

    MaxRetryError: HTTPConnectionPool(host='120.27.34.24', port=9001): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001E5709F1F60>: Failed to establish a new connection: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。'))

    
    During handling of the above exception, another exception occurred:
    

    ConnectionError                           Traceback (most recent call last)

    <ipython-input-21-670bda5a8072> in <module>
          2 from requests.auth import HTTPBasicAuth
          3 
    ----> 4 r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
          5 print(r.status_code)
    

    D:\Anaconda3\lib\site-packages\requests\api.py in get(url, params, **kwargs)
         73 
         74     kwargs.setdefault('allow_redirects', True)
    ---> 75     return request('get', url, params=params, **kwargs)
         76 
         77 
    

    D:\Anaconda3\lib\site-packages\requests\api.py in request(method, url, **kwargs)
         58     # cases, and look like a memory leak in others.
         59     with sessions.Session() as session:
    ---> 60         return session.request(method=method, url=url, **kwargs)
         61 
         62 
    

    D:\Anaconda3\lib\site-packages\requests\sessions.py in request(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
        531         }
        532         send_kwargs.update(settings)
    --> 533         resp = self.send(prep, **send_kwargs)
        534 
        535         return resp
    

    D:\Anaconda3\lib\site-packages\requests\sessions.py in send(self, request, **kwargs)
        644 
        645         # Send the request
    --> 646         r = adapter.send(request, **kwargs)
        647 
        648         # Total elapsed time of the request (approximately)
    

    D:\Anaconda3\lib\site-packages\requests\adapters.py in send(self, request, stream, timeout, verify, cert, proxies)
        514                 raise SSLError(e, request=request)
        515 
    --> 516             raise ConnectionError(e, request=request)
        517 
        518         except ClosedPoolError as e:
    

    ConnectionError: HTTPConnectionPool(host='120.27.34.24', port=9001): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001E5709F1F60>: Failed to establish a new connection: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。'))



```python
import requests

r = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
print(r.status_code)
```

### 异常处理


```python
import requests
from requests.exceptions import ReadTimeout, ConnectionError, HTTPError, RequestException

try:
    response = requests.get('http://httpbin.org/get', timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except ConnectionError:
    print('Connection error')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')
```

    200
    
