import open3d as o3d
import numpy as np
from pyransac3d import Cylinder
from classify_thread import classify_thread
from lookup_screw import find_standard_screw

# === ΠΑΡΑΜΕΤΡΟΙ ===
PLY_FILE = "../Screws/M10ft.ply"  # Τροποποίησέ το με το αρχείο σου
VOXEL_SIZE = 0.3
THRESHOLD = 0.5
CROP_PERCENTAGE = 0.6
MAX_ITER = 3000

def load_and_preprocess_pcd(filename):
    pcd = o3d.io.read_point_cloud(filename)
    pcd = pcd.voxel_down_sample(voxel_size=VOXEL_SIZE)
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(knn=30))
    return pcd

def crop_center_section(points):
    z_vals = points[:, 2]
    z_min, z_max = np.min(z_vals), np.max(z_vals)
    z_center = (z_min + z_max) / 2
    z_range = z_max - z_min
    low = z_center - (CROP_PERCENTAGE / 2) * z_range
    high = z_center + (CROP_PERCENTAGE / 2) * z_range
    mask = (z_vals >= low) & (z_vals <= high)
    return points[mask], z_min, z_max

def estimate_diameter(points):
    cyl = Cylinder()
    axis, center, radius, inliers = cyl.fit(points, thresh=THRESHOLD, maxIteration=MAX_ITER)
    diameter = round(2 * radius, 2)
    return diameter, len(inliers)

def estimate_length(z_min, z_max):
    return round(z_max - z_min, 2)

def main():
    print("📦 Ανάγνωση και ανάλυση αρχείου:", PLY_FILE)
    pcd = load_and_preprocess_pcd(PLY_FILE)
    points = np.asarray(pcd.points)

    cropped_points, z_min, z_max = crop_center_section(points)
    diameter, inliers = estimate_diameter(cropped_points)
    length = estimate_length(z_min, z_max)

    thread_type = classify_thread(pcd)
    screw_type, url = find_standard_screw(diameter, length, thread_type)

    print("\n📊 Αποτελέσματα Αναγνώρισης:")
    print(f"➤ Διάμετρος: {diameter} mm")
    print(f"➤ Μήκος: {length} mm")
    print(f"➤ Σπείρωμα: {thread_type}")
    print(f"➤ Τυποποιημένος Τύπος: {screw_type}")
    print(f"🔗 McMaster-Carr URL: {url}")

if __name__ == "__main__":
    main()
