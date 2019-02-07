#!/usr/bin/python
import elaphe
from PIL import Image, ImageDraw, ImageFont

DEFAULT_IMG_SIZE = (200,200)
DEFAULT_IMG_MODE = 'RGBA'
DEFAULT_IMG_BGCOLOR = 'white'

class CodeGenerator:
    def __init__(self, student_level, student_number, student_name, student_nickname, student_birthdate, student_contact, student_leader, student_contactleader, student_network):
        # create image
        self.code = Image.new(DEFAULT_IMG_MODE, DEFAULT_IMG_SIZE, (255, 255, 255, 0))

        student_details = student_level + student_number + student_name + student_nickname + student_birthdate + student_contact + student_leader + student_contactleader + student_network
        qrcode = elaphe.barcode('qrcode', student_details, options=dict(version=3), scale=3)
        qrcode.thumbnail(DEFAULT_IMG_SIZE, Image.ANTIALIAS)
        self.code.paste(qrcode, (int((DEFAULT_IMG_SIZE[0] - qrcode.size[0]) / 2), int((DEFAULT_IMG_SIZE[1] - qrcode.size[1]) / 2)))

    def show(self):
        self.code.show()

    def save(self, filename, format='PNG'):
        self.code.save(filename, format)


if __name__ == '__main__':
   mylabel = PropertyLabel('', '', '', '', '', '', '', '')
   mylabel.show