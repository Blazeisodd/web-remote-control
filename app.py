# Python Flask Server for Web Remote Control
from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'remote-control-secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Serve the main page
@app.route('/')
def index():
    return send_from_directory('public', 'client.html')

# Handle socket connections
@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')
    emit('status', {'message': 'Connected to server'})

@socketio.on('disconnect')
def handle_disconnect():
    print(f'Client disconnected: {request.sid}')

# Relay signaling data between peers
@socketio.on('signal')
def handle_signal(data):
    print(f"Signal from {request.sid} to {data.get('to')}")
    emit('signal', {
        'from': request.sid,
        'signal': data.get('signal')
    }, room=data.get('to'))

# Broadcast list of connected clients
@socketio.on('request-peers')
def handle_request_peers():
    # Get all connected clients except the requester
    from flask_socketio import request
    all_clients = list(socketio.server.manager.rooms['/'].keys())
    peers = [sid for sid in all_clients if sid != request.sid]
    emit('peer-list', peers)

# Handle mouse/keyboard events
@socketio.on('control-event')
def handle_control_event(data):
    print(f"Control event: {data.get('type')}")
    # You would process mouse/keyboard commands here
    emit('control-response', {'status': 'received', 'data': data})

if __name__ == '__main__':
    print('🖥️  Web Remote Control Server')
    print('Starting server on http://localhost:3000')
    print('Press Ctrl+C to stop\n')
    socketio.run(app, host='0.0.0.0', port=3000, debug=True)
