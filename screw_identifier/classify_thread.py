def classify_thread(pcd):
    """
    Επιστρέφει "Fully" ή "Partial" σπείρωμα, βασισμένο στο μήκος.
    Μελλοντικά μπορεί να αντικατασταθεί με μοντέλο ML.
    """
    z_vals = [point[2] for point in pcd.points]
    length = max(z_vals) - min(z_vals)
    return "Partial" if length > 30 else "Fully"
