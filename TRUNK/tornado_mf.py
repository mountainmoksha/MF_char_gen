#!/usr/bin/env python3
"""web server for Mutant Future character generator"""

import tornado.ioloop
import tornado.web
import gen_char
import create_pdf
import create_xml
import char_xml_parser


class ScreenFormatter():
    """object that generates html for masthead, nav and footer"""

    def create_style_sheet(self, title):
        """create style sheet for page"""

        ret_str = '<html>'
        # Google Analytics
        ret_str = ret_str +'<script>'
        ret_str = ret_str +'  (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){'
        ret_str = ret_str +'(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),'
        ret_str = ret_str +'m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)'
        ret_str = ret_str +'})(window,document,\'script\',\'https://www.google-analytics.com/analytics.js\',\'ga\');'
        ret_str = ret_str + 'ga(\'create\', \'UA-83215397-1\', \'auto\');'
        ret_str = ret_str + 'ga(\'send\', \'pageview\');'
        ret_str = ret_str + '</script>'
        ret_str = ret_str + '<head><title>' + title + '</title>'
        ret_str = ret_str + '<meta name="keywords" '
        ret_str = ret_str + 'content="Mutant Future Character Generator, '
        ret_str = ret_str + 'Mutant Future, Labyrinth Lord">'
        ret_str = ret_str + '<style>'
        ret_str = ret_str + 'header {'
        ret_str = ret_str + '    background-color:blue;'
        ret_str = ret_str + '    color:white;'
        ret_str = ret_str + '    text-align:center;'
