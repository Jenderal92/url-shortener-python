#Youtube : Py
#My Friendo : h0d3_g4n - Moslem - Kiddenta - Naskleng45
# Jenderal92 #
###MODULE###
import requests,json,sys,time,random,os
from colorama import Fore
###BANNER###
def Banner():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]

    x = '''
    _____  
^..^     \9
(oo)_____/ 
   WW  WW
URL Shortener | Python Code
1. Bit.ly Shortener
2. Chilp.it Shortener
3. Clck.ru Shortener
               
'''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.02)
Banner()

###START###

def bitly():
	try:
		url_e = raw_input("URL[ You Must Use http:// ] : ")
		shin_agent = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Content-Type': 'application/json'}
		shin_token = {
		'access_token': 'aaa3fc7cbc1eee1900b66448289b8c6b7596cb27',
		'uri': url_e ,
		'format': 'json',
		}
		shin_gets = requests.get('https://api-ssl.bitly.com/v3/shorten', headers=shin_agent, params=shin_token)
		result = shin_gets.json()
		print('--------------------------------------------------------------')
		print(Fore.GREEN + 'RESULT : '+ result['data']['url'] + Fore.WHITE)
		print('--------------------------------------------------------------')
	except: pass
def chilpit():
	try:
		url_e = raw_input("URL[ You Must Use http:// ] : ")
		shin_agent = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36',
		}
		shin_gets = requests.get('http://chilp.it/api.php?url='+url_e, headers=shin_agent).text
		print('--------------------------------------------------------------')
		print(Fore.GREEN + 'RESULT : '+ shin_gets + Fore.WHITE)
		print('--------------------------------------------------------------')
	except: pass
def clckru():
	try:
		url_e = raw_input("URL[ You Must Use http:// ] : ")
		shin_agent = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36',
		}
		shin_gets = requests.get('https://clck.ru/--?url='+url_e, headers=shin_agent).text
		print('--------------------------------------------------------------')
		print(Fore.GREEN + 'RESULT : '+ shin_gets + Fore.WHITE)
		print('--------------------------------------------------------------')
	except: pass

def Main():
	try:
		choose = raw_input('Choose Number : ' )
		if choose == '1':
			bitly()
		elif choose == '2':
			chilpit()
		elif choose == '3':
			clckru()
	except:
		pass

Main()
def ulangi():
	ulangin = raw_input("Apakah anda Ingin mengulangi program? Y/N : ")
	if ulangin=="y":
		os.system("python2 shorten.py")
	elif ulangin =="n":
		print("CODED BY SHIN_CODE")
		sys.exit()
		
ulangi()