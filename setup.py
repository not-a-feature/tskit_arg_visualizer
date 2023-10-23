from setuptools import setup

setup(
    name="tskit_arg_visualizer",
    version="v0.0.1-alpha",
    url='https://github.com/kitchensjn/tskit_arg_visualizer',
    author="James Kitchens",
    author_email="kitchensjn@gmail.com",
    packages=["tskit_arg_visualizer"],
    install_requires=[
        "msprime",
        "IPython",
    ],
    include_package_data=True,
)