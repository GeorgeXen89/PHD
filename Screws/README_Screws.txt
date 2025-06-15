📁 Φάκελος: Screws

Σκοπός: Περιέχει point clouds (.PLY) και CAD αρχεία (.SLDPRT) τυποποιημένων βιδών, καθώς και scripts ανάλυσης και μέτρησης. Αποτελεί το βασικό dataset και πειραματικό περιβάλλον για την αναγνώριση χαρακτηριστικών όπως:
- διάμετρος,
- μήκος,
- μορφή σπειρώματος.

Χρησιμοποιείται σε συνδυασμό με τα εργαλεία RANSAC και Open3D.

📦 Περιεχόμενα:
- Point Clouds (.PLY) για M5, M10, M10ft (fully-threaded).
- CAD αρχεία για οπτική/γεωμετρική σύγκριση.
- Scripts για preprocessing, fitting, visualization, μέτρηση.
- Υπάρχει και Excel αρχείο με προδιαγραφές ή πειραματικά αποτελέσματα.

📂 Δομή:

Screws/
    Screws/
        # 4. process_screw.py
        92620A412_Zinc Yellow-Chromate Plated Hex Head Screw.PLY
        92620A412_Zinc Yellow-Chromate Plated Hex Head Screw.SLDPRT
        94863A209_High-Strength Class 10.9 Steel Hex Head Screw.SLDPRT
        classify_thread.py
        estimate_screw_diameter.py
        fit_cylinder_ransac.py
        M10.PLY
        M10.SLDPRT
        M10ft.PLY
        M10ft.SLDPRT
        measure_full.py
        measure_partial.py
        preprocess.py
        trexei konta.py
        view_ply.py
        αποτελέσματα προγράμματος.xlsx