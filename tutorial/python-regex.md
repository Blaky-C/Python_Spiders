
# 正则表达式
### re.match


```python
re.match(pattern, string, flags=0)
```

--- 
### 最常规的匹配


```python
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
print(result)
print(result.group())
print(result.span())
```

    41
    <re.Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
    Hello 123 4567 World_This is a Regex Demo
    (0, 41)
    

### 泛匹配


```python
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())
```

    <re.Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
    Hello 123 4567 World_This is a Regex Demo
    (0, 41)
    

### 匹配目标


```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\s.*Demo$', content)
print(result)
print(result.group(1))
print(result.span())
```

    <re.Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
    1234567
    (0, 40)
    

### 贪婪匹配


```python
import re
 
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello.*(\d+).*Demo$', content)
print(result)
print(result.group(1))
```

    <re.Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
    7
    

### 非贪婪匹配


```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
```

    <re.Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
    1234567
    

### 匹配模式


```python
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content, re.S)
print(result)
print(result.group(1))
```

    <re.Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
    1234567
    

### 转义


```python
import re

content = 'price is $5.00'
result = re.match('price is $5.00', content)
print(result)
```

    <re.Match object; span=(0, 14), match='price is $5.00'>
    


```python
import re

content = 'price is $5.00'
result = re.match('price is \$5\.00', content)
print(result)
```

    <re.Match object; span=(0, 14), match='price is $5.00'>
    

总结：尽量使用泛匹配、使用括号得到匹配目标、尽量使用非贪婪模式、有换行符就用re.S
### re.search


```python
import re

content = "Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
result = re.match('Hello.*?(\d+).*?Demo', content)
print(result)
```

    None
    


```python
import re

content = "Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))
```

    <re.Match object; span=(14, 54), match='Hello 1234567 World_This is a Regex Demo'>
    1234567
    

为了匹配方便，能用search久不用match
### 匹配演练


```python
import re

html = '''
    <dl class="lemmaWgt-lemmaTitle lemmaWgt-lemmaTitle-">
<dd class="lemmaWgt-lemmaTitle-title">
<h1>微星R9270X</h1>
<li data-viewer="3" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link" style="display: inline-block;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="lock-lemma" nslog-type="10003105" target="_blank" href="javascript:;" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
<a href="/planet/talk?lemmaId=19418627" target="_blank" class="lemma-discussion cmn-btn-hover-blue cmn-btn-28 j-discussion-link" nslog-type="90000102"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_discussion-solid"></em>讨论<span class="num">999</span></a>
</dd>
</dl>
'''

result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
if result:
    print(result.group(1), result.group(2))
```

    <re.Match object; span=(116, 189), match='<li data-viewer="3" class="active">\n<a href="/3.>
    齐秦 往事随风
    


```python
import re

html = '''
    <dl class="lemmaWgt-lemmaTitle lemmaWgt-lemmaTitle-">
<dd class="lemmaWgt-lemmaTitle-title">
<h1>微星R9270X</h1>
<li data-viewer="2" class="active">
<a href="/3.mp3" singer="周杰伦">龙卷风</a>
</li>
<li data-viewer="3" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link" style="display: inline-block;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="lock-lemma" nslog-type="10003105" target="_blank" href="javascript:;" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
<a href="/planet/talk?lemmaId=19418627" target="_blank" class="lemma-discussion cmn-btn-hover-blue cmn-btn-28 j-discussion-link" nslog-type="90000102"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_discussion-solid"></em>讨论<span class="num">999</span></a>
</dd>
</dl>
'''

result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
if result:
    print(result.group(1), result.group(2))
```

    <re.Match object; span=(116, 189), match='<li data-viewer="2" class="active">\n<a href="/3.>
    周杰伦 龙卷风
    

### re.findall


```python
import re

html = '''
    <dl class="lemmaWgt-lemmaTitle lemmaWgt-lemmaTitle-">
<dd class="lemmaWgt-lemmaTitle-title">
<h1>微星R9270X</h1>
<li data-viewer="2" class="active">
<a href="/3.mp3" singer="周杰伦">龙卷风</a>
</li>
<li data-viewer="3" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link" style="display: inline-block;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="lock-lemma" nslog-type="10003105" target="_blank" href="javascript:;" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
<a href="/planet/talk?lemmaId=19418627" target="_blank" class="lemma-discussion cmn-btn-hover-blue cmn-btn-28 j-discussion-link" nslog-type="90000102"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_discussion-solid"></em>讨论<span class="num">999</span></a>
</dd>
</dl>
'''

result = re.findall('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
print(result[0], result[1])
for r in result:
    print(r)
```

    [('周杰伦', '龙卷风'), ('齐秦', '往事随风')]
    ('周杰伦', '龙卷风') ('齐秦', '往事随风')
    ('周杰伦', '龙卷风')
    ('齐秦', '往事随风')
    

### re.sub


```python
import re

content = "Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
result = re.sub('\d+','', content)
print(result)
```

    Extra strings Hello  World_This is a Regex Demo Extra strings
    


```python
import re

content = "Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
result = re.sub('\d+','Replace', content)
print(result)
```

    Extra strings Hello Replace World_This is a Regex Demo Extra strings
    


```python
import re

content = "Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
result = re.sub('(\d+)',r'\1 8910', content)
print(result)
print(result.strip())
```

    Extra strings Hello 1234567 8910 World_This is a Regex Demo Extra strings
    

### re.compile
将正则表达式编译成正则表达式对象


```python
import re

content = "Extra strings Hello 1234567 World_This is a Regex Demo Extra strings"
pattern = re.compile('Hello.*Demo', re.S)
# pattern = 'Hello.*Demo'
result = re.search(pattern, content)
print(result)
```

    <re.Match object; span=(14, 54), match='Hello 1234567 World_This is a Regex Demo'>
    

### 实战练习


```python
import requests
import re

content = requests.get('https://book.douban.com/').text
# print(content)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
print(results)
for result in results:
    url, name, author, date = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print(url, name, author, date)
```
