import os
import subprocess
from uranium import task_requires


def main(build):
    build.packages.install(".", develop=True)
    build_grammar(build)


def build_grammar(build):
    source = os.path.join(build.root, "nlgen", "cfg", "markup_grammar.grako")
    target = os.path.join(build.root, "nlgen", "cfg", "markup_parser.py")
    build.executables.run([
        "grako", "--outfile", target,
        "--name", "CFGMarkup",
        source
    ])


@task_requires("main")
def build_docs(build):
    build.packages.install("Babel")
    build.packages.install("sphinx")
    build.packages.install("sphinx_rtd_theme")
    return subprocess.call(
        ["make", "html"], cwd=os.path.join(build.root, "docs")
    )


@task_requires("main")
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
