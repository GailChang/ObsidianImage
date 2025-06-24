import os
import urllib.parse
from pathlib import Path

REPO_DIR = Path(__file__).parent / 'Repository'
IMAGES_MD = REPO_DIR / 'IMAGES.md'
GITHUB_BASE = 'https://gailchang.github.io/ObsidianImage/Repository/'

# 支援的圖片副檔名
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'}

def get_image_files():
    return sorted([
        f for f in REPO_DIR.iterdir()
        if f.suffix.lower() in IMAGE_EXTS and f.is_file()
    ])

def generate_md(images):
    lines = [
        '# 圖片連結清單',
        '',
        '以下是目前 Repository 資料夾內所有圖片的可嵌入連結：',
        ''
    ]
    for img in images:
        url = GITHUB_BASE + urllib.parse.quote(img.name)
        lines.append(f'- ![{img.name}]({url})')
    lines.append('\n> 所有圖片連結皆可直接嵌入筆記或網頁。')
    return '\n'.join(lines)

def main():
    images = get_image_files()
    md = generate_md(images)
    with open(IMAGES_MD, 'w', encoding='utf-8') as f:
        f.write(md)

if __name__ == '__main__':
    main()
