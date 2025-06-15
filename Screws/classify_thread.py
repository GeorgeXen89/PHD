# 1. classify_thread.py
import open3d as o3d
import numpy as np

def classify_thread(pcd, voxel_size=0.3, crop_frac=0.6):
    """
    Κατηγοριοποίηση βίδας σε μερικό ή ολικό σπείρωμα.
    Επιστρέφει 'partial' ή 'full'.
    Χρησιμοποιεί histogram ακτίνων για εντοπισμό peaks.
    """
    # Downsample
    pcd = pcd.voxel_down_sample(voxel_size)
    points = np.asarray(pcd.points)
    # Crop κεντρικό τμήμα
    z = points[:, 2]
    z_min, z_max = z.min(), z.max()
    low = (z_min + z_max) / 2 - crop_frac * (z_max - z_min) / 2
    high = (z_min + z_max) / 2 + crop_frac * (z_max - z_min) / 2
    seg = points[(z >= low) & (z <= high)]

    # Υπολογισμός άξονα με manual PCA
    cen = seg.mean(axis=0)
    cen_pts = seg - cen
    cov = np.cov(cen_pts, rowvar=False)
    eigvals, eigvecs = np.linalg.eigh(cov)
    axis = eigvecs[:, np.argmax(eigvals)]

    # Αποστάσεις σημείων από άξονα
    proj = cen_pts.dot(axis)
    perp = cen_pts - np.outer(proj, axis)
    dists = np.linalg.norm(perp, axis=1)

    # Ιστόγραμμα ακτίνων
    hist, edges = np.histogram(dists, bins=60)
    # Εύρεση peaks (τοπικών μεγίστων)
    peaks = 0
    for i in range(1, len(hist)-1):
        if hist[i] > hist[i-1] and hist[i] > hist[i+1] and hist[i] > 0.1 * hist.max():
            peaks += 1
    # Αν υπάρχουν >1 peaks, partial thread, αλλιώς full
    return 'partial' if peaks > 1 else 'full'

if __name__ == '__main__':
    ply_path = input('Δώσε το μονοπάτι του PLY αρχείου: ')
    pcd = o3d.io.read_point_cloud(ply_path)
    if not pcd.has_points():
        print("⚠️ Δεν φορτώθηκε point cloud. Έλεγξε το μονοπάτι.")
    else:
        kind = classify_thread(pcd)
        print(f'Detected thread: {kind}')
