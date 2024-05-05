import os
import collections

audio = ["mp3", "wav", "raw", "mid", "midi", "m4a"]
video = ["mp4", "mpg", "mpeg", "avi", "mov", "mkv"]
images  = ["png", "jpg", "jpeg", "gif", "svg", "ico", "webp"]
docs  = ["txt", "pdf", "csv", "xls", "xlsx", "ods", "doc", "docx", "odt", "ppt", "pptx", "rtf"]
comp = ["zip", "z", "7z", "rar"]
code = ["cs", "py", "bat", "html", "css", "js"]
exe = ["exe"]
domaines = [[audio, video, images, docs, comp, code, exe],
            ["Music", "Movies", "Pictures", "Documents", "Other", "Code", "Applications"]]

# - - - Création des différents dossiers - - - - - - - - - - - - - - - -
root_path = os.path.expanduser("~")
for name in domaines[1]:
    dir_path = os.path.join(root_path, name)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# - - - tri des fichiers par extension - - - - - - - - - - - - - - - - -
dwnld_path = os.path.join(root_path, "Downloads")
file_mapping = collections.defaultdict(list)
file_list = os.listdir(dwnld_path)
for name in file_list:
    if name[0] != ".":
        file_ext = name.split(".")[-1]
        file_mapping[file_ext].append(name)

# - - - rangement dans les dossiers correspondant aux extensions - - - -
for ext, file_list in file_mapping.items():
    found_yet = False
    for index, domaine in enumerate(domaines[0]):
        if ext in domaine:
            found_yet = True
            for file in file_list:
                os.rename(os.path.join(dwnld_path, file), os.path.join(root_path, domaines[1][index], file))
    if not found_yet:
        for file in file_list:
            os.rename(os.path.join(dwnld_path, file), os.path.join(root_path, "Other", file))