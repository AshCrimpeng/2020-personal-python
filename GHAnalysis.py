import sys
import os
import getopt
import json

def findjson(filedir): 
    filenames=os.listdir(filedir)
    with open('data.json','w',encoding = 'utf-8') as f:
        for filename in filenames:
            filepath = filedir+'\\'+filename
            for line in open(filepath,encoding = 'utf-8'):
                f.writelines(line)
    return

def count_1(data_s,username,eventname):
    cnt = 0
    for data in data_s:
        if data['actor']['login'] == username and data['type'] == eventname:
            cnt = cnt + 1
    print(cnt)
    return

def count_2(data_s,reponame,eventname):
    cnt = 0
    for data in data_s:
        if data['repo']['name'] == reponame and data['type'] == eventname:
            cnt = cnt + 1
    print(cnt)
    return

def count_3(data_s,username,reponame,eventname):
    cnt = 0
    for data in data_s:
        if data['repo']['name'] == reponame and data['repo']['name'] == reponame and data['type'] == eventname:
            cnt = cnt + 1
    print(cnt)
    return

if __name__=="__main__":
    opts,arv= getopt.getopt(sys.argv[1:],'i:u:r:e:',['user=','repo=','event=','init='])
    filedir = ""
    reponame = ""
    username = ""
    eventname = ""
    for opt in opts:
        if opt[0] == '-i' or opt[0] == '--init':
            filedir = opt[1]
            findjson(filedir)
            break
        elif opt[0] == '-u' or opt[0] == '--user':
            username = opt[1]
        elif opt[0] == '-r' or opt[0] == '--repo':
            reponame = opt[1]
        elif opt[0] == '-e' or opt[0] == '--event':
            eventname = opt[1]
    data_s=[]
    f = open('data.json','r',encoding = 'utf-8')
    for line in f.readlines():
        data_s.append(json.loads(line))
    if reponame == "" or username == "":
        if username == "":
            count_2(data_s,reponame,eventname) 
        else:
            count_1(data_s,username,eventname)
    else:
        count_3(data_s,username,reponame,eventname)
