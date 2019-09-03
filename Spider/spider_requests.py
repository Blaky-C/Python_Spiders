import requests
import re
import os
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3',
        'Cookie': '_ga=GA1.2.2060384622.1566969873; _gid=GA1.2.1298263752.1567408019; '
                  'ASMEAccess=53616c7465645f5f565aac84d629df2454ad9e922c9681df6b9faf28b80aa96303d05c197e03'
                  '5f10a167e312927b07ff482f583ea655303c48d3ba3cf5af5d4a449460f815b462dc '
    }
    session = requests.Session()
    page = session.get(url, headers=headers)
    return page.text


def download_from_txt(list_path, target_path):
    url_list = []
    with open(list_path, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            url_list.append(line)
    for i, url in enumerate(url_list):
        get_file(url, target_path)
        print("Target "+str(i+1)+" finished.\n")


def get_file(url, target):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3',
        'Cookie': '_ga=GA1.2.2060384622.1566969873; _gid=GA1.2.1298263752.1567408019; '
                  'ASMEAccess=53616c7465645f5f565aac84d629df2454ad9e922c9681df6b9faf28b80aa96303d05c197e03'
                  '5f10a167e312927b07ff482f583ea655303c48d3ba3cf5af5d4a449460f815b462dc '
    }
    file_name = url.split('/')[-1]
    obj = requests.get(url, headers=headers)
    with open(target+file_name, 'wb') as f:
        f.write(obj.content)
    # file_name = "08169126.pdf"
    # obj = requests.get(url, headers=headers)
    # # f = open(file_name, 'wb')
    # with open(file_name, 'wb') as f2:
    #     f2.write(obj.content)
    # block_sz = 8192
    # while True:

    # buffer = obj.read(block_sz)
    # if not buffer:
    #     break

    # f.write(obj.content)
    # f.close()
    # print("Download successfully." + " " + file_name)


def parse_page_with_bs4(url, html, to_path):
    soup = BeautifulSoup(html, 'lxml')
    contents = soup.select('.content')[0].find_all('a')

    url_lists = []
    for c in contents:
        # print(c.attrs['href'])
        url_lists.append(url+c.attrs['href'])

    # print(url_lists)
    print('Fetch list numbers: '+str(len(url_lists)))
    with open(to_path, 'w') as f:
        for l in url_lists:
            print(l)
            f.write(l+'\n')


def parse_parse_with_regex(html, to_path, pattern):
    print(html)


# settings:
# url = 'https://asme.pinetec.com/detc2019/data/pdfs/trk-2/'
# # content = get_html("https://dblp.uni-trier.de/db/journals/tvt/tvt67.html")
#
# content = get_html(url+'index.html')
# parse_page_with_bs4(url, content, './output/190903_asme.txt')

# download_from_txt('./output/190903_asme.txt')
get_file("https://asme.pinetec.com/detc2019/data/pdfs/trk-2/DETC2019-98440.pdf", './output/190903/')
# get_file("https://ieeexplore.ieee.org/ielx7/25/8259379/08169126.pdf?tag=1&tag=1")
