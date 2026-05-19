from setuptools import find_packages, setup

package_name = 'turtlesim_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi31415',
    maintainer_email='pi31415@example.com',
    description='Turtlesim controller package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'exec_name = folder_name.file_name:main',
        ],
    },
)