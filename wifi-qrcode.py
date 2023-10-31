# import modules
import qrcode
from PIL import Image

content_array = [['2.4GHz.png', 'WIFI:T:WPA;S:<2.4Ghz-SSID>;P:<2.4GHz-password>;;'],
                 ['5GHz.png', 'WIFI:T:WPA;S:<5GHz-SSID>;P:<5GHz-password>;;']]
           
for content in content_array:
    # taking image which user wants
    # in the QR code center
    Logo_link = content[0]

    logo = Image.open(Logo_link)

    # taking base width
    basewidth = 100

    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.LANCZOS)
    QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # taking url or text
    text = content[1]

    # adding URL or text to QRcode
    QRcode.add_data(text)

    # generating QR code
    QRcode.make()

    # taking color name from user
    QRcolor = 'Black'

    # adding color to QR code
    QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
	   (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    # save the QR code generated
    QRimg.save('QRcode-'+Logo_link)
    QRimg.close()

    print('QR code generated!')
