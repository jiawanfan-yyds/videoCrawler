import requests
import re
import subprocess
import json

json_file_path = "config.json"

# 读取JSON文件中的数据
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

html_url = data.get("html_url", "") #要爬取的网页链接
cookie = data.get("cookie", "") #自己的cookie
UserAgent = data.get("User-Agent", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188')

headers = {
    'referer': 'https://www.bilibili.com/',
    'User-Agent': UserAgent, #输入自己的用户代理
    "Cookie": cookie,
}

response = requests.get(url=html_url,headers=headers,timeout=10)

# with open('response.txt', 'w') as f:
#     f.write(response.text)

#提取视频标题
video_name = re.findall('"title":"(.*?)",',response.text)[0].replace(' ','')

print(video_name)

#提取视频信息
html_data = re.findall('<script>window.__playinfo__=(.*?)</script>',response.text)[0]
#转成json字典数据
json_data = json.loads(html_data)
# pprint.pprint(json_data)

#默认无大会员，取[0]为id为80，即取高清1080p
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
video_url = json_data['data']['dash']['video'][0]['baseUrl']
# print(video_url)

video_content = requests.get(url=video_url,headers=headers).content
audio_content = requests.get(url=audio_url,headers=headers).content

with open(video_name + '.mp4', mode='wb') as video:
    video.write(video_content)

with open(video_name + '.mp3', mode='wb') as audio:
    audio.write(audio_content)

#合并音视频
cmd = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental {video_name}output.mp4'
subprocess.run(cmd,shell=True)
