import time
import jwt
import requests
import json
import logging

class App:
    def __init__(self,app_id,org,private_key):
        self.app_id = app_id
        self.org = org
        self.private_key = private_key
        self.token_header = self.__get_token_header()
        logging.info('token_header : ' + str(self.token_header))

    def __generate_jwt(self):
        payload = {
            'iat': int(time.time()),
            'exp': int(time.time()) + 300,
            'iss': self.app_id,
        }
        return jwt.encode(payload, self.private_key, algorithm='RS256')

    def __get_headers(self):
        jwt = self.__generate_jwt()
        return {
            'Authorization': 'Bearer {}'.format(jwt),
            'Accept': 'application/vnd.github+json',
        }

    def __get_installation_id(self):
        url = 'https://api.github.com/users/{}/installation'.format(
            self.org)
        response = requests.get(url, headers=self.__get_headers())
        return json.loads(response.text).get('id')

    def __get_token(self):
        url = 'https://api.github.com/app/installations/{}/access_tokens'.format(
            str(self.__get_installation_id()))
        response = requests.post(url, headers=self.__get_headers())
        return json.loads(response.text).get('token')
    
    def __get_token_header(self):
        token = self.__get_token()
        return {
            'Authorization': 'token {}'.format(token),
            'Accept': 'application/vnd.github.inertia-preview+json',
        }
    
    def workflow(self, repo, ref, inputs, workflow_id):
        url = 'https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches'.format(
            owner=self.org, repo=repo, workflow_id=workflow_id)
        payload = json.dumps({
            'ref': ref,
            'inputs': inputs
        })
        return requests.post(url, payload, headers=self.token_header)
