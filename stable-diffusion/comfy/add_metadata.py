from pathlib import Path
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import shutil
import argparse


def load_metadata(image_path: Path) -> PngInfo:
    metadata = PngInfo()
    with Image.open(image_path) as image:
        for key in image.text:
            metadata.add_text(key, image.text[key])
    return metadata


def add_metadata(image_path: Path, metadata: PngInfo) -> None:
    with Image.open(image_path) as image:
        image.save(image_path, pnginfo=metadata, optimize=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("image")
    parser.add_argument("workflow_image")

    args = parser.parse_args()

    image_path = Path(args.image)
    workflow_image_path = Path(args.workflow_image)
    backup_path = image_path.parent / f"{image_path.stem}.backup{image_path.suffix}"

    shutil.copy2(image_path, backup_path)
    metadata = load_metadata(workflow_image_path)
    add_metadata(image_path, metadata)
