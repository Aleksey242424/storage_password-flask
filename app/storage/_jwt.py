from jwt import decode,encode

def generate_token(data,data_name):
    token = encode({f'{data_name}':data},key='secret',algorithm='HS256')
    return token

def decode_token(token):
    data = decode(token,key='secret',algorithms=['HS256'])
    return data