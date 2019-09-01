
# Beautiful Soup
### 基本使用


```python
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<div id="app">
<div class="bili-header-m report-wrap-module">
<div class="nav-menu"><div class="blur-bg" style="background-image:url(//i0.hdslb.com/bfs/archive/8d6fabfc509c2ed91ae8d9d5986903c14b96b329.png);"></div><div class="nav-mask"></div><div class="nav-wrapper clearfix bili-wrapper"><div class="nav-con fl"><ul><li report-id="playpage_main" class="nav-item home"><a href="//www.bilibili.com" title="主站" class="t"><i class="header-iconfont header-icon-bilibili-tv"></i>
            主站
            <!----></a><!----></li><li report-id="Webtab_click_audio" class="nav-item mbili"><a href="//www.bilibili.com/audio/home/?type=10" target="_blank" title="来探索bilibili音乐的世界吧~" class="t">音频</a></li><li report-id="playpage_game" class="nav-item game"><a href="//game.bilibili.com" target="_blank" title="游戏中心" class="t">游戏中心</a><!----></li><li report-id="playpage_live" class="nav-item live"><a href="//live.bilibili.com" target="_blank" title="直播" class="t">直播</a><!----></li><li report-id="playpage_buy" class="nav-item buy"><a href="//show.bilibili.com/platform/home.html?msource=pc_web" target="_blank" title="会员购" class="t">会员购</a></li><li report-id="playpage_manga" class="nav-item manga"><a href="//manga.bilibili.com" target="_blank" title="漫画" class="t">漫画
              <span class="manga-publish manga-publish-home">上线</span></a><!----></li><li class="nav-item loc-menu"><a href="https://bw.bilibili.com/2019/index.html#/shanghai/" target="_blank" class="t">BW</a><!----></li><li class="nav-item loc-menu"><a href="https://www.bilibili.com/blackboard/activity-x_FCW7eIA.html" target="_blank" class="t">70年</a><!----></li><li report-id="playpage_download" class="nav-item mobile"><i class="header-iconfont header-icon-Navbar_mobile b-icon-app"></i><a id="header-mobile-app" href="//app.bilibili.com" target="_blank" title="下载APP" class="t">下载APP</a><!----></li></ul></div><div report-id="playpage_contribution" class="up-load fr"><a href="//member.bilibili.com/v2#/upload/video/frame" target="_blank" class="u-link">
          投稿
          <p class="story">...</p>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)
```

    <html>
     <head>
      <title>
       The Dormouse's story
      </title>
     </head>
     <body>
      <div id="app">
       <div class="bili-header-m report-wrap-module">
        <div class="nav-menu">
         <div class="blur-bg" style="background-image:url(//i0.hdslb.com/bfs/archive/8d6fabfc509c2ed91ae8d9d5986903c14b96b329.png);">
         </div>
         <div class="nav-mask">
         </div>
         <div class="nav-wrapper clearfix bili-wrapper">
          <div class="nav-con fl">
           <ul>
            <li class="nav-item home" report-id="playpage_main">
             <a class="t" href="//www.bilibili.com" title="主站">
              <i class="header-iconfont header-icon-bilibili-tv">
              </i>
              主站
              <!-- -->
             </a>
             <!-- -->
            </li>
            <li class="nav-item mbili" report-id="Webtab_click_audio">
             <a class="t" href="//www.bilibili.com/audio/home/?type=10" target="_blank" title="来探索bilibili音乐的世界吧~">
              音频
             </a>
            </li>
            <li class="nav-item game" report-id="playpage_game">
             <a class="t" href="//game.bilibili.com" target="_blank" title="游戏中心">
              游戏中心
             </a>
             <!-- -->
            </li>
            <li class="nav-item live" report-id="playpage_live">
             <a class="t" href="//live.bilibili.com" target="_blank" title="直播">
              直播
             </a>
             <!-- -->
            </li>
            <li class="nav-item buy" report-id="playpage_buy">
             <a class="t" href="//show.bilibili.com/platform/home.html?msource=pc_web" target="_blank" title="会员购">
              会员购
             </a>
            </li>
            <li class="nav-item manga" report-id="playpage_manga">
             <a class="t" href="//manga.bilibili.com" target="_blank" title="漫画">
              漫画
              <span class="manga-publish manga-publish-home">
               上线
              </span>
             </a>
             <!-- -->
            </li>
            <li class="nav-item loc-menu">
             <a class="t" href="https://bw.bilibili.com/2019/index.html#/shanghai/" target="_blank">
              BW
             </a>
             <!-- -->
            </li>
            <li class="nav-item loc-menu">
             <a class="t" href="https://www.bilibili.com/blackboard/activity-x_FCW7eIA.html" target="_blank">
              70年
             </a>
             <!-- -->
            </li>
            <li class="nav-item mobile" report-id="playpage_download">
             <i class="header-iconfont header-icon-Navbar_mobile b-icon-app">
             </i>
             <a class="t" href="//app.bilibili.com" id="header-mobile-app" target="_blank" title="下载APP">
              下载APP
             </a>
             <!-- -->
            </li>
           </ul>
          </div>
          <div class="up-load fr" report-id="playpage_contribution">
           <a class="u-link" href="//member.bilibili.com/v2#/upload/video/frame" target="_blank">
            投稿
            <p class="story">
             ...
            </p>
           </a>
          </div>
         </div>
        </div>
       </div>
      </div>
     </body>
    </html>
    The Dormouse's story
    

