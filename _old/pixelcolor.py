from PIL import Image, ImageDraw, ImageFont
import datetime

chunk = 15

fntsize = 20
fntsize = 8
fnt = ImageFont.truetype("arial.ttf", fntsize)
#92D050 00B0F0

trichunk = 15


#Min min = 2
start = 2
end = 20
imdir = "images2"

##end = int(input("Nb "))
##chunk = int(input("taille vue "))
##trichunk = int(input("taille tri "))
##imdir = input("dir images ")

def mathmap(x, in_min, in_max, out_min, out_max):
    return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def getcolor(index):
    r = int(mathmap(index, 0.0, 1.0, 146, 0))
    g = int(mathmap(index, 0.0, 1.0, 208, 176))
    b = int(mathmap(index, 0.0, 1.0, 80, 240))
    return (r, g, b)

def getcolorold(index):
    return (0, 255-int(rgbindex/1.5), rgbindex)

triwidth = (end-2)*trichunk
triheight = (end-2)*trichunk
triimg = Image.new('RGB', (triwidth, triheight), color = 'white')
trid = ImageDraw.Draw(triimg)

for j in range(0, end):
    for k in range(0, end):
        trid.rectangle( ( (j*trichunk,(k-2)*trichunk), ((j+1)*trichunk,(k-1)*trichunk) ), fill='white', outline=(100,100,100))


for i in range(start, end):
    width = (i-1)*chunk
    height = (i+1)*chunk
    img = Image.new('RGB', (width, height), color = 'white')
    d = ImageDraw.Draw(img)

    for j in range(1, i):
            sqcolor = getcolor(j/(i-1))
            sqx = (j-1)*chunk
            
            d.rectangle( ( (sqx, 0), (sqx+chunk, chunk) ), fill=sqcolor, outline='black')
            d.text((sqx+0.1*chunk, 0), str(j), font=fnt, fill='black')
            
    for j in range(1, i):
        for k in range(0, i+1):
            sqvalue = (j*k)%i
            sqcolor = getcolor(sqvalue/(i-1))
            sqx = (j-1)*chunk
            sqy = (k+1)*chunk
            
            d.rectangle( ((sqx, sqy), (sqx+chunk, sqy+chunk)), fill=sqcolor, outline='black')
            d.text( (sqx+0.1*chunk, sqy), str(sqvalue), font=fnt, fill='black')
            if (sqvalue == i-j):
                if (k == i-1):
                    trid.rectangle( ( ((j-1)*trichunk,(k-1)*trichunk), (j*trichunk,k*trichunk) ), fill='black')
                break
    
    img.save(imdir+'/view'+str(i)+'.png')
    print (str(i)+" finised at "+datetime.datetime.now().strftime("%H:%M:%S"))
#img.show()

triimg.save(imdir+'/_trian.png')
#triimg.show()

