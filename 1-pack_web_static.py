#!/usr/bin/python3
"""
    The following code block defines a function called 
    do_pack() that is responsible for creating a compressed archive file in the .tgz format. 
    This archive file is generated from the contents of the web_static folder present in an AirBnB Clone repository.

    All the files within the web_static folder must be added to the archive file,
    and it should be stored inside a folder called "versions". 
    The name of the archive file should be in the format "web_static_<year><month><day><hour><minute><second>.tgz",
    with the timestamp indicating the exact moment the archive was generated.

    The do_pack() function returns the path of the archive file if it has been generated successfully,
    and None otherwise.
"""
import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """Compresses the web_static folder into a .tgz archive"""
    try:
        day = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_N = "versions/web_static_{}.tgz".format(day)
        local("tar -czvf {} web_static".format(file_N))
        return file_N
    except FileNotFoundError:
        return None
