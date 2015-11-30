import json
from qiniu import Auth

__author__ = 'max'


def upload(title, image, **kwargs):
    access_key = "HKrteOKWoa0b7lO6eXy_su1isCx9_dYxHJI2wuX9"
    secret_key = "js3gA8BCYbVrVpMhs-GT75Md9OlUFhjld-Bkl8LS"
    q = Auth(access_key, secret_key)

    bucket = "newsbomb"
    key = title
    token = q.upload_token(bucket, key)
    return token
