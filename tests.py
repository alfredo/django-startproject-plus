#!/usr/bin/env python

import os
import shutil
import subprocess
import tempfile
import unittest

class TestStartProject(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.mkdtemp(prefix="startproject-test-")
        self.cwd = os.getcwd()
        os.chdir(self.temp)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.temp)

    def test_template(self):
        os.mkdir('src')
        with open('src/test.py', 'w') as src:
            src.write('{{ project_name }} {{ value }}')
        proc = subprocess.Popen([
            'django-startproject.py',
            '--template', 'src',
            '--extra_context', '{"value": "ok"}',
            'dst'], stderr=subprocess.PIPE)
        dummy, stderr = proc.communicate()
        self.assertEqual(proc.returncode, 0,
                         'Error running django-startproject.py:\n%s' %
                         stderr.decode('utf-8'))
        with open('dst/test.py') as dst:
            self.assertEqual(dst.read(), 'dst ok')

if __name__ == '__main__':
    unittest.main()

