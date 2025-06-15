import open3d as o3d

# Άλλαξε εδώ με το σωστό όνομα του αρχείου σου
filename = "92620A412_Zinc Yellow-Chromate Plated Hex Head Screw.ply"

# Φόρτωσε το point cloud
pcd = o3d.io.read_point_cloud(filename)

# Εμφάνιση
o3d.visualization.draw_geometries([pcd])
