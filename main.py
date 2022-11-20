import os
from time import sleep

import requests
from lxml import etree
from html.parser import HTMLParser

role_menu_id = 0
headers = {
    # ':authority': 'abook.hep.com.cn',
    # ':method': 'GET',
    # ':scheme': 'https',
    'cookie': '',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'
}
get_list_url = 'https://abook.hep.com.cn/selectResource.action?roleMenuId=' + str(role_menu_id)
text = requests.get(get_list_url, headers=headers).text
context_tree = etree.HTML(text)
# print(etree.tostring(context_tree).decode('utf-8'))
# 不从根节点查找
context_list = context_tree.xpath('//table/tr')
try:
    os.makedirs('./' + str(role_menu_id))
except:
    pass
for i in context_list:
    text_str = etree.tostring(i, encoding='utf-8', pretty_print=True, method="html").decode("utf-8")
    # print(text_str)
    file_name = etree.HTML(text_str).xpath("//img/@title")[0].replace(' ', '_') + '.pptx'
    file_url = "https://abook.hep.com.cn/ICourseFiles/" + etree.HTML(text_str).xpath("//input/@value")[1]
    print(file_url)
    # print(file_name)
    with open(r'./' + str(role_menu_id) + '/' + file_name, 'wb') as f:
        f.write(requests.get(file_url, headers=headers).content)
    sleep(10)
# for i in context_list:
#     print(str(i.xpath("//img/@title")))
#     # print(str(etree.tostring(i, encoding='utf-8', pretty_print=True, method="html").decode("utf-8")))
#     # break
#     # print(HTMLParser.feed(str(etree.tostring(i).decode("unicode_escape"))))
