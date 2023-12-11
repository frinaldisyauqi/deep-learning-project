import gdown
import os
import zipfile

dataset_path = "./dataset/"
output_path = "./output/"

try:  
    os.mkdir(dataset_path)  #Make directory for dataset
except OSError as error:  
    pass 

try:  
    os.mkdir(output_path)  #Make directory for output
except OSError as error:  
    pass

url = "https://drive.google.com/uc?id=1r1WdU8ToKdPPeWG_1yeRVJWhcuznLrEd"
output = dataset_path + 'dataset.zip'
gdown.cached_download(url, output, quiet=False)

with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall(dataset_path)
