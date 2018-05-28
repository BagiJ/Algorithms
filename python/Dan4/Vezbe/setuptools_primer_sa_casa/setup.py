from setuptools import setup 

setup(	name='primer_setuptools', 
        version='1.0', 
        description='Opis paketa', 
        author='Ime i prezime autora',
        author_email='mailautora@negde.com',
        url='http://ulrprojekta.com/', 
        packages=['prvipaket', 'drugipaket', 
                   'drugipaket.podpaket'], # ako je kod razvrstan po folderima (paketima)
        scripts = ['gsearch.py'], # ako je neka skripta izvan paketa
)
