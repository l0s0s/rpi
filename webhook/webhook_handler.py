from flask import Flask, request
import os
import git

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        if data['ref'] == 'refs/heads/main':
            repo = git.Repo('/home/losos/rpi')
            origin = repo.remotes.origin
            origin.pull()
            os.system('docker-compose -f /home/losos/rpi/docker-compose.yml down')
            os.system('docker-compose -f /home/losos/rpi/docker-compose.yml up -d')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
