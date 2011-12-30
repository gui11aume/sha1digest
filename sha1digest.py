# -*- coding: utf-8 -*-

import os
from hashlib import sha1

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


class MainHandler(webapp.RequestHandler):
   def get(self):
      dot = os.path.dirname(__file__)
      content_path = os.path.join(dot, 'only_page.html')
      self.response.out.write(open(content_path).read())
      # Yes... That's it.


def main():
   application = webapp.WSGIApplication(
        [('/', MainHandler),
        ], debug=True)
   run_wsgi_app(application)


if __name__ == '__main__':
   main()
