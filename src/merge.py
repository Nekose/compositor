from PIL import Image, ImageDraw, ImageFont
import os

def two_way_merge(source1: str, source1label: str, source2: str, source2label: str, destination: str, horizontal:bool = True) -> None:
    """
    Merges images found in two folders. Images are matched alphabetically
    :param source1: folder for first picture set
    :param source1label: label to be placed on all pictures from first picture set
    :param source2: folder for second picture set
    :param source2label: label to be placed on all pictures from first picture set
    :param destination: destination folder
    :param horizontal: Default True, designates if folders should be joined horizontally or vertically
    :return: None
    """
    folder1 = []
    folder2 = []
    for filename in os.listdir(source1):
        if filename.endswith((".jpg",".jpeg","png","gif")):
            folder1.append(filename)
    for filename in os.listdir(source2):
        if filename.endswith((".jpg",".jpeg","png","gif")):
            folder2.append(filename)
    folder1.sort()
    folder2.sort()
    myFont = ImageFont.truetype("src/arial.ttf", 60)
    for combo in zip(folder1,folder2):
        image1 = Image.open(source1 + "/" + combo[0])
        d1 = ImageDraw.Draw(image1)
        d1.text((28, 36), source1label, fill=(255, 255, 255), font=myFont)
        #image1.show()
        image2 = Image.open(source2 + "/" + combo[1])
        d2 = ImageDraw.Draw(image2)
        d2.text((28, 36), source2label, fill=(255, 255, 255), font=myFont)
        image1_size = image1.size
        if horizontal == True:
            new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (255,255,255))
            new_image.paste(image1,(0,0))
            new_image.paste(image2,(image1_size[0],0))
        else:
            new_image = Image.new('RGB', (image1_size[0], 2 * image1_size[1]), (255, 255, 255))
            new_image.paste(image1, (0, 0))
            new_image.paste(image2, (0, image1_size[1]))
        filename = combo[0]
        print(f"merging {combo[0]} with {combo[1]}")
        if not os.path.isdir(f'src/images/{destination}/'):
            os.mkdir(f'src/images/{destination}/')
        new_image.save(f"src/images/{destination}/{filename}","JPEG",quality=95)

def four_way_merge(source1,source1label,source2,source2label,source3,source3label,source4,source4label,destination):
    folder1 = []
    folder2 = []
    folder3 = []
    folder4 = []
    myFont = ImageFont.truetype("src/arial.ttf", 60)
    for filename in os.listdir(source1):
        if filename.endswith((".jpg",".jpeg","png","gif")):
            folder1.append(filename)
    for filename in os.listdir(source2):
        if filename.endswith((".jpg",".jpeg","png","gif")):
            folder2.append(filename)
    for filename in os.listdir(source3):
        if filename.endswith((".jpg",".jpeg","png","gif")):
            folder3.append(filename)
    for filename in os.listdir(source4):
        if filename.endswith((".jpg",".jpeg","png","gif")):
            folder4.append(filename)
    folder1.sort()
    folder2.sort()
    folder3.sort()
    folder4.sort()
    for file1,file2,file3,file4 in zip(folder1,folder2,folder3,folder4):
        image1 = Image.open(source1 + "/" + file1)
        d1 = ImageDraw.Draw(image1)
        d1.text((28, 36), source1label, fill=(255, 255, 255), font=myFont)
        dimensions = image1.size
        print(dimensions)
        image2 = Image.open(source2 + "/" + file2)
        d2 = ImageDraw.Draw(image2)
        d2.text((28, 36), source2label, fill=(255, 255, 255), font=myFont)
        image3 = Image.open(source3 + "/" + file3)
        d3 = ImageDraw.Draw(image3)
        d3.text((28, 36), source3label, fill=(255, 255, 255), font=myFont)
        image4 = Image.open(source4 + "/" + file4)
        d4 = ImageDraw.Draw(image4)
        d4.text((28, 36), source4label, fill=(255, 255, 255), font=myFont)
        new_image = Image.new('RGB', (2 * dimensions[0], 2 * dimensions[1]), (255, 255, 255))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (dimensions[0], 0))
        new_image.paste(image3, (0, dimensions[1]))
        new_image.paste(image4, (dimensions[0], dimensions[1]))
        filename = file1
        #new_image.show()
        print(f"merging {file1},{file2},{file3},{file4}")
        if not os.path.isdir(f'src/images/{destination}/'):
            os.mkdir(f'src/images/{destination}/')
        new_image.save(f"src/images/{destination}/{filename}", "JPEG", quality=95)

def three_way_merge(source1,source1label,source2,source2label,source3,source3label,destination):
    folder1 = []
    folder2 = []
    folder3 = []
    myFont = ImageFont.truetype("src/arial.ttf", 60)
    for filename in os.listdir(source1):
        if filename.endswith((".jpg",".jpeg","png","gif")):
            folder1.append(filename)
    for filename in os.listdir(source2):
        if filename.endswith((".jpg",".jpeg","png","gif")):
            folder2.append(filename)
    for filename in os.listdir(source3):
        if filename.endswith((".jpg",".jpeg","png","gif")):
            folder3.append(filename)
    folder1.sort()
    folder2.sort()
    folder3.sort()
    for file1,file2,file3 in zip(folder1,folder2,folder3):
        image1 = Image.open(source1 + "/" + file1)
        d1 = ImageDraw.Draw(image1)
        d1.text((28, 36), source1label, fill=(255, 255, 255), font=myFont)
        dimensions = image1.size
        print(dimensions)
        image2 = Image.open(source2 + "/" + file2)
        d2 = ImageDraw.Draw(image2)
        d2.text((28, 36), source2label, fill=(255, 255, 255), font=myFont)
        image3 = Image.open(source3 + "/" + file3)
        d3 = ImageDraw.Draw(image3)
        d3.text((28, 36), source3label, fill=(255, 255, 255), font=myFont)
        new_image = Image.new('RGB', (2 * dimensions[0], 2 * dimensions[1]), (30,30,30))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (dimensions[0], 0))
        new_image.paste(image3, (int(dimensions[0] / 2), dimensions[1]))
        filename = file1
        #new_image.show()
        print(f"merging {file1},{file2},{file3}")
        if not os.path.isdir(f'src/images/{destination}/'):
            os.mkdir(f'src/images/{destination}/')
        new_image.save(f"src/images/{destination}/{filename}", "JPEG", quality=95)