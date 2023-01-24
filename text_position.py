from PIL import ImageFont, ImageDraw, Image
from matplotlib import font_manager

class TextPosition:

    def __init__(self, ui):

        self.font = font_manager.FontProperties(family='sans-serif', weight='bold')
        self.file = font_manager.findfont(self.font)
        self.font = ImageFont.truetype(self.file, 50)
        self.watermark_text = "Watermark"
        self.red_value = 255
        self.blue_value = 255
        self.green_value = 255
        self.alpha_value = 255

        txt = Image.new('RGBA', (501, 461), (255, 255, 255, 0))

        d = ImageDraw.Draw(txt)

        d.text(self.font_position(0, 0, 20, 20), self.watermark_text, font=self.font, fill=(255, 0, 0, 100))
        txt.save("new.png")
        ui.watermark.setStyleSheet("image: url(new.png);")

    def create_text(self, x, y, ui):
        txt = Image.new('RGBA', (x, y), (255, 255, 255, 0))
        font_size = ui.text_size.value()
        self.font = ImageFont.truetype(self.file, font_size)
        d = ImageDraw.Draw(txt)
        x_value = ui.x_position_slider.value()
        y_value = ui.y_position_slider.value()
        self.red_value = int(ui.red_slider.value()/100 * 255)
        self.blue_value = int(ui.blue_slider.value()/100 * 255)
        self.green_value = int(ui.green_slider.value()/100 * 255)
        self.alpha_value = int(ui.alpha_slider.value()/100 * 255)
        self.watermark_text = ui.watermark_text.text()
        d.text(self.font_position(x_value, y_value, x, y), self.watermark_text,
               font=self.font, fill=(self.red_value, self.green_value, self.blue_value, self.alpha_value))
        txt.save("new.png")
        ui.watermark.setStyleSheet("image: url(new.png);")

    def font_position(self, x_value, y_value, x, y):
        x_position = int(x_value / 100 * x)
        y_position = int(y_value / 100 * y)
        text_position = (x_position, y_position)
        return text_position
