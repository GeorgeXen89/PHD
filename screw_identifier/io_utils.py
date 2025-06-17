import open3d as o3d

def load_and_preprocess_pcd(filename, voxel_size=0.3):
    pcd = o3d.io.read_point_cloud(filename)
    pcd = pcd.voxel_down_sample(voxel_size=voxel_size)
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(knn=30))
    return pcd
