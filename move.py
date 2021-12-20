import glob
import os
import shutil
import time
import zipfile
import logging
from shutil import copytree, rmtree

#get the unique variable to defferentiate date
date=input("enter date: yyyymmdd: ")    
"""path1 = "C:/python_work/folder_zip/Billingsample/Billingsample/"
#path2="_040219"""
path='C:/python_work/folder_zip/bank.txt'
try:
    with open(path, 'r') as file_object:
        lines=file_object.read()
        #print(lines)
        logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.warning(f'name \n{lines}, exist in {path}') 
except:
    print(f"The file does not exist in the location")
    logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.warning(f'The files named -bank.txt does not exist in the location:') 
    

else:
    contents1=lines.split('\n')
    print(contents1)
    
    for name in contents1[:]:
        print(name)
        add="_155959"
        destination=str(os.makedirs("C://python_work//folder_zip//output//"+ name+date+add))
        for file in os.listdir(f"C:/python_work/folder_zip/Billingsample/Billingsample/{date}"):
            if file.startswith(str(name)):
                print(file)
                src = f'C:/python_work/folder_zip/Billingsample/Billingsample/{date}/{file}'
                dst = "C://python_work//folder_zip//output//"+ name+date+add
                print(dst)
                shutil.copy2(src, dst)
                #os.rename("C://python_work//folder_zip//output//"+ name,"C://python_work//folder_zip//output//"+ name+date)
                logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.warning(f'The files patterns: Zipped soruce files is being moved to their individual Folders {dst}')
                #r"C://python_work//folder_zip//output//"
                #dst=str(os.makedirs("C://python_work//folder_zip//output//"+ name))
                


# function to Zip the directories
def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])  
#let zip 3line


path='C:/python_work/folder_zip/bank.txt'
try:
    with open(path, 'r') as file_object:
        lines=file_object.read()
        #print(lines)
except:
    print(f"The file does not exist in the location")

else:
    contents1=lines.split('\n')
    print(contents1)

    
    for name in contents1[:]:
       # pattern = name  
        path2 = "C://python_work//folder_zip//output//"+ name+date+add
        #path3="_155959"
        src_folder2=f"{path2}"
#dst_folder = f'C:/python_work/sample/3line Card management Limited_{date}_155959/ '
        print(src_folder2)

        logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.warning(f'The files patterns: {src_folder2} is being prepared for zipping')
        #make a list of the content of the source path 
        file_names = os.listdir(src_folder2)
        print(file_names)
        pattern = src_folder2
        dst_folder = pattern
        print(pattern)
        #loop through the list to move files with a unique pattern (src_folder + "/3*") to the destination path (3line)
        for file_name in file_names[:]:
            pattern=pattern
            #pattern = str(src_folder) + "/" + str({name}) + "/_*"
            
            for file in glob.iglob(pattern, recursive=True):
        # extract file name form file path
                file_name = os.path.basename(file)
                dst_folder = src_folder2

        file_names = os.listdir(src_folder2.strip(" "))                
        zip_directory(f'{src_folder2}', f'{dst_folder}.zip')
        logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.warning(f'The files patterns: {file_names} has been Zipped')

print(f"Moving zip files to Zip ...............")

zip_src = 'C:/python_work/folder_zip/output/'
zip_dst= 'C:/python_work/folder_zip/zip'


  
files_zip = glob.iglob(os.path.join(zip_src, "*.zip"))
for file_zip in files_zip:
    if os.path.isfile(file_zip):
        shutil.copy2(file_zip, zip_dst)
    print(file_zip)

    
       
        
    logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.warning(f'The files patterns: {file_zip} has been moved to {zip_dst}')
print(f'Done moving......')
                

      
           
