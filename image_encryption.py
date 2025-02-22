from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Perform a simple encryption by swapping pixel values
    encrypted_array = img_array.copy()
    height, width, _ = img_array.shape

    for i in range(height):
        for j in range(width):
            # Swap the red and blue channels
            encrypted_array[i, j, 0], encrypted_array[i, j, 2] = img_array[i, j, 2], img_array[i, j, 0]

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path):
    # Open the encrypted image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Perform decryption by swapping back the pixel values
    decrypted_array = img_array.copy()
    height, width, _ = img_array.shape

    for i in range(height):
        for j in range(width):
            # Swap the red and blue channels back
            decrypted_array[i, j, 0], decrypted_array[i, j, 2] = img_array[i, j, 2], img_array[i, j, 0]

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    while True:
        action = input("Would you like to encrypt or decrypt an image? (e/d) or 'q' to quit: ").strip().lower()

        if action == 'e':
            input_image = input("Enter the name of the image file to encrypt (e.g., input_image.jpg): ").strip()
            output_image = input("Enter the name for the encrypted image file (e.g., encrypted_image.jpg): ").strip()
            try:
                encrypt_image(input_image, output_image)
            except Exception as e:
                print(f"Error: {e}")

        elif action == 'd':
            input_image = input("Enter the name of the encrypted image file to decrypt (e.g., encrypted_image.jpg): ").strip()
            output_image = input("Enter the name for the decrypted image file (e.g., decrypted_image.jpg): ").strip()
            try:
                decrypt_image(input_image, output_image)
            except Exception as e:
                print(f"Error: {e}")

        elif action == 'q':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit.")