import shutil
import setuptools

class Cleanup(setuptools.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        shutil.rmtree("./build")
        shutil.rmtree("./dpgwidgets.egg-info")


setuptools.setup(cmdclass = {"clean": Cleanup})

