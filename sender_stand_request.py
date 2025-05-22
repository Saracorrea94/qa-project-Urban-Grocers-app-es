import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

def post_new_client_kit(auth_token, kit_body):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)

def get_user_token():
    user_body = data.user_body
    response_user = post_new_user(user_body)
    return response_user.json()["authToken"]


def create_kit(kit_body=None):
    auth_token = get_user_token()
    kit_body = {"name": kit_body} if kit_body is not None else {}
    return post_new_client_kit(auth_token, kit_body)


