from setuptools import setup

setup(
    name="guided-diffusion",
    py_modules=["guided_diffusion", "ldm", "encoders", "util", "models"],
    install_requires=["blobfile>=1.0.5", "torch", "tqdm"],
)
