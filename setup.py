from distutils.core import setup

setup(
	name='csurl',
	packages=['csurl'],
	version='1.0.0-beta.1',
	description='ChakSoft URL access module binding for Python 3.x',
	author='Michael Chacaton',
	author_email='chako256@gmail.com',
	url='https://github.com/Choko256/csurl-python',
	download_url='https://github.com/Choko256/csurl-python/tarball/1.0.0-beta.1',
	keywords=['csurl', 'link', 'shorten'],
	classifiers=[],
	setup_requires=['requests'],
	tests_require=['pytest']
)