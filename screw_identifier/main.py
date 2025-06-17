from io_utils import load_and_preprocess_pcd
from geometry_analysis import crop_center_section, estimate_diameter, estimate_length
from thread_classifier import classify_thread
from standard_matcher import find_standard_screw
import numpy as np

PLY_FILE = "../Screws/M10ft.ply"

def main():
    pcd = load_and_preprocess_pcd(PLY_FILE)
    points = np.asarray(pcd.points)

    cropped, z_min, z_max = crop_center_section(points)
    diameter, _ = estimate_diameter(cropped)
    length = estimate_length(z_min, z_max)

    thread_type = classify_thread(pcd)
    screw_type, url = find_standard_screw(diameter, length, thread_type)

    print(f"\n📊 Αναγνώριση:\nΔιάμετρος: {diameter} mm\nΜήκος: {length} mm\nΣπείρωμα: {thread_type}")
    print(f"Τυποποιημένος Τύπος: {screw_type}\n🔗 McMaster URL: {url}")

if __name__ == "__main__":
    main()
