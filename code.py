#!/usr/bin/env python
import web

urls = (
    '/(.*)', 'index'
)


class index:        
    def GET(self, name):
        render = web.template.render('templates/')
        return render.index(name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
