import os
import zipfile
# MAKE a function to Zip files
def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])

date=input("enter date: yyyymmdd: ")    
path2 = "C:/python_work/sample/3line Card management Limited_"
path3="_155959"
src_folder2=f"{path2}{date}{path3}"
#dst_folder = f'C:/python_work/sample/3line Card management Limited_{date}_155959/ '
print(src_folder2)

#make a list of the content of the source path 
file_names = os.listdir(src_folder2.strip(" "))                
zip_directory(f'{src_folder2}', f'{src_folder2}.zip')


  
path2 = "C:/python_work/sample/9 Payment Service Bank_"
path3="_155959"
src_folder2=f"{path2}{date}{path3}"
#dst_folder = f'C:/python_work/sample/3line Card management Limited_{date}_155959/ '
print(src_folder2)

#make a list of the content of the source path 
file_names = os.listdir(src_folder2.strip(" "))                
zip_directory(f'{src_folder2}', f'{src_folder2}.zip')


path2 = "C:/python_work/sample/AB Microfinance bank_"
path3="_155959"
src_folder2=f"{path2}{date}{path3}"
#dst_folder = f'C:/python_work/sample/3line Card management Limited_{date}_155959/ '
print(src_folder2)

#make a list of the content of the source path 
file_names = os.listdir(src_folder2.strip(" "))                
zip_directory(f'{src_folder2}', f'{src_folder2}.zip')