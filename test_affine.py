import nibabel as nib
import numpy as np
import open3d as o3d
from nibabel.affines import apply_affine

epi_img = nib.load('./test.nii.gz')
epi_img_data = epi_img.get_fdata()
np.set_printoptions(precision=3, suppress=True)

print(epi_img.affine)
M = epi_img.affine[:3, :3]
abc = epi_img.affine[:3, 3]
def f(i, j, k):
   """ Return X, Y, Z coordinates for i, j, k """
   return M.dot([i, j, k]) + abc

epi_vox_center = (np.array(epi_img_data.shape) - 1) / 2.
print(epi_vox_center)
print(list(epi_vox_center))
print("Directly: ", epi_img.affine.dot(list(epi_vox_center) + [1]))
print(f(epi_vox_center[0], epi_vox_center[1], epi_vox_center[2]))
print("Auto: ", apply_affine(epi_img.affine, epi_vox_center))
print(apply_affine(epi_img.affine, np.zeros((1, 3))))