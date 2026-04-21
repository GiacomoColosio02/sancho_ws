from setuptools import find_packages, setup

package_name = 'sancho_perception'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='giacomo',
    maintainer_email='colosio.giacomo.2002@gmail.com',
    description='Nodi di percezione per SANCHO: camera e rilevazione della traccia fluorescente',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'camera_node = sancho_perception.camera_node:main',
        ],
    },
)