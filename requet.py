import subprocess

def mettre_a_jour_pip():
    try:
        subprocess.check_call(['pip', 'install', '--upgrade', 'pip'])
        print("pip a été mis à jour avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la mise à jour de pip : {e}")

def installer_modules(liste_modules):
    for module in liste_modules:
        try:
            subprocess.check_call(['pip', 'install', module])
            print(f"Le module {module} a été installé avec succès.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de l'installation du module {module}: {e}")

# Mettre à jour pip
mettre_a_jour_pip()

# Liste des modules à installer
modules_a_installer = ['Pillow', 'Requests', 'streamlit','streamlit_lottie']  # Remplacez par les noms des modules que vous souhaitez installer

# Installer les modules
installer_modules(modules_a_installer)

