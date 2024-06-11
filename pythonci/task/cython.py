import os.path
from pythonci.task import BaseTask


TARBALL = 'https://files.pythonhosted.org/packages/d5/f7/2fdd9205a2eedee7d9b0abbf15944a1151eb943001dbdc5233b1d1cfc34e/Cython-3.0.10.tar.gz'


class Task(BaseTask):
    name = "Cython"

    def _install(self):
        self.app.download_extract_tarball(TARBALL, self.dirname)
        self.app.chdir(self.dirname)

        self.app.run_python(["setup.py", "install"], cwd=self.dirname)

    def _run_tests(self):
        self.app.run_python(['runtests.py', '-vv', '--no-pyregr'],
                            cwd=self.dirname)
