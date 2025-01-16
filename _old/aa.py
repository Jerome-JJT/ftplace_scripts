

prec = 54

def getImage():
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    import numpy as np
    imgdest = mpimg.imread("aa.jpg").copy()

    imgsrc = mpimg.imread("def.png").copy()

    for a in enumerate(imgsrc):
        for b in enumerate(a[1]):
            for i in range(0,3):
                imgdest[a[0]][b[0]][i] -= imgdest[a[0]][b[0]][i]%prec
                imgdest[a[0]][b[0]][i] = int(b[1][i]*prec)

    plt.imshow(imgdest)
    mpimg.imsave("ab.jpg",imgdest)
    #plt.show()


def viewImage():
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    import numpy as np
    img = mpimg.imread("gg.jpg").copy()

    print(img)

    for a in enumerate(img):
        print(a[1])

    plt.imshow(img)
    #plt.show()

def testImage():
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    import numpy as np
    img = mpimg.imread("gg.jpg").copy()


    for a in range(0,100):
        for b in range(0,100):
            img[a][b][0] = 255
            img[a][b][1] = 255
            img[a][b][2] = 255

    plt.imshow(img)
    plt.show()

#viewImage()

def notReadImage():
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    import numpy as np

    imgread = mpimg.imread("aa.jpg").copy()

    for a in enumerate(imgread):
        for b in enumerate(a[1]):
            for i in range(0,3):
                imgread[a[0]][b[0]][i] = ((imgread[a[0]][b[0]][i]%prec)*prec)
                
    plt.imshow(imgread)
    plt.show()
    

def readImage():
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    import numpy as np

    imgread = mpimg.imread("ab.jpg").copy()

    for a in enumerate(imgread):
        for b in enumerate(a[1]):
            for i in range(0,3):
                imgread[a[0]][b[0]][i] = (imgread[a[0]][b[0]][i]%prec)*(256/prec)
                
    plt.imshow(imgread)
    plt.show()

#getImage()
#readImage()

                
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
imgdest = mpimg.imread("te/inp.jpg").copy()
plt.imshow(imgdest)
plt.show()


#print(str(number)[1:])








    
