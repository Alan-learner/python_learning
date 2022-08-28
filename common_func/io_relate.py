import os
from common_func.time_relate import get_time_stamp


def get_timed_file_path(dir_name, file_name: str):
    time_stamp = get_time_stamp()
    if "." in file_name:
        name_list = file_name.split(".")
        name_list.insert(-1, time_stamp)
        name_list.insert(-1, ".")
        timed_file_name = "".join(name_list)
    else:
        timed_file_name = file_name + time_stamp
    path = os.path.join(dir_name, timed_file_name)
    return path
