import requests,time

csrf=""

def _login(header, email,password):
    # this function needs assistance
    URL= "http://www.hackthebox.eu/login"
    req = requests.Session()
    client = req.get(url=URL,headers={'User-Agent':header})
    global csrf
    csrf = client.content[7274:7314]
    data ={
        "_token":csrf,
        "email":email,
        "password":password
    }
    time.sleep(3)
    client = req.post(URL,data=data,headers={'User-Agent':header})
    print(client.cookies)
    """cookies= {
        '_ga':'GA1.2.431663185.1600803235',
        'ajs_user_id':'%22348c6fda4b3e098f81e3cb56f8839638%22',
        ' __auc':'e95872d0174e251f475471ebb06',
        'cookieconsent_status':'dismiss',
        '_gid':'A1.2.1657432880.1605626186',
        '__cfuid':'d63882b703c4bed14b56eb39d42ef1a481603729550',
        'ajs_anonymous_id':'%222dededfa-f412-4b9d-a40f-0c795897c06a%22',
        'XSRF-TOKEN':client.cookies.get('XSRF-TOKEN'),
        'hackthebox_session':client.cookies.get('hackthebox_session'),
        '_gat':'1'
    }"""
    return req

def _id_by_name(header,token,name):
    URL="https://www.hackthebox.eu/api/user/id"
    data={
        'username': name,
        'api_token': token
    }
    user = requests.post(URL,data=data,headers={'User-Agent':header})
    try:
        return user.json()
    except:
        return "Not Found"

def _get_user_info(header,id):
    # this functions needs assisance
    data=login(header,"all.in.one.bot.2020@gmail.com","iG4NEFFXwVDx92j")
    print(data)
    URL="https://www.hackthebox.eu/home/users/profile/"
    URL=URL+str(id)
    info=data.get(URL,headers={'User-Agent':header})
    print(info.text)

def _user_by_identifier(header,identifier):
    URL = "https://www.hackthebox.eu/api/users/identifier/"
    URL=URL+identifier
    info=requests.get(URL,headers={'User-Agent':header})
    return info.json()