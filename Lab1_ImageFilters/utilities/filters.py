# import numpy as np
# from scipy.signal import medfilt2d
# from PIL import Image
# import matplotlib.pyplot as plt

# def median_filter(image, kernel_size=3):
#     """
#     Applies a Median filter to the input image.

#     :param image: 2D numpy array representing the image (grayscale or single channel).
#     :param kernel_size: Size of the filter kernel (odd integer, e.g., 3, 5, 7).
#     :return: Filtered image as a 2D numpy array.
#     """
#     return medfilt2d(image, kernel_size=kernel_size)


# def median_of_medians(values, group_size=5):
#     """
#     Finds the median of medians for a 1D list of values.

#     :param values: List or 1D numpy array of values.
#     :param group_size: Size of the groups to compute medians.
#     :return: The median of medians.
#     """
#     if len(values) <= group_size:
#         return np.median(values)

#     medians = []
#     for i in range(0, len(values), group_size):
#         group = values[i:i + group_size]
#         medians.append(np.median(group))
#     return np.median(medians)


# def conditional_median_of_medians(values, threshold=10, group_size=5):
#     """
#     Computes a conditional median of medians, applying a threshold to select the final value.

#     :param values: List or 1D numpy array of values.
#     :param threshold: Value threshold for the conditional check.
#     :param group_size: Size of the groups to compute medians.
#     :return: The conditional median of medians.
#     """
#     median_value = median_of_medians(values, group_size=group_size)
#     if median_value > threshold:
#         return np.median(values)
#     else:
#         return median_value


# def apply_conditional_median_of_medians(image, kernel_size=3, threshold=10, group_size=5):
#     """
#     Applies a Conditional Median of Medians filter to a 2D image.

#     :param image: 2D numpy array representing the image.
#     :param kernel_size: Size of the kernel (odd integer, e.g., 3, 5, 7).
#     :param threshold: Threshold for conditional median of medians.
#     :param group_size: Group size for the median of medians calculation.
#     :return: Filtered image as a 2D numpy array.
#     """
#     filtered_image = np.copy(image)
#     pad_size = kernel_size // 2
#     padded_image = np.pad(image, pad_size, mode='reflect')

#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             # Extract the local window
#             window = padded_image[i:i + kernel_size, j:j + kernel_size].flatten()
#             # Apply the conditional median of medians
#             filtered_image[i, j] = conditional_median_of_medians(window, threshold, group_size)

#     return filtered_image


# def main(input_image_path, filter_type='median', kernel_size=3, threshold=10, group_size=5):
#     """
#     Main function to apply a filter on an image and display the result.

#     :param input_image_path: Path to the input image file.
#     :param filter_type: The type of filter to apply ('median', 'median_of_medians', 'conditional_median_of_medians').
#     :param kernel_size: Size of the kernel for the filter (odd integer, e.g., 3, 5, 7).
#     :param threshold: Threshold for the conditional median of medians.
#     :param group_size: Group size for the median of medians calculation.
#     """
#     # Open and convert the image to grayscale
#     image = Image.open(input_image_path).convert('L')
#     image_array = np.array(image)

#     if filter_type == 'median':
#         filtered_image = median_filter(image_array, kernel_size=kernel_size)
#     elif filter_type == 'median_of_medians':
#         filtered_image = apply_conditional_median_of_medians(image_array, kernel_size, threshold=1e9, group_size=group_size)
#     elif filter_type == 'conditional_median_of_medians':
#         filtered_image = apply_conditional_median_of_medians(image_array, kernel_size, threshold=threshold, group_size=group_size)
#     else:
#         raise ValueError(f"Unknown filter type: {filter_type}")

#     # Display the original and filtered images
#     plt.figure(figsize=(10, 5))
#     plt.subplot(1, 2, 1)
#     plt.title('Original Image')
#     plt.imshow(image_array, cmap='gray')
#     plt.axis('off')

#     plt.subplot(1, 2, 2)
#     plt.title(f'Filtered Image ({filter_type})')
#     plt.imshow(filtered_image, cmap='gray')
#     plt.axis('off')

