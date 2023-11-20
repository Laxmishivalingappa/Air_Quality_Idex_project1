from setuptools import setup,find_packages

HYPON_E_DOT = "-e ."

def get_requirements(file_name):
    requirements=[]
    with open(file_name) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPON_E_DOT in requirements:
            requirements.remove(HYPON_E_DOT)
    return requirements






setup (
    name = "Internship_project",
    author ="Dev_mandloi",
    author_email= "devmandloi37@gmail.com",
    version = "0.0.0.1",
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()
    
)