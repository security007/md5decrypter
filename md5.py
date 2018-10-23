#/usr/bin/python
import requests
import random
import re
import sys
import time

def api(x):
	print "[+] Wait! i'm doing my job"
	ua = ["Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)"]
	req = requests.get("https://md5.pinasthika.com/api/decrypt?value="+x, headers = {'User-agent': random.choice(ua)}).text
	cek = re.findall("\"result\":\"(.+?)\"}",req)
	code = re.findall("\"result\":{\"status\":{\"code\":(.+?),\"description\"",req)

	for a in code:
		if (a != 200):
			print "[x] Not found hashes"
			sys.exit()
	for b in cek :
		print "[*] Found ===>",b
		print "[+] Zuhahaha I'm the best :v"
def brute(hash,wordlist):
	buka = open(wordlist,'rb')
	baca = buka.readlines()
	print "[+] Searching..."
	for x in baca:
		ua = ["Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)"]
		req = requests.get("https://md5.pinasthika.com/api/encrypt?value="+x.rstrip("\r\n"), headers = {'User-agent': random.choice(ua)}).text
		cek = re.findall("\"result\":\"(.+?)\"}",req)
		for xx in cek:
			if (xx == hash):
				print "="*100
				print "[*] w00t!! I found this fucking bitch!! ==>",hash,"::",x,
				print "[+] I'm the best :v"
				print "="*100
				sys.exit()
			else:
				print "[-]",xx,"==>",hash,"[ Doesn't match ]"
def main():
	banner = """

               _ _____   _____                             _            
              | | ____| |  __ \                           | |           
 _ __ ___   __| | |__   | |  | | ___  ___ _ __ _   _ _ __ | |_ ___ _ __ 
| '_ ` _ \ / _` |___ \  | |  | |/ _ \/ __| '__| | | | '_ \| __/ _ \ '__|
| | | | | | (_| |___) | | |__| |  __/ (__| |  | |_| | |_) | ||  __/ |   
|_| |_| |_|\__,_|____/  |_____/ \___|\___|_|   \__, | .__/ \__\___|_|   
 CODED BY : SECURITY007                         __/ | |                 
                                               |___/|_|                 
											   """
	print banner
	pilihan = """
Options:
1. API
2. BRUTEFORCE
0. Exit
	
	"""
	print pilihan
	pilih = raw_input("Choose options [1/2] $> ")
	if (pilih == "1"):
		hash = raw_input("MD5 $> ")
		api(hash)
		raw_input('Press any key to continue')
		return main()
	elif (pilih == "2"):
		hash = raw_input("MD5 $> ")
		wl = raw_input("Wordlist $> ")
		try:
			brute(hash,wl)
		except IOError:
			print "[Errno 2] No such file or directory: "+wl
			return main()
		except:
			print "[x] Connection error"
		raw_input('Press any key to continue')
		return main()
	elif (pilih == "0"):
		print "[:'(] Bye.."
		time.sleep(1)
		sys.exit()		
	else:
		print "Wrong input"
		return main()
if __name__ == "__main__":
	main()

