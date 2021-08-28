import shutil
import setuptools
import subprocess

class Cleanup(setuptools.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Building...")
        subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"])
        print("\nCleaning up...", end="")
        dirs = ("./build", "./pixlengine.egg-info")
        for dir in dirs:
            try:
                shutil.rmtree(dir)
            except OSError:
                pass
        print("done.")


setuptools.setup(cmdclass = {"process": Cleanup})
