#!/usr/bin/python3
import xml.etree.ElementTree as ET
import urllib.request
import os
from datetime import datetime
from datetime import timedelta
from datetime import timezone

downloaddir = "downloads"

with open("last-fetch","r") as f:
    earliest = float(f.readline())
f.close()

OPMLtree = ET.parse("podcasts_opml.xml")
OPMLroot = OPMLtree.getroot()

count = 0

if (OPMLroot.tag == "opml"):
    OPMLbody = OPMLroot.find('body')
    podcasts = OPMLbody.find('outline')
    for podcast in podcasts.findall('outline'):
        podcastName = podcast.get("text")
        podcastURL = podcast.get("xmlUrl")
        podcastType = podcast.get("type")
        print (podcastName, podcastURL, podcastType)
        with urllib.request.urlopen(podcastURL) as f:
            podcastRoot = ET.fromstring(f.read())
            for channel in podcastRoot.findall('channel'):
                for item in channel.findall('item'):
                    title = item.find('title');
                    enclosure = item.find('enclosure')
                    try: 
                        localDate = datetime.strptime(item.find('pubDate').text,"%a, %d %b %Y %H:%M:%S %z")
                    except:
                        localDate = datetime.strptime(item.find('pubDate').text,"%a, %d %b %Y %H:%M:%S %Z")
                    date = localDate.timestamp()
                    if (date < earliest):
                        continue
                    filename = "{2}/{0:02d}-{1}.mp3".format(count,"".join(x for x in title.text if x.isalnum()),downloaddir)
                    count = count + 1
                    url = enclosure.get('url')
                    print("downloading {0} from {1} to {2}".format(title.text, url, filename))
                    try: 
                        urllib.request.urlretrieve(url, filename)
                    except:
                        print("failed to download podcast from {0}".format(url))

with open("last-fetch","w") as f:
    f.write(str(datetime.now().timestamp()))
f.close()
        
