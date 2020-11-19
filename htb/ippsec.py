from os import path
def _ippsec(name):
    with open("htb/dataset") as f:
        data=f.read()
    data=eval(data)
    link=None
    for i in range(0,len(data)):
        if(data[i]["machine"]=="HackTheBox - "+name):
            vid_id=data[i]['videoId']
            link=("https://www.youtube.com/watch?v="+vid_id)
    if(link):
        return link
    else:
        return "Not Found"