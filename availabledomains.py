#!/usr/bin/python
import sys
import requests
import re
requests.packages.urllib3.disable_warnings()
' Main Function '
def main():
	domains = []
	availableD = []
	with open('domains.txt', 'r+') as f:
		for domainName in f.read().splitlines():
			domains.append(domainName)

	for line in domains:
		try:
			url = "https://www.nic.ae/masterFlow.html?_flowId=searchDomainAjax&_ky=1E20299BBEE725D3C6715DAF0F20CECA&fullDomains=" + line + "&idnLanguage=ENG&transType=RG&tag=ENG&recno=1&totaldoms=11&act=RGA"
			r = requests.get(url, verify=False)
			if "This Domain is Available" in r.text:
				print line + " is Available :)"
				availableD.append(line)
				with open('avail.txt','a') as data:
					data.write(line + '\n')
			else:
				print line + " is not available"
		except Exception, e:
			print line + ' caused error --- Exc: ' + str(e)
if __name__ == "__main__":
	print '-------------------------------'
	print '     Developed by 0d Team'
	print '-------------------------------'
	main()
