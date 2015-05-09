import Tkinter
from PIL import ImageDraw, Image, ImageTk


window = Tkinter.Tk(className=" Track Image")

image = Image.open("track.png")
image = image.resize((900, 600), Image.ANTIALIAS)

#-------------------------------------------------- draw = ImageDraw.Draw(image)
#-------------------------------------- draw.line((0, 0) + image.size, fill=128)
#--------------------- draw.line((0, image.size[1], image.size[0], 0), fill=128)


canvas = Tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)


canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    print "clicked at: ", event.x, event.y
    #draw = ImageDraw.Draw(image, None)
    #draw.ellipse((event.x-100,event.y-100,event.x+100,event.y+100), fill=(100,100,100), outline=(255,255,255))
    
    #canvas.create_rectangle(event.x-10,event.y-10,event.x+10,event.y+10)
    
    
#===============================================================================
#     draw = ImageDraw.Draw(image)
#     draw.line((event.x-5,event.y-5) + (event.x+5,event.y+5), fill=128)
#     draw.line((event.x-5,event.y+5) + (event.x+5,event.y-5), fill=128)
# 
#     
#     
#     canvas.insert()
#===============================================================================
    


    #draw.ellipse((event.x-5,event.y-5,event.x+5,event.y+5), fill=(255,255,255))
    #draw.point((event.x,event.y),fill=(255,0,0))
    #.point(event.x, event.y,'red')    
        


canvas.bind("<Button-1>", callback)
Tkinter.mainloop()
