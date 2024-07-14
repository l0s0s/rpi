from flask import Flask, request, abort
import os
import git
import hmac
import hashlib

app = Flask(__name__)

SECRET_TOKEN = os.getenv('WEBHOOK_SECRET_TOKEN')

def verify_github_signature(request):
    signature = request.headers.get('X-Hub-Signature-256')
    if signature is None:
        return False

    sha_name, signature = signature.split('=')
    if sha_name != 'sha256':
        return False

    mac = hmac.new(bytes(SECRET_TOKEN, 'utf-8'), msg=request.data, digestmod=hashlib.sha256)
    return hmac.compare_digest(mac.hexdigest(), signature)

@app.route('/webhook', methods=['POST'])
def webhook():
    if not verify_github_signature(request):
        abort(403)

    data = request.json
    if data['ref'] == 'refs/heads/main':
        repo = git.Repo('/home/losos/rpi')
        origin = repo.remotes.origin
        origin.pull()
        os.system('docker-compose -f /home/losos/rpi/docker-compose.yml down')
        os.system('docker-compose -f /home/losos/rpi/docker-compose.yml up -d')
        return 'Updated successfully', 200
    return 'Invalid request', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
