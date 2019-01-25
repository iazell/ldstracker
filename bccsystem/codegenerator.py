#!/usr/bin/python
import elaphe
from PIL import Image, ImageDraw, ImageFont

DEFAULT_IMG_SIZE = (609,203)
DEFAULT_IMG_MODE = 'RGB'
DEFAULT_IMG_BGCOLOR = 'white'

class CodeGenerator:
    def __init__(self, student_number, student_name, student_nickname, student_birthdate, student_contact, student_leader, student_contactleader, student_network):
        # create image
        self.code = Image.new(DEFAULT_IMG_MODE, DEFAULT_IMG_SIZE, DEFAULT_IMG_BGCOLOR)

        student_details = student_number + student_name + student_nickname + student_birthdate + student_contact + student_leader + student_contactleader + student_network
        qrcode = elaphe.barcode('qrcode', student_details, options=dict(version=3), scale=3)
        self.code.paste(qrcode, (200,5))

    def show(self):
        self.code.show()

    def save(self, filename, format='PNG'):
        self.code.save(filename, format)


if __name__ == '__main__':
   mylabel = PropertyLabel('', '', '', '', '', '', '', '')
   mylabel.show