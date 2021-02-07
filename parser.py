def parse_obj_file(file):
    ignored = 0
    for line in file.split("\n"):
        if line[0] != "v" and line[0] != "f":
            ignored += 1

    return ignored