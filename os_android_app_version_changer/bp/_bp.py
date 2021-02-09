import fileinput

import os
import sys
import re
from os_android_app_version_changer.objs.VersionProperties import VersionProperties
from os_android_app_version_changer.bp import _res


def change_version(project_path, version_properties):
    build_gradle_file = os.path.join(project_path, 'app', 'build.gradle')
    for line in fileinput.input(build_gradle_file, inplace=1):
        # set the right version name or version code, if required
        if not version_properties.new_version_code != VersionProperties.KEEP_OLD_VERSION and _res.VERSION_CODE in line:
            line = _change_version_props(line, version_properties.new_version_code, _res.VERSION_CODE)
            sys.stdout.write(line)
            continue

        elif version_properties.new_version_name != VersionProperties.KEEP_OLD_VERSION and _res.VERSION_NAME in line:
            line = _change_version_props(line, version_properties.new_version_name, _res.VERSION_NAME)
            sys.stdout.write(line)
            continue

        sys.stdout.write(line)


# will set and get the current version of the project
def _change_version_props(line, new_version, version_name):
    # set the right version name or version code, if required
    line_without_version = re.sub('[.0-9"+]', '', line).replace('\n', '').rstrip()

    if new_version != VersionProperties.KEEP_OLD_VERSION and version_name in line:

        # if raise version by one
        if new_version == VersionProperties.RAISE_VERSION_BY_ONE:
            curr_version = re.sub('[a-zA-Z" +]', '', line).replace('\n', '')
            if '.' not in curr_version:
                curr_version = int(curr_version) + 1
            else:
                version = curr_version.split('.')
                version[-1] = str(int(version[-1]) + 1)
                curr_version = '.'.join(version)
            if version_name == _res.VERSION_NAME:
                curr_version = f'"{curr_version}"'
            return f'{line_without_version} {curr_version}\n'
        else:
            if version_name == _res.VERSION_NAME:
                new_version = f'"{new_version}"'
            return f'{line_without_version} {new_version}\n'
