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


class EditHandler(tornado.web.RequestHandler):
    """generate a character and edit attrs and muts"""

    def data_received(self, chunk):
        print('chunk is', chunk)

    def get(self):
        """respond to HTTP get method"""

        print('in EditHandler::get')

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
        form_file_body_p = open('char_gen_form/mf_char_edit_body.html', 'r')
        form_lines = form_file_body_p.read()
        str_score = str((character['attributes'])['Strength'])
        form_lines = form_lines.replace('<option value="' + str_score + '" STR_SELECTED',
                                       '<option value="' + str_score + '" selected')
        int_score = str((character['attributes'])['Intelligence'])
        form_lines = form_lines.replace('<option value="' + int_score + '" INT_SELECTED',
                                       '<option value="' + int_score + '" selected')
        dex_score = str((character['attributes'])['Dexterity'])
        form_lines = form_lines.replace('<option value="' + dex_score + '" DEX_SELECTED',
                                       '<option value="' + dex_score + '" selected')
        self.write(form_lines)
        form_file_body_p.close()
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

        print('in PDFViewHandler::get')
#        for section in self.request.uri.split('?'):
#            this_section = section.split('=')
#            if this_section[0] == 'class_select':
#                class_select = section.split('=')[1]
#                if class_select == 'Random':
#                    class_select = None
#                else:
#                    class_select = class_select.replace("%20", " ")
#            if this_section[0] == 'method':
#                method = section.split('=')[1]
#            if this_section[0] == 'sub_spec':
#                if section.split('=')[1] == 'true':
#                    sub_spec = True
#            if this_section[0] == 'assign_name':
#                if section.split('=')[1] == 'true':
#                    assign_name = True
#            if this_section[0] == 'rand_synth':
#                if section.split('=')[1] == 'true':
#                    rand_synth = True
#            if this_section[0] == 'rand_repl':
#                if section.split('=')[1] == 'true':
#                    rand_repl = True
#            if this_section[0] == 'level_select':
#                if section.split('=')[1] == 'Random':
#                    level_select = None
#                else:
#                    level_select = int(section.split('=')[1])

        # after you know the name, retr from db

        character = gen_char.char()

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
