import os
from send2trash import send2trash

raw_type = ".CR3" # change as required: uppercase ".CR2" ".CR3" ".NEF" ".DNG" etc.
compressed_type_1 = ".JPG" # change as required: uppercase ".PNG", ".HEIF", etc.
compressed_type_2 = ".JPEG" # change as required (as above). if no second spelling/type, keep as ".JPEG".

verbose = True # True prints name of every file deleted to console. False only prints number of files deleted.

# create list of all jpegs
def create_jpeg_list():
    jpeg_list = []
    for root, dirs, files in os.walk("./"):
        for file in files:
            if compressed_type_1 in file.upper() or compressed_type_2 in file.upper():
                jpeg_list.append(file)
    #print("jpeg_list = " + str(jpeg_list))
    return jpeg_list

# create list of all raws
def create_raw_list(raw_type):
    raw_list = []
    for root, dirs, files in os.walk("./"):
        for file in files:
            if raw_type in file.upper():
                raw_list.append(file)
    #print("raw_list = " + str(raw_list))
    return raw_list

# create list of raws with no jpeg counterpart
def create_culled_list(jpeg_list, raw_list, raw_type):
    #remove extension from all elements in raw_list
    blank_list = [(raw.upper()).replace(raw_type, "") for raw in raw_list]
    #print("blank_list = " + str(blank_list))
    blank_jpeg_list = [(jpeg.upper()).replace(compressed_type_1, "") for jpeg in jpeg_list]
    blank_jpeg_list = [(jpeg.upper()).replace(compressed_type_2, "") for jpeg in blank_jpeg_list]
    #print("blank_jpeg_list = " + str(blank_jpeg_list))
    blank_culled_list = [name for name in blank_list if name not in blank_jpeg_list]
    #print("blank_culled_list = " + str(blank_culled_list))
    culled_list = [name + raw_type for name in blank_culled_list]
    #print("culled_list = " + str(culled_list))
    return culled_list

#send elements in culled_list to recycle bin
def recycle(culled_list, verbosity):
    files_list = ["./" + file for file in culled_list]
    culled_counter = 0
    for file in files_list:
        send2trash(file)
        culled_counter += 1
        if verbosity == True:
            print(file + " was sent to trash.")
    print("Culling finished. " + str(culled_counter) + " Raw files were sent to trash.")

def main():
    jpeg_list = create_jpeg_list()
    raw_list = create_raw_list(raw_type)
    culled_list = create_culled_list(jpeg_list, raw_list, raw_type)
    recycle(culled_list, verbose)

main()
