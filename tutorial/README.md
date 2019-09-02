### Python爬虫入门

  ##### 相关教程及文档

  - [https://www.bilibili.com/video/av19057145](https://www.bilibili.com/video/av19057145)
  - [https://www.python.org/](https://www.python.org/)
  - [https://docs.python.org/3.7/library/urllib.html](https://docs.python.org/3.7/library/urllib.html)
  - [https://2.python-requests.org//en/master/user/advanced/#advanced](https://2.python-requests.org//en/master/user/advanced/#advanced)


  ##### 适合测试爬虫的网站

  - [http://httpbin.org/](http://httpbin.org/)
  - [https://m.weibo.cn/](https://m.weibo.cn/)
  - [https://book.douban.com/](https://book.douban.com/)
    -[]

---

  #### 工具安装
  * 工具和环境：
      * Anaconda
      * Pycharm
  * 数据库：
      * MongoDB
      * Redis
      * MySQL
      * Navicat

  #### 常用的python库
  * urllib
  * requests
  * selenium+chromedriver
  * phantomjs
  * beautifulsoup4
  * pyquery
  * pymysql
  * pymongo
  * redis
  * flask+django: 代理服务器框架
  * jupyter: ```jupyter notebook```

  #### 爬虫的基本原理
  ##### 基本原理：
  请求网页并提取数据的自动化程序
  ##### 基本步骤：
  1. 发起请求 2. 获取相应内容 3. 解析内容 4. 保存数据
  ##### 爬取的目标数据
  * 网页文本：HTML、JSON数据
  * 二进制文件：图片等
  * 其他：视频等
  ##### 页面的解析方法
  * 直接处理
  * AJAX请求时当作JSON数据处理
  * 使用regex正则表达式
  * BeautifulSoup进行页面解析
  * PyQuery
  * XPath
  ##### 解决JS页面的渲染问题
  * 分析AJAX请求
  * Selenium+webdriver的解决方式
  * splash
  * PyV8+Ghost.py
  ##### 数据的保存方式
  * 保存为文本
  * 保存为关系型数据库
  * 保存为Key-Value型的非关系型数据库
  * 保存为二进制文件

  #### 结合Chrome浏览器分析Request和Response
  ##### Request请求方式：
  * get方法：在url上增加参数
  * post方法：用参数构成一个form data单独传递

  ##### url：统一资源定位符

  ##### Response响应的构成
  * 响应状态
  * 响应头
  * 响应体

  #### Urllib库
  Python内置的HTTP请求库
  ##### 参考笔记
  [https://github.com/LaplaceJack/Python_Spiders/blob/master/tutorial/python-urllib.md](https://github.com/LaplaceJack/Python_Spiders/blob/master/tutorial/python-urllib.md)

  ##### 常用方法：
  * urllib.request
  * urllib.error
  * urllib.parse
  * urllib.robotparser

  #### Requests库
  基于urllib的HTTP库
  ##### 参考笔记
  [https://github.com/LaplaceJack/Python_Spiders/blob/master/tutorial/python-requests.md](https://github.com/LaplaceJack/Python_Spiders/blob/master/tutorial/python-requests.md)

  ##### 反爬虫robot的应对方法
  设置好request header的信息

  #### 正则表达式
  对字符串进行操作的逻辑公式
  ##### 参考笔记
  [https://github.com/LaplaceJack/Python_Spiders/blob/master/tutorial/python-regex.md](https://github.com/LaplaceJack/Python_Spiders/blob/master/tutorial/python-regex.md)

  ##### 常用的匹配模式

| 模式  | 表示                     |
| ----- | ------------------------ |
| \w    | 匹配字母和数字           |
| \s    | 匹配空白符               |
| \d    | 匹配数字                 |
| ^     | 字符串开头               |
| $     | 字符串结尾               |
| {n}   | 指定出现次数             |
| .*    | 任意字符（不匹配换行符） |
| (\d+) | 定义group                |


  ##### 贪婪模式和非贪婪模式

  **贪婪匹配**：正则表达式趋于最大长度的匹配
  **非贪婪匹配**：匹配到结果就好
  **注意**：正则表达式的匹配默认为贪婪模式，在量词后面加上一个```?``` 则表示非贪婪模式

  例：
  ```python
  string str = 'abcaxc'
  pattern p = 'ab.*c'
  ```
  上例中贪婪模式的匹配结果为：```abcaxc```
  非贪婪模式的匹配结果为：```abc```

  ##### 常用到的方法
  * re.match()
  * re.search()
  * re.findall()
  * re.sub()

  ##### 正则表达式符号
  ![5cf2ba38b5afdd0192804132c9b9c557.png](en-resource://database/7292:0)


  ### BeautifulSoup4
  对请求页面进行结构解析

  ##### 参考笔记
  [https://github.com/LaplaceJack/Python_Spiders/blob/master/tutorial/python-BeautifulSoup.md](https://github.com/LaplaceJack/Python_Spiders/blob/master/tutorial/python-BeautifulSoup.md)

  ##### 可使用的解析方法
  * python标准库的解析：htmlparser
  * lxml解析
  * xml：唯一能解析xml文本
  * html5lib

  ##### 简单用例
  标签选择器：```soup.body.p.attrs['name']```
  标准选择器：```soup.find_all('ul')```
  CSS选择器：```soup.select('.panel .panel-heading')```