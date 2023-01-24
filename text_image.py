from PIL import ImageFont, ImageDraw, Image
from matplotlib import font_manager


class TextImage:

    def __init__(self, x, y, text, r, g, b, a, ui, x_proportion):
        font_size_s = ui.text_size.value()
        font_size_b = int(font_size_s*x/x_proportion)
        self.font = font_manager.FontProperties(family='sans-serif', weight='bold')
        self.file = font_manager.findfont(self.font)
        self.font = ImageFont.truetype(self.file, font_size_b)

        txt = Image.new('RGBA', (x, y), (255, 255, 255, 0))

        d = ImageDraw.Draw(txt)

        x_position = int(ui.x_position_slider.value()/100 * x)
        y_position = int(ui.y_position_slider.value()/100 * y)

        d.text((x_position, y_position), text, font=self.font, fill=(r, g, b, a))
        txt.save("final.png")
