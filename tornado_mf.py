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
        self.write('<title>Mutant Future Character Generator</title>')
        self.write('</style></head><body>')
        self.write('<header><h1>Mutant Future Character Generator</h1></header>')
        self.write('<font size="2">')
        self.create_nav()
        self.write('</font>')
        self.write('<font size="2">')
        self.create_body()
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
        self.write('body_text {')
        self.write('    width:800px;')
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
        self.write('<head></head>')

    def create_body(self):
        """create body section"""

        self.write('<body_text>')
        self.write('Mutant Future was created by ' +
                   '<a href=\"http://www.goblinoidgames.com/\">' +
                   'Goblinoid Games<a> ' +
                   'who kindly granted permission to use their pdf character sheets<br>')
        self.write('<br>')
        self.write('This character generator is ' +
                   '<a href=\"http://www.gnu.org/copyleft/gpl.html\">' +
                   'free software<a><br>')
        self.write('It was created by ' +
                   '<a href=\"https://amutatedpumanamedgrrr.wordpress.com/\">' +
                   'A Mutated Puma Named Grrr<a><br>')
        self.write('Check out the source Code at ' +
                   '<a href=\"https://github.com/exit0/MF_char_gen/\">' +
                   'https://github.com/exit0/MF_char_gen/<a><br>')
        self.write('Please submit bugs and feature requests at ' +
                   '<a href=\"https://github.com/exit0/MF_char_gen/issues/\">' +
                   'https://github.com/exit0/MF_char_gen/issues/<a><br>')
        self.write('</body_text>')



    def create_nav(self):
        """create navigation section"""

        self.write('<nav>')

        self.write('<b>Class:</b><br>')
        self.write('<form>')
        self.write('<select id="class_select">')
        self.write('<option value="BASIC_ANDROID">Basic Android</option>')
        self.write('<option value="SYNTHETIC_ANDROID">Synthetic Android</option>')
        self.write('<option value="REPLICANT">Replicant</option>')
        self.write('<option value="MUTANT_HUMAN">Mutant Human</option>')
        self.write('<option value="MUTANT_ANIMAL">Mutant Animal</option>')
        self.write('<option value="MUTANT_PLANT">Mutant Plant</option>')
        self.write('<option value="PURE_HUMAN">Pure Human</option>')
        self.write('<option value="RANDOM">Random</option>')
        self.write('</select><br>')
        self.write('<input type="checkbox" id="sub" value="sub_spec" />' +
                   'Assign sub-species for animals and plants<br>')
        self.write('<button type="button" onclick="generate_character()">Generate</button><br>')
        self.write('</form>')

        self.write('<script>')
        self.write('function generate_character() {')
        self.write('     window.location = document.getElementById("class_select").value + "?" + document.getElementById("sub").value + "=" + document.getElementById("sub").checked;')
        self.write('}')
        self.write('</script>')

        self.write('</nav>')


class CharacterHandler(tornado.web.RequestHandler):
    """Handler Purely for Humans"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        if self.request.uri == '/BASIC_ANDROID':
            character = gen_char.char('Basic Android')
        elif self.request.uri == '/SYNTHETIC_ANDROID':
            character = gen_char.char('Synthetic Android')
        elif self.request.uri == '/REPLICANT':
            character = gen_char.char('Replicant')
        elif self.request.uri == '/MUTANT_HUMAN':
            character = gen_char.char('Mutant Human')
        elif self.request.uri == '/MUTANT_ANIMAL':
            character = gen_char.char('Mutant Animal')
        elif self.request.uri == '/MUTANT_PLANT':
            character = gen_char.char('Mutant Plant')
        elif self.request.uri == '/PURE_HUMAN':
            character = gen_char.char('Pure Human')
        else: # random
            character = gen_char.char()

        self.write('<b>Name:</b><br>')
        self.write('<br>')
        self.write('<b>Type: </b>' + character['type'] + '<br>')
        self.write('<br>')
        for attribute in character['attributes']:
            self.write('<b>' + attribute + ' : </b>' +
                       str((character['attributes'])[attribute]) + '<br>')
        self.write('<br>')
        self.write('<b>AC: </b>' + str(character['AC']) + '<br>')
        self.write('<br>')
        self.write('<b>HP: </b>' + str(character['HP']) + '<br>')
        self.write('<br>')
        self.write('<b>GP: </b>' + str(character['GP']) + '<br>')
        self.write('<br>')
        self.write('<b>Physical Mutations:</b><br>')
        self.write('<br>')
        for mutation in character['physical']:
            self.write(mutation + '<br>')
        self.write('<br>')
        self.write('<b>Mental Mutations:</b><br>')
        self.write('<br>')
        for mutation in character['mental']:
            self.write(mutation + '<br>')
        self.write('<br>')
        self.write('<b>Plant Mutations:</b><br>')
        self.write('<br>')
        for mutation in character['plant']:
            self.write(mutation + '<br>')
        self.write('<br>')
        self.write('<b>Modifiers:</b><br>')
        self.write('<br>')
        for modifier in character['modifiers']:
            self.write(modifier + '<br>')
        self.write('<br>')
        self.write('<a href="/">Back</a> ')



def make_app():
    """Assemble all available functions for MF char gen"""

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/BASIC_ANDROID", CharacterHandler),
        (r"/SYNTHETIC_ANDROID", CharacterHandler),
        (r"/REPLICANT", CharacterHandler),
        (r"/MUTANT_HUMAN", CharacterHandler),
        (r"/MUTANT_ANIMAL", CharacterHandler),
        (r"/MUTANT_PLANT", CharacterHandler),
        (r"/PURE_HUMAN", CharacterHandler),
        (r"/RANDOM", CharacterHandler),
    ])


if __name__ == "__main__":
    APP = make_app()
    APP.listen(8888)
    tornado.ioloop.IOLoop.current().start()
