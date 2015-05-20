__author__ = 'palash'
import urllib.request
url = 'http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_'
encoding ='ISO-8859-2'
startindex = 373
endindex = -17
word_dict = {}

for i in range(97,123):
    final_url = url + chr(i) + '.html'
    response = urllib.request.urlopen(final_url)
    html = response.read()
    html = html.decode(encoding)
    html = html[startindex:endindex]
    index = 0
    w = ''
    count = 0
    key = ''
    while index < len(html):
        if html[index] == '<':
            while html[index]!='>':
                index =  index + 1
                if html[index] == 'P' and html[index-1]=='/':
                    count = 0
                    w = ''
            index = index + 1
        else:
            w = w + html[index]
            index = index + 1
            if index < len(html) and html[index] == '(' and count == 0:
                if len(w) > 2:
                    key = w[1:]
                else:
                    key = w
                key = key[:-1]
                duplicate_key = key.lower()
                count = count + 1
                while html[index] != ')':
                    index = index + 1
                index = index + 1
                value = ''
                while html[index]!='<':
                    value = value + html[index]
                    if index == len(html):
                        break
                    else:
                        index = index + 1
                value = value[1:]
                if key not in word_dict.keys():
                    word_dict[key] = value
                    word_dict[duplicate_key] = value
                else:
                    word_dict[key] = word_dict[key] + '/' +  value
                    word_dict[duplicate_key] = word_dict[duplicate_key] + '/' + value