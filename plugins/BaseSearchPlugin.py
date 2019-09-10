#from __future__ import unicode_literals, division, absolute_import
import logging, json, datetime, time #, urllib, urllib2, re, , HTMLParser, requests

from bs4 import BeautifulSoup
from flexget import plugin
from flexget.entry import Entry
from flexget.components.sites.utils import normalize_unicode
from flexget.utils import requests

log = logging.getLogger("BaseSearchPlugin")

class BaseSearchPlugin(object):
    config = {}
    name = "BaseSearchPlugin"

       
    schema = {
        'type': 'object',
        'properties': {
            'hoster': {'type': 'string'}
        },
        'additionalProperties': False
    }
    
    def create_entries(self, search_result_entries):
    
        entries = set()
        for search_result_entry in search_result_entries:
            for link in search_result_entry.getLinks():
                entry = Entry()
                entry['title'] = search_result_entry.getTitle()
                entry['url'] = link
                entry['imdb_url'] = search_result_entry.getImdbUrl() ##experimental
                
                if search_result_entry.getSize() > 0:
                    entry['content_size'] = search_result_entry.getSize()
                    
                log.verbose("Entry -> Title:"+ search_result_entry.getTitle()+", Link: " + link + ", Size: "+ str(search_result_entry.getSize()))
                entries.add(entry)

        return entries
        
    