
from distutils.core import setup


setup(
	name = "expm",
	version = "0.0.1",
	author = "Nilofar Rahmani",
	author_email = "nilofar.z.rahmani@exxommobil.com",
	description = "Installs required packages",
	url = "https://github.com/ranganathanbarath/expm",
	dependency_links=[
		'git@gitserver.xtonet.com:NetworkAutomationFramework/netCatz-pypi.git'
	]
)

