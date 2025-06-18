import numpy as np
from pyransac3d import Cylinder

def crop_center_section(points, crop_percentage=0.6):
    z_vals = points[:, 2]
    z_min, z_max = np.min(z_vals), np.max(z_vals)
    z_center = (z_min + z_max) / 2
    z_range = z_max - z_min
    low = z_center - (crop_percentage / 2) * z_range
    high = z_center + (crop_percentage / 2) * z_range
    mask = (z_vals >= low) & (z_vals <= high)
    return points[mask], z_min, z_max

from pyransac3d import Cylinder
import numpy as np

def robust_estimate_diameter(points, n_runs=10, threshold=0.5, max_iter=3000, min_inliers=100):
    diameters = []

    for _ in range(n_runs):
        cyl = Cylinder()
        axis, center, radius, inliers = cyl.fit(points, thresh=threshold, maxIteration=max_iter)
        if len(inliers) >= min_inliers:
            diameters.append(2 * radius)

    if diameters:
        final_diameter = round(np.median(diameters), 2)
        return final_diameter, len(diameters)
    else:
        return None, 0  # No reliable fit


def estimate_length(z_min, z_max):
    return round(z_max - z_min, 2)
