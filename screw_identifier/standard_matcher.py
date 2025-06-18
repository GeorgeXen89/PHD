import pandas as pd

def find_standard_screw(diameter, length, thread_type):
    df = pd.read_csv("iso_screws.csv")
    filtered = df[df["thread_type"] == thread_type].copy()

    # Ενισχυμένο βάρος στη διάμετρο (π.χ. ×5)
    filtered["distance"] = (((filtered["diameter"] - diameter)*5)**2 + (filtered["length"] - length)**2)**0.5

    best_match = filtered.loc[filtered["distance"].idxmin()]
    screw_type = best_match["type"]
    head = screw_type.split()[0].split("x")[0].lower()
    url = f"https://www.mcmaster.com/screws/{head}-socket-head-cap-screws/"
    return screw_type, url
