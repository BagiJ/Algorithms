import urllib2 
import urllib 
import json 

def search(query): 

    url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&" 

    query = urllib.urlencode( {'q' : query } ) 
    response = urllib2.urlopen (url + query ).read() 
    data = json.loads ( response ) 
    results = data [ 'responseDetails' ]

    print results
    return results
