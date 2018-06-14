#Q1
'''
An access token is an object that describes the security context of a process or thread.
The information in a token includes the identity and privileges of the user account associated with the process or thread.
Access token:
3219667436-d7hMh9fbDDWakW9zIw83ZNiuOxLkVEjQNCXvryb
'''
#q2
'''
>nslookup
Default Server:  UnKnown
Address:  192.168.43.1

> facebook.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    facebook.com
Addresses:  2a03:2880:f12f:83:face:b00c:0:25de
          157.240.16.35

> google.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4007:80f::200e
          172.217.163.174

'''

#q3
#settings->project interpreter -> install tweepy
import tweepy
consumer_key= "fKePCtpAzbVYbyQzY7kuASYWH"
consumer_secret= "pHQNVQXNPkhWYoTLFKmz2sHmmLw8XPKiE1kBfhcRrjxesDfOLv"
access_token= "708684294164602880-VpqkA6n3l0veP4NZwdSSP8jYKlAhtjX"
access_token_secret= "phxxLxzc8838dOEwxIMesIB7EI0uwY71AE1j99M0I1pIx"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
status="testing"
api.update_status(status=status)

#q4
'''
API is a part of library which defnes how an application communicates with external code.
API can be written in any language.
Library is written in same language which is a collection of all the functionalities required
for the use case.
For example, flickrj is an api client of Flickr for Java
And math is a library in Java.
'''
#q5
#settings->project interpreter -> install spotipy
import spotipy
katyperry_uri = 'spotify:artist:6jJ0s89eD6GaHleKKya26X'
spotify = spotipy.Spotify()
results = spotify.artist_albums(katyperry_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
for album in albums:
    print((album['name']))
