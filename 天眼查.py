import requests
from lxml import etree


class TianYanCha():

    def __init__(self, url):

        self.data = ""
        self.url = url

        # 请求头
        self.headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62",
            "Cookie": "XSRF-TOKEN=XUBI03dg0koDfxvLVtXuHu5k; SUB=_2AkMWugyWf8NxqwJRmfEUymniZIl0wgDEieKg5v1NJRMxHRl-yT9jqlJftRB6PToifV1vP1NgaLOi5HjPQxmR7g2dYoUZ; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5AjUN7oa_.oPMW3vzeMpcD; WBPSESS=5Gh1MjbHbWED7wnbzL0Heqj5BbJhfq8p2w7ajK0wkyS4wd4f77j-GOW1u0ouKk4ri_koJJ1vWlBivBGVPEe2BZyxpMdv82g0LanRMsHOEsQx_8V3WPz73Mu4oBsSnnKS",
            "Content-Type": "application/json; charset=UTF-8",
            "Accept-Encoding": "gzip, deflate, br"
        }

        self.item_list = {} # 存储队列

    def zhixing(self):

        self.response = requests.get(url=self.url, headers=self.headers).text  # 起始URL
        # print(self.response)

        self.fen1 = etree.HTML(self.response)

        self.datas1 = self.fen1.xpath(
            '//div[@class="search-result-single   "]/div[@class="content"]/div[@class="header"]/a/@href')

        # print(self.datas1) # 详情页url
        for self.dataaa in self.datas1:
            self.urls = self.dataaa # 详情页url地址
            # print(self.urls)

    def xiang_qing(self):

        import time
        time.sleep(1)
        self.response_content = requests.get(url=self.urls, headers=self.headers).text

        self.datalist = etree.HTML(self.response_content)

        self.datas = self.datalist.xpath('//div[@class="box -company-box "]')

        # 公司数据
        for self.data in self.datas:
            self.item_list["公司名称"] = self.data.xpath('./div[@class="content"]/div[@class="header"]/h1/text()')
            self.item_list['注册资本'] = self.data.xpath(
                '//*[@id="_container_baseInfo"]/table[2]/tbody/tr[1]/td[2]/div/text()')
            self.item_list['成立日期'] = self.data.xpath(
                '//*[@id="_container_baseInfo"]/table[2]/tbody/tr[2]/td[2]/div/text()')
            self.item_list['行业'] = self.data.xpath('//*[@id="_container_baseInfo"]/table[2]/tbody/tr[5]/td[4]/text()')
            self.item_list['注册地址    '] = self.data.xpath(
                '//*[@id="_container_baseInfo"]/table[2]/tbody/tr[10]/td[2]/text()')
            self.item_list['经营范围'] = self.data.xpath(
                '//*[@id="_container_baseInfo"]/table[2]/tbody/tr[11]/td[2]/span/text()')
            self.item_list['法定代表人'] = self.data.xpath(
                '//*[@id="_container_baseInfo"]/table[1]/tbody/tr[1]/td[1]/div/div[1]/div[2]/div[1]/a/@title')

        print(self.item_list)


if __name__ == '__main__':
    for i in range(1,100):
        url = "https://www.tianyancha.com/company/2310290454"+str(i)+"?key=%E5%9B%BD%E5%AE%B6%E7%94%B5%E7%BD%91" # 分页

        tianyancha = TianYanCha(url)
        tianyancha.zhixing()
        tianyancha.xiang_qing()
