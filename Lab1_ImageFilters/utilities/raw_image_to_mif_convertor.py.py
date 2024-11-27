# from PIL import Image
# import numpy as np

# def create_mif_file(channel_data, file_name, word_width=2048, depth=256):
#     """
#     Creates a MIF file for the given channel data.

#     :param channel_data: 2D numpy array of the channel.
#     :param file_name: Name of the MIF file to save.
#     :param word_width: Number of bits in each word.
#     :param depth: Number of words (rows).
#     """
#     height, width = channel_data.shape
#     bits_per_pixel = word_width // width

#     with open(file_name, 'w') as f:
#         f.write(f"WIDTH={word_width};\n")
#         f.write(f"DEPTH={depth};\n")
#         f.write("ADDRESS_RADIX = BIN;\n")
#         f.write("DATA_RADIX = BIN;\n")
#         f.write("CONTENT\n")
#         f.write("BEGIN\n")

#         for address in range(depth):
#             if address < height:
#                 row_data = ''.join(f"{pixel:0{bits_per_pixel}b}" for pixel in channel_data[address])
#                 f.write(f"{address:08b} : {row_data};\n")
#             else:
#                 f.write(f"{address:08b} : {'0' * word_width};\n")

#         f.write("END;\n")


# def image_to_mif(image_path):
#     """
#     Converts an image to three MIF files for R, G, and B channels.

#     :param image_path: Path to the input image.
#     """
#     # Open and resize image to fit 2048 bits width
#     image = Image.open(image_path).convert("RGB")
#     target_width = 2048 // 8  # Each pixel is 8 bits for R, G, or B
#     target_height = 256      # Number of rows (words)
#     image = image.resize((target_width, target_height))

#     # Split into R, G, and B channels
#     r_channel, g_channel, b_channel = image.split()

#     # Convert channels to numpy arrays
#     r_data = np.array(r_channel)
#     g_data = np.array(g_channel)
#     b_data = np.array(b_channel)

#     # Create MIF files for each channel
#     create_mif_file(r_data, "r_channel.mif")
#     create_mif_file(g_data, "g_channel.mif")
#     create_mif_file(b_data, "b_channel.mif")

# # Replace 'input_image.jpg' with the path to your image file
# image_to_mif('input_image.jpg')










import numpy as np

def create_mif_file(channel_data, file_name, word_width=2048, depth=256):
    """
    Creates a MIF file for the given channel data.

    :param channel_data: 2D numpy array of the channel.
    :param file_name: Name of the MIF file to save.
    :param word_width: Number of bits in each word (2048).
    :param depth: Number of words (256).
    """
    height, width = channel_data.shape
    bits_per_pixel = word_width // width

    with open(file_name, 'w') as f:
        f.write(f"WIDTH={word_width};\n")
        f.write(f"DEPTH={depth};\n")
        f.write("ADDRESS_RADIX = BIN;\n")
        f.write("DATA_RADIX = BIN;\n")
        f.write("CONTENT\n")
        f.write("BEGIN\n")

        for address in range(depth):
            if address < height:
                # Convert each pixel to a binary string and concatenate to form the word
                row_data = ''.join(f"{pixel:08b}" for pixel in channel_data[address])
                # Truncate or pad to ensure each row is exactly 'word_width' bits
                row_data = row_data.ljust(word_width, '0')[:word_width]
                f.write(f"{address:08b} : {row_data};\n")
            else:
                # Pad with zeros for addresses beyond the image height
                f.write(f"{address:08b} : {'0' * word_width};\n")

        f.write("END;\n")


def raw_to_mif(raw_file_path, width=256, height=256, word_width=2048, depth=256):
    """
    Reads a .raw image file and converts it to three MIF files for R, G, and B channels.

    :param raw_file_path: Path to the .raw file.
    :param width: Image width (default 256 pixels).
    :param height: Image height (default 256 pixels).
    :param word_width: Number of bits in each word (2048).
    :param depth: Number of words (256).
    """
    # Read the raw file and reshape into RGB format
    with open(raw_file_path, 'rb') as f:
        raw_data = np.fromfile(f, dtype=np.uint8)
    
    # Assuming the raw file is a flattened array of 256x256x3 (RGB)
    image_data = raw_data.reshape((height, width, 3))
    
    # Separate channels
    r_channel = image_data[:, :, 0]
    g_channel = image_data[:, :, 1]
    b_channel = image_data[:, :, 2]

    # Create MIF files
    create_mif_file(r_channel, "r_channel.mif", word_width, depth)
    create_mif_file(g_channel, "g_channel.mif", word_width, depth)
    create_mif_file(b_channel, "b_channel.mif", word_width, depth)


# Replace 'lena_005noise_256x256.raw' with your provided file path
raw_to_mif('lena_005noise_256x256.raw')



