from setuptools import setup, find_packages

setup(
    name = 'angie-sirius',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/cad.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = "image format changer",
    install_requires = ['setuptools', "lina@git+https://github.com/TakutoYoshikai/lina.git", "cad@git+https://github.com/TakutoYoshikai/cad.git", "parade@git+https://github.com/TakutoYoshikai/parade.git", "sirius@git+https://github.com/TakutoYoshikai/sirius.git"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "angie-sirius = angie_sirius.angie_sirius:main",
        ]
    }
)
