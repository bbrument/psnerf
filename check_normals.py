import os
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':


    # 
    INPUT_NORMALS_PATH = "dataset/buddha/sdm_out/outnpy"
    INPUT_NORMAL_MAPS_PATH = "dataset/buddha/sdm_out/outimg"
    GT_NORMALS_PATH = "dataset/buddha/normal/npy"
    RNB_NORMALS_PATH = "../Playing_with_NeuS/data/DiLiGenT-MV/buddhaPNG/normal"

    # Get all .npy files
    input_normals = os.listdir(INPUT_NORMALS_PATH)
    input_normal_maps = os.listdir(INPUT_NORMAL_MAPS_PATH)
    gt_normals = os.listdir(GT_NORMALS_PATH)
    rnb_normals = os.listdir(RNB_NORMALS_PATH)

    # Sort .npy files
    input_normals.sort()
    input_normal_maps.sort()
    gt_normals.sort()
    rnb_normals.sort()

    # Loop
    for input_normal, input_normal_map, gt_normal, rnb_normal in zip(input_normals, input_normal_maps, gt_normals, rnb_normals):

        # Get full path
        input_path = os.path.join(INPUT_NORMALS_PATH, input_normal)
        input_map_path = os.path.join(INPUT_NORMAL_MAPS_PATH, input_normal_map)
        gt_path = os.path.join(GT_NORMALS_PATH, gt_normal)
        rnb_path = os.path.join(RNB_NORMALS_PATH, rnb_normal)

        # Load normals
        input_normal = np.load(input_path)
        input_normal_map = plt.imread(input_map_path)[:,:,0:3]
        gt_normal = np.load(gt_path)
        rnb_normal = plt.imread(rnb_path)[:,:,0:3]

        # Crop 
        rnb_normal = rnb_normal[0:input_normal.shape[0], 106:input_normal.shape[1]+106, :]

        # Convert as a normal map
        input_normal = (input_normal + 1) / 2
        gt_normal = (gt_normal + 1) / 2

        # Compute difference
        diff = np.abs(input_normal - input_normal_map)

        # Take a random pixel and plot the normals
        # i = np.random.randint(0, input_normal.shape[0])
        # j = np.random.randint(0, input_normal.shape[1])
        i = input_normal.shape[0] // 2
        j = input_normal.shape[1] // 2
        print(f"Pixel ({i}, {j})")
        print(f"Input normal: {input_normal[i, j]}")
        print(f"Input normal map: {input_normal_map[i, j]}")
        print(f"GT normal: {gt_normal[i, j]}")
        print(f"RNB normal: {rnb_normal[i, j]}")
        print(f"Diff: {diff[i, j]}")

        # Plot normals
        plt.subplot(1, 5, 1)
        plt.imshow(input_normal)
        plt.subplot(1, 5, 2)
        plt.imshow(input_normal_map)
        plt.subplot(1, 5, 3)
        plt.imshow(gt_normal)
        plt.subplot(1, 5, 4)
        plt.imshow(rnb_normal)
        plt.subplot(1, 5, 5)
        plt.imshow(diff)

        # Show
        plt.show()
        break