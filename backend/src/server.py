import socketio

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins="*")

@sio.event
async def connect(sid, environ, auth):
    if not auth:
        raise socketio.exceptions.ConnectionRefusedError('Authentication missing')
    
    player_id = auth.get('player_id')
    if not player_id:
        raise socketio.exceptions.ConnectionRefusedError('Player ID missing')
    
    await sio.save_session(sid, {'player_id': player_id})
    
    print(f"Player {player_id} connected on socket {sid}")

@sio.event
async def disconnect(sid):
    print(f"Player ID {sid} has disconnected")

app = socketio.ASGIApp(sio)