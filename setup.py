import shutil
import setuptools

class Cleanup(setuptools.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        dirs = ("./build", "./dist", "./dpgwidgets.egg-info")
        for dir in dirs:
            try:
                shutil.rmtree(dir)
            except OSError:
                pass


setuptools.setup(cmdclass = {"clean": Cleanup})

