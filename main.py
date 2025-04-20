import os
import hashlib
import pyperclip # type: ignore
import qrcode # type: ignore
from PIL import Image # type: ignore

def clipboard(file_path):
    pyperclip.copy(file_path)
    print("File path copied to clipboard.")

def encode(data):
    hash_val = hashlib.md5(data.encode()).hexdigest()[:6]
    return hash_val

def image_creation(data):
    qr = qrcode.QRCode(version=3, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    fill = input("Enter fill corol (default = black): ") or "black"
    back = input("Enter background color (default = white): ") or "white"
    try:
        image = qr.make_image(fill_color= fill, back_color = back)
    except ValueError as e:
        print(f'Color error: {e}')
        print('Falling back to default colors.')
        image =qr.make_image(fill_color = 'Black', back_color = "white")
    
    return image

def log_data(folder, file_name, data):
    with open(os.path.join(folder, "qr_log.txt"), "a") as log_file:
        log_file.write(f"{file_name}: {data}\n")

def folder_creation(name):
    if not os.path.exists(name):
        os.makedirs(name)

def qrGenerator():

    while True:
        data = input("Enter anything to generate QR code : ")
        if (data == ''):
            print('No input. Please enter information to generate a QR code')
        else:
            break

    image = image_creation(data)
    
    folder_name= 'QRcodes'
    folder_creation(folder_name)


    file_name = f"qr_code_{encode(data)}.png"
    file_path = os.path.join(folder_name,file_name)
    image.save(file_path)
    print(f'QR code generated in {file_path}')

    clipboard(file_path)
    
    #Image.open(file_path).show()
    log_data(folder_name,file_name,data)


    
if __name__ == '__main__':
    while True:
        qrGenerator()
        again = input("Generate another QR code? (y/n): ").lower()
        if again != 'y':
            break