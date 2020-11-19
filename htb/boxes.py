import requests
import os

def _refresh_list(header,token):
    payload={
        'api_token': token
    }
    URL="https://www.hackthebox.eu/api/machines/get/all/"
    client = requests.get(URL, params=payload, headers={'User-Agent': header})
    with open("htb/boxlist") as f:
        existing_list=f.read()
    existing_list=eval(existing_list)
    if(client.json() == existing_list):
        return existing_list
    else:
        new_list=client.json()
        with open("htb/boxlist", "w") as f:
            f.write(str(new_list))
        existing_list=new_list
        return existing_list

def _get_box_id(header,token,name):
    existing_list=_refresh_list(header, token)
    for i in range(0,(existing_list[-1]['id'])):
        if(name==existing_list[i]['name']):
            boxid=existing_list[i]['id']
            break
        else:
            boxid=None
    if(boxid):
        return boxid
    else:
        return "Not Found"

def _get_matrix(header,token,name):
    URL="https://www.hackthebox.eu/api/machines/get/matrix/"
    payload = {
        'api_token': token
    }
    if(_get_box_id(header, token,name) == "Not Found"):
        print("Box Not Found")
        exit(-1)
    else:
        id=_get_box_id(header,token,name)
    URL=URL+str(id)
    client = requests.get(URL,params=payload ,headers={'User-Agent': header})
    machinestatus=client.json()
    if(machinestatus['success']=='1'):
        user_rating={
            'Enumeration':machinestatus['aggregate'][0],
            'Real-Life':machinestatus['aggregate'][1],
            'CVE':machinestatus['aggregate'][2],
            'Custom-Exploitation':machinestatus['aggregate'][3],
            'CTF-Like':machinestatus['aggregate'][4]
        }
        maker_rating={
            'Enumeration': machinestatus['maker'][0],
            'Real-Life': machinestatus['maker'][1],
            'CVE': machinestatus['maker'][2],
            'Custom-Exploitation': machinestatus['maker'][3],
            'CTF-Like': machinestatus['maker'][4]
        }
        final={
            'user':user_rating,
            'maker':maker_rating
        }
        return final
    else:
        return "Machine not found"

def _box_info(header, token,name):
    existing_list=_refresh_list(header, token)
    for i in range(0,(existing_list[-1]['id'])):
        if(name==existing_list[i]['name']):
            box=existing_list[i]
            break
        else:
            box=None
    if(box):
        return box
    else:
        return "Box not found"