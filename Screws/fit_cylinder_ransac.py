import open3d as o3d
import numpy as np
from pyransac3d import Cylinder

diameters = []
lengths = []

# === Πολλαπλές επαναλήψεις για σταθερότητα ===
for i in range(10):
    pcd = o3d.io.read_point_cloud("92620A412_Zinc Yellow-Chromate Plated Hex Head Screw.ply")
    pcd = pcd.voxel_down_sample(voxel_size=0.3)
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(knn=30))

    points = np.asarray(pcd.points)
    cyl = Cylinder()
    axis, center, radius, inliers = cyl.fit(points, thresh=0.5, maxIteration=3000)

    inlier_points = points[inliers]
    axis = axis / np.linalg.norm(axis)
    projections = np.dot(inlier_points - center, axis)
    min_proj = np.min(projections)
    max_proj = np.max(projections)
    length = max_proj - min_proj
    diameter = 2 * radius

    diameters.append(diameter)
    lengths.append(length)

# === Μέσοι όροι και εμφάνιση ===
avg_diameter = np.mean(diameters)
avg_length = np.mean(lengths)

print(f"Διάμετρος κυλίνδρου: {avg_diameter:.2f} mm")
print(f"Μήκος κυλίνδρου: {avg_length:.2f} mm")
