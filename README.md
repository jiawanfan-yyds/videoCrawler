## 环境条件
使用环境  | 版本要求
------------- | -------------
Python  | >= 3

## 开始安装

>Linux
 1. 安装Python3环境

``` shell
sudo apt-get install python3.10.9
```

 2. 安装PIP包依赖

``` shell
pip3 install -r requirements.txt
```

 3. 获得程序

``` shell
git clone 
```

## 配置

 ### 在各个目录下的`config.json`文件中填入自己的相关信息
 >bilibili的`config.json`下`html_url`中填入要爬取视频的网页链接，`cookie`中填入自己的cookie， `User-Agent`中填入自己的用户代理（可选）
 >樱花动漫的`config.json`同样

## 补充
樱花动漫开了IP代理池，如果觉得慢可以关掉代理

## 运行
``` shell
python3 bilibiliCrawler.py
```

``` shell
python3 yhdmCrawler.py
```

## 计划
[x] 已完成bilibili视频爬取
[x] 已完成樱花动漫视频爬取
[ ] 其他待续……



