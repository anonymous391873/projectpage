import os
import subprocess
from pathlib import Path

ROOT_DIR = Path("/code/CVPR/projectpage/static/videos")

def convert_mkv_to_mp4(folder_path: Path):
    mkv_files = folder_path.glob("*.mkv")
    for mkv_file in mkv_files:
        mp4_file = mkv_file.with_suffix(".mp4")
        if mp4_file.exists():
            print(f"[SKIP] Already exists: {mp4_file}")
            continue
        try:
            print(f"[CONVERT] {mkv_file.name} → {mp4_file.name}")
            subprocess.run(
                ["ffmpeg", "-i", str(mkv_file), "-c:v", "libx264", "-c:a", "aac", "-y", str(mp4_file)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
        except subprocess.CalledProcessError:
            print(f"[ERROR] Failed to convert: {mkv_file}")

def main():
    for subfolder in sorted(ROOT_DIR.iterdir()):
        if subfolder.is_dir():
            print(f"\n=== Processing folder: {subfolder} ===")
            convert_mkv_to_mp4(subfolder)

if __name__ == "__main__":
    main()
