from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        name='Fishy',
        description='GUI app for learning word corpus',
        keywords='Learning languages',
        version='1.2.2',
        author='Egor Kolotaev',
        author_email='ekolotaev@gmail.com',
        license="MIT",
        url='http://github.com/kolotaev/Fishy',
        long_description='GUI app for learning word corpus. Build with tkinter',
        entry_points={
            'console_scripts': [
                'fishy = main:run',
            ],
        },
        py_modules=['app', 'resources', 'main'],
        python_requires='>=3.6',
        install_requires=[
            'google_speech',
            'googletrans>=4.0.0rc1',
        ],
        extras_require={},
        packages=find_packages(exclude='tests'),
        classifiers=[],
    )
