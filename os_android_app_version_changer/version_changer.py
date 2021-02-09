from os_android_app_version_changer.bp import _bp


###########################################################################
# this module meant to change the version code and version name of an app #
###########################################################################

def change_version(project_path, version_properties):
    """
    Will change the project's app's version and name.

    Args:
        project_path: the path to your android app's project
        version_properties: an instance which holds the properties of your desired name and version
    """

    _bp.change_version(project_path, version_properties)
