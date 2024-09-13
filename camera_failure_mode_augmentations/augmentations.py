"""Various augmentations to apply to simulate different camera failure modes."""

import cv2
from PIL import Image, ImageEnhance


def blur(img: Image, intensity: int):
    """Apply a Gaussian blur to the image.  An intensity of 1 is no blur, while
    and intensity of 25 is extreme blur and about the maximum expected from a
    physical camera.
    """
    img = cv2.blur(img, (intensity, intensity))
    return img


def bright(img: Image, intensity: float):
    """Apply a birghtness transform to the image.  An intensity of 1 is no
    change.  An intensity less than 1 leads to a darker image with 0 being
    entirely black.  An intensity greater than 1 leads to a more saturated
    image.
    """
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(intensity)
    return img


def chromab(img: Image, int: float):
    pass


def deapix(img: Image, location: int):
    pass

def nbayf(img: Image):
    pass

def demos(img: Image):
    pass

def noise(img: Image, intensity: int):
    pass

def sharp(img: Image, intensity: int):
    pass

def flare(img: Image, intensity: int):
    pass

def rain(img: Image):
    pass

def ice(img: Image):
    pass

def dirty(img: Image):
    pass

def cond(img: Image):
    pass

def brle(img: Image):
    pass

def band(img: Image):
    pass