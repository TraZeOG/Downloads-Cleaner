from vacuum_settings import *

def clean_download():
    # - - - Création des différents dossiers - - - - - - - - - - - - - - - -
    for name in domaines[1]:
        dir_path = os.path.join(root_path, name)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
            logging.info(f"Dossier créé : {dir_path}")
            
    # - - - Vérification du dossier "Downloads" - - - - - - - - - - - - - -
    dwnld_path = os.path.join(root_path, "Downloads")
    if not os.path.isdir(dwnld_path):
        logging.error(f"Le dossier {dwnld_path} n'existe pas.")
        print(f"Le dossier {dwnld_path} n'existe pas. Le script va s'arrêter.")
        exit(1)

    # - - - Tri des fichiers par extension - - - - - - - - - - - - - - - -
    file_mapping = collections.defaultdict(list)
    file_list = os.listdir(dwnld_path)
    for name in file_list:
        if name[0] != "." and os.path.isfile(os.path.join(dwnld_path, name)):
            file_ext = name.split(".")[-1].lower()
            file_mapping[file_ext].append(name)

    # - - - Rangement dans les dossiers correspondants - - - - - - - - - -
    for ext, file_list in file_mapping.items():
        found_yet = False
        for index, domaine in enumerate(domaines[0]):
            if ext in domaine:
                found_yet = True
                for file in file_list:
                    src = os.path.join(dwnld_path, file)
                    dest = os.path.join(root_path, domaines[1][index], file)

                    # Vérification des collisions
                    if os.path.exists(dest):
                        logging.warning(f"Collision détectée : {dest} existe déjà.")
                        print(f"Collision détectée pour {file}.")
                    else:
                        shutil.move(src, dest)
                        logging.info(f"Fichier déplacé : {src} → {dest}")
        
        # Si aucune catégorie n'est trouvée, déplacer dans "Other"
        if not found_yet:
            for file in file_list:
                src = os.path.join(dwnld_path, file)
                dest = os.path.join(root_path, "Other", file)

                # Vérification des collisions
                if os.path.exists(dest):
                    logging.warning(f"Collision détectée : {dest} existe déjà.")
                    print(f"Collision détectée pour {file}.")
                else:
                    shutil.move(src, dest)
                    logging.info(f"Fichier déplacé : {src} → {dest}")