import open3d as o3d

# Φόρτωση του .ply αρχείου
pcd = o3d.io.read_point_cloud("92620A412_Zinc Yellow-Chromate Plated Hex Head Screw.ply")

# Downsampling για μείωση σημείων
pcd = pcd.voxel_down_sample(voxel_size=0.3)  # πειραματίσου με το 0.3 αν θέλεις

# Υπολογισμός κανονικών
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(knn=30))

# Προβολή για να δεις ότι όλα πήγαν καλά
o3d.visualization.draw_geometries([pcd])
