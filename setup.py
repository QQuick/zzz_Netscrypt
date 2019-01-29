from setuptools import setup

setup (
    name = 'Netscrypt',
    version = '0.0.1',
    description = 'Proxy package for Transcrypt, supporting client- and server-side proxies, to enable seamless cooperation between Transcrypt client and CPython server, using one source language',
    long_description = '',
    keywords = ['transcrypt', 'python', 'proxy', 'websockets', 'sockets', 'netscrypt'],
    url = 'http://www.transcrypt.org',
    author = 'Jacques de Hooge',
	author_email = 'jacques.de.hooge@qquick.org',
    packages = ['netscrypt'],
    include_package_data = True,
    classifiers = [
		'Development Status :: 1 - Planning',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.7'
	]
)
