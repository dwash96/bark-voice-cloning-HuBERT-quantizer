from setuptools import setup

setup(
    name='bark_hubert_quantizer',
    version='0.0.4',
    packages=['bark_hubert_quantizer'],
    install_requires=[
        'audiolm-pytorch==1.1.4',
        'fairseq @ git+https://github.com/liyaodev/fairseq.git@b963eac7a04c539ad59fb1e23277f2ff7ee29e74',
        'huggingface-hub',
        'sentencepiece',
        'transformers',
        'encodec',
        'soundfile; platform_system == "Windows"',
        'sox; platform_system != "Windows"'
    ],
)