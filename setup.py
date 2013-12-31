from distutils.core import setup

setup(
    name='instagram-recommend-user',
    version='0.1',
    description='recommend a relavant people to follow for instagram user',
    keywords='instagram recommend user',
    authors="esmacns,serraunl",
    author_emails='esmacansu@std.sehir.edu.tr,fatmaunal@std.sehir.edu.tr',
    url='https://github.com/serraunl/instagram-recommend-user',
    classifiers=[
        'Programming Language :: Python',
    ],
    py_modules=["recommendation_project"],
    install_requires=[
        'python-instagram',
        'tkinter',
        'webbrowser'
    ],
)
