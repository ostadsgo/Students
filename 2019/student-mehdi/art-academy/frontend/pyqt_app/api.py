import requests

HOST = 'http://127.0.0.1:8000'
BASE_URL = f'{HOST}/api/v1'
AUTH = ('admin', '123admin')

schemas = {
    'users': f'{BASE_URL}/users/',
}


def check_status(method, response):
    if method == 'GET' or method == 'PUT':
        return response.status_code == 200
    elif method == 'POST':
        return response.status_code == 201
    elif method == 'DELETE':
        return response.status_code == 204
    else:
        return 'Methods have to be [GET, POST, PUT, DELETE]'


def get_users():
    r = requests.get(schemas.get('users'), auth=AUTH)
    return r


def add_user(username, password):
    data = {'username': username, 'password': password}
    r = requests.post(schemas.get('users'), data=data, auth=AUTH)
    return r


def udpate_user(user_id, username, password, new_user=None, new_pass=None):
    data = {'user_id': user_id, 'username': username, 'password': password}

    if new_user is not None:
        data['username'] = new_user
        if new_pass is not None:
            data['password'] = new_pass
        r = requests.put(schemas.get('users') + f'{user_id}/', data=data, auth=AUTH)
    elif new_pass is not None:
        data['password'] = new_pass
        r = requests.put(schemas.get('users') + f'{user_id}/', data=data, auth=AUTH)
    return r


def udpate_user2(username, password, new_user=None, new_pass=None):
    data = {'username': username, 'password': password}

    if new_user is not None:
        data['username'] = new_user
        if new_pass is not None:
            data['password'] = new_pass
        r = requests.put(schemas.get('users') + f'{username}/', data=data, auth=AUTH)
    elif new_pass is not None:
        data['password'] = new_pass
        r = requests.put(schemas.get('users') + f'{username}/', data=data, auth=AUTH)

    return r


def delete_user(user_id):
    data = {'user_id': user_id}
    r = requests.delete(f'{schemas.get("users")}{user_id}/', data=data, auth=AUTH)
    return r


def admin_auth(username, password):
    data = {'username': username, 'password': password}

    r = requests.post(HOST+'/auth/', data=data)
    if r.status_code == 200:
        return r.json()
    else:
        return r.status_code


if __name__ == '__main__':
    r = udpate_user2('sam', 's',  new_pass='xxxsam123')
    print(r)
    # if r.get('status_code') == 200:
    #     print('updated!')