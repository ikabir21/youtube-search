## Setup

### For postgresql setup
> 1. for linux **sudo -u postres psql** 
> 2. CREATE DATABASE <DB_NAME>;
> 3. CREATE USER &lt;username&gt; WITH PASSWORD '<password>';
> 4. ALTER ROLE &lt;username&gt; SET client_encoding TO 'utf8';
> 5. ALTER ROLE &lt;username&gt; SET default_transaction_isolation TO 'read committed';
> 6. ALTER ROLE &lt;username&gt; SET timezone TO 'UTC';
> 7. GRANT ALL PRIVILEGES ON DATABASE <DB_NAME> TO &lt;username&gt;;

### DB config
<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '&lt;DB_NAME&gt;',
        'USER': '&lt;username&gt;',
        'PASSWORD': '&lt;password&gt;',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
</pre>

### Clone and install packages
> 1. git clone https://github.com/ikabir21/youtube-search.git
> 2. cd youtube-search
> 3. for linux **python3 -m venv ./venv**
> 4. pip install -r requirements.txt 
> 5. source .env

## Run the server

> 1. ./manage.py makemigrations
> 2. ./manage.py migrate
> 3. ./manage.py createsuperuser
> 4. ./manage.py runserver

## Install rabbitmq-server
> 1. sudo apt-get install rabbitmq-server
> 2. systemctl enable rabbitmq-server
> 3. sudo systemctl start rabbitmq-server
> 4. CELERY_BROKER_URL = "amqp://myuser:mypassword@localhost:5672/myvhost" or leave empty for localhost
> 5. celery -A youtube-search worker -l info

## Features
> 1. Server calls the YouTube API continuously in background (async) with an interval of 10 seconds for fetching the latest videos for a predefined search query
> 2. A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime
> 3. Support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key
> 4. An admin panel to view the stored videos with filters and sorting options

## Screenshots

### Admin panel showing videos
<p align="center">
<img src="images/videos_admin.png">
</p>

### Admin Panel Showing Api keys
<p align="center">
<img src="images/api_key.png">
</p>

### Searched Results with pagination

<p align="center">
<img src="images/video_search.png">
</p>
<p align="center">
<img src="images/video_search2.png">
</p>