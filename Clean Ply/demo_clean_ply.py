import open3d as o3d

# Διαβάζουμε το point cloud από αρχείο PLY
pcd = o3d.io.read_point_cloud("model.ply")
print(f"Αρχικά σημεία: {len(pcd.points)}")

# Καθαρισμός - Αφαίρεση απομονωμένων σημείων
pcd_clean, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
print(f"Μετά τον καθαρισμό: {len(pcd_clean.points)}")

# Downsampling - Μείωση πυκνότητας για πιο ελαφρύ αρχείο
pcd_down = pcd_clean.voxel_down_sample(voxel_size=0.5)

# Αποθήκευση καθαρού νέφους
o3d.io.write_point_cloud("cleaned_model.ply", pcd_down)
print("Αποθηκεύτηκε ως cleaned_model.ply")

# Οπτικοποίηση
o3d.visualization.draw_geometries([pcd_down])
