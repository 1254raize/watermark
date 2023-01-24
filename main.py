import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow
from watermark import Ui_MainWindow
from PIL import ImageFont, ImageDraw, Image
from text_position import TextPosition
from text_image import TextImage


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen_file.triggered.connect(self.open_file_dialog)
        self.ui.x_position_slider.valueChanged.connect(self.slider)
        self.ui.y_position_slider.valueChanged.connect(self.slider)
        self.ui.red_slider.valueChanged.connect(self.slider)
        self.ui.green_slider.valueChanged.connect(self.slider)
        self.ui.blue_slider.valueChanged.connect(self.slider)
        self.ui.alpha_slider.valueChanged.connect(self.slider)
        self.ui.watermark_text.textChanged.connect(self.slider)
        self.ui.save_button.clicked.connect(self.file_save)
        self.ui.text_size.textChanged.connect(self.slider)
        self.x = 501
        self.y = 461
        self.text_position = TextPosition(self.ui)
        self.fname = ""
        self.show()

    def open_file_dialog(self):
        home_dir = str(Path.home())
        print(home_dir)

        self.fname, ok = QFileDialog.getOpenFileName(None, "Select an Image", home_dir, "Images (*.png *.jpg)")

        if ok:

            with Image.open(self.fname).convert("RGBA") as im:

                self.x = int(im.size[0])
                self.y = int(im.size[1])
                aspect_ratio = self.x/self.y
                if self.x > self.y:
                    self.x = 501
                    self.x = int(self.x/aspect_ratio)
                elif self.y > self.x:
                    self.y = 461
                    self.x = int(self.y*aspect_ratio)
                else:
                    self.x = 501
                    self.y = 461

                print(im.size)
                print(f"{self.x} / {self.y}")

                # self.create_text(self.x, self.y)

                # combined = Image.alpha_composite(im, txt)
                # combined.save("new.png")
                # combined.show()

                self.ui.image.setStyleSheet(f"image: url({self.fname});")
                self.ui.watermark.setStyleSheet("image: url(new.png);")

    def slider(self):
        self.text_position.create_text(self.x, self.y, self.ui)

    def file_save(self):
        with Image.open(self.fname).convert("RGBA") as im:
            draw = ImageDraw.Draw(im)
            name = QFileDialog.getSaveFileName(self, 'Save File', "Images (*.png *.jpg)")

            TextImage(x=im.size[0],
                      y=im.size[1],
                      text=self.text_position.watermark_text,
                      r=self.text_position.red_value,
                      g=self.text_position.green_value,
                      b=self.text_position.blue_value,
                      a=self.text_position.alpha_value,
                      ui=self.ui,
                      x_proportion=self.x)

            txt = Image.open("final.png")
            print(name)
            combined = Image.alpha_composite(im, txt)
            combined.save(f"{name[0]}.png")
            combined.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Window()
    sys.exit(app.exec())
