# Git Tarball Proxy

## Concept
- The main idea of the microservice is provide a tarball from git having only in one place your accesswide token in the organization, avoiding security risks

## Components
- Flask + Gunicorn + Docker

## Quickstart
- Edit example_settings.py with your desired settings 
- rename or copy the file to settings.py

- Build
``` sh
docker build . -t gitproxytarball
```

- Run 
``` sh
docker run --name gitproxy -p 8000:8000 gitproxytarball
```