#        ret_str = ret_str + '    height:15%;'
        ret_str = ret_str + '    height:152;'
        ret_str = ret_str + '    padding:5px;	 '
        ret_str = ret_str + '}'
        ret_str = ret_str + 'nav {'
        ret_str = ret_str + '    line-height:20px;'
        ret_str = ret_str + '    background-color:#eeeeee;'
        ret_str = ret_str + '    float:left;'
        ret_str = ret_str + '    height:80%;'
        ret_str = ret_str + '    padding:5px;	      '
        ret_str = ret_str + '}'
        ret_str = ret_str + 'body_col0 {'
        ret_str = ret_str + '    width:400px;'
        ret_str = ret_str + '    float:left;'
        ret_str = ret_str + '    height:80%;'
        ret_str = ret_str + '    padding:10px;	 	 '
        ret_str = ret_str + '}'
        ret_str = ret_str + 'body_col1 {'
        ret_str = ret_str + '    width:400px;'
        ret_str = ret_str + '    float:left;'
        ret_str = ret_str + '    height:80%;'
        ret_str = ret_str + '    padding:10px;	 	 '
        ret_str = ret_str + '}'
        ret_str = ret_str + 'footer {'
        ret_str = ret_str + '    background-color:blue;'
        ret_str = ret_str + '    color:white;'
        ret_str = ret_str + '    clear:both;'
        ret_str = ret_str + '    text-align:center;'
        ret_str = ret_str + '    height:5%;'
        ret_str = ret_str + '    padding:5px;	 	 '
        ret_str = ret_str + '}'
        ret_str = ret_str + '</style>'
        ret_str = ret_str + '</style></head>'

        return ret_str


    def create_nav(self):
        """create navigation section"""

        ret_str = '<nav>'
        ret_str = ret_str + '<form>'
        ret_str = ret_str + '<b>Create a character</b><br>'
        ret_str = ret_str + '<br>'
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
        ret_str = ret_str + '<br>'
        ret_str = ret_str + '<input type="checkbox" id="sub" value="sub_spec" checked="checked"/>'
        ret_str = ret_str + 'Assign sub-species for animals and plants<br>'
        ret_str = ret_str + str('<input type="checkbox" id="name" ' +
                                'value="assign_name" checked="checked"/>')
        ret_str = ret_str + 'Assign randomized name<br>'
        ret_str = ret_str + '<input type="checkbox" id="synth" value="rand_synth"/>'
        ret_str = ret_str + 'Include synthetic androids in randomized results<br>'
        ret_str = ret_str + '<input type="checkbox" id="repl" value="rand_repl"/>'
        ret_str = ret_str + 'Include replicants in randomized results<br>'
        ret_str = ret_str + '<br>'
        ret_str = ret_str + '<b>Attribute generation method:</b><br>'
        ret_str = ret_str + '<select id="method">'
        ret_str = ret_str + '<option value="3d6">3d6</option>'
        ret_str = ret_str + '<option value="4d6-L">4d6-L</option>'
        ret_str = ret_str + '</select><br>'
        ret_str = ret_str + '<br><br>'
        ret_str = ret_str + str('<button type="button" onclick="generate_character()">' +
                                'Generate</button><br>')
        ret_str = ret_str + '</form>'
        ret_str = ret_str + '<script>'
        ret_str = ret_str + 'function generate_character() {'
        ret_str = ret_str + '     window.location = document.getElementById("class_select").value '
        ret_str = ret_str + '+ "?" + document.getElementById("sub").value + "=" + '
        ret_str = ret_str + 'document.getElementById("sub").checked'
        ret_str = ret_str + '+ "?" + document.getElementById("method").id'
        ret_str = ret_str + '+ "=" + document.getElementById("method").value'
        ret_str = ret_str + '+ "?" + document.getElementById("level_select").id'
        ret_str = ret_str + '+ "=" + document.getElementById("level_select").value'
        ret_str = ret_str + '+ "?" + document.getElementById("synth").value'
        ret_str = ret_str + '+ "=" + document.getElementById("synth").checked'
        ret_str = ret_str + '+ "?" + document.getElementById("repl").value'
        ret_str = ret_str + '+ "=" + document.getElementById("repl").checked'
        ret_str = ret_str + '+ "?" + document.getElementById("name").value'
        ret_str = ret_str + '+ "=" + document.getElementById("name").checked;'
        ret_str = ret_str + '}'
        ret_str = ret_str + '</script><br>'
        if 1 == 0:
            ret_str = ret_str + '--------------------------------------<br>'
            ret_str = ret_str + '<b>Upload character xml:</b><br>'
            ret_str = ret_str + '<form action="DISPLAY_XML">'
            ret_str = ret_str + '  <input type="file" name="user_xml" accept="xml">'
            ret_str = ret_str + '  <input type="submit">'
            ret_str = ret_str + '</form>'
            ret_str = ret_str + '--------------------------------------<br>'
        ret_str = ret_str + '<a href="/">Home</a>'
        ret_str = ret_str + '</nav>'

        return ret_str


    def create_head(self):
        """create header for MF char gen"""

        ret_str = '<body><header><img src="MF_logo_color.png" alt="MF_logo_color.png" height="150" width="600"></header>'

        return ret_str


    def create_foot(self):
        """create footer for MF char gen"""

        ret_str = '<footer>Mutant Future</footer>'

        return ret_str


    def create_char_display(self, character):
        """display details of character to the right of the nav pane"""

        ret_str = str('<body_col0>')
        if 'name' in character:
            ret_str = ret_str + str(str('<a href="/char_pdfs/' +
                                        character['name'].replace(' ', '_') +
                                        '.pdf">Export PDF</a>     '))
            ret_str = ret_str + str(str('<a href="/char_xmls/' +
                                        character['name'].replace(' ', '_') +
                                        '.xml">Export XML</a>'))
        else:
            ret_str = ret_str + str(str('<a href="/char_pdfs/' +
                                        character['alt-name'].replace(' ', '_') +
                                        '.pdf">Export PDF</a>     '))
            ret_str = ret_str + str(str('<a href="/char_xmls/' +
                                        character['alt-name'].replace(' ', '_') +
                                        '.xml">Export XML</a>'))
        ret_str = ret_str + str('<br><br>')

        if 'name' in character:
            ret_str = ret_str + str('<b>Name: </b>' + character['name'] + '<br>')
        else:
            ret_str = ret_str + str('<b>Name:</b><br>')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>Type: </b>' + character['type'])
        if 'sub_type' in character:
            ret_str = ret_str + str(' (' + character['sub_type'] +')')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>Level: </b>' + str(character['level']))
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>XP: </b>' + str(character['XP']))
        ret_str = ret_str + str('<br>')
        for attribute in character['attributes']:
            ret_str = ret_str + str('<b>' + attribute + ' : </b>' +
                                    str((character['attributes'])[attribute]) + '<br>')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>AC: </b>' + str(character['AC']) + '<br>')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>HP: </b>' + str(character['HP']) + '<br>')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>GP: </b>' + str(character['GP']) + '<br>')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>Saving Throws: </b><br><br>')
        ret_str = ret_str + str('<b>Energy Attacks: </b>' + str(character['energy_save']) + '<br>')
        ret_str = ret_str + str('<b>Poison or Death: </b>' +
                                str(character['poison_death_save']) + '<br>')
        ret_str = ret_str + str('<b>Stun Attacks: </b>' + str(character['stun_save']) + '<br>')
        ret_str = ret_str + str('<b>Radiation: </b>' + str(character['rad_save']) + '<br>')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>Physical Mutations:</b><br>')
        ret_str = ret_str + str('<br>')
        for mutation in character['physical']:
            ret_str = ret_str + str(mutation + '<br>')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>Mental Mutations:</b><br>')
        ret_str = ret_str + str('<br>')
        for mutation in character['mental']:
            ret_str = ret_str + str(mutation + '<br>')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>Plant Mutations:</b><br>')
        ret_str = ret_str + str('<br>')
        for mutation in character['plant']:
            ret_str = ret_str + str(mutation + '<br>')
        ret_str = ret_str + str('</body_col0>')
        ret_str = ret_str + str('<body_col1>')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>Modifiers:</b><br>')
        ret_str = ret_str + str('<br>')
        for modifier in character['modifiers']:
            ret_str = ret_str + str(modifier + '<br>')
        ret_str = ret_str + str('<br>')
        ret_str = ret_str + str('<b>Level Modifiers:</b><br>')
        ret_str = ret_str + str('<br>')
        for key in character['level_modifiers']:
            ret_str = ret_str + str((character['level_modifiers'])[key] + '<br>')
        ret_str = ret_str + str('</body_col1>')

        return ret_str


