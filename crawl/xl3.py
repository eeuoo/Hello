import openpyxl
from PIL import Image

book = openpyxl.load_workbook("/Users/lhj/images/xl_output.xlsx")

sheet = book.active

imgFile = '/Users/lhj/images/test4.png'
# img =  openpyxl.drawing.image.Image(imgFile)
# sheet.add_image(img, 'B5')


img2 = Image.open(imgFile)
new_img = img2.resize((50,30))
new_img.save('new_test4.png')
img3 = openpyxl.drawing.image.Image('new_test4.png')
sheet.add_image(img3, 'A5')

book.save("/Users/lhj/images/xl_output.xlsx")