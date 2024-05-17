import subprocess
from pathlib import Path


def download_annotations(dst_dir: str = '.'):
    """
    Args
        `dst_dir`: destination directory to save annotations. Default to `<current directory>/annotations`.
    """
    dst_dir = Path(dst_dir)
    dst_dir.mkdir(parents=True, exist_ok=True)
    zip_file_path = dst_dir / 'annotations_trainval2017.zip'
    print('downloading...')
    subprocess.run([
        "wget",
        "-c", "http://images.cocodataset.org/annotations/annotations_trainval2017.zip",
        "-P", str(dst_dir)
    ])
    print('unzipping...')
    subprocess.run(['unzip', str(zip_file_path)])
    print('removing...')
    subprocess.run(['rm', str(zip_file_path)])
