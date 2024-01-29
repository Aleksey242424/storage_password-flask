from jwt import decode,encode
from flask import current_app


def generate_token(user_id):
    token = encode({'user_id':user_id},key='secret',algorithm='HS256')
    return token

def decode_token(token):
    data = decode(token,key='secret',algorithms=['HS256'])
    return data