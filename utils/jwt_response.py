def jwt_response_payload_handler(token, user=None, request=None):
    # 自定义jwt认证返回的数据
    return {
        'token': token,
        "id": user.id,
        "username": user.username
    }