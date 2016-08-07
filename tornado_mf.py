#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import gen_char

class MainHandler(tornado.web.RequestHandler):
    """Handler for main page of MF char gen"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        self.write('<html><head><style>')
        self.create_style_sheet()
        self.write('</style></head><body>')
        self.write('<header><h1>Mutant Future Character Generator</h1></header>')
        self.write('<font size="2">')
        self.create_nav()
        self.write('</font>')
        self.write('<footer>Mutant Future</footer></body></html>')

    def create_style_sheet(self):
        """create style sheet for page"""

        self.write('header {')
        self.write('    background-color:blue;')
        self.write('    color:white;')
        self.write('    text-align:center;')
        self.write('    padding:5px;	 ')
        self.write('}')
        self.write('nav {')
        self.write('    line-height:20px;')
        self.write('    background-color:#eeeeee;')
        self.write('    float:left;')
        self.write('    padding:5px;	      ')
        self.write('}')
        self.write('procs_list {')
        self.write('    width:350px;')
        self.write('    float:left;')
        self.write('    padding:10px;	 	 ')
        self.write('}')
        self.write('files_list {')
        self.write('    width:350px;')
        self.write('    float:left;')
        self.write('    padding:10px;	 	 ')
        self.write('}')
        self.write('footer {')
        self.write('    background-color:blue;')
        self.write('    color:white;')
        self.write('    clear:both;')
        self.write('    text-align:center;')
        self.write('    padding:5px;	 	 ')
        self.write('}')
        self.write('</style>')
#        self.write('<head><meta http-equiv="refresh" content="3"></head>')
        self.write('<head></head>')


    def create_nav(self):
        """create navigation section"""

        self.write('<nav>')
        self.write("<a href=\"/PURE_HUMAN\">Pure Human</a><br>")
        self.write('</nav>')


class PureHumanHandler(tornado.web.RequestHandler):
    """Handler Purely for Humans"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        gen_char.char('Pure Human')

        self.write('hello whirled')


def make_app():
    """Assemble all available functions for MF char gen"""

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/PURE_HUMAN", PureHumanHandler),
    ])


if __name__ == "__main__":
    APP = make_app()
    APP.listen(8888)
    tornado.ioloop.IOLoop.current().start()
