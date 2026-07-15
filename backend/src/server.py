import socketio
import uuid

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins="*")

rooms = {}
player_id_to_room = {}

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

@sio.event
async def create_room(sid,data):
    session = await sio.get_session(sid)
    name = data.get("name")
    player_id = session.get('player_id')
    if not player_id:
        return {"status": "error", "message": "Player ID missing in session"}
    room_code_gen = uuid.uuid4()
    room_code = str(room_code_gen)
    sio.enter_room(sid,room_code)
    player = [{
        "player_name": name,
        "player_id":player_id
    }]
    room = {
        "host_id": player_id,
        "room_code": room_code,
        "players": player,
        "status": "waiting"
    }
    rooms[room_code] = room
    player_id_to_room[player_id] = room_code
    return rooms[room_code]
@sio.event
async def join_room(sid,data):
    session = await sio.get_session(sid)
    room_code = data.get("room_code")
    name = data.get("name")
    player_id = session.get('player_id')
    if not player_id:
        return {"status": "error", "message": "Player ID missing in session"}
    if not room_code:
        return {"status": "error", "message": "Room Code missing"}
    if room_code not in rooms:
        return {"status": "error", "message": "Room Code doesnt exist"}
    sio.enter_room(sid,room_code)
    player = {
        "player_name": name,
        "player_id": player_id
    }
    rooms[room_code]["players"].append(player)
    player_id_to_room[player_id] = room_code
    await sio.emit("player_joined", {"players": rooms[room_code]["players"]}, room=room_code)
app = socketio.ASGIApp(sio)