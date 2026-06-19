import socketio

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins="*")

@sio.event
async def connect(sid,environ):
    pass

@sio.event
async def disconnect(sid):
    pass