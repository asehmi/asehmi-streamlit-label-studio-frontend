import setuptools

setuptools.setup(
    name="streamlit-label-studio-frontend",
    version="0.0.2",
    author="",
    author_email="",
    description="A Streamlit component integrating Label Studio Frontend in Streamlit applications",
    long_description="A Streamlit component integrating Label Studio Frontend in Streamlit applications",
    long_description_content_type="text/plain",
    url="https://github.com/asehmi/streamlit-label-studio-frontend",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.10",
    install_requires=[
        "streamlit >= 1.35.0",
    ],
)
