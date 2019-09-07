import requests, json

outputFilename = 'Ombi-Movie-Requests.xml'
ombiUrl = 'OMBI-URL'
ombiApiKey = 'OMBI-KEY'

response = requests.get(ombiUrl+'/api/v1/Request/movie', headers={
    'accept': 'application/json',
    'ApiKey': ombiApiKey,
})

movieRequests = json.loads(response.text)

## Schreibe RSS
outputFile = open(outputFilename, "w")
# Schreibe RSS
outputFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
outputFile.write("<rss version=\"2.0\">\n")
outputFile.write("<channel>\n")
outputFile.write("<title>Ombi Movie Requests</title>\n")
outputFile.write("<description>Ombi Movie Request RSS Generator for Flexget</description>\n")
#outputFile.write("<link>ombi</link>\n")
outputFile.write("<ttl> </ttl>\n")

def make_rss(tmdb_id):
	outputFile.write("<item>\n")
	outputFile.write("<tmdb_id>" + str(tmdb_id) +"</tmdb_id>\n")
	outputFile.write("</item>\n")


for req in movieRequests:
	if req['approved']:
		make_rss(req['theMovieDbId'])
		
# Schreibe RSS footer
outputFile.write("</channel>\n")
outputFile.write("</rss>")
outputFile.close()