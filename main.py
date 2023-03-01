import PIL.Image
ASCII_chars = ["@","#","S","%","?","*","+",";",":",",","."]



#resizing the image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width/1.65
    new_height =  int(new_width*ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


# adding a gray filter to the resized image
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)


#pixels to ascii tranform
def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_chars[pixel//25] for pixel in pixels])
    return(characters)



def main(new_width=100):
    path = input("srbs tswira")
    try:
       image= PIL.Image.open(path)
    except:
        print(path,"this is an invalid path")

    new_image_data = pixel_to_ascii(grayify(resize_image(image)))


    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    print(ascii_image)

    with open("ascii_image.txt","w") as f:
     f.write(ascii_image)





main()