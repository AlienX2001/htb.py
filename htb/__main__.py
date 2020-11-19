import htb.boxes as b
import htb.users as u
import htb.ippsec as i

header="Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko"

# all commands related to users

def login(email,password):
    #has issues
    return u._login(header,email,password)

def id_by_name(token,name):
    return u._id_by_name(header,token,name)

def get_user_info(userid):
    #has issues
    return u._get_user_info(header,userid)

def user_by_identifier(identifier):
    try:
        return u._user_by_identifier(header,identifier)
    except:
        return "User Not Found"

# all commands related to boxes

def get_matrix(token,name):
    try:
        return b._get_matrix(header, token, name)
    except:
        return "Box not Found"

def box_info(token,name):
    return b._box_info(header, token, name)

# ippsec walkthroughs

def walkthrough(name):
    return i._ippsec(name)