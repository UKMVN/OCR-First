#
# Code này phòng trường hợp
# 1. Bạn Lê Hồng Sơn quá ngooo để impl
# 2. Xem 1
# 3. Xem lại 2
#

from pathlib import Path
import requests

def do_detect_scene(image: Path) -> str:
    print(f"Processing file: {image.name}")
    url = 'http://localhost:8000/detect_scene'
    with open(image, 'rb') as f:
        responses = requests.post(url, files={'image': f}).json()
    return responses['result'] if responses['status'] else ""