class MainHandler(tornado.web.RequestHandler):
    """Handler for main page of MF char gen"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

#        screen_formatter = ScreenFormatter()
#
#        self.write(screen_formatter.create_style_sheet("Mutant Future Character Generator"))
#        self.write('<body>')
#        self.write(screen_formatter.create_head())
#        self.write('<font size="2">')
#        self.write(screen_formatter.create_nav())
#        self.write('</font>')
#        self.write('<font size="2">')
#        self.create_body0()
#        self.write('</font>')
#        self.write(screen_formatter.create_foot())
#        self.write('</body></html>')

        form_file_p = open('char_gen_form/mf_char_gen.html', 'r')
        for form_line in form_file_p:
            self.write(form_line)


    def create_body0(self):
        """create body section"""

        self.write('<body_col0>')
        self.write('<b>This is a Mutant Future Character Generator!</b><br><br>')
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
        self.write('<br>')
        self.write('Check out the source Code at ' +
                   '<a href=\"https://github.com/exit0/MF_char_gen/\">' +
                   'https://github.com/exit0/MF_char_gen/<a><br>')
        self.write('<br>')
        self.write(str('Please <a href="mailto:' +
                       'mfchargen@gmail.com?Subject=mfchargen%20impreovements"' +
                       'target="_top">email us</a> with ideas for improvements<br>'))
        self.write('<br>')
        self.write('Our <a href=\"/VIEW_ANIMALS\">current list</a> of animals was lifted from ')
        self.write('<a href=\"http://lib.colostate.edu/wildlife/atoz.php?letter=ALL\"> ')
        self.write('http://lib.colostate.edu/wildlife/atoz.php?letter=ALL</a> ')
        self.write('please email us with suggestions<br>')
        self.write('<br>')
        self.write('Much the same goes for <a href=\"/VIEW_PLANTS\">our plants</a>')
        self.write('</body_col0>')


class AnimalViewHandler(tornado.web.RequestHandler):
    """view the animals currently in the generator"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        screen_formatter = ScreenFormatter()

        self.write(screen_formatter.create_style_sheet("Animals Viewer"))
        self.write('<body>')
        self.write(screen_formatter.create_head())
        self.write('<font size="2">')
        self.write(screen_formatter.create_nav())
        self.write('</font>')
        self.write('<font size="2">')
        self.create_body0()
        self.write('</font>')
        self.write(screen_formatter.create_foot())
        self.write('</body></html>')

    def create_body0(self):
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

        self.write(screen_formatter.create_style_sheet("Plants Viewer"))
        self.write('<body>')
        self.write(screen_formatter.create_head())
        self.write('<font size="2">')
        self.write(screen_formatter.create_nav())
        self.write('</font>')
        self.write('<font size="2">')
        self.create_body0()
        self.write('</font>')
        self.write(screen_formatter.create_foot())
        self.write('</body></html>')

    def create_body0(self):
        """create the specific body for this handler"""

        with open('MF_plants.txt', 'r') as plants_file:
            plants = plants_file.read().splitlines()

        for plant in plants:
            self.write(plant + '<br>')


