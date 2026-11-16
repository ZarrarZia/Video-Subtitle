from setuptools import setup, find_packages

setup(
    version="1.0",
    name="auto_subtitle",
    packages=find_packages(),
    py_modules=["auto_subtitle"],
    author="ZarrarZia, Miguel Piedrafita",
    url="https://github.com/ZarrarZia/Video-Subtitle",
    python_requires=">=3.8",
    install_requires=[
        'openai-whisper',
    ],
    description="Automatically generate subtitles for videos with OpenAI Whisper and burn them in with FFmpeg",
    entry_points={
        'console_scripts': ['auto_subtitle=auto_subtitle.cli:main'],
    },
    include_package_data=True,
)
