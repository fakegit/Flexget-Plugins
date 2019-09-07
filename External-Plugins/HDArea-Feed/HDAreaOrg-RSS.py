import feedparser, re, urllib.request, urllib.error, urllib.parse, requests
from bs4 import BeautifulSoup 

quality = "1080p"
hoster = "shareonline"			 # uploaded;uplaoded;oboom;cloudzer;filemonkey
outputFilename = "HDArea.xml"   # wo soll die rss-datei gespeichert werden ?

## Schreibe RSS
outputFile = open(outputFilename, "w")
# Schreibe RSS
outputFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
outputFile.write("<rss version=\"2.0\">\n")
outputFile.write("<channel>\n")
outputFile.write("<title>HDAreaOrg RSS-Generator</title>\n")
outputFile.write("<description>Hd-area.org RSS Generator for Flexget</description>\n")
outputFile.write("<link>Hd-area.org</link>\n")
outputFile.write("<ttl> </ttl>\n")

def clean_hoster(hoster):
	hoster = hoster.lower().replace('-','').replace(' ','')
	hoster = hoster.replace('.biz','').replace('.net','')
	return hoster

def make_rss(title, link):
	outputFile.write("<item>\n")
	outputFile.write("<title>"+title+"</title>\n")
	outputFile.write("<link>"+link+"</link>\n")
	outputFile.write("</item>\n")

def replaceUmlauts(title):
	title = title.replace(chr(228), "ae").replace(chr(196), "Ae")
	title = title.replace(chr(252), "ue").replace(chr(220), "Ue")
	title = title.replace(chr(246), "oe").replace(chr(214), "Oe")
	title = title.replace(chr(223), "ss")
	title = title.replace('&amp;', "&")
	title = "".join(i for i in title if ord(i)<128)
	return title

def get_download(hda_url, rls_title):
	req_page = requests.get(hda_url).text
	soup_ = BeautifulSoup(req_page, "html.parser")
	links = soup_.findAll("span", {"style":"display:inline;"})
	for link in links:
		url = link.a["href"]
		if hoster.lower() in clean_hoster(link.text):
			make_rss(rls_title,url)
	
for site in ('top-rls','neues','movies'): #
	for pg in ('1','2','3'):
		address = ('http://hd-area.org/index.php?pg='+pg+'&s=' + site)
		page = urllib.request.urlopen(address).read()
		soup = BeautifulSoup(page, "html.parser")
		for all in soup.findAll("div", {"class" : "topbox"}):
			for title in all.findAll("div", {"class" : "title"},limit=1):
				a = title.a
				title = a.get("title")
				url = a.get("href")
				
				#title = title.getText()
				title = replaceUmlauts(title)
				season = re.compile('.*S\d|\Sd{2}|eason\d|eason\d{2}.*')
				if (quality in title) and not season.match(title):
					get_download(url, title)

# Schreibe RSS footer
outputFile.write("</channel>\n")
outputFile.write("</rss>")
outputFile.close()