#     plt.show()


# # Example usage
# # Replace 'input_image.jpg' with the path to your image file
# main(input_image_path='lena_005noise_256x256.raw', filter_type='conditional_median_of_medians', kernel_size=5, threshold=10, group_size=5)



####################################   THE ABOVE CODE WORK  WITH IMAGE FILE BUT NOT WITH RAW FILE  #########################################

### CODE FOR READING RAW FILE AND CONVERTING IT INTO IMAGE FILE
import numpy as np
import matplotlib.pyplot as plt


def read_raw_image(file_path, width, height, channels=3):
    """
    Reads a raw image file and reshapes it into a 3D numpy array (height x width x channels).

    :param file_path: Path to the raw file.
    :param width: Width of the image.
    :param height: Height of the image.
    :param channels: Number of color channels (default: 3 for RGB).
    :return: Numpy array of shape (height, width, channels).
    """
    # Read the raw file as binary data
    with open(file_path, 'rb') as f:
        raw_data = np.fromfile(f, dtype=np.uint8)
    
    # Reshape the data into (height, width, channels)
    image = raw_data.reshape((height, width, channels))
    return image


def apply_conditional_median_of_medians(image, kernel_size=3, threshold=10, group_size=5):
    """
    Applies a Conditional Median of Medians filter to a 2D image.

    :param image: 2D numpy array representing the image.
    :param kernel_size: Size of the kernel (odd integer, e.g., 3, 5, 7).
    :param threshold: Threshold for conditional median of medians.
    :param group_size: Group size for the median of medians calculation.
    :return: Filtered image as a 2D numpy array.
    """
    filtered_image = np.copy(image)
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='reflect')

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Extract the local window
            window = padded_image[i:i + kernel_size, j:j + kernel_size].flatten()
            # Apply the conditional median of medians
            filtered_image[i, j] = conditional_median_of_medians(window, threshold, group_size)

    return filtered_image


def conditional_median_of_medians(values, threshold=10, group_size=5):
    """
    Computes a conditional median of medians, applying a threshold to select the final value.

    :param values: List or 1D numpy array of values.
    :param threshold: Value threshold for the conditional check.
    :param group_size: Size of the groups to compute medians.
    :return: The conditional median of medians.
    """
    median_value = median_of_medians(values, group_size=group_size)
    if median_value > threshold:
        return np.median(values)
    else:
        return median_value


def median_of_medians(values, group_size=5):
    """
    Finds the median of medians for a 1D list of values.

    :param values: List or 1D numpy array of values.
    :param group_size: Size of the groups to compute medians.
    :return: The median of medians.
    """
    if len(values) <= group_size:
        return np.median(values)

    medians = []
    for i in range(0, len(values), group_size):
        group = values[i:i + group_size]
        medians.append(np.median(group))
    return np.median(medians)


# def main(input_image_path, width=256, height=256, filter_type='conditional_median_of_medians', kernel_size=3, threshold=10, group_size=5):
#     """
#     Main function to apply a filter on an image and display the result.

#     :param input_image_path: Path to the input image file.
#     :param width: Width of the raw image.
#     :param height: Height of the raw image.
#     :param filter_type: The type of filter to apply ('median', 'median_of_medians', 'conditional_median_of_medians').
#     :param kernel_size: Size of the kernel for the filter (odd integer, e.g., 3, 5, 7).
#     :param threshold: Threshold for the conditional median of medians.
#     :param group_size: Group size for the median of medians calculation.
#     """
#     # Read the raw image
#     raw_image = read_raw_image(input_image_path, width, height)

#     # Convert the image to grayscale for simplicity (average over RGB channels)
#     grayscale_image = np.mean(raw_image, axis=2).astype(np.uint8)

#     # Apply the chosen filter
#     if filter_type == 'conditional_median_of_medians':
#         filtered_image = apply_conditional_median_of_medians(grayscale_image, kernel_size, threshold, group_size)
#     else:
#         raise ValueError(f"Unknown filter type: {filter_type}")

