from distutils.core import setup

setup(
    name='os_android_app_version_changer',
    packages=['os_android_app_version_changer',
              'os_android_app_version_changer.bp'],
    version='1.00',
    license='MIT',
    description='will change the version (name and code) of an android app programmatically (dynamically)',
    author='Oz Shabat',
    author_email='admin@os-apps.com',
    url='https://github.com/osfunapps/os-android-app-version-changer-py',
    keywords=['python', 'osfunapps', 'version-code', 'version-name', 'android', 'version', 'automation'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',  # Again, pick a license

        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9'
    ],
)
