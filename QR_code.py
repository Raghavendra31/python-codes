import qrcode


img = qrcode.make('https://github.com/Raghavendra31')
type(img)  
img.save("some_file.png")
