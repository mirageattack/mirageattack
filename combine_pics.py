from PIL import Image
import sys

def combine_images(image_paths, output_path='combined_image.jpg', grid_rows=3, grid_cols=2, img_size=(400, 300)):
    """
    Combines multiple images into a single grid-based image.
    
    Args:
    - image_paths: List of paths to the 5 input images.
    - output_path: Path to save the combined image (default: 'combined_image.jpg').
    - grid_rows: Number of rows in the grid (default: 3 for 3x2 grid).
    - grid_cols: Number of columns in the grid (default: 2).
    - img_size: Tuple of (width, height) to resize each image to (default: (400, 300)).
    
    Note: For 5 images, this will place them in a 3x2 grid, leaving the bottom-right cell empty.
    """
    if len(image_paths) > grid_rows * grid_cols:
        raise ValueError("Too many images for the specified grid size.")
    
    # Load and resize images
    images = []
    for path in image_paths:
        img = Image.open(path)
        img = img.resize(img_size, Image.Resampling.LANCZOS)
        images.append(img)
    
    # Calculate combined image dimensions
    combined_width = grid_cols * img_size[0]
    combined_height = grid_rows * img_size[1]
    combined_img = Image.new('RGB', (combined_width, combined_height), color='white')
    
    # Place images in the grid
    for idx, img in enumerate(images):
        row = idx // grid_cols
        col = idx % grid_cols
        x = col * img_size[0]
        y = row * img_size[1]
        combined_img.paste(img, (x, y))
    
    # Save the combined image
    combined_img.save(output_path)
    print(f"Combined image saved to {output_path}")


path_1 = "/Users/hkus3lab/mirageattack/paper_fig/4-mirage-atlas.png"
path_2 = "/Users/hkus3lab/mirageattack/paper_fig/4-mirage-comet.png"
path_3 = "/Users/hkus3lab/mirageattack/paper_fig/4-mirage-gemini.png"
path_4 = "/Users/hkus3lab/mirageattack/paper_fig/4-mirage-okc.png"
path_5 = "/Users/hkus3lab/mirageattack/paper_fig/4-mirage-tars.png"

if __name__ == "__main__":
    image_paths = [path_1, path_2, path_3, path_4, path_5]    
    combine_images(image_paths)