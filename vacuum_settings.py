import os
import shutil
import collections
import logging

# Extensions par catégories
audio = ["mp3", "wav", "raw", "mid", "midi", "m4a"]
video = ["mp4", "mpg", "mpeg", "avi", "mov", "mkv"]
images = ["png", "jpg", "jpeg", "gif", "svg", "ico", "webp"]
docs = ["txt", "pdf", "csv", "xls", "xlsx", "ods", "doc", "docx", "odt", "ppt", "pptx", "rtf"]
comp = ["zip", "z", "7z", "rar"]
code = ["cs", "py", "bat", "html", "css", "js"]
exe = ["exe"]
domaines = [
    [audio, video, images, docs, comp, code, exe],
    ["Music", "Movies", "Pictures", "Documents", "Other", "Code", "Applications"],
]

# Configuration du journal
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

root_path = os.path.expanduser("~")