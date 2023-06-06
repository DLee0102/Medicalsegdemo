import nibabel as nib
import numpy as np
import open3d as o3d

def trans2Descartes(img_data, color):
    pass


np_img = nib.load('./test.nii.gz')
np_img_data = np_img.get_fdata().astype(np.uint8)

print(np_img_data.shape)
print(np_img_data.shape[0]*np_img_data.shape[1]*np_img_data.shape[2])

n_i, n_j, n_k = np_img_data.shape
center_i = (n_i - 1) // 2  # // for integer division
center_j = (n_j - 1) // 2
center_k = (n_k - 1) // 2
print([center_i, center_j, center_k])
organ_pointscount = 0
print(np.sum(np_img_data==6))