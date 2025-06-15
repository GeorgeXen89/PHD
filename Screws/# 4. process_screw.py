import argparse
import open3d as o3d
from classify_thread import classify_thread
from measure_partial import measure_partial
from measure_full import measure_full

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ολοκληρωμένη επεξεργασία βίδας PLY')
    parser.add_argument('ply', help='Μονοπάτι αρχείου PLY')
    args = parser.parse_args()
    pcd = o3d.io.read_point_cloud(args.ply)
    kind = classify_thread(pcd)
    print(f'Detected thread: {kind}')
    if kind == 'partial':
        dia, inl = measure_partial(args.ply)
        print(f'Partial thread diameter: {dia:.2f} mm (inliers={inl})')
    else:
        dia, inl = measure_full(args.ply)
        print(f'Full thread diameter: {dia:.2f} mm (inliers={inl})')