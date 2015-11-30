
import logging
import json

import transaction
from pyramid.view import view_config
from pyramid.request import Response


__author__ = 'max'

log = logging.getLogger(__name__)
MODULE_DIR = "newsbomb_recommends.views"


@view_config(route_name='generic', renderer='json')
def api(request):
    try:
        module = request.matchdict["module"]
        method = request.matchdict["method"]

        if request.method == "GET":
            params = json.loads(request.params.get("params", "{}"))
        elif request.method == "POST":
            params = request.params.mixed()
            log.warning("params:%s" % params)
        # Allow cross domain call for AJAX
        request.response = Response()
        request.response.headerlist = []
        request.response.headerlist.extend(
            (
                ('Access-Control-Allow-Origin', '*'),
                ('Content-Type', 'application/json; charset=UTF-8')
            )
        )

        module_path = "%s.%s" % (MODULE_DIR, module)
        # import module
        mod = __import__(module_path)
        components = module_path.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        func = getattr(mod, method, None)
        if func:
            result = None
            with transaction.manager:
                result = func(**params)
            if method == "verify_email":
                return result
            return {"status": "success", "data": result}
        else:
            return {"status": "error", "data": ["No such method: %s." % method]}
    # except ValidationError, ex:
    #     return {"status": "error", "data": [ex.message]}
    except Exception, ex:
        log.exception("%s, %s, %s" % (module, method, ex))
        return {"status": "exception", "data": [ex.message]}

#EOF