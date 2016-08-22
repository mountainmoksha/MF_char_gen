#!/usr/bin/env python3
"""web server for Mutant Future character generator"""

import tornado.ioloop
import tornado.web
import gen_char
import create_pdf


class ScreenFormatter():
    """object that generates html for masthead, nav and footer"""

    def create_style_sheet(self):
        """create style sheet for page"""

        ret_str = '<html><head>'
        ret_str = ret_str + '<meta name="keywords" '
        ret_str = ret_str + 'content="Mutant Future Character Generator, '
        ret_str = ret_str + 'Mutant Future, Labyrinth Lord">'
        ret_str = ret_str + '<style>'
        ret_str = ret_str + 'header {'
        ret_str = ret_str + '    background-color:blue;'
        ret_str = ret_str + '    color:white;'
        ret_str = ret_str + '    text-align:center;'
        ret_str = ret_str + '    padding:5px;	 '
        ret_str = ret_str + '}'
        ret_str = ret_str + 'nav {'
        ret_str = ret_str + '    line-height:20px;'
        ret_str = ret_str + '    background-color:#eeeeee;'
        ret_str = ret_str + '    float:left;'
        ret_str = ret_str + '    height:100%;'
        ret_str = ret_str + '    padding:5px;	      '
        ret_str = ret_str + '}'
        ret_str = ret_str + 'body_text {'
        ret_str = ret_str + '    width:800px;'
        ret_str = ret_str + '    float:left;'
        ret_str = ret_str + '    padding:10px;	 	 '
        ret_str = ret_str + '}'
        ret_str = ret_str + 'footer {'
        ret_str = ret_str + '    background-color:blue;'
        ret_str = ret_str + '    color:white;'
        ret_str = ret_str + '    clear:both;'
        ret_str = ret_str + '    text-align:center;'
        ret_str = ret_str + '    padding:5px;	 	 '
        ret_str = ret_str + '}'
        ret_str = ret_str + '</style>'
        ret_str = ret_str + '<head></head>'
        ret_str = ret_str + '<title>Mutant Future Character Generator</title>'
        ret_str = ret_str + '</style></head>'

        return ret_str


    def create_nav(self):
        """create navigation section"""

        ret_str = '<nav>'
        ret_str = ret_str + '<form>'
        ret_str = ret_str + '<b>Create a character</b><br>'
        ret_str = ret_str + '<b>Class:</b><br>'
        ret_str = ret_str + '<select id="class_select">'
        ret_str = ret_str + '<option value="RANDOM">Random</option>'
        ret_str = ret_str + '<option value="BASIC_ANDROID">Basic Android</option>'
        ret_str = ret_str + '<option value="MUTANT_HUMAN">Mutant Human</option>'
        ret_str = ret_str + '<option value="MUTANT_ANIMAL">Mutant Animal</option>'
        ret_str = ret_str + '<option value="MUTANT_PLANT">Mutant Plant</option>'
        ret_str = ret_str + '<option value="PURE_HUMAN">Pure Human</option>'
        ret_str = ret_str + '<option value="SYNTHETIC_ANDROID">Synthetic Android</option>'
        ret_str = ret_str + '<option value="REPLICANT">Replicant</option>'
        ret_str = ret_str + '</select><br>'
        ret_str = ret_str + '<b>Level:</b><br>'
        ret_str = ret_str + '<select id="level_select">'
        ret_str = ret_str + '<option value=1>1</option>'
        ret_str = ret_str + '<option value=2>2</option>'
        ret_str = ret_str + '<option value=3>3</option>'
        ret_str = ret_str + '<option value=4>4</option>'
        ret_str = ret_str + '<option value=5>5</option>'
        ret_str = ret_str + '<option value=6>6</option>'
        ret_str = ret_str + '<option value=7>7</option>'
        ret_str = ret_str + '<option value=8>8</option>'
        ret_str = ret_str + '<option value=9>9</option>'
        ret_str = ret_str + '<option value=10>10</option>'
        ret_str = ret_str + '<option value="Random">Random</option>'
        ret_str = ret_str + '</select><br>'
        ret_str = ret_str + '<input type="checkbox" id="sub" value="sub_spec" checked="checked"/>'
        ret_str = ret_str + 'Assign sub-species for animals and plants<br>'
        ret_str = ret_str + str('<input type="checkbox" id="name" ' +
                                'value="assign_name" checked="checked"/>')
        ret_str = ret_str + 'Assign randomized name<br>'
        ret_str = ret_str + '<input type="checkbox" id="synth" value="rand_synth"/>'
        ret_str = ret_str + 'Include synthetic androids in randomized results<br>'
        ret_str = ret_str + '<input type="checkbox" id="repl" value="rand_repl"/>'
        ret_str = ret_str + 'Include replicants in randomized results<br>'
        ret_str = ret_str + str('<button type="button" onclick="generate_character()">' +
                                'Generate</button><br>')
        ret_str = ret_str + '</form>'
        ret_str = ret_str + '<script>'
        ret_str = ret_str + 'function generate_character() {'
        ret_str = ret_str + '     window.location = document.getElementById("class_select").value '
        ret_str = ret_str + '+ "?" + document.getElementById("sub").value + "=" + '
        ret_str = ret_str + 'document.getElementById("sub").checked'
        ret_str = ret_str + '+ "?" + document.getElementById("level_select").id'
        ret_str = ret_str + '+ "=" + document.getElementById("level_select").value'
        ret_str = ret_str + '+ "?" + document.getElementById("synth").value'
        ret_str = ret_str + '+ "=" + document.getElementById("synth").checked'
        ret_str = ret_str + '+ "?" + document.getElementById("repl").value'
        ret_str = ret_str + '+ "=" + document.getElementById("repl").checked'
        ret_str = ret_str + '+ "?" + document.getElementById("name").value'
        ret_str = ret_str + '+ "=" + document.getElementById("name").checked;'
        ret_str = ret_str + '}'
        ret_str = ret_str + '</script>'
        ret_str = ret_str + '<a href="/">Home</a>'
        ret_str = ret_str + '</nav>'

        return ret_str

    def create_head(self):
        """create header for MF char gen"""

        ret_str = '<body><header><img src="MF_logo_color.png" alt="MF_logo_color.png"></header>'

        return ret_str


    def create_foot(self):
        """create footer for MF char gen"""

        ret_str = '<footer>Mutant Future</footer>'

        return ret_str


