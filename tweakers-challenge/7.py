from PIL import Image
im = Image.open("7.jpg")
pixels = im.load()

for y in range(0,im.size[1]):
   for x in range(0,im.size[0]):
       # eerst de randen skippen
       if x not in [0,1,im.size[0]-1, im.size[0]-2] and y not in [0,1,im.size[1]-1, im.size[1]-2]:
           # en nu de pixels selecteren... een beetje wit telt ook als wit.
           if pixels[x,y] not in  [(255,255,255), (254, 254, 254),(253, 253, 253)]:
               print ("X: "+str(x)+" Y:"+str(y) + " " + str(pixels[x,y] ))