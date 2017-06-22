#!/usr/bin/env python3
"""web server for Mutant Future character generator"""

import tornado.ioloop
import tornado.web
import gen_char
import db_access
import create_pdf
import logging

class MainHandler(tornado.web.RequestHandler):
    """Handler for main page of MF char gen"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        form_file_head_p = open('char_gen_form/mf_char_gen_head.html', 'r')
        for form_line in form_file_head_p:
            self.write(form_line)
        form_file_head_p.close()
        form_file_body_p = open('char_gen_form/mf_char_gen_body.html', 'r')
        for form_line in form_file_body_p:
            self.write(form_line)
        form_file_body_p.close()
        form_file_foot_p = open('char_gen_form/mf_char_gen_foot.html', 'r')
        for form_line in form_file_foot_p:
            self.write(form_line)
        form_file_foot_p.close()


class CommitHandler(tornado.web.RequestHandler):
    """commit a character's changes to the db"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        name = None

        for section in self.request.uri.split('?'):
            this_section = section.split('=')
            if this_section[0] == 'name':
                name = section.split('=')[1]
            if this_section[0] == 'Strength':
                strength = section.split('=')[1]
            if this_section[0] == 'Dexterity':
                dexterity = section.split('=')[1]
            if this_section[0] == 'Constitution':
                constitution = section.split('=')[1]
            if this_section[0] == 'Intelligence':
                intelligence = section.split('=')[1]
            if this_section[0] == 'Willpower':
                willpower = section.split('=')[1]
            if this_section[0] == 'Charisma':
                charisma = section.split('=')[1]

        name = name.replace('%20', ' ')

        character = db_access.query_by_name(name)

        (character['attributes'])['Strength'] = strength
        (character['attributes'])['Dexterity'] = dexterity
        (character['attributes'])['Constitution'] = constitution
        (character['attributes'])['Intelligence'] = intelligence
        (character['attributes'])['Willpower'] = willpower
        (character['attributes'])['Charisma'] = charisma

        db_access.rm_by_name(character['name'])
        db_access.insert_char(character)

        name = name.replace(' ', '%20')

        self.write('<head>')
        self.write('<meta http-equiv="refresh" content="0; url=/VIEW_PDF?name=' + name + '" />')
        self.write('</head>')

        return


