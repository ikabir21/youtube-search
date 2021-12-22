from __future__ import absolute_import, unicode_literals
from django.conf import settings
import googleapiclient.discovery
from celery import shared_task
from django.db import IntegrityError
from datetime import datetime
import time
from .models import *


def save_to_db(videos):
		print(len(videos))
		for video in videos:
				print(video['snippet']['title'])
				try:
						Videos.objects.create(
								title=video['snippet']['title'],
								description=video['snippet']['description'],
								thumbnails=video['snippet']['thumbnails']['high']['url'],
								publishing_time=video['snippet']['publishedAt'],
								video_uid=video['id']['videoId']
						)
				# Process to next Video if current video already exists
				except IntegrityError:
						print("Duplicate Video")
						continue

def get_videos(query, api_service_name, api_version, api_key):
		# Try to save Videos
		try:
				youtube = googleapiclient.discovery.build(
						api_service_name,
						api_version,
						developerKey=api_key
				)
				res = youtube.search().list(
						q=query, 
      			maxResults=50,
						part="snippet", 
						order="date"
				).execute()
				print(res)
				print("Using API Key: {}".format(api_key))
				save_to_db(videos=res['items'])
    
				return True
		except googleapiclient.errors.HttpError:
				print("quota exceeded for API key: {}".format(api_key))
				return False


# Celery Task Define
@shared_task
def save_youtube_videos(query, api_service_name, api_version, api_key):

		# Validate API Key, Get Videos, Save to DB
		get_videos(query, api_service_name, api_version, api_key)


# Begining of Search
def start_youtube_search(query, api_service_name, api_version):
		# Get all the api keys provided
		api_keys = ApiKeys.objects.all()
		if (len(api_keys) == 0):
				print("Oops! No API key found...")
		else:
				# start with the first api key
				api_key = api_keys[0]
				key_count = 0
				while True:
						print("\nworking")

						# 10 seconds pause
						time.sleep(10)
						query = "cricket"
						api_service_name = "youtube"
						api_version = "v3"

						# If current API key is valid save videos to DB
						is_key_valid = get_videos(query, api_service_name, api_version, api_key)
						if not is_key_valid:
								# If current API Key is invalid try using next one
								key_count += 1
								api_key = api_keys[(api_keys.index(api_key) + 1) % len(api_keys)]

						# Stop searching if all API keys are used
						if key_count == len(api_keys):
									print("working")
									print("All api keys are exhausted...")
									break
