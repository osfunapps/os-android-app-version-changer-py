class VersionProperties:
    KEEP_OLD_VERSION = -1       # set to keep the old version
    RAISE_VERSION_BY_ONE = -2   # raise the version by one (if set in version name, will raise in a fraction)

    def __init__(self, new_version_code: int, new_version_name):
        """
        Create this instance in order to set the desired version code and name for the new release.
        NOTICE: each of this properties can also hold VersionProperties.KEEP_OLD_VERSION or VersionProperties.RAISE_VERSION_BY_ONE.

        Args:
          new_version_code: the version code to be placed in the build.gradle for the new release
          new_version_name: the version name to be placed in the build.gradle for the new release
        """
        self.new_version_code = new_version_code
        self.new_version_name = new_version_name