class PDFViewHandler(tornado.web.RequestHandler):
    """generate a character and view the PDF"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        class_select = None
        sub_spec = False
        assign_name = False
        rand_synth = False
        rand_repl = False
        level_select = 1

        for section in self.request.uri.split('?'):
            this_section = section.split('=')
            if this_section[0] == 'class_select':
                class_select = section.split('=')[1]
                if class_select == 'Random':
                    class_select = None
                else:
                    class_select = class_select.replace("%20", " ")
            if this_section[0] == 'method':
                method = section.split('=')[1]
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

        character = gen_char.char(class_select)

        file_name = create_pdf.gen_char_pdf(character)

        file_name = create_pdf.combine_pdfs(file_name)

        redir_location = '<html><head>'
        redir_location += '<meta http-equiv="refresh" content="0; '
        redir_location += file_name + '" />'
        redir_location += '</head></html>'
        self.write(redir_location)


class DisplayXMLHandler(tornado.web.RequestHandler):
    """Handler For all Characters"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        screen_formatter = ScreenFormatter()

        self.write(screen_formatter.create_style_sheet("XML Viewer"))
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

        screen_formatter = ScreenFormatter()

        file_name = 'char_xmls/'

        for section in self.request.uri.split('?'):
            this_section = section.split('=')
            if len(this_section) == 1:
                base_url = this_section[0]
            else:
                if this_section[0] == 'user_xml':
                    file_name = file_name + section.split('=')[1]

        character = char_xml_parser.parse_char_xml(file_name)
        self.write(screen_formatter.create_char_display(character))

        return

class CharacterHandler(tornado.web.RequestHandler):
    """Handler For all Characters"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        app_name = (self.request.uri.split('?')[0])[1:]

        screen_formatter = ScreenFormatter()

        self.write(screen_formatter.create_style_sheet(app_name))
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
                if this_section[0] == 'method':
                    method = section.split('=')[1]
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
            character = gen_char.char('Basic Android', level_select, sub_spec, assign_name,
                                      False, False, method)
        elif base_url == '/SYNTHETIC_ANDROID':
            character = gen_char.char('Synthetic Android', level_select, sub_spec, assign_name,
                                      False, False, method)
        elif base_url == '/REPLICANT':
            character = gen_char.char('Replicant', level_select, sub_spec, assign_name,
                                      False, False, method)
        elif base_url == '/MUTANT_HUMAN':
            character = gen_char.char('Mutant Human', level_select, sub_spec, assign_name,
                                      False, False, method)
        elif base_url == '/MUTANT_ANIMAL':
            character = gen_char.char('Mutant Animal', level_select, sub_spec, assign_name,
                                      False, False, method)
        elif base_url == '/MUTANT_PLANT':
            character = gen_char.char('Mutant Plant', level_select, sub_spec, assign_name,
                                      False, False, method)
        elif base_url == '/PURE_HUMAN':
            character = gen_char.char('Pure Human', level_select, sub_spec, assign_name,
                                      False, False, method)
        else: # random
            character = gen_char.char(None, level_select, sub_spec, assign_name, rand_synth,
                                      rand_repl, method)

        create_pdf.combine_pdfs(create_pdf.gen_char_pdf(character))
        create_xml.gen_char_xml(character)

        screen_formatter = ScreenFormatter()
        self.write(screen_formatter.create_char_display(character))

        return


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
        (r"/DISPLAY_XML", DisplayXMLHandler),
        (r"/VIEW_ANIMALS", AnimalViewHandler),
        (r"/VIEW_PLANTS", PlantViewHandler),
        (r"/VIEW_PDF", PDFViewHandler),
        (r"/(MF_logo_color\.png)", tornado.web.StaticFileHandler, {"path": "./images"}),
        (r"/char_pdfs/(.*)", tornado.web.StaticFileHandler, {"path": "./char_pdfs"},),
        (r"/char_xmls/(.*)", tornado.web.StaticFileHandler, {"path": "./char_xmls"},),
        (r"/mf_char_gen_files/formoid1/(.*)", tornado.web.StaticFileHandler,
            {"path": "./char_gen_form/mf_char_gen_files/formoid1"},),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./"},),
    ])


if __name__ == "__main__":
    APP = make_app()
    APP.listen(80)
    tornado.ioloop.IOLoop.current().start()
