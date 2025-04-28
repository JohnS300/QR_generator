from qrcode import QRCode
from PIL import Image


def build_qr(data: str, fill_color: str, back_color: str) -> Image.Image:
    """
    Create a QR code image with given fill and background colors.
    """
    qr = QRCode(version=3, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    try:
        return qr.make_image(fill_color=fill_color, back_color=back_color)
    except ValueError as e:
        print(f"Color error: {e}, falling back to defaults.")
        return qr.make_image(fill_color="black", back_color="white")