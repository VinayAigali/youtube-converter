import os
import subprocess
import sys

def youtube_to_mp4(url, folder="vid downloads"):
    """Download a YouTube video as MP4 into a folder next to the script."""
    # Get the folder path relative to this script
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder)
    os.makedirs(out, exist_ok=True)

    exe = sys.executable.replace("pythonw.exe", "python.exe")

    cmd = [
        exe, "-m", "yt_dlp",
        "-f", "bestvideo+bestaudio/best",      # Best quality video+audio
        "-o", os.path.join(out, "%(title)s.%(ext)s"),  # Save with video title
        "--merge-output-format", "mp4",        # Merge into MP4
        "--ignore-errors",                      # Continue even if minor errors occur
        url
    ]

    print("\nRunning command:\n" + " ".join(cmd))
    subprocess.run(cmd)

    print(f"\n✅ Download finished. Videos saved in: {out}")

if __name__ == "__main__":
    link = input("YouTube URL: ").strip()
    if link:
        youtube_to_mp4(link)
    else:
        print("No URL entered. Exiting.")
