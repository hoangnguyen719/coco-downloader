from typing import Union, List
from pathlib import Path

from pycocotools.coco import COCO
import requests

from .config import COCO2017_CLASSES

def _check_valid_class(class_name: str):
    """
    Check if class name is valid and one of COCO's classes.
    """
    assert isinstance(class_name, str), "Class name must be type `str`."
    return class_name in COCO2017_CLASSES


def _load_coco_annotation(coco_annot_path: str):
    """
    Load COCO annotation JSON file.
    """
    assert isinstance(coco_annot_path, str), "coco_annot_path must be a string"
    coco_annot_path = Path(coco_annot_path)
    assert coco_annot_path.is_file(), "coco_annot_path does not exist as a file"
    assert coco_annot_path.suffix == '.json', "coco_annot_path must link to a JSON file"

    return COCO(str(coco_annot_path))


def _coco_get_image_by_class_names(class_names: Union[List[str], str], coco_annot: COCO):
    cat_ids = coco_annot.getCatIds(catNms=class_names)
    img_ids = coco_annot.getImgIds(catIds=cat_ids)
    return coco_annot.loadImgs(img_ids)


def get_images_by_classes(
    classes: Union[List[str], str],
    coco_annot_path: str,
    all_classes: bool = False
) -> list:
    """
    Args
        `classes`: a `list` of `str`s, each of which is a class name.

        `coco_annot_path`: path to the JSON COCO annotation file.

        `all_classes`: whether to include only images that contain all classes. Default to False.

    Return
        `images`: a `list` of `dict`, each of which is an image's metadata in COCO format.
    """
    if isinstance(classes, str):
        classes = [classes]
    elif not isinstance(classes, list):
        raise Exception("Classes must be a string or a list of string.")
    
    coco = _load_coco_annotation(coco_annot_path=coco_annot_path)

    if all_classes:
        images = [_coco_get_image_by_class_names(class_names=classes, coco_annot=coco)]
    else:
        images = {}
        for cls in classes:
            _check_valid_class(class_name=cls)
            cat_ids = coco.getCatIds(catNms=[cls])
            img_ids = coco.getImgIds(catIds=cat_ids)
            new_images = coco.loadImgs(img_ids)
            for im in new_images:
                images[im['file_name']] = im
        images = list(images.values())
    return images


def download_file_by_url(url: str, save_name: str):
    content = requests.get(url).content
    with open(save_name, 'wb') as handler:
        handler.write(content)