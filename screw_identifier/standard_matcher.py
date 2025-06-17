def find_standard_screw(diameter, length, thread_type):
    standards = {5: "M5", 6: "M6", 8: "M8", 10: "M10", 12: "M12"}
    closest_d = min(standards.keys(), key=lambda x: abs(x - diameter))
    screw_type = f"{standards[closest_d]}x{int(round(length))} {thread_type}"
    url = f"https://www.mcmaster.com/screws/{standards[closest_d]}-socket-head-cap-screws/"
    return screw_type, url
