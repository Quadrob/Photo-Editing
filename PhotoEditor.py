
#Simple Application that applies a desired filter to the recived image using the python pillow module
#
#   Robert Zeelie      Created 09 Sep 2019
#
#Scroll to the bottom of this file and replace the input with disired image and run

from PIL import Image


#Black and white filter functions
def black_and_white(input_image):
    #function that turns a color image to a normal black and white image
    old_image = Image.open(input_image)
    new_image = old_image.convert('L')
    new_image.save('BW_Image.JPEG')
   
def black_and_white_dithering(input_image, dithering=True):
    #function that turns a color image to black and white image but with more white noise(dithering)
    old_image = Image.open(input_image)
    if dithering:
        new_image = old_image.convert('1')  
    else:
        new_image = old_image.convert('1', dither=Image.NONE)
        
    new_image.save('BW_Dithring_Image.JPEG')


#Sepia filter functions
def make_sepia_palette(color):
    #function to make a palette which will make our image look more vintage
    palette = []
    r, g, b = color
    for i in range(255):
        palette.extend((r*i//255, g*i//255, b*i//255))
 
    return palette
 
def create_sepia(input_image):
    #function which turns our image to black and white and then applies the sepia palette using putPalette()
    whitish_color = (255, 240, 192)
    sepia = make_sepia_palette(whitish_color)
 
    old_image = Image.open(input_image)
    blackAndwhite_image = old_image.convert('L')
    # add the sepia toning
    blackAndwhite_image.putpalette(sepia)
    
    # convert to RGB for easier saving
    sepia_image = blackAndwhite_image.convert('RGB')
    sepia_image.save('Sepia_Image.JPEG')


#color enhancement filter functions
def saturate(input_image):
    #function that turns a color image to a more saturated and warmer look
    old_image = Image.open(input_image)
    new_image = old_image.convert('CMYK')
    new_image.save('Color_Enhance.JPEG')


    
 
if __name__ == '__main__':
    #call the functions with the desired input image
    
    black_and_white_dithering('image.JPEG')
    black_and_white('image.JPEG')
    create_sepia('image.JPEG')
    saturate('image.JPEG')
    print("\nImage transformation complete, Please find edited image in this project folder.\n\n\t\tThank You.\n\nRobert Zeelie")