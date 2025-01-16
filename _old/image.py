




def getImage():
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    import numpy as np
    
    img = mpimg.imread("aa.jpg")
    #img.setflags(write=1)
    img = img.copy()

    for i in range(0,10):
        for j in range(0,10):
            #print(img[i][j][0])
            img[i][j][0] = 255
            img[i][j][1] = 255
            img[i][j][2] = 255

    plt.imshow(img)
    plt.show()

    #for a in img:
    #    for b in a:
     #       print(b)


def getImA():
    from matplotlib import pyplot as plt
    from matplotlib import cm

    from PIL import Image
    from numpy import array

    im = Image.open('ab.jpg')

    return(im)
    #ncols, nrows = im.size
    #ima = array(im.getdata()).reshape((nrows, ncols))
    #plt.imshow(ima, cmap=cm.Greys_r)


def getIm():
    from skimage import io
    im = io.imread('plop.png')

    import matplotlib.pyplot as plt

    plt.imshow(im)
    plt.show()

    print(im)



a = getIm()



