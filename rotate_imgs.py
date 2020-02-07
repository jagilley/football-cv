from PIL import Image
import rtCustom2
from rtCustom2 import get_oline_angle

def rotate_img(pil_image):
    """
    Given an instance of a PIL image, rotate it by the
    angle of the offensive line
    """
    # uses a placeholder for the eventual oline angle internal API
    oline_ang = get_oline_angle()
    # naturally, pil_image should by of type PIL.Image
    rotated = pil_image.rotate(oline_ang)
    rotated.show()
    return rotated