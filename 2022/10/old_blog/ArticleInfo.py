import os
from time import localtime, strftime
import json
import re

os.chdir(os.path.dirname(__file__))

articles = os.listdir('./articles/')

if 'index.html' in articles:
    articles.remove('index.html')

ArticlesLenth = len(articles)
os.makedirs('./config/', exist_ok=True)

with open('./config/EasilyReadArticleConfig.json', 'r+', encoding='utf8') as f:
    x = f.read()
    if len(x) == 0:
        Eread = []
    else:
        Eread = json.loads(x)

TempList = []
newEread = []
EreadIndex = {}

for n, i in enumerate(Eread):
    EreadIndex[i['aid']] = i['tagList']

for n, i in enumerate(articles, 1):
    FileStat = os.stat(f'./articles/{i}')
    FileCreatedTime = FileStat.st_ctime
    FileModifedTime = FileStat.st_mtime
    with open(f'./articles/{i}', 'r', encoding='utf-8') as f:
        line = f.readline().strip()
        detail = f.readline().strip()
        detail += f.readline().strip()
    result = re.match(r'#+\s+', line)
    if result:
        CutIndex = result.span()[1]
    line = line[CutIndex:]
    StructFileCreatedTime = localtime(FileCreatedTime)
    StructFileModifedTime = localtime(FileModifedTime)
    aid = int(i.replace('.md', ''))

    EreadAidList = [int(a['aid']) for a in Eread]

    if Eread == [] or Eread == None:
        tagList = []
    else:
        if aid in EreadAidList:
            tagList = EreadIndex[aid]
        else:
            tagList = []

    TempList.append({
        "aid": aid,
        "title": line,
        "detail": detail.strip(),
        "tagList": tagList,
        "createdTime": {
            "timeStamp": FileCreatedTime,
            "tm_year": StructFileCreatedTime.tm_year,
            "tm_mon": StructFileCreatedTime.tm_mon,
            "tm_mday": StructFileCreatedTime.tm_mday,
            "tm_hour": StructFileCreatedTime.tm_hour,
            "tm_min": StructFileCreatedTime.tm_min,
            "tm_sec": StructFileCreatedTime.tm_sec,
        },
        "modifiedTime": {
            "timeStamp": FileModifedTime,
            "tm_year": StructFileModifedTime.tm_year,
            "tm_mon": StructFileModifedTime.tm_mon,
            "tm_mday": StructFileModifedTime.tm_mday,
            "tm_hour": StructFileModifedTime.tm_hour,
            "tm_min": StructFileModifedTime.tm_min,
            "tm_sec": StructFileModifedTime.tm_sec,
        }
    })


    # Eread的重写
    newEread.append({
        "aid": aid,
        "title": line,
        "tagList": tagList,
        "createdTime": strftime("%Y-%m-%d %H:%M:%S", StructFileCreatedTime),
        "modifiedTime": strftime("%Y-%m-%d %H:%M:%S", StructFileModifedTime)
    })
with open('./config/ArticleConfig.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(TempList, ensure_ascii=False))

with open('./config/EasilyReadArticleConfig.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(newEread, ensure_ascii=False))
