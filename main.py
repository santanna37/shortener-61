# Imports 
import pyshorteners  

url_longa = input('URL: ')

type_tiny = pyshorteners.Shortener()

link_curto = type_tiny.tinyurl.short(url_longa)

print('link: ' + link_curto)