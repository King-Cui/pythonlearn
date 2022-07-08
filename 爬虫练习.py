import requests
import pandas as pd
# 引入panda库进行数据保存
import time


# 引入time以添加延时功能，防止被反爬

def getHTMLText(url, headers):
    # 该函数是为了打开并获取目标网站源代码文本
    try:
        r = requests.get(url=url, headers=headers, timeout=30)
        # 请求打开目标网址
        r.raise_for_status()
        # 判定打开网址是否成功
        return r
        # 返回获取的页面源代码，这里不需要.text，保留json代码格式即可，方便提取数据
    except:
        return '获取网页出错'


def getData(html, textList, attitudes_countList, comments_countList, created_atList, reposts_countList):
    for i in range(20):
        # 因为每一页保存的内容数量不一，但基本都在20以内，所以这里设置为20避免遗漏
        try:
            jsonData = html.json()['data']['list'][i]
            # 微博相关数据被保存在上述标签中
            textList.append(jsonData['text_raw'])
            attitudes_countList.append(jsonData['attitudes_count'])
            comments_countList.append(jsonData['comments_count'])
            created_atList.append(jsonData['created_at'])
            reposts_countList.append(jsonData['reposts_count'])
            # 依次保存微博文本、点赞数、评论数、发博时间、转发数数据
        except:
            pass


def saveData(textList, attitudes_countList, comments_countList, created_atList, reposts_countList):
    data = {'text_raw': textList, 'created_at': created_atList, 'reposts_count': reposts_countList,
            'attitudes_count': attitudes_countList, 'comments_count': comments_countList}
    # 将爬取的微博文本/发博时间/转赞评数据存为字典
    LidanWeiboData = pd.DataFrame(data)
    LidanWeiboData.to_excel(r'C:\Users\86155\Desktop\LidanWeiboData.xlsx')
    # 调用panda库将结果保存到本地桌面的excel表格


def main():
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62',
        'Cookie': 'XSRF-TOKEN=XUBI03dg0koDfxvLVtXuHu5k; SUB=_2AkMWugyWf8NxqwJRmfEUymniZIl0wgDEieKg5v1NJRMxHRl-yT9jqlJftRB6PToifV1vP1NgaLOi5HjPQxmR7g2dYoUZ; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5AjUN7oa_.oPMW3vzeMpcD; WBPSESS=5Gh1MjbHbWED7wnbzL0Heqj5BbJhfq8p2w7ajK0wkyS4wd4f77j-GOW1u0ouKk4ri_koJJ1vWlBivBGVPEe2BZyxpMdv82g0LanRMsHOEsQx_8V3WPz73Mu4oBsSnnKS'}

    # 此处登录网页的请求头信息需换成自己的
    basic_url = 'https://weibo.com/ajax/statuses/mymblog?uid=1288345514&page='
    # 这个URL就是前面所说的getIndex?URL
    page = 11
    # 设置page为11意味着爬取10页内容
    textList = []
    attitudes_countList = []
    comments_countList = []
    created_atList = []
    reposts_countList = []
    # 设置一些空列表分别放文本、点赞数、评论数、发博时间、转发数数据
    for i in range(1, page):
        print('正在处理第{}页内容'.format(i))
        url = basic_url + str(i)
        # 使用for循环依次打开对应页码网页
        html = getHTMLText(url, headers)
        # 调用函数获取网页源代码
        getData(html, textList, attitudes_countList, comments_countList, created_atList, reposts_countList)
        time.sleep(2)
        # 加入2秒延时防止被反爬
    saveData(textList, attitudes_countList, comments_countList, created_atList, reposts_countList)
    print('数据保存完毕')

main()