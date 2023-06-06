import nibabel as nib
import numpy as np
import open3d as o3d

epi_img = nib.load('./testdata/890fa10d-a01d-4423-92e2-80d9a55558b2.nii.gz')
epi_img_data = epi_img.get_fdata().astype(np.uint8)
print(epi_img)
# print(epi_img_data.dtype)
# print(epi_img_data.shape)

binary_img = epi_img_data == 6
mask = binary_img.astype(np.uint8)
output_img_data = mask * epi_img_data

output_path = './test.nii.gz'
nib.save(nib.Nifti1Image(output_img_data.astype(np.uint8), epi_img.affine, epi_img.header.copy()), output_path)
