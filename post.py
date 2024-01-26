#!/usr/bin/env python3

from mastodon import Mastodon
import csv, random, configparser

# read config
config = configparser.ConfigParser()
config.read('config.ini')

# initialize pytooter
mastodon = Mastodon(access_token = 'pytooter_usercred.secret')

# define post
postText = config['Post']['Text']
mediaDescription = config['Post']['MediaDescription']
mediaFilename = config['Post']['MediaFilename']

if config['Bot'].getboolean('DryRun'):
  print(postText)
  print(mediaDescription)
  print(mediaFilename)
else:
  media = mastodon.media_post(media_file = mediaFilename, description = mediaDescription) # upload media
  mastodon.status_post(status = postText, visibility = "unlisted", media_ids = media) # do the posting