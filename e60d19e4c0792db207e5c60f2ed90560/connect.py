import requests, subprocess,os
import pyuac
from pyuac import main_requires_admin

def download_list(url,file_number):
    download_list = url
    config_link = requests.get(url).content
    with open('C:/Users/USER/vpn/'+str(file_number)+'.ovpn', 'wb') as ovpn_file:
        ovpn_file.write(config_link)

# def download_ovpn(url):
#     initial_link = "https://www.vpngate.net/en/"
#     with open('C:/Users/USER/vpn/', 'a') as tobe_download:
#         for link in tobe_download.get
def api_connection():
    pass


# @main_requires_admin
def connetion():
    file = 'vpngate_public-vpn-207.opengw.net_tcp_443.ovpn'
    path = 'C:/Users/USER/vpn/' + file
    args = [
    'openvpn',
    '--config',path
        ]
    if not pyuac.isUserAdmin():
        import ctypes
        # ctypes.windll.shell32.IsUserAnAdmin()
        pyuac.runAsAdmin()
    r = subprocess.run(args, shell=True, universal_newlines=True)
    r.stdout

    # def run():
    #     pass
connetion()

# listdir= os.listdir('C:/Users/USER/vpn2/vpn-project-iampopg/config/')
# for files in listdir:
#     file = files
#     path = 'C:/Users/USER/vpn2/vpn-project-iampopg/config/' + file
#     print(path)
#     break
	