### 标签选择器


```python
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<div id="app">
<div class="bili-header-m report-wrap-module">
<div class="nav-menu"><div class="blur-bg" style="background-image:url(//i0.hdslb.com/bfs/archive/8d6fabfc509c2ed91ae8d9d5986903c14b96b329.png);"></div><div class="nav-mask"></div><div class="nav-wrapper clearfix bili-wrapper"><div class="nav-con fl"><ul><li report-id="playpage_main" class="nav-item home"><a href="//www.bilibili.com" title="主站" class="t"><i class="header-iconfont header-icon-bilibili-tv"></i>
            主站
            <!----></a><!----></li><li report-id="Webtab_click_audio" class="nav-item mbili"><a href="//www.bilibili.com/audio/home/?type=10" target="_blank" title="来探索bilibili音乐的世界吧~" class="t">音频</a></li><li report-id="playpage_game" class="nav-item game"><a href="//game.bilibili.com" target="_blank" title="游戏中心" class="t">游戏中心</a><!----></li><li report-id="playpage_live" class="nav-item live"><a href="//live.bilibili.com" target="_blank" title="直播" class="t">直播</a><!----></li><li report-id="playpage_buy" class="nav-item buy"><a href="//show.bilibili.com/platform/home.html?msource=pc_web" target="_blank" title="会员购" class="t">会员购</a></li><li report-id="playpage_manga" class="nav-item manga"><a href="//manga.bilibili.com" target="_blank" title="漫画" class="t">漫画
              <span class="manga-publish manga-publish-home">上线</span></a><!----></li><li class="nav-item loc-menu"><a href="https://bw.bilibili.com/2019/index.html#/shanghai/" target="_blank" class="t">BW</a><!----></li><li class="nav-item loc-menu"><a href="https://www.bilibili.com/blackboard/activity-x_FCW7eIA.html" target="_blank" class="t">70年</a><!----></li><li report-id="playpage_download" class="nav-item mobile"><i class="header-iconfont header-icon-Navbar_mobile b-icon-app"></i><a id="header-mobile-app" href="//app.bilibili.com" target="_blank" title="下载APP" class="t">下载APP</a><!----></li></ul></div><div report-id="playpage_contribution" class="up-load fr"><a href="//member.bilibili.com/v2#/upload/video/frame" target="_blank" class="u-link">
          投稿
          <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
          <p class="story">...</p>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
print(soup.title.string)
print(soup.title)
print(type(soup.title))
print(soup.head)
# 选择元素
print(soup.p)
# 获取名称
print(soup.title.name)
# 获取属性
print(soup.p.attrs['name'])
print(soup.p['name'])
# 获取内容
print(soup.p.string)
# 嵌套选择
print(soup.head.title.string)
```

    The Dormouse's story
    <title>The Dormouse's story</title>
    <class 'bs4.element.Tag'>
    <head><title>The Dormouse's story</title></head>
    <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
    title
    dormouse
    dormouse
    The Dormouse's story
    The Dormouse's story
    [<b>The Dormouse's story</b>]
    <list_iterator object at 0x000002195AE68E10>
    

### 子节点和子孙节点


```python
html = '''
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <div id="app">
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
                and
                
            </p>
        </div>
        <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
        <p class="story">...</p>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.p.contents)
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
    
# 获取所有子孙节点
for i, child in enumerate(soup.p.descendants):
    print(i, child)

```

    <list_iterator object at 0x000002195AE56B38>
    <p class="story">
                    Once upon a time there were three little sisters; and their names were
                    <a class="sister" href="http://example.com/elsie" id="link1">
    <span>Elsie</span>
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
                    and
                    
                </p>
    

### 父节点和祖先节点


```python
html = '''
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <div id="app">
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
                and
                
            </p>
        </div>
        <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
        <p class="story">...</p>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

print(soup.a.parent)
print(list(enumerate(soup.a.parents)))
```

    <p class="story">
                    Once upon a time there were three little sisters; and their names were
                    <a class="sister" href="http://example.com/elsie" id="link1">
    <span>Elsie</span>
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
                    and
                    
                </p>
    [(0, <p class="story">
                    Once upon a time there were three little sisters; and their names were
                    <a class="sister" href="http://example.com/elsie" id="link1">
    <span>Elsie</span>
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
                    and
                    
                </p>), (1, <div id="app">
    <p class="story">
                    Once upon a time there were three little sisters; and their names were
                    <a class="sister" href="http://example.com/elsie" id="link1">
    <span>Elsie</span>
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
                    and
                    
                </p>
    </div>), (2, <body>
    <div id="app">
    <p class="story">
                    Once upon a time there were three little sisters; and their names were
                    <a class="sister" href="http://example.com/elsie" id="link1">
    <span>Elsie</span>
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
                    and
                    
                </p>
    </div>
    <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
    <p class="story">...</p>
    </body>), (3, <html>
    <head>
    <title>The Dormouse's story</title>
    </head>
    <body>
    <div id="app">
    <p class="story">
                    Once upon a time there were three little sisters; and their names were
                    <a class="sister" href="http://example.com/elsie" id="link1">
    <span>Elsie</span>
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
                    and
                    
                </p>
    </div>
    <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
    <p class="story">...</p>
    </body></html>), (4, <html>
    <head>
    <title>The Dormouse's story</title>
    </head>
    <body>
    <div id="app">
    <p class="story">
                    Once upon a time there were three little sisters; and their names were
                    <a class="sister" href="http://example.com/elsie" id="link1">
    <span>Elsie</span>
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
                    and
                    
                </p>
    </div>
    <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
    <p class="story">...</p>
    </body></html>)]
    

### 兄弟节点


```python
html = '''
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <div id="app">
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
                and
                
            </p>
        </div>
        <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
        <p class="story">...</p>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

print(list(enumerate(soup.a.next_siblings)))
print(list(enumerate(soup.a.previous_siblings)))
```

    [(0, '\n'), (1, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>), (2, '\n                and\n                \n            ')]
    [(0, '\n                Once upon a time there were three little sisters; and their names were\n                ')]
    

# 标准选择器
### find_all(name, attrs, recursive, text, **kwargs)
### name


```python
html = '''
<div class="panel">
	<div class="panel-heading">
		<h4>Hello</h4>
	</div>
	<div class="panel-body">
		<ul class="list" id="list-1">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
			<li class="element">Jay</li>
		</ul>
		<ul class="list list-small" id="list-2">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
		</ul>
	</div>
</div>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.find_all('ul'))
print(type(soup.find_all('ul')[0]))
```

    [<ul class="list" id="list-1">
    <li class="element">Foo</li>
    <li class="element">Bar</li>
    <li class="element">Jay</li>
    </ul>, <ul class="list list-small" id="list-2">
    <li class="element">Foo</li>
    <li class="element">Bar</li>
    </ul>]
    <class 'bs4.element.Tag'>
    


```python
html = '''
<div class="panel">
	<div class="panel-heading">
		<h4>Hello</h4>
	</div>
	<div class="panel-body">
		<ul class="list" id="list-1">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
			<li class="element">Jay</li>
		</ul>
		<ul class="list list-small" id="list-2">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
		</ul>
	</div>
</div>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
```

    [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>]
    [<li class="element">Foo</li>, <li class="element">Bar</li>]
    

### attrs


```python
html = '''
<div class="panel">
	<div class="panel-heading">
		<h4>Hello</h4>
	</div>
	<div class="panel-body">
		<ul class="list" id="list-1">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
			<li class="element">Jay</li>
		</ul>
		<ul class="list list-small" id="list-2">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
		</ul>
	</div>
</div>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))

print(soup.find_all(text='Foo'))
```

    [<ul class="list" id="list-1">
    <li class="element">Foo</li>
    <li class="element">Bar</li>
    <li class="element">Jay</li>
    </ul>]
    []
    [<ul class="list" id="list-1">
    <li class="element">Foo</li>
    <li class="element">Bar</li>
    <li class="element">Jay</li>
    </ul>]
    [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>, <li class="element">Foo</li>, <li class="element">Bar</li>]
    ['Foo', 'Foo']
    

### find(name, attrs, recursive, text, **kwargs)


```python
html = '''
<div class="panel">
	<div class="panel-heading">
		<h4>Hello</h4>
	</div>
	<div class="panel-body">
		<ul class="list" id="list-1">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
			<li class="element">Jay</li>
		</ul>
		<ul class="list list-small" id="list-2">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
		</ul>
	</div>
</div>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.find('ul'))
print(type(soup.find('ul')))
print(soup.find('page'))
```

    <ul class="list" id="list-1">
    <li class="element">Foo</li>
    <li class="element">Bar</li>
    <li class="element">Jay</li>
    </ul>
    <class 'bs4.element.Tag'>
    None
    

### find_parents()  & find_parent()
### find_next_siblings  &  find_next_sibling()
### find_previous_siblings  &  find_previous_sibling()
### find_all_next()  &  find_next()
### find_all_previous()  &  find_previous()

---
# CSS选择器


```python
html = '''
<div class="panel">
	<div class="panel-heading">
		<h4>Hello</h4>
	</div>
	<div class="panel-body">
		<ul class="list" id="list-1">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
			<li class="element">Jay</li>
		</ul>
		<ul class="list list-small" id="list-2">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
		</ul>
	</div>
</div>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))
```

    [<div class="panel-heading">
    <h4>Hello</h4>
    </div>]
    [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>, <li class="element">Foo</li>, <li class="element">Bar</li>]
    [<li class="element">Foo</li>, <li class="element">Bar</li>]
    <class 'bs4.element.Tag'>
    


```python
html = '''
<div class="panel">
	<div class="panel-heading">
		<h4>Hello</h4>
	</div>
	<div class="panel-body">
		<ul class="list" id="list-1">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
			<li class="element">Jay</li>
		</ul>
		<ul class="list list-small" id="list-2">
			<li class="element">Foo</li>
			<li class="element">Bar</li>
		</ul>
	</div>
</div>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul.select('li'))
    # 获取属性
    print(ul['id'])
    print(ul.attrs['id'])
    
# 获取内容
for li in soup.select('li'):
    print(li.get_text())
```

    [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>]
    list-1
    list-1
    [<li class="element">Foo</li>, <li class="element">Bar</li>]
    list-2
    list-2
    Foo
    Bar
    Jay
    Foo
    Bar
    

## 推荐
* 推荐使用xml解析库，必要时使用html.parser
* 标签选择筛选功能弱但是速度快
* 记住常用的获取属性和文本值的方法
