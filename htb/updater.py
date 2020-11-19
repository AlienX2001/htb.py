# this is the updtaer script of dataset file which is a local copy of ippsec.rocks's db of links
# this is not required fuctioning of the wrapper
# it only needs to be run when the local dataset becomes a bit outdated to re-download it from ippsec.rocks's db
import requests,os

def update():
    re = requests.get("https://raw.githubusercontent.com/IppSec/ippsec.github.io/master/dataset.json")
    remote=re.text
    with open("htb/dataset") as f:
        local=f.read()
    if(remote==local):
        return "remote and local copy are same, update not needed"
    else:
        with open("htb/dataset", "w") as f:
            f.write(remote)
        return "remote and local copy were different so updated the local copy"