import requests,time,re
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    "cookie":"此处填你登录edusrc后的cookie"
    }
url = 'https://src.sjtu.edu.cn/rank/firm/?page='
bing = 'https://cn.bing.com/search?q='


def insertfile(elapse):
    domain_file=open("sub_domain.txt","a")
    domain_file.write(str(elapse)+"\n")
    domain_file.close()

def school_domain(url):
    for i in url:
        if "edu.cn" in i:
            d=str(i.encode('utf-8'))
            ul=re.search('[a-zA-Z0-9]+.(com|cn|net|org|biz|info|cc|tv|top|vip|edu\.cn|com\.cn)',d)
            print("域名："+i+" 提取结果为："+ul.group())
            insertfile(ul.group())
            break
def schoolsite(n):
    global bing
    for i in n:
        bingurl=bing+i
        req = requests.get(bingurl,headers=headers)
        tree=etree.HTML(req.text)
        res=tree.xpath('//div[@class="b_caption"]/div/cite/text()')
        res1=school_domain(res)

def schoolname(url):
    for i in range(1,187):
        pageurl=url+str(i)
        req = requests.get(pageurl,headers=headers)
        tree = etree.HTML(req.text)
        res = tree.xpath('//td[@class="am-text-center"]/a/text()')
        print("爬取 %s"%(res))
        schoolsite(res)




def main():
    schoolname(url)
if __name__ == "__main__":
    main()