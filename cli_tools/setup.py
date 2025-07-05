from setuptools import setup

setup(
    name="cli_tools",
    version="1.0",
    py_modules=["greeter"],
    install_requires=[
        "Click",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "greetings=greeter:greet",
            "add=calculator:add",
            "sub=calculator:subtract",
            "authenticate=authenticate:auth",
            "login=authenticate:login",
            "note=fileutils:note",
            "concat=fileutils:concat",
            "notes=notes:main",
            "download=fileutils:download",
        ]
    }
)
