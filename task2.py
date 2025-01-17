from PIL import Image
import numpy as np
import os

def encrypt_image(input_image_path, output_image_path):
    # Open the image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Encrypt the image by swapping pixel values and applying a simple operation
    encrypted_array = np.copy(img_array)
    height, width, channels = img_array.shape

    for i in range(height):
        for j in range(width):
            # Swap pixel values with the next pixel
            if j < width - 1:
                encrypted_array[i, j], encrypted_array[i, j + 1] = img_array[i, j + 1], img_array[i, j]
            # Apply a simple operation (e.g., add 1 to each pixel value)
            encrypted_array[i, j] = (encrypted_array[i, j] + 1) % 256

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path):
    # Open the encrypted image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Decrypt the image by reversing the operations
    decrypted_array = np.copy(img_array)
    height, width, channels = img_array.shape

    for i in range(height):
        for j in range(width):
            # Reverse the simple operation (subtract 1 from each pixel value)
            decrypted_array[i, j] = (decrypted_array[i, j] - 1) % 256
            # Swap pixel values back
            if j > 0:
                decrypted_array[i, j], decrypted_array[i, j - 1] = img_array[i, j - 1], img_array[i, j]

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_image_path = input("Enter the path of the image to encrypt: ")
            if os.path.exists(input_image_path):
                output_image_path = input("Enter the path to save the encrypted image: ")
                encrypt_image(input_image_path, output_image_path)
            else:
                print("The specified image file does not exist. Please try again.")
        
        elif choice == '2':
            input_image_path = input("Enter the path of the image to decrypt: ")
            if os.path.exists(input_image_path):
                output_image_path = input("Enter the path to save the decrypted image: ")
                decrypt_image(input_image_path, output_image_path)
            else:
                print("The specified image file does not exist. Please try again.")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()