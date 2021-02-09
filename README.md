Introduction
------------

Run this module to change your Android app's version code and name externally.

## Installation
Install via pip:

    pip install os-android-app-version-changer

## Quick usage
Define your Version properties and run the code:

```python
from os_android_app_version_changer.objs.VersionProperties import VersionProperties
from os_android_app_version_changer import version_changer

version_props = VersionProperties(new_version_code=VersionProperties.RAISE_VERSION_BY_ONE,
                                  new_version_name="1.0.3")

version_changer.change_version(project_path='/path/to/project', 
                               version_properties=version_props)
```
NOTICE: NOTICE: each of these properties can also hold, apart from specific versions, ```VersionProperties.KEEP_OLD_VERSION``` or ```VersionProperties.RAISE_VERSION_BY_ONE```.

## Licence
MIT