# This is a sample Python script.
from docker import APIClient
from docker import DockerClient
from flask import Flask
from flask import request
from flask_cors import CORS
from flask import render_template
from flask import redirect
from flask import jsonify
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
app = Flask(__name__, static_folder='static')
CORS(app)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
base_tcp_url = config['DOCKER']['TCP_URL']

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

@app.route('/containers', methods=['GET'])
def list_containers():
    cli = APIClient(base_url=base_tcp_url)
    containers = cli.containers(all=True)
    return jsonify(containers)

@app.route('/container/start', methods=['POST'])
def start_container():
    if request.method == 'POST':
        data = request.json
        print(data)
        containerId = data['containerId']
        cli = APIClient(base_url=base_tcp_url)
        try:
            cli.start(container=containerId)
            response = {'reposta':'Foi que foi'}
        except:
            response = {'reposta': 'Erro'}
        return jsonify(response)

@app.route('/gui/', defaults={'path': ''})
@app.route('/gui/<path:path>')
def catch_all(path):
    _path = path.lower().strip()

    if path in ["", "/", None]:
        return app.send_static_file("gui/index.html")

    elif _path.endswith(".css"):
        return app.send_static_file("gui/"+path)

    elif _path.endswith(".ico"):
        return app.send_static_file("gui/"+path)

    elif _path.endswith(".js"):
        return app.send_static_file("gui/"+path)

    return app.send_static_file("gui/index.html")


@app.route('/container/stop', methods=['POST'])
def stop_container():
    if request.method == 'POST':
        data = request.json
        print(data)
        containerId = data['containerId']
        cli = APIClient(base_url=base_tcp_url)
        try:
            cli.stop(container=containerId)
            response = {'reposta': 'Foi que foi'}
        except:
            response = {'reposta': 'Erro'}
        return jsonify(response)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config['DEFAULT']['Port'], debug=config['DEFAULT']['Debug'])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
