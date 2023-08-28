import proxy_ip
import random
import os
import requests
from multiprocessing.pool import ThreadPool
from tqdm import tqdm

proxy_ip.get_main_url()
proxy_ip.check_ip()
proxy_ip.get_proxy_ip()
proxies = proxy_ip.get_proxy_ip()

proxy = {'HTTP': random.choice(proxies)}

path = r'video/'

video_name = 'test'

header = {
    'User-Agent': proxy_ip.UserAgent,
}

url = proxy_ip.data.get("url", "")

failure_list = []  # 保存下载失败的片段

if os.path.exists(path + video_name + "/"):
    pass
else:
    os.makedirs(path + video_name + "/")

def download(num, flag=0):
    url.format(num)
    with open(path + video_name + "/" + str(url).split('/')[-1][-7:], 'wb') as f:
        try:
            r = requests.get(url, proxies=proxy, headers=header, timeout=5)
            r.raise_for_status()
            r.encoding = 'utf-8'
            f.write(r.content)
            if flag == 1:
                failure_list.remove(num)

        except:
            print("请求失败！")
            if num not in failure_list:
                failure_list.append(num)

def get_video():
    files = os.listdir(path + video_name + "/")
    for file in tqdm(files, desc="正在转换视频格式："):
        if os.path.exists(path + video_name + "/" + file):
            with open(path + video_name + "/" + file, 'rb') as f1:
                with open(path + video_name + '.mp4', 'ab') as f2:
                    f2.write(f1.read())
        else:
            print("失败")

def check_ts():
    print("开始检查：")
    while failure_list:
        for num in failure_list:
            download(num,1)
    print("ts文件下载完成")
    get_video()

if __name__ == '__main__':
    #开启线程池
    pool = ThreadPool(100)
    results = pool.map(download, range(1, 354+1))
    pool.close()
    pool.join()

check_ts()