import os
from datetime import datetime

from PIL import Image as ImageModule
from PIL.Image import Image


class ImageProcessor:
    PADDING_COLOR = (114, 114, 114)
    DATETIME_FORMAT = "%Y%m%d%H%M%S"
    OUTPUT_ROOT = "dataset"

    def __init__(self, folder: str):
        if not os.path.isdir(folder):
            raise ValueError(f"Folder '{folder}' does not exist.")

        self.folder = folder

    def process_folder(self, output_size: int = 640):
        """Process all images in the folder.

        See `process_image` for details about the processing.
        See `_create_output_folder` for details about the output folder.
        Supported file formats: .jpg
        """
        output_folder = self._create_output_folder()
        for file in os.listdir(self.folder):
            if not file.endswith(".jpg"):
                return

            image_input_path = os.path.join(self.folder, file)
            image_output_path = os.path.join(output_folder, file)
            with ImageModule.open(image_input_path) as image:
                image = self.process_image(image, output_size)
                image.save(image_output_path)

    def process_image(self, image: Image, output_size: int) -> Image:
        """Process a single image.

        - Resize the image to a square of size `output_size`.
        - Add padding at bottom and right if necessary.

        Returns:
            Image: The new processed image as RGB.
        """

        image = self._resize_square(image, output_size)
        image = self._add_padding(image, output_size)
        return image

    def _resize_square(self, image: Image, output_size: int) -> Image:
        """Resize the image to fit inside a square of size `output_size`.

        The aspect ratio is preserved.
        """
        ratio = output_size / max(image.size)
        new_size = (round(image.width * ratio), round(image.height * ratio))
        return image.resize(new_size)

    def _add_padding(self, image: Image, output_size: int):
        """Add padding at bottom and right to make the image square."""

        new_image = ImageModule.new(
            "RGB", (output_size, output_size), self.PADDING_COLOR
        )
        new_image.paste(image, (0, 0))
        return new_image

    def _create_output_folder(self):
        """Create a new output folder based on the current datetime."""
        folder_path = os.path.join(
            self.OUTPUT_ROOT, datetime.now().strftime(self.DATETIME_FORMAT)
        )
        os.makedirs(folder_path, exist_ok=True)
        return folder_path
