from setuptools import setup, find_packages

setup(
    name="prometheus-eval",
    version="0.1.0",
    description="Local version of the Prometheus Eval package",
    author="Your Name",
    packages=find_packages(),  # This auto-discovers prometheus_eval/
    install_requires=[
        # put any required packages here, like:
        "transformers",
        "torch",
        "vllm",
        "litellm",
    ],
    python_requires=">=3.10",
)
