# CoderDojoChi v2

## Requirements
- Docker

## Installation
1. Fork this repo.
2. Run the following commands changing `USERNAME` to your GitHub username.

```bash
# Clone forked repo
git clone git@github.com:USERNAME/c2.git

# Go into project repository
cd c2

# Add upstream remote
git remote add upstream git@github.com:CoderDojoChi/c2.git

# Disable push for upstream
git remote set-url --push upstream DISABLE

# Build and run docker
docker-compose build
docker-compose up
```

## Running the App

```bash
# Running with log output
docker-compose up

# Running daemon mode (in the background)
docker-compose up -d

# Attaching a log output to already-running process
docker-compose logs web
docker-compose logs db
```

Load the website via [localhost:8000](http://localhost:8000) and going to [/admin/](http://localhost:8000/admin). The debug admin login info is:

Username: **admin@admin.com**\
Password: **coderdojochi**

---

## Management
For a full list of management options, start the app, then create a shell into the instance. the following commands:

```bash
# In one window
docker-compose up

# In another window
docker-compose run web bash
invoke --list
```

## Migrations
```bash
# Create migrations
docker-compose run web python manage.py makemigrations

# Save a single app's model as fixtures
docker-compose run web python manage.py dumpdata APP.MODEL > web/APP/fixtures/MODEL.json

# Run Migrations
docker-compose run web python manage.py migrate

```

---

## Testing
```bash
# Run all tests
docker-compose run web invoke django-test

# Run test for <app>
docker-compose run web invoke django-test <app>

# Example for 'account' app
docker-compose run web invoke django-test account
```

---

## Deployment
```bash
```
