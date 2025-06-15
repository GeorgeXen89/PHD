import open3d as o3d
import numpy as np
from pyransac3d import Cylinder

# Παράμετροι
PLY_FILE = "92620A412_Zinc Yellow-Chromate Plated Hex Head Screw.ply"
VOXEL_SIZE = 0.3
CROP_PERCENTAGE = 0.6  # Κρατάμε το κεντρικό 60% (κόβουμε κεφάλι & άκρη)
THRESHOLD = 0.5
MAX_ITER = 3000

# Φόρτωση και αρχική επεξεργασία
pcd = o3d.io.read_point_cloud(PLY_FILE)
pcd = pcd.voxel_down_sample(voxel_size=VOXEL_SIZE)
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(knn=30))

# Νumpy array με τα σημεία
points = np.asarray(pcd.points)

# Περιορίζουμε στο κεντρικό 60% κατά τον άξονα Z
z_vals = points[:, 2]
z_min, z_max = np.min(z_vals), np.max(z_vals)
z_center = (z_min + z_max) / 2
z_range = z_max - z_min
low = z_center - (CROP_PERCENTAGE / 2) * z_range
high = z_center + (CROP_PERCENTAGE / 2) * z_range
mask = (z_vals >= low) & (z_vals <= high)
cropped_points = points[mask]

# Εφαρμογή RANSAC για ανίχνευση κυλίνδρου
cyl = Cylinder()
axis, center, radius, inliers = cyl.fit(cropped_points, thresh=THRESHOLD, maxIteration=MAX_ITER)
diameter = 2 * radius

# Αποτελέσματα
print(f"⌀ Υπολογισμένη διάμετρος βίδας: {diameter:.2f} mm (Inliers: {len(inliers)})")
 