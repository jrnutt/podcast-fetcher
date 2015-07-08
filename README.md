# Simple Podcast Fetcher #

## Introduction ##

This is a dead simple podcast fetcher written to scratch my personal
itch. I have a car stereo that can read MP3 files from a USB flash
drive and play them back (there is an AUX input I can plug my phone
into, but it's a soft top Jeep and the volume from my phone is
insufficient). I needed a simple way to download a set of podcasts on
a semi-regular basis and copy them to a flash drive for playback in
the car. I looked at some of the other podcast managers, but they all
try to do too much and aren't really friendly for my use case. This
particular script uses all standard Python 3 libraries and doesn't
require any additional packages.

## Setup ##

In the directory where you plan to run the script, create a directory
called "downloads", this is where the downloaded podcasts will be
put. Next, unless you want to download every edition of every podcast
in your list, use the "date" command to create the "last-fetch" file
like this:

   date --date="sometime in the past" +%s >last-fetch

See "date --help" for more information on the --date
argument.

Finally, you'll need an opml file listing all the podcasts you want to
download episodes for. You can usually export this from an RSS feed
reader or other podcast fetcher. It's a fairly simple XML file, each
outline entry has a type, text and xmlUrl entry. The type should be
"rss" for the current version of podcast-fetcher, the text is a
description of the podcast and xmlUrl is the URL of the podcast RSS
feed.

## Usage ##

Once everything is in place, simply run the script. It will load your
podcast list from the OPML file, then check each podcast feed in turn
for podcasts with a date later than the date in the "last-fetch"
file. If it finds one, it will download it into the "downloads"
directory with a name consisting of a sequential number and the
episode title. Once you've downloaded the podcasts, the rest of the
workflow is up to you. For me, I simply erase all the old podcasts off
the flash drive and copy on the new ones, then when I've listened to
them all, run the script again to pick up more.