#     # Display the original and filtered images
#     plt.figure(figsize=(10, 5))
#     plt.subplot(1, 2, 1)
#     plt.title('Original Image (Grayscale)')
#     plt.imshow(grayscale_image, cmap='gray')
#     plt.axis('off')

#     plt.subplot(1, 2, 2)
#     plt.title(f'Filtered Image ({filter_type})')
#     plt.imshow(filtered_image, cmap='gray')
#     plt.axis('off')

#     plt.show()


# # # Example usage
# # # Replace 'lena_005noise_256x256.raw' with your provided file path
# # main(input_image_path='lena_005noise_256x256.raw', width=256, height=256, filter_type='conditional_median_of_medians', kernel_size=5, threshold=10, group_size=5)
# def main(input_image_path, width=256, height=256, filter_type='conditional_median_of_medians', kernel_size=3, threshold=10, group_size=5):
#     """
#     Main function to apply a filter on an RGB image and display the result.

#     :param input_image_path: Path to the input image file.
#     :param width: Width of the raw image.
#     :param height: Height of the raw image.
#     :param filter_type: The type of filter to apply ('median', 'median_of_medians', 'conditional_median_of_medians').
#     :param kernel_size: Size of the kernel for the filter (odd integer, e.g., 3, 5, 7).
#     :param threshold: Threshold for the conditional median of medians.
#     :param group_size: Group size for the median of medians calculation.
#     """
#     # Read the raw image
#     raw_image = read_raw_image(input_image_path, width, height)

#     # Separate the RGB channels
#     r_channel = raw_image[:, :, 0]
#     g_channel = raw_image[:, :, 1]
#     b_channel = raw_image[:, :, 2]

#     # Apply the chosen filter to each channel
#     if filter_type == 'conditional_median_of_medians':
#         r_filtered = apply_conditional_median_of_medians(r_channel, kernel_size, threshold, group_size)
#         g_filtered = apply_conditional_median_of_medians(g_channel, kernel_size, threshold, group_size)
#         b_filtered = apply_conditional_median_of_medians(b_channel, kernel_size, threshold, group_size)
#     else:
#         raise ValueError(f"Unknown filter type: {filter_type}")

#     # Combine the filtered channels back into an RGB image
#     filtered_image = np.stack((r_filtered, g_filtered, b_filtered), axis=2)

#     # Display the original and filtered images
#     plt.figure(figsize=(10, 5))
#     plt.subplot(1, 2, 1)
#     plt.title('Original Image (RGB)')
#     plt.imshow(raw_image.astype(np.uint8))
#     plt.axis('off')

#     plt.subplot(1, 2, 2)
#     plt.title(f'Filtered Image ({filter_type})')
#     plt.imshow(filtered_image.astype(np.uint8))
#     plt.axis('off')

#     plt.show()


# # Example usage
# # Replace 'lena_005noise_256x256.raw' with your provided file path
# main(input_image_path='lena_005noise_256x256.raw', width=256, height=256, filter_type='conditional_median_of_medians', kernel_size=5, threshold=10, group_size=5)













































import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import medfilt2d


def read_raw_image(file_path, width, height, channels=3):
    """
    Reads a raw image file and reshapes it into a 3D numpy array (height x width x channels).

    :param file_path: Path to the raw file.
    :param width: Width of the image.
    :param height: Height of the image.
    :param channels: Number of color channels (default: 3 for RGB).
    :return: Numpy array of shape (height, width, channels).
    """
    with open(file_path, 'rb') as f:
        raw_data = np.fromfile(f, dtype=np.uint8)
    image = raw_data.reshape((height, width, channels))
    return image


def apply_median_filter(image, kernel_size=3):
    """
    Applies a Median filter to an RGB image.
    This filter computes the median of a local window around each pixel
    and replaces the pixel value with the computed median.
    """
    filtered_image = np.zeros_like(image)
    for channel in range(image.shape[2]):  # Process each channel (R, G, B)
        filtered_image[:, :, channel] = medfilt2d(image[:, :, channel], kernel_size=kernel_size)
    return filtered_image