class EditHandler(tornado.web.RequestHandler):
    """generate a character and edit attrs and muts"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def attr_dropdown(self, character, attr='Strength'):
        """generate drop-down for discreet attribute"""

        ret_str = '<label class="title">' + attr + '</label>'
        ret_str += '<div class="large">'
        ret_str += '<span>'
        ret_str += '<select name="' + attr.lower() + '" id="' + attr.lower() + '_select">'
        score = int((character['attributes'])[attr])
        for attr_idx in range(3, 18):
            if score == attr_idx:
                out_line = '<option value="' + str(attr_idx) + '" selected>'
                out_line += str(attr_idx) + '</option>'
                ret_str += out_line
            else:
                out_line = '<option value="' + str(attr_idx) + '">'
                out_line += str(attr_idx) + '</option>'
                ret_str += out_line
        ret_str += '</span>'
        ret_str += '</select>'
        ret_str += '</div>'
        ret_str += '<br>'

        return ret_str

    def get(self):
        """respond to HTTP get method"""

        class_select = None
        sub_spec = False
        assign_name = False
        rand_synth = False
        rand_repl = False
        level_select = 1
        method = '3d6'

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

        log_line = str('character request: class_select=' + str(class_select) +
                       ' sub_spec=' + str(sub_spec) + ' assign_name=' + str(assign_name)
                       + ' rand_synth=' + str(rand_synth) + ' rand_repl='
                       + str(rand_repl) + ' level_select=' + str(level_select) +
                       ' method=' + method)
        logger.info(log_line)

        character = gen_char.char(class_select, level_select, sub_spec,
                                  assign_name, rand_synth, rand_repl,
                                  method)

        log_line = 'returning: ' + str(character)
        logger.info(log_line)

        db_access.insert_char(character)

        form_file_head_p = open('char_gen_form/mf_char_gen_head.html', 'r')
        for form_line in form_file_head_p:
            self.write(form_line)
        form_file_head_p.close()

        self.write('<body class="blurBg-false" style="background-color:#1A2223">')
        self.write('<link rel="stylesheet" href="mf_char_gen_files/formoid1/formoid-biz-red.css" ')
        self.write('type="text/css" />')
        self.write('<form class="formoid-biz-red" style="background-color:#1A2223;')
        self.write('font-size:14px;font-family:')
        self.write('\'Open Sans\',\'Helvetica Neue\', \'Helvetica\', Arial, ')
        self.write('Verdana, sans-serif;color:#ECECEC;max-width:480px;min-width:150px">')
        self.write('<img src="MF_logo_color.png" alt="MF_logo_color.png" width="100%">')

        self.write('<div class="title">')
        if character['use-name']:
            self.write('<h2>Name:  ' + character['name'] + '</h2>')
        else:
            self.write('<h2>Name:</h2>')
        self.write('<h2>Class:  ' + character['type'] + '</h2>')
        self.write('</div>')

        self.write('<div class="element-select">')

        for attr in character['attributes']:
            self.write(self.attr_dropdown(character, attr))

        self.write('<i></i></span></div></div><br>')
        self.write('<div><button type="button" onclick="view_pdf()" ')
        self.write('style="background-color:red;">VIEW PDF</button></div>')
        self.write('<br><img src="MF_logo_color.png" alt="MF_logo_color.png" width="100%">')
        self.write('</form>\n')
        self.write('<script>\n')
        self.write('function view_pdf() {\n')
        self.write('view_url = \"COMMIT_CHAR?name=' + character['name'].replace(' ', '%20') + '\"\n')
        for attr in character['attributes']:
            self.write('view_url += \"?' + attr + '=\"\n')
            self.write(str('view_url += document.getElementById("' + attr.lower() +
                           '_select").value' + '\n'))
        self.write('window.open(view_url)\n')
        self.write('}\n')
        self.write('</script>\n')
        self.write('<br>')
        self.write('</body>')

        form_file_foot_p = open('char_gen_form/mf_char_gen_foot.html', 'r')
        for form_line in form_file_foot_p:
            self.write(form_line)
        form_file_foot_p.close()


class PDFViewHandler(tornado.web.RequestHandler):
    """view a character PDF"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        name = None

        for section in self.request.uri.split('?'):
            this_section = section.split('=')
            if this_section[0] == 'name':
                name = section.split('=')[1]
                name = name.replace('%20', ' ')

        if name is None:
            character = gen_char.char()
        else:
            character = db_access.query_by_name(name)

        file_name = create_pdf.gen_char_pdf(character)

        file_name = create_pdf.combine_pdfs(character, file_name)

        redir_location = '<html><head>'
        redir_location += '<meta http-equiv="refresh" content="0; '
        redir_location += file_name + '" />'
        redir_location += '</head></html>'
        self.write(redir_location)


def make_app():
    """Assemble all available functions for MF char gen"""

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/VIEW_PDF", PDFViewHandler),
        (r"/EDIT_CHAR", EditHandler),
        (r"/COMMIT_CHAR", CommitHandler),
        (r"/(MF_logo_color\.png)", tornado.web.StaticFileHandler, {"path": "./images"}),
        (r"/char_pdfs/(.*)", tornado.web.StaticFileHandler, {"path": "./char_pdfs"},),
        (r"/char_xmls/(.*)", tornado.web.StaticFileHandler, {"path": "./char_xmls"},),
        (r"/mf_char_gen_files/formoid1/(.*)", tornado.web.StaticFileHandler,
         {"path": "./char_gen_form/mf_char_gen_files/formoid1"},),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./"},),
    ])


if __name__ == "__main__":

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('/var/log/mfchargen.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info('Tornado layer starting')

    APP = make_app()
    APP.listen(80)
    tornado.ioloop.IOLoop.current().start()
