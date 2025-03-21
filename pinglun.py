from DrissionPage import ChromiumPage
import csv
#创建文件对象
f = open("douyin.csv",mode = "w",encoding = "utf-8",newline = "")
#字典写入方法
csv_writer = csv.DictWriter(f,fieldnames = ["地区","评论"])
#写入表头
csv_writer.writeheader()
#d打开浏览器
driver = ChromiumPage()
#监听数据包
driver.listen.start("aweme/v1/web/comment/list/")
#访问网站
driver.get("https://v.douyin.com/ifn8sn1f/ ")
for page in range(100):
    #下滑页面
    print(f"正在采集第{page+1}页的数据内容")
    driver.scroll.to_bottom()
    resp = driver.listen.wait()
#直接获取数据包响应的数据
    json_data = resp.response.body
#解析数据，提取评论数据所在列表
    comments = json_data["comments"]
    for index in comments:
        text = index['text']
        ip_label = index["ip_label"]#地区
        dit = {
        "地区":ip_label,
        "评论":text,
        }
#写入数据
        csv_writer.writerow(dit)
        print(dit)

