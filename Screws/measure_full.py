import open3d as o3d
import numpy as np
from pyransac3d import Cylinder

def measure_full(ply_file, voxel_size=0.3, thresh=0.5, max_iter=3000):
    """
    Υπολογίζει διάμετρο βίδας με ολικό σπείρωμα.
    """
    pcd = o3d.io.read_point_cloud(ply_file)
    pcd = pcd.voxel_down_sample(voxel_size)
    pts = np.asarray(pcd.points)
    cyl = Cylinder()
    _, _, radius, inliers = cyl.fit(pts, thresh=thresh, maxIteration=max_iter)
    return 2 * radius, len(inliers)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Μετρά διάμετρο σε ολικό σπείρωμα.')
    parser.add_argument('ply', help='Αρχείο PLY')
    args = parser.parse_args()
    dia, inl = measure_full(args.ply)
    print(f'Full thread diameter: {dia:.2f} mm (inliers={inl})')