# -*- coding: utf-8 -*-
from core.models import SiteConfiguration


def set_config(get_response):

    def middleware(request):
        config = SiteConfiguration.for_site(request.site)
        request.config = config
        response = get_response(request)
        return response

    return middleware
