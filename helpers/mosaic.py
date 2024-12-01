import glob
import random
from PIL import Image


def create_image_mosaic(
    input_pattern, output_path, tile_width=300, tile_height=300, columns=5
):
    """
    Create a mosaic of uniformly sized and cropped images using Pillow.

    :param input_pattern: Glob pattern to select input images (e.g., '/path/to/images/*.jpg')
    :param output_path: Path to save the output mosaic image
    :param tile_width: Width of each tile in the mosaic
    :param tile_height: Height of each tile in the mosaic
    :param columns: Number of columns in the mosaic
    """
    image_paths = glob.glob(input_pattern)

    # Calculate rows needed
    total_images = len(image_paths)
    rows = (total_images + columns - 1) // columns

    # Create a blank canvas for the mosaic
    mosaic_width = tile_width * columns
    mosaic_height = tile_height * rows
    mosaic = Image.new("RGB", (mosaic_width, mosaic_height), color="white")

    random.shuffle(image_paths)
    for index, image_path in enumerate(image_paths):
        with Image.open(image_path) as img:
            # Calculate crop dimensions to maintain aspect ratio and fill the tile
            img_ratio = img.width / img.height
            tile_ratio = tile_width / tile_height

            if img_ratio > tile_ratio:
                # Image is wider relative to tile, so crop width
                new_width = int(img.height * tile_ratio)
                left = (img.width - new_width) // 2
                crop_box = (left, 0, left + new_width, img.height)
            else:
                # Image is taller relative to tile, so crop height
                new_height = int(img.width / tile_ratio)
                top = (img.height - new_height) // 2
                crop_box = (0, top, img.width, top + new_height)

            # Crop and resize
            cropped_img = img.crop(crop_box)
            resized_img = cropped_img.resize((tile_width, tile_height), Image.LANCZOS)

            # add to mosaic
            row = index // columns
            col = index % columns
            x = col * tile_width
            y = row * tile_height
            mosaic.paste(resized_img, (x, y))

    mosaic.save(output_path)
    print(f"Mosaic created and saved to {output_path}")


if __name__ == "__main__":
    input_images = "content/projects/*/feature*"
    output_mosaic = "mosaic.jpg"
    create_image_mosaic(input_images, output_mosaic)
