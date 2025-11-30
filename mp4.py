import os
import subprocess
import sys

def youtube_to_mp4(url, folder="/tmp/videos"):
    """Download a video to /tmp because Render only allows writing there."""
    os.makedirs(folder, exist_ok=True)

    exe = sys.executable.replace("pythonw.exe", "python.exe")

    cmd = [
        exe, "-m", "yt_dlp",
        "-f", "bestvideo+bestaudio/best",
        "-o", os.path.join(folder, "%(title)s.%(ext)s"),
        "--merge-output-format", "mp4",
        "--ignore-errors",
        url
    ]

    print("\nRunning command:\n" + " ".join(cmd))
    subprocess.run(cmd)

    print(f"\n✅ Download finished. Videos saved in: {folder}")

    return folder
