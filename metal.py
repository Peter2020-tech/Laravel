import glob(pathname, *, recursive=False)


def get_content_of_file(file):   
    date = None
    
    with open(file, "r") as my_file:
        data = my_file.realines()