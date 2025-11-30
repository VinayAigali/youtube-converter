from flask import Flask, render_template, request, send_file
from mp4 import youtube_to_mp4
import os
import glob

app = Flask(__name__)

DOWNLOAD_FOLDER = "vid downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")

    if not url:
        return "No URL entered."

    # Call your existing download function
    youtube_to_mp4(url)

    # Get latest downloaded file
    files = glob.glob(os.path.join(DOWNLOAD_FOLDER, "*"))
    latest = max(files, key=os.path.getctime)

    # Send file to browser
    return send_file(latest, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