class MainHandler(tornado.web.RequestHandler):
    """Handler for main page of MF char gen"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        screen_formatter = ScreenFormatter()

        self.write(screen_formatter.create_style_sheet())
        self.write('<body>')
        self.write(screen_formatter.create_head())
        self.write('<font size="2">')
        self.write(screen_formatter.create_nav())
        self.write('</font>')
        self.write('<font size="2">')
        self.create_body()
        self.write('</font>')
        self.write(screen_formatter.create_foot())
        self.write('</body></html>')


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
        self.write('<br>')
        self.write('Our <a href=\"/VIEW_ANIMALS\">current list</a> of animals was lifted from ')
        self.write('<a href=\"http://lib.colostate.edu/wildlife/atoz.php?letter=ALL\"> ')
        self.write('http://lib.colostate.edu/wildlife/atoz.php?letter=ALL</a> ')
        self.write('please contact us on github for suggestions re: additions, ')
        self.write('subtractions and improvements<br>')
        self.write('Much the same goes for <a href=\"/VIEW_PLANTS\">our plants</a>')
        self.write('</body_text>')



class AnimalViewHandler(tornado.web.RequestHandler):
    """view the animals currently in the generator"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        screen_formatter = ScreenFormatter()

        self.write(screen_formatter.create_style_sheet())
        self.write('<body>')
        self.write(screen_formatter.create_head())
        self.write('<font size="2">')
        self.write(screen_formatter.create_nav())
        self.write('</font>')
        self.write('<font size="2">')
        self.create_body()
        self.write('</font>')
        self.write(screen_formatter.create_foot())
        self.write('</body></html>')

    def create_body(self):
        """create the specific body for this handler"""

        with open('MF_animals.txt', 'r') as animals_file:
            animals = animals_file.read().splitlines()

        for animal in animals:
            self.write(animal + '<br>')


