# -*- coding: <utf-8> -*-

import os
import zipfile
import datetime
import time


current_date = datetime.datetime.now()
cur_date = time.mktime(current_date.timetuple())

src_dir = "C:\\users\\admin\\onedrive\\"
#dest_file = "c:\\users\\admin\\google drive\\"+str(cur_date)+".zip"
dest_file = "C:\\users\\admin\\onedrive\\"+"backup_"+str(cur_date)+".zip"


def zipdir (src_path, zip_handle):

    for root, dirs, files in os.walk(src_path):
        print("Root: "+root)

        for file in files:
            
            print("File: "+str(file))

            #print("OS-Path-Join: "+str(os.path.join(root, file)))

            try:
                zip_handle.write(os.path.join(root, file))
                                
            except:
                print("ERROR")


if __name__ == '__main__':

    zipf = zipfile.ZipFile(dest_file, 'w', zipfile.ZIP_DEFLATED)
    zipdir(src_dir, zipf)
    zipf.close()








