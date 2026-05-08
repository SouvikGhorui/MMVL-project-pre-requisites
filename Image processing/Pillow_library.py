from PIL import Image
img = Image.open('Photos/test_flower.jpg')
print(img.size)

#squeeze the image into desired size
small_img = img.resize((500,500))
small_img.save('Photos/small_test_flower.jpg')

# resize the image
img.thumbnail((500,500))
img.save('Photos/crop_test_flower.jpg')

