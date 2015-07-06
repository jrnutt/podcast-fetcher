#!python
import xml.etree.ElementTree as ET

OPMLtree = ET.parse("podcasts_opml.xml")
OPMLroot = OPMLtree.getroot()

if (OPMLroot.tag == "opml"):
    print ("have a valid opml file")
    OPMLbody = OPMLroot.find('body')
    podcasts = OPMLbody.find('outline')
    for podcast in podcasts.findall('outline'):
        podcastName = podcast.get("text")
        podcastURL = podcast.get("xmlUrl")
        podcastType = podcast.get("type")
        print (podcastName, podcastURL, podcastType)
