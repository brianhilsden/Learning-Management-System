import qrcode

# Function to generate QR code
def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in the QR code
        border=4,  # thickness of the border (minimum is 4)
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

# Example usage
product_id = "12345"
price = "5000"  # in KSH
data = f"https://brian-omondi.vercel.app/"  # URL for payment
file_path = f"qr_code_{product_id}.png"  # File name for the QR code image
generate_qr_code(data, file_path)
