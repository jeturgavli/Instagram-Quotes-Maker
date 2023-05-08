from PIL import Image, ImageDraw, ImageFont
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)



def main():
    template = input("Chose Background : ")
    templateBg = Image.open(f'Backgrounds/{template}.jpg')

    font_object =  ImageFont.truetype('Fonts/arial.ttf', 40 )

    drawing_object = ImageDraw.Draw(templateBg)

    Parmanet_BG = Image.open('Program Stuff/Img-2.png')
    templateBg.paste(Parmanet_BG, Parmanet_BG)

    text0 = input("0 line : ")
    text1 = input("1 Line : ")
    text2 = input("2 Line : ")
    text3 = input("3 Line : ")
    text4 = input("4 Line : ")
    
    # L0-450 L1-500 L2-550 L3-600 L4-650 L5-700 L6-750 L7-800 L8-850 L9-900
    print("")
    
    white = (251,255,255)
    black = (0,0,0)

    if white or black:
        color = input("White or black color : ")

        
    textcolor = color

    #shadows
    drawing_object.text((122,750), text0, fill=black, font = font_object )
    drawing_object.text((122,800), text1, fill=black, font = font_object )
    drawing_object.text((122,850), text2, fill=black, font = font_object )
    drawing_object.text((122,900), text3, fill=black, font = font_object )
    drawing_object.text((122,950), text4, fill=black, font = font_object )
    

    drawing_object.text((120,750), text0, fill=textcolor, font = font_object )
    drawing_object.text((120,800), text1, fill=textcolor, font = font_object )
    drawing_object.text((120,850), text2, fill=textcolor, font = font_object )
    drawing_object.text((120,900), text3, fill=textcolor, font = font_object )
    drawing_object.text((120,950), text4, fill=textcolor, font = font_object )


    BGQuoteSave = input("Save Your Image Name : ")
    templateBg.save(f'Quotes_Output/{BGQuoteSave}.jpg')

    Repeat = input("Would You Like To Run Again ? Y or N ",).lower()
    if Repeat =="y":
        main()
    else:
        print("n")
        exit()

    print("")


main()

