#Python pillow app with different filter implimatations to edit images
#
#   Robert Zeelie      Created 09 Sep 2019
#
#Scroll to the bottom of this file and replace the input with disired image and uncomment then run
#The list carries on so heres some more exampls:
# Multibandfilter, Rankfilter, etc



from PIL import Image
from PIL import ImageFilter


#functions for each filter
def blur(input_image):
    #function that makes a color image blured
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.BLUR)
    new_image.save('Blur_Image.JPEG')
    
def contour(input_image):
    #function that contours a color image 
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.CONTOUR)
    new_image.save('Contoured_Image.JPEG')
    
def boxblur(input_image):
    #function that allows you to adjust blur amount on image
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.BoxBlur(10))#adjusting the number in boxblur() adjusts blur
    new_image.save('Boxblur_Image.JPEG')

def gaussianblur(input_image):
    #function that makes a color image slightly blured
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.GaussianBlur)
    new_image.save('GaussianBlur_Image.JPEG')
    
def findedge(input_image):
    #function that makes a color image darker with more black noise
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.FIND_EDGES)
    new_image.save('Find_Edges_Image.JPEG')
    
def smooth(input_image):
    #function that makes a color image smooth
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.SMOOTH)
    new_image.save('Smooth_Image.JPEG')
    
def moresmooth(input_image):
    #function that makes a color image smoother than smooth
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.SMOOTH_MORE)
    new_image.save('More_Smooth_Image.JPEG')

    
def detail(input_image):
    #function that makes a color image more detailed
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.DETAIL)
    new_image.save('Detailed_Image.JPEG')
    
def edgeenhance(input_image):
    #function that makes a color image more sharp
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.EDGE_ENHANCE)
    new_image.save('Edge_Enhance_Image.JPEG')
    
def edgeenhancemore(input_image):
    #function that makes a color image even more sharper than edgeenhance
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    new_image.save('Edge_Enhance_More_Image.JPEG')
    
def sharp(input_image):
    #function that makes a color image Sharper than the edgeenhances
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.SHARPEN)
    new_image.save('Sharp_Image.JPEG')
    
def emboss(input_image):
    #function that makes a color image gray with the image carved
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.EMBOSS)
    new_image.save('Emboss_Image.JPEG')
    
def unsharpmask(input_image):
    #function that makes a color image blurs the image, unsharpens and controls brightness
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.UnsharpMask(radius = 10, percent = 500, threshold = 3))
    #radius = blur amount, percent = unsharpen in percent, threshold = brightness
    new_image.save('UnsharpMask_Image.JPEG')
    
def minfilter(input_image):
    #function that makes a color image faded
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.MinFilter)
    new_image.save('Min_Filter_Image.JPEG')
    
def maxfilter(input_image):
    #function that makes a color image faded and brighter
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.MaxFilter)
    new_image.save('Max_Filter_Image.JPEG')
    
def mediumfilter(input_image):
    #function that makes a color image faded and slighttly brighter
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.MedianFilter)
    new_image.save('Medium_Filter_Image.JPEG')
    
def modefilter(input_image):
    #function that makes a color image brighter
    old_image = Image.open(input_image)
    new_image = old_image.filter(ImageFilter.ModeFilter)
    new_image.save('Mode_Filter_Image.JPEG')
    


if __name__ == '__main__':
    #call the functions with the desired input image
    
    #blur('image.JPEG')
    #contour('image.JPEG')
    #boxblur('image.JPEG')
    #gaussianblur('image.JPEG')
    #findedge('image.JPEG')
    #smooth('image.JPEG')
    #moresmooth('image.JPEG')
    #detail('image.JPEG')
    #edgeenhance('image.JPEG')
    #edgeenhancemore('image.JPEG')
    #sharp('image.JPEG')
    #emboss('image.JPEG')
    #unsharpmask('image.JPEG')
    #minfilter('image.JPEG')
    #maxfilter('image.JPEG')
    #mediumfilter('image.JPEG')
    modefilter('image.JPEG')
    print("\nImage transformation complete, Please find edited image in this project folder.\n\n\t\tThank You.\n\nRobert Zeelie")