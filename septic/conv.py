from PIL import Image
import os

def convert_heic_to_png(input_folder, output_folder):
    """
    Convert all .heic images in the input_folder to .png images and save them to the output_folder.

    Args:
        input_folder (str): Path to the folder containing .heic files.
        output_folder (str): Path to the folder where .png files will be saved.
    """
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")

            try:
                # Open and convert the image
                with Image.open(input_path) as img:
                    img.save(output_path, "PNG")
                print(f"Converted: {filename} -> {os.path.basename(output_path)}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    input_folder = "."  # Replace with your input folder path
    output_folder = "."  # Replace with your output folder path
    convert_heic_to_png(input_folder, output_folder)
