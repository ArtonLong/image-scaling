from PIL import Image

def nearestNeighborScaling(original, new_width, new_height):
    width, height = original.size
    new_image = Image.new("RGB", (new_width, new_height))
    for x in range(0, new_width):  
      for y in range(0, new_height):
        srcX = int( round( float(x) / float(new_width) * float(width) ) )
        srcY = int( round( float(y) / float(new_height) * float(height) ) )
        srcX = min( srcX, width-1)
        srcY = min( srcY, height-1)
        color = original.getpixel((srcX, srcY))

        #color = grayScale(color)
        #color = invertColor(color)
        #color = addFilter(color, (0,0,25))

        new_image.putpixel((x,y), color)

    return new_image

def addFilter(color, filter): 
  new_color = []

  for i, c in enumerate(color):
    new_color.append(max(min(c + filter[i], 255), 0))
  return tuple(new_color)
   
def invertColor(color):
  return (255-color[0], 255-color[1], 255-color[2])

def grayScale(color):
  c = max(color)
  return (c,c,c)

img = Image.open("test.jpeg")
width, height = img.size
print("old: ", width, height)

new_width = int(width*3)
new_height = int(height*3)
print("new: ", new_width, new_height)

new_img = nearestNeighborScaling(img, new_width, new_height)

new_img.save("resized_image.jpeg")