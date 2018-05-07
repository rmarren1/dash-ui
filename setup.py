import io
from setuptools import setup, find_packages

main_ns = {}
exec(open('dash_ui/version.py').read(), main_ns)  # pylint: disable=exec-used

setup(
    name='dash_ui',
    version=main_ns['__version__'],
    author='Ryan rmarren1',
    author_email='rymarr@tuta.io    ',
    packages=find_packages(),
    license='MIT',
    description=('Some abstractions to make creating UIs easier in Dash.'),
    long_description=io.open('README.md', encoding='utf-8').read(),
    install_requires=[
        'Flask>=0.12',
        'flask-compress',
        'plotly',
        'dash_renderer',
        'dash'
    ]
)
