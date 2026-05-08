from PIL import Image
img = Image.open('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/test_flower.jpg')
print(img.size)

#squeeze the image into desired size
small_img = img.resize((500,500))
small_img.save('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/small_test_flower.jpg')

# resize the image
img.thumbnail((500,500))
img.save('C:/Users/sghor/Desktop/Souvik/Programming/Image processing/Photos/crop_test_flower.jpg')

