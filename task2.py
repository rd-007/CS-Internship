from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, output_path, key):
    """
    Encrypts an image by swapping pixel values and applying XOR operation.
    """
    # Open the image
    img = Image.open(image_path)
    pixels = np.array(img)

    # Perform encryption
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            # Swap pixel values (e.g., swap red and blue channels)
            pixels[i, j][0], pixels[i, j][2] = pixels[i, j][2], pixels[i, j][0]

            # Apply XOR operation to each channel
            pixels[i, j] ^= key

    # Save the encrypted image
    encrypted_img = Image.fromarray(pixels)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    """
    Decrypts an image by reversing the encryption process.
    """
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = np.array(img)

    # Perform decryption
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            # Apply XOR operation to each channel (reverse the encryption)
            pixels[i, j] ^= key

            # Swap pixel values back (e.g., swap red and blue channels)
            pixels[i, j][0], pixels[i, j][2] = pixels[i, j][2], pixels[i, j][0]

    # Save the decrypted image
    decrypted_img = Image.fromarray(pixels)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    # Input parameters
    image_path = input("Enter the path to the image (e.g., image.jpg): ")
    
    # Validate image path
    while not os.path.isfile(image_path):
        print("Invalid file path. Please try again.")
        image_path = input("Enter the path to the image (e.g., image.jpg): ")

    output_encrypted = input("Enter the path to save the encrypted image (e.g., encrypted_image.png): ")
    output_decrypted = input("Enter the path to save the decrypted image (e.g., decrypted_image.png): ")
    
    # Validate output paths
    if not output_encrypted.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        print("Invalid output format for encrypted image. Defaulting to .png")
        output_encrypted += '.png'
    
    if not output_decrypted.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        print("Invalid output format for decrypted image. Defaulting to .png")
        output_decrypted += '.png'

    try:
        key = int(input("Enter an integer key for encryption/decryption: "))
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return

    # Encrypt the image
    encrypt_image(image_path, output_encrypted, key)

    # Decrypt the image
    decrypt_image(output_encrypted, output_decrypted, key)

if __name__ == "__main__":
    main()
