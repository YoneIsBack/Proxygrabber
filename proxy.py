import sys
import requests
from collections import OrderedDict




http = ['https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
	'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
	'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
	'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
	'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt']

socks4 = ['https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
	'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
	'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
	'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
	'']

socks5 = ['https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
	'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
	'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
	'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
	'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt ']

http_https = ['https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt',
	'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http%2Bs.txt']

https = ['https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
	'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
	'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt']



def get_http():
	proxies = ""
	for x in http:
		response = requests.get(x)
		proxies = proxies + response.text
	print(proxies)
	scraped = str(len(proxies.split("\n")))


	f = open("http.txt", "w")
	f.write(proxies)
	f.close()
	print("scraped: " + scraped)


def get_https():
	proxies = ""
	for x in https:
		response = requests.get(x)
		proxies = proxies + response.text
	print(proxies)
	"\n".join(list(OrderedDict.fromkeys(proxies.split("\n"))))
	scraped = str(len(proxies.split("\n")))

	f = open("https.txt", "w")
	f.write(proxies)
	f.close()
	print("scraped: " + scraped)


if __name__ == "__main__":
	proxy_type = ''
	try:
		proxy_type = sys.argv[1]
	except:
		print("Usage: python " + sys.argv[0] + " <proxy type>\n")
		print("Proxy types:\nall\nhttp\nhttps\nsocks4\nsocks5")
		sys.exit(1)

	if proxy_type == "http":
		get_http()
	elif proxy_type == "https":
		get_https()
	else:
		print("Type error")