import os

def afficher_contenu_dossier(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"---Dossier: {dirpath}---")
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            print(f"\n---Fichier: {filepath}---")
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    contenu = f.read()
                    print(contenu)
            except Exception as e:
                print(f"<Erreur lecture fichier : {e}>")

if __name__ == "__main__":
    dossiers = [
        r"C:\smartmaritime\SMM_BACKEND\api",
        r"C:\smartmaritime\SMM_BACKEND\smartmaritime"
    ]
    for dossier in dossiers:
        afficher_contenu_dossier(dossier)
