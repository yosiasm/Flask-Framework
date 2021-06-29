# from flask_socketio import SocketIO, emit, join_room, leave_room
# from flask import request
# import eventlet
# eventlet.monkey_patch()
# socketio = SocketIO(logger=True, engineio_logger=True)

# @socketio.on('connect')
# def connect():
#     print('connecting')
#     foo = request.args.get('satker_id')
#     join_room(foo)
#     emit('after connect', {'room': foo},room=foo)

# @socketio.on('disconnect')
# def disconnect():
#     foo = request.args.get('satker_id')
#     leave_room(foo)
#     emit('Client disconnected',{'room': foo},room=foo)

# from . import notifikasi