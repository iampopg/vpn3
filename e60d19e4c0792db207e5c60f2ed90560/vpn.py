# import runasAdminJan
import requests,base64, tempfile, subprocess, time, pyuac

    # x = runasAdmin
    # print('running runing running')
api = 'http://www.vpngate.net/api/iphone/'

# print(api_server)

def select_server(list):
    
        x=1
        while x <=len(list):
            for i in list:
                print(x,i)
                # break
                x+=1
        county = input('enter county name in full: ')
        if county in list:
            return county
        else:
            print('wrong input, try again')
            exit()

def pick_server(supported):
    winner = sorted(supported, key=lambda s: float(s[2].replace(',','.')), reverse=True)[0]
    # print(winner)
    return winner

def connection(winner):
    # import runasAdmin
    _, path = tempfile.mkstemp()
    f = open(path, 'w')
    f.write(base64.b64decode(winner[-1]).decode('utf-8'))
    # f.write('\nscript-security 2\nup \\Program Files\\OpenVPN\\config\ndown \\Program Files\\OpenVPN\\config')
    f.close()
    if not pyuac.isUserAdmin():
        # pyuac.runAsAdmin()
        pass
    x = subprocess.Popen(['openvpn', '--config', path])
    try:
        while True:
            time.sleep(6)
        # termination with Ctrl+C
    except:
        try:
            x.kill()
        except:
            pass
        while x.poll() != 0:
            time.sleep(1)
        print('\nVPN terminated')
        # print(winner)

if __name__ == '__main__':
    try:
        
        print('im here in try')
        vpn_data = requests.get(api).text.replace('\r','')
        servers = [line.split(',') for line in vpn_data.split('\n')]
        servers = [s for s in servers[2:] if len(s) > 1]

    except NameError:
        pass
    serv_list = []
    for i in servers:
        serv_list.append(i[5])
       
    serv_list = list(set(serv_list))

    desired = select_server(serv_list)
    print(desired, type(desired))
   
    # num_serv =  [s for s in servers]
    # print(type(num_serv[0][5]))
    # print(type('ssh'))

    
    num_serv =  [s for s in servers if desired in s[5] ]

    supported = [s for s in num_serv if len(s[-1]) > 0]
    # print('supposeted' +str(supported))
    print('{0}  of  {1}  servers support OpenVPN'.format(str(len(supported)), desired ))

    winner = pick_server(supported)
    # print('winner here'+ str(winner))
    print("\n\n The speed of the selected server is : {} MBps\n\n".format(str(float(winner[4]) / 10**6)))
    print("please wait connecting to the vpn server.......")
    connection(winner)
        
    print('Thnakyou for using us')