# 2. measure_partial.py
import open3d as o3d
import numpy as np
from pyransac3d import Cylinder

def measure_partial(ply_file, voxel_size=0.3, crop_frac=0.6, thresh=0.5, max_iter=3000):
    """
    Υπολογίζει διάμετρο βίδας με μερικό σπείρωμα.
    """
    pcd = o3d.io.read_point_cloud(ply_file)
    pcd = pcd.voxel_down_sample(voxel_size)
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(knn=30))
    pts = np.asarray(pcd.points)
    z = pts[:, 2]
    low = np.percentile(z, (1 - crop_frac) / 2 * 100)
    high = np.percentile(z, (1 + crop_frac) / 2 * 100)
    cropped = pts[(z >= low) & (z <= high)]
    cyl = Cylinder()
    _, _, radius, inliers = cyl.fit(cropped, thresh=thresh, maxIteration=max_iter)
    return 2 * radius, len(inliers)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Μετρά διάμετρο σε μερικό σπείρωμα.')
    parser.add_argument('ply', help='Αρχείο PLY')
    args = parser.parse_args()
    dia, inl = measure_partial(args.ply)
    print(f'Partial thread diameter: {dia:.2f} mm (inliers={inl})')