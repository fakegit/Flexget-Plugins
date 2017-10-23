# Flexget-Plugins

Search plugins for Series and Movies. 

Supported:
* serienjunkies.org
* dokujunkies.org (experimental)
* hd-area.org
* hd-world.org
* movie-blog.org

## Installation

Just put the plugin folder next to your Flexget-Configuration.

Install BeautifulSoup4 with `pip install beautifulsoup4` and you're ready to go.

## Usage:
```  
from:
  - searchSerienjunkies:
    hoster: shareonline
    language: german
  - searchDokujunkies:
    hoster: uploaded
    language: german
```

```
from:
  - searchHdarea:
    hoster: uploaded;shareonline
  - searchHdworld:
    hoster: rapidgator
  - searchMovieBlog:
    hoster: zippyshare
```

Supported hosters:
* shareonline
* uploaded
* rapidgator
* filer
* boom
* zippyshare

Multiple hosters are supported too, just use `;` as seperator.
Don't use other hoster than listed above. 


All plugins are still in a testing-state. Feel free to contribute :-)
    
