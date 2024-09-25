import os
from setuptools import setup, find_packages

# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    lines = f.readlines()
    long_description = ''.join(lines)

print([
  package for package in find_packages() if package.startswith("robosuite")
])

def package_files(directory, allow_extensions=None):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            if allow_extensions and not any([filename.endswith(ext) for ext in allow_extensions]):
                continue
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('robosuite_task_zoo/models', allow_extensions=['py', 'xml', 'stl'])

setup(
    name="robosuite_task_zoo",
    packages=[
        package for package in find_packages() if package.startswith("robosuite")
    ],
    install_requires=[
        "numpy>=1.13.3,<2",
        "numba>=0.49.1",
        "scipy>=1.2.3",
    ],
    eager_resources=['*'],
    include_package_data=True,
     package_data={
        'robosuite_task_zoo': extra_files,
    },
    python_requires='>=3',
    description="robosuite task zoo",
    author="Yuke Zhu",
    url="https://github.com/ARISE-Initiative/robosuite-task-zoo",
    author_email="yukez@cs.utexas.edu",
    version="0.1",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
