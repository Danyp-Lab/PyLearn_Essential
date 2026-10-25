import matplotlib.pyplot as plt
import qrcode


def create_qrcode(user_input):
    """Generate and save a QR code image based on the user input."""
    qr_image = qrcode.make(user_input)
    qr_image.save("Qrcode.png")
    return qr_image


def display_qrcode(qr_image):
    """Display the QR code image using matplotlib."""
    plt.imshow(qr_image)
    plt.axis("off")  # Remove axes
    plt.show()


if __name__ == "__main__":
    # Get user contact information
    user_contact_info = input("Enter your name and phone number (e.g., 'dany +989370000000'): ")

    # Create and display QR code
    qr_img = create_qrcode(user_contact_info)
    display_qrcode(qr_img)
