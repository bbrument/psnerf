import os
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':


    # INPUT_MASK = "/home/lilian/dev/Playing_with_NeuS/data/DiLiGenT-MV/buddhaPNG/mask/000.png"
    # CROPPED_MASK = "/home/lilian/dev/psnerf/dataset/buddha/mask/view_01.png"

    INPUT_MASKS = "/home/lilian/dev/Playing_with_NeuS/data/DiLiGenT-MV/pot2PNG/mask/"
    CROPPED_MASKS = "/home/lilian/dev/psnerf/dataset/pot2/mask"

    # Get all masks
    input_masks = os.listdir(INPUT_MASKS)
    cropped_masks = os.listdir(CROPPED_MASKS)

    # Sort masks
    input_masks.sort()
    cropped_masks.sort()

    # Loop
    for input_mask, cropped_mask in zip(input_masks, cropped_masks):

        # Get full path
        input_path = os.path.join(INPUT_MASKS, input_mask)
        cropped_path = os.path.join(CROPPED_MASKS, cropped_mask)

        # Load masks
        input_mask = plt.imread(input_path)
        cropped_mask = plt.imread(cropped_path)

        # Get size of masks
        input_height, input_width = input_mask.shape
        cropped_height, cropped_width = cropped_mask.shape
        diff_height = input_height - cropped_height
        diff_width = input_width - cropped_width

        # 
        for off_j in range(diff_width):
            for off_i in range(diff_height):

                # Get the mask of the current offset
                mask = input_mask[off_j:off_j+cropped_height, off_i:off_i+cropped_width]

                # Check if the masks are equal
                if np.array_equal(mask, cropped_mask):
                    print(f"Found a match at offset ({off_i}, {off_j})")
                    break