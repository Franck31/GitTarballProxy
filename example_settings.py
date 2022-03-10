#Application
GIT_URL="https://api.github.com"
TOKEN=""
ORGANIZATION="Franck31"
BRANCH="master"
HEADERS = {
    'authorization': "token " + TOKEN,
    'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    'accept': "application/vnd.github.v3.raw",
    }
#Webserver
ENVIRONMENT = 'production'
APP_ENV = ENVIRONMENT
DEBUG = False
LOG_LEVEL = 'INFO'