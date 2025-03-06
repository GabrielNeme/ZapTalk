from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
mensagens = []

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('connect')
def handle_connect():
    print("Usuário conectado")
    for mensagem in mensagens:
        emit("message", mensagem)

@socketio.on('message')
def handle_message(data):
    print(f"Mensagem recebida: {data}")
    mensagens.append(data)
    send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=8000, debug=True)