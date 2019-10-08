import os.path
from pythonci.task import BaseTask


NUMPY_ZIP = 'https://files.pythonhosted.org/packages/ac/36/325b27ef698684c38b1fe2e546e2e7ef9cecd7037bcdb35c87efec4356af/numpy-1.17.2.zip'


class Task(BaseTask):
    name = "numpy"

    def _install(self):
        # rely on Fedora to provide OpenBLAS or pull it differently?
        self.app.pip_install_update(["Cython"])

        self.app.download_extract_zip(NUMPY_ZIP, self.dirname)
        self.app.chdir(self.dirname)

        # Force to run Cython: regenerate C files generated by Cython
        cmd = r"rm -f -v $(grep -rl '/\* Generated by Cython') PKG-INFO"
        self.app.run_command([cmd], shell=True, cwd=self.dirname)

        self.app.run_python(["setup.py", "install"], cwd=self.dirname)

    def _run_tests(self):
        self.app.pip_install_update(["nose", "pytest"])
        script = os.path.join(self.dirname, 'tools', 'test-installed-numpy.py')
        self.app.run_python([script, "--mode=full"])