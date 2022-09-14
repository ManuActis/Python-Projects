import os
images_extensions = [".jpg", ".jpeg", ".png"]
text_extensions = [".doc", ".txt", ".pdf"]

#Custom paths of my personal computer

downloads_folder = "\\Users\\Manuel\\Downloads\\"
images_folder = "\\Users\\Manuel\Desktop\\archivos\\imagenes\\"
text_files_folder = "\\Users\\Manuel\\Desktop\\archivos\\documentos-texto\\"
others_folder = "\\Users\\Manuel\\Desktop\\archivos\\otros\\"

#os.chdir(downloads_folder)
#print(f"""current dir is: {os.getcwd}""")

for filename in os.listdir(downloads_folder):
    try:
        name, extension = os.path.splitext(downloads_folder + filename)

        if extension in images_extensions:
            os.rename(downloads_folder + filename, images_folder + filename)
            print(f"{filename} moved to images")

        elif extension in text_extensions:
            os.rename(downloads_folder + filename, text_files_folder + filename)
            print(f"{filename} moved to text")

        else:
            os.rename(downloads_folder + filename, others_folder + filename)
            print(f"{filename} moved to others")

        
    except FileNotFoundError as e:
        print(f"{filename} was not found")