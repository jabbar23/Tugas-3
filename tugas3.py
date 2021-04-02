import PIL
from PIL import Image, ImageEnhance, ImageDraw, ImageFont

img = Image.open('zenitsu.jpg')

#1
#img.show()
#img.save('zenitsu.bmp', format='BMP')

#2
"""
print(img.filename)
print(img.format)
print(img.mode)
print(img.size)
print(img.width)
print(img.height)
print(img.info)
"""

#3
#resized_img = img.resize((600, 600))
#resized_img.save('resized.jpg')

#4
#img.thumbnail((120, 120))
#img.save('thumb.jpg')

#5
#crop_img = img.crop((340, 20, 560, 230))
#crop_img.save('cropped.jpg')

#6
#border_img = PIL.Image.new(mode='RGB', size=(img.width+20, img.height+20), color='skyblue')
#border_img.paste(img, (10, 10))
#border_img.save('border.jpg')

#7
#rotated = img.transpose(Image.ROTATE_180)
#rotated.show()
#rotated.save('rotate180.jpg')

#8
#flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
#flipped.show()
#flipped.save('flipped.jpg')

#9
"""
# buat instansi enhancer untuk brightness
enhancer = ImageEnhance.Brightness(img)

factor = 1
# panggil metode enhance untuk memanipulasi
im_output = enhancer.enhance(factor)
#im_output.save('original-image.png')

factor = 0.5 # darkens
im_output = enhancer.enhance(factor)
im_output.save('darkened.png')

factor = 1.5 # brightens
im_output = enhancer.enhance(factor)
im_output.save('brightened.png')

enhancer = ImageEnhance.Contrast(img)

factor = 1
im_output = enhancer.enhance(factor)
#im_output.save('original-image.png')

factor = 0.5 # kurangi kontras
im_output = enhancer.enhance(factor)
im_output.save('less-contrast.png')

factor = 1.5 # tambah kontras
im_output = enhancer.enhance(factor)
im_output.save('more-contrast.png')

enhancer = ImageEnhance.Sharpness(img)

factor = 1
im_s_1 = enhancer.enhance(factor)
#im_s_1.save('original-image.png')

factor = 15
im_s_1 = enhancer.enhance(factor)
im_s_1.save('blurred.png')

factor = 2
im_s_1 = enhancer.enhance(factor)
im_s_1.save('sharpened.png')
"""

#10
"""
# Buka gambar sumber
img = Image.open('zenitsu.jpg')
width, height = img.size  # lebar dan tinggi untuk kalkulasi koordinat teks

# menambahkan elemen 2d ke gambar yang sudah ada
draw = ImageDraw.Draw(img)

text = 'JAR - 56417826' # ganti dengan npm mu...

# mendefinisikan font baru, lengkap dengan ukurannya
font = ImageFont.truetype('arial.ttf', 40)
# hitung lebar dan tinggi font relatif terhadap gambar utama
textwidth, textheight = draw.textsize(text, font)

# hitung koordinat x, y teks
margin = 15
x = width - textwidth - margin
y = height - textheight - margin

# terapkan watermark
draw.text((x, y), text, fill='blue',font=font)
img.show()

# Simpan gambar
img.save('watermark.jpg')
"""