def median_of_medians(values, group_size=5):
    """
    Computes the Median of Medians for a given 1D list of values.
    This method divides the values into groups of a fixed size, computes the median
    of each group, and then computes the median of those medians.
    """
    if len(values) <= group_size:
        return np.median(values)
    medians = [np.median(values[i:i + group_size]) for i in range(0, len(values), group_size)]
    return np.median(medians)


def apply_median_of_medians_filter(image, kernel_size=3, group_size=5):
    """
    Applies a Median of Medians filter to an RGB image.
    This filter computes the Median of Medians for a local window around each pixel
    and replaces the pixel value with the computed value.
    """
    filtered_image = np.zeros_like(image)
    pad_size = kernel_size // 2

    for channel in range(image.shape[2]):  # Process each channel (R, G, B)
        padded_image = np.pad(image[:, :, channel], pad_size, mode='reflect')
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                window = padded_image[i:i + kernel_size, j:j + kernel_size].flatten()
                filtered_image[i, j, channel] = median_of_medians(window, group_size=group_size)
    return filtered_image


def conditional_median_of_medians(values, threshold=10, group_size=5):
    """
    Computes a Conditional Median of Medians for a given 1D list of values.
    If the Median of Medians exceeds a given threshold, it returns the regular median.
    Otherwise, it returns the Median of Medians.
    """
    mom_value = median_of_medians(values, group_size=group_size)
    return np.median(values) if mom_value > threshold else mom_value


def apply_conditional_median_of_medians_filter(image, kernel_size=3, threshold=10, group_size=5):
    """
    Applies a Conditional Median of Medians filter to an RGB image.
    This filter computes a Conditional Median of Medians for a local window
    around each pixel and replaces the pixel value with the computed value.
    """
    filtered_image = np.zeros_like(image)
    pad_size = kernel_size // 2

    for channel in range(image.shape[2]):  # Process each channel (R, G, B)
        padded_image = np.pad(image[:, :, channel], pad_size, mode='reflect')
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                window = padded_image[i:i + kernel_size, j:j + kernel_size].flatten()
                filtered_image[i, j, channel] = conditional_median_of_medians(
                    window, threshold=threshold, group_size=group_size)
    return filtered_image


def main(input_image_path, width=256, height=256, kernel_size=3, threshold=10, group_size=5):
    """
    Main function to apply all filters on an RGB image and display the results.
    """
    # Read the raw image
    raw_image = read_raw_image(input_image_path, width, height)

    # Apply all filters
    median_result = apply_median_filter(raw_image, kernel_size=kernel_size)
    median_of_medians_result = apply_median_of_medians_filter(raw_image, kernel_size=kernel_size, group_size=group_size)
    conditional_median_of_medians_result = apply_conditional_median_of_medians_filter(
        raw_image, kernel_size=kernel_size, threshold=threshold, group_size=group_size)

    # Display the original and filtered images
    plt.figure(figsize=(15, 10))
    
    # Original Image
    plt.subplot(2, 2, 1)
    plt.title('Original Image (RGB)')
    plt.imshow(raw_image.astype(np.uint8))
    plt.axis('off')

    # Median Filter Result
    plt.subplot(2, 2, 2)
    plt.title('Median Filter Result')
    plt.imshow(median_result.astype(np.uint8))
    plt.axis('off')

    # Median of Medians Result
    plt.subplot(2, 2, 3)
    plt.title('Median of Medians Result')
    plt.imshow(median_of_medians_result.astype(np.uint8))
    plt.axis('off')

    # Conditional Median of Medians Result
    plt.subplot(2, 2, 4)
    plt.title('Conditional Median of Medians Result')
    plt.imshow(conditional_median_of_medians_result.astype(np.uint8))
    plt.axis('off')

    # Show all plots
    plt.tight_layout()
    plt.show()


# Example usage
# Replace 'lena_005noise_256x256.raw' with your provided file path
main(input_image_path='lena_005noise_256x256.raw', width=256, height=256, kernel_size=3, threshold=5, group_size=5)



