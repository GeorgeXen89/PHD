def classify_thread(pcd):
    z_vals = [point[2] for point in pcd.points]
    length = max(z_vals) - min(z_vals)
    return "Partial" if length > 30 else "Fully"
