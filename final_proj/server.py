#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj4.settings")
# import django
# if django.VERSION >= (1, 7):
#     django.setup()
import socket
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint
import world_ups_pb2 as World_Ups
ip_port = ('127.0.0.1', 12345)

sk = socket.socket()            # 
sk.bind(ip_port)                # 
sk.listen(5)                    #
print('open socket and wait client to connect...')
conn, address = sk.accept()     # 
var_int_buff = []
while True:     # 
    # client_data = conn.recv(1024).decode()      # 
    # process_data
    buf = conn.recv(1)
    var_int_buff += buf
    print(var_int_buff)
    msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
    if new_pos != 0:
        break
    print(msg_len)
    buf_message = conn.recv(msg_len)
    tmessage = World_Ups.UConnected()
    tmessage.ParseFromString(buf_message)
    id = tmessage.worldid
    # if client_data == "exit":       # 
    #     exit("end connection")
    # print("from%s and send the message:%s" % (address, client_data))
    message ='server already receive the message: ' + id
    conn.sendall(message.encode())    # feedback
conn.close()    # close connection
