# Postgres on Docker

## Why?

* Separate Postgres via Docker. But I use Orbstack instead of Docker on my Mac
* Didn't want Postgres to be locally installed, having a separate container makes it easy to deploy for different projects or situation
  
## Quick Start

* Install [HomeBrew](https://brew.sh)
* Install OrbStack. This is a faster & better version of Docker on MacOS
```
% brew install orbstack
```
* Install [GitHub Desktop for Mac](https://github.com/apps/desktop)
* File | Clone Repository | URL: ```https://github.com/danielpoon/postgres-docker.git```
* In a terminal:
```
% cd ~/Documents/GitHub/postgres-docker
% cp env-example .env
```
* Edit the .env file ```% nano .env```
* Build and start the containers by using the start.sh and stop.sh will be faster than typing docker commands
```
% sh ./start.sh
```
That's it. You should be able to test it with
```
% python connection-test.py
```

## The Details

- We're using Postgres 17 using default port 5432
- Database data mapped to : /var/lib/postgresql/data
- Self-restart if down
- Nothing fancy, no SSL
