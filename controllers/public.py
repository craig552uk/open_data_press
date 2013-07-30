# -*- coding: utf-8 -*-
#
# Public site route handlers
#

from webapp2 import RequestHandler

class ProfileRoute(RequestHandler):

    def get(self, profile_slug):
        self.response.write('')

class DataSourceRoute(RequestHandler):

    def get(self, profile_slug, data_source_slug):
        self.response.write('')

class DataViewRoute(RequestHandler):

    def get(self, profile_slug, data_source_slug, data_view_ext):
        self.response.write('')