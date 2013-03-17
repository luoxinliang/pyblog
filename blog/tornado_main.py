#!/usr/bin/env python
#-*- coding:Utf-8 -*- 

from tornado.options import options, define
import django.core.handlers.wsgi
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi 

os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

define('port', type=int, default=8080)

def main():
    wsgi_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
    tornado_app = tornado.web.Application(
    [
      ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
      ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
