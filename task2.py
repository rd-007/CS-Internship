from PIL import Image
import numpy as np
import argparse

def encrypt_image(image_path, output_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Simple encryption by swapping pixel values
    encrypted_array = image_array.copy()
    encrypted_array[:, :, 0], encrypted_array[:, :, 1] = image_array[:, :, 1], image_array[:, :, 0]
    
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Simple decryption by swapping pixel values back
    decrypted_array = image_array.copy()
    decrypted_array[:, :, 0], decrypted_array[:, :, 1] = image_array[:, :, 1], image_array[:, :, 0]
    
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Encrypt or decrypt an image using pixel manipulation.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")

    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_image(args.input, args.output)
    elif args.mode == "decrypt":
        decrypt_image(args.input, args.output)
    