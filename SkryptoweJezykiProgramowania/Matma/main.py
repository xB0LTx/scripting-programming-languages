from scipy.ndimage import morphology
import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = np.array([
        [0, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ])
    structural_object = np.array([
        [1, 1, 1]
    ])
    erosion_result = morphology.binary_erosion(matrix, structure=structural_object, origin=(0, 0))

    print("Macierz po operacji erozji:")
    print(erosion_result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
