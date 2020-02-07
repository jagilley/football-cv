def bgr(rgb: list) -> list:
    return list(reversed(rgb))

red = ([17, 15, 100], [50, 56, 200])
blue = ([86, 31, 4], [220, 88, 50])
yellow = ([25, 146, 190], [62, 174, 250])
gray = ([103, 86, 65], [145, 133, 128])

customRed = ([17, 15, 100], [100, 100, 255])

ranges = {
    "cr1": customRed,
    "cr2": (bgr([120, 61, 61]), bgr([237, 62, 97])),
    "cr3": (bgr([100, 14, 15]), bgr([255, 62, 97]))
}