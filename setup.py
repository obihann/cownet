from distutils.core import setup

setup(
	name='Cownet',
	version='0.1.0',
	author='Jeffrey Hann',
	author_email='jeffhann@gmail.com',
	scripts=['bin/cownet.py'],
	url='http://obihann.github.io/Cownet/',
	license='LICENSE',
	description='I wanted to view my up to date network usage in a easy to read and friendly way. So I built a tool that pulls the data in from netstat, and displays a cleaned up output in Cowsay. ',
)