class PlantViewHandler(tornado.web.RequestHandler):
    """view the plants currently in the generator"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        screen_formatter = ScreenFormatter()

        self.write(screen_formatter.create_style_sheet())
        self.write('<body>')
        self.write(screen_formatter.create_head())
        self.write('<font size="2">')
        self.write(screen_formatter.create_nav())
        self.write('</font>')
        self.write('<font size="2">')
        self.create_body()
        self.write('</font>')
        self.write(screen_formatter.create_foot())
        self.write('</body></html>')

    def create_body(self):
        """create the specific body for this handler"""

        with open('MF_plants.txt', 'r') as plants_file:
            plants = plants_file.read().splitlines()

        for plant in plants:
            self.write(plant + '<br>')


class CharacterHandler(tornado.web.RequestHandler):
    """Handler For all Characters"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        screen_formatter = ScreenFormatter()

        self.write(screen_formatter.create_style_sheet())
        self.write('<body>')
        self.write(screen_formatter.create_head())
        self.write('<font size="2">')
        self.write(screen_formatter.create_nav())
        self.write('</font>')
        self.write('<font size="2">')
        self.create_body()
        self.write('</font>')
        self.write(screen_formatter.create_foot())
        self.write('</body></html>')


    def create_body(self):
        """return html for MF character for web interface"""

        sub_spec = False
        assign_name = False
        rand_synth = False
        rand_repl = False
        level_select = 1

        for section in self.request.uri.split('?'):
            this_section = section.split('=')
            if len(this_section) == 1:
                base_url = this_section[0]
            else:
                if this_section[0] == 'sub_spec':
                    if section.split('=')[1] == 'true':
                        sub_spec = True
                if this_section[0] == 'assign_name':
                    if section.split('=')[1] == 'true':
                        assign_name = True
                if this_section[0] == 'rand_synth':
                    if section.split('=')[1] == 'true':
                        rand_synth = True
                if this_section[0] == 'rand_repl':
                    if section.split('=')[1] == 'true':
                        rand_repl = True
                if this_section[0] == 'level_select':
                    if section.split('=')[1] == 'Random':
                        level_select = None
                    else:
                        level_select = int(section.split('=')[1])

        if base_url == '/BASIC_ANDROID':
            character = gen_char.char('Basic Android', level_select, sub_spec, assign_name)
        elif base_url == '/SYNTHETIC_ANDROID':
            character = gen_char.char('Synthetic Android', level_select, sub_spec, assign_name)
        elif base_url == '/REPLICANT':
            character = gen_char.char('Replicant', level_select, sub_spec, assign_name)
        elif base_url == '/MUTANT_HUMAN':
            character = gen_char.char('Mutant Human', level_select, sub_spec, assign_name)
        elif base_url == '/MUTANT_ANIMAL':
            character = gen_char.char('Mutant Animal', level_select, sub_spec, assign_name)
        elif base_url == '/MUTANT_PLANT':
            character = gen_char.char('Mutant Plant', level_select, sub_spec, assign_name)
        elif base_url == '/PURE_HUMAN':
            character = gen_char.char('Pure Human', level_select, sub_spec, assign_name)
        else: # random
            character = gen_char.char(None, level_select, sub_spec, assign_name, rand_synth,
                                      rand_repl)

        create_pdf.combine_pdfs(create_pdf.gen_char_pdf(character))

        self.write(str('<a href="/char_pdfs/' +
                       character['name'].replace(' ', '_') + '.pdf">View PDF</a>'))
        self.write('<br><br>')

        if 'name' in character:
            self.write('<b>Name: </b>' + character['name'] + '<br>')
        else:
            self.write('<b>Name:</b><br>')
        self.write('<br>')
        self.write('<b>Type: </b>' + character['type'])
        if 'sub_type' in character:
            self.write(' (' + character['sub_type'] +')')
        self.write('<br>')
        self.write('<b>Level: </b>' + str(character['level']))
        self.write('<br>')
        self.write('<b>XP: </b>' + str(character['XP']))
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
        self.write('<b>Saving Throws: </b><br><br>')
        self.write('<b>Energy Attacks: </b>' + str(character['energy_save']) + '<br>')
        self.write('<b>Poison or Death: </b>' + str(character['poison_death_save']) + '<br>')
        self.write('<b>Stun Attacks: </b>' + str(character['stun_save']) + '<br>')
        self.write('<b>Radiation: </b>' + str(character['rad_save']) + '<br>')
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
        self.write('<b>Level Modifiers:</b><br>')
        self.write('<br>')
        for key in character['level_modifiers']:
            self.write((character['level_modifiers'])[key] + '<br>')
        self.write('<br>')



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
        (r"/VIEW_ANIMALS", AnimalViewHandler),
        (r"/VIEW_PLANTS", PlantViewHandler),
        (r"/(MF_logo_color\.png)", tornado.web.StaticFileHandler, {"path": "./images"}),
        (r"/char_pdfs/(.*)", tornado.web.StaticFileHandler, {"path": "./char_pdfs"},),
    ])


if __name__ == "__main__":
    APP = make_app()
    APP.listen(8888)
    tornado.ioloop.IOLoop.current().start()
