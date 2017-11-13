"""
    zoom.services

    background services
"""

import os
import shlex
import subprocess


def run(command, returncode=False, location=None):
    """Run a shell command and return the response as a string

        >>> run("echo testing")
        'testing\\n'

        >>> run("echo testing", location="/")
        'testing\\n'

    """
    save_dir = os.getcwd()
    try:
        if location:
            os.chdir(location)

        if returncode:
            process = subprocess.Popen(
                shlex.split(command),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate()
            return process.returncode, str(stdout), str(stderr)
        else:
            return subprocess.Popen(
                shlex.split(command),
                stdout=subprocess.PIPE
            ).communicate()[0].decode('utf-8')
    finally:
        os.chdir(save_dir)