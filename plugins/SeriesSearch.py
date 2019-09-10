# -*- coding: utf-8 -*-
import logging, re, html.parser #, urllib, urllib2, json, requests

from flexget import plugin
from flexget.event import event
from flexget.utils.tools import parse_filesize
from flexget.components.sites.utils import normalize_unicode

from .BaseSearchPlugin import BaseSearchPlugin
from .SerienjunkiesApi import SerienjunkiesApi

log = logging.getLogger("SeriesSearchPlugin")
LANGUAGE = ['english', 'german']


DEFAULT_LANG = 'german'
DEFAULT_HOST = 'shareonline'

class SearchSerienjunkies(BaseSearchPlugin):

    schema = {
        'type': 'object',
        'properties': {
            'hoster': {'type': 'string'},
            'language': {'type': 'string', 'enum': LANGUAGE},
        },
        'additionalProperties': True
    }
    
    """
        Serienjunkies search plugin.
    """
    name = "searchSerienjunkies"
    def search(self, task, entry, config):
        api = SerienjunkiesApi( config )
        results = api.search(entry.get('search_strings', [entry['title']]))
        return self.create_entries(results)

@event('plugin.register')
def register_plugin():
    plugin.register(SearchSerienjunkies, 'searchSerienjunkies', interfaces=['search'], api_ver=2)
    
