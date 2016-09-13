import os
import subprocess
from uranium import task_requires


@task_requires("build_grammar")
def main(build):
    build.packages.install(".", develop=True)


def build_grammar(build):
    build.packages.install("grako")
    source = os.path.join(build.root, "nlgen", "cfg", "markup_grammar.grako")
    target = os.path.join(build.root, "nlgen", "cfg", "markup_parser.py")
    build.executables.run([
        "grako", "--outfile", target,
        "--name", "cfg_markup",
        source
    ])


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


@task_requires(build_grammar)
def distribute(build):
    """ distribute the uranium package """
    build.packages.install("wheel")
    build.executables.run([
        "python", "setup.py",
        "sdist", "bdist_wheel", "--universal", "upload"
    ])
