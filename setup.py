from setuptools import setup, find_packages

setup(
    name='midiSynth',
    version='0.2',
    description='',
    author='annahung31',
    author_email='fbiannahung@gmail.com',
    url='https://github.com/annahung31/midi_synth.git',
    packages=find_packages(),
    package_data={'': ['examples_data/*']},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
    ],
    keywords='music midi mir',

    license='MIT',
    install_requires=[
        'numpy >= 1.19.5',
        'scipy >= 1.5.4',
        'pretty_midi >= 0.2.9',
        'ipython >= 7.16.1'
    ]
)


"""
python setup.py sdist
twine upload dist/*
"""