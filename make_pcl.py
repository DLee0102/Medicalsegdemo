import nibabel as nib
import numpy as np
from nibabel.affines import apply_affine


def create_output(vertices, colors, filename):
    colors = colors.reshape(-1, 3)
    vertices = np.hstack([vertices.reshape(-1, 3), colors])
    np.savetxt(filename, vertices, fmt='%f %f %f %d %d %d')     # 必须先写入，然后利用write()在头部插入ply header
    ply_header = '''ply
    		format ascii 1.0
    		element vertex %(vert_num)d
    		property float x
    		property float y
    		property float z
    		property uchar red
    		property uchar green
    		property uchar blue
    		end_header\n
'''
    with open(filename, 'r+') as f:
        old = f.read()
        f.seek(0)
        f.write(ply_header % dict(vert_num=len(vertices)))
        f.write(old)


if __name__ == '__main__':
    epi_img = nib.load('./test.nii.gz')
    epi_img_data = epi_img.get_fdata().astype(np.uint8)

    print(apply_affine(epi_img.affine, np.zeros((1, 3))))
    voxel_coordinates = np.float32(np.argwhere(epi_img_data == 6))
    print(voxel_coordinates.shape)
    epi_vox_center = (np.array(epi_img_data.shape) - 1) // 2
    print(epi_vox_center)
    print(voxel_coordinates)
    for i in range(voxel_coordinates.shape[0]):
        voxel_coordinates[i, :] -= epi_vox_center
        # print("apply_affine: ", apply_affine(epi_img.affine, voxel_coordinates[i, :]))
        # print("voxel: ", voxel_coordinates[i, :])
        voxel_coordinates[i, :] = apply_affine(epi_img.affine, voxel_coordinates[i, :])
    print(voxel_coordinates)

    output_file = 'test.ply'
    voxel_coordinates = np.float32(voxel_coordinates)
    color_matrix = np.ones((voxel_coordinates.shape[0], 3)) * 150
    create_output(voxel_coordinates, color_matrix, output_file)

    

# for i in range(epi_img_data.shape[0]):
#     for j in range(epi_img_data.shape[1]):
#         for k in range(epi_img_davta.shape[2]):
#             if epi_img_data[i, j, k] == 6:
#                 print(epi_img_data[i, j, k])