import os
import subprocess


def main(build):
    build.packages.install(".", develop=True)


def test(build):
    main(build)
    build.packages.install("pytest")
    build.packages.install("pytest-cov")
    pytest = os.path.join(build.root, "bin", "py.test")
    subprocess.call([
        pytest, "--cov", "nlgen",
        "nlgen/tests",
        "--cov-report", "term-missing"
    ] + build.options.args)


def distribute(build):
    """ distribute the uranium package """
    build.packages.install("wheel")
    build.executables.run([
        "python", "setup.py",
        "sdist", "bdist_wheel", "--universal", "upload"
    ])
