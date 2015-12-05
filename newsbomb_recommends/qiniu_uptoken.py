import logging

from qiniu import Auth
from pyramid.view import view_config

__author__ = 'max'

LOGGER = logging.getLogger(__name__)


@view_config(route_name='qiniu_uptoken', renderer='json')
def qiniu_uptoken(request):
    LOGGER.debug("qiniu uptoken request is %s" % request)
    access_key = "HKrteOKWoa0b7lO6eXy_su1isCx9_dYxHJI2wuX9"
    secret_key = "js3gA8BCYbVrVpMhs-GT75Md9OlUFhjld-Bkl8LS"
    params = request.params.mixed()
    LOGGER.info("request params is %s" % params)
    q = Auth(access_key, secret_key)

    bucket = params.get("bucketcxvxcv")
    key = params.get("title")
    try:
        token = q.upload_token(bucket, key)
    except Exception as e:
        LOGGER.exception(e.message)
        return e.message
    LOGGER.info("response uptoken is %s" % token)
    return {"uptoken": token}
