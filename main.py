from src.image_processor import ImageProcessor

if __name__ == "__main__":
    DEFAULT_INPUT_FOLDER = "input_images"
    DEFAULT_OUTPUT_SIZE = 640

    input_folder = (
        input(f"Enter the folder path containing the images: [{DEFAULT_INPUT_FOLDER}] ")
        or DEFAULT_INPUT_FOLDER
    )
    image_processor = ImageProcessor(input_folder)

    output_size = int(
        input("Enter the desired output size: [640] ") or DEFAULT_OUTPUT_SIZE
    )
    image_processor.process_folder(output_size)
