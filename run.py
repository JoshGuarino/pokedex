import os
import subprocess

#terminal commands to run the app
def run_app():
    os.chdir('pokedex')
    subprocess.call(["python3", "app.py"])

#install depedencies
def dep_install():
    subprocess.call(["pipenv", "install"])   

if __name__ == '__main__':
    dep_install()
    run_app()