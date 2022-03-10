import flask    
import requests
import settings
import requests

app = flask.Flask(__name__)
app.config.from_object('settings')
app.logger.info(f'Starting app in {settings.APP_ENV} environment')

def error_messages(status_code,repo):
    if status_code == 404:
        app.logger.info(f"Repo {repo} not found in git or bad permissions")
        return ("The repo you requested is not found",404)
    if status_code == 401:
        app.logger.error("TOKEN unauthorized, please check") 
        return ("Contact your administrator, unauthorized",401)


#Request handler
@app.route('/<repo>', methods=['GET'])
def tarball(repo):
    url = "%s/repos/%s/%s/tarball/%s" % (settings.GIT_URL,settings.ORGANIZATION,repo,settings.BRANCH)
    response = requests.request("GET", url, stream=True, headers=settings.HEADERS)
    if response.status_code != 200:
        message = error_messages(response.status_code,repo)
        return (message)
    else:
        file = response.raw
        filename = repo + '.tar.gz'
        app.logger.info(f"Repo {repo} downloaded")
        return flask.send_file(file, download_name=filename, as_attachment=True)


