# -*- coding: utf-8 -*-
"""
@author: luiggi
"""

import os 
import shutil
   
# Select the Path you want to Sort and where you want to sort it
path = 'Path/To/Sort/It/To'
inputpath = 'From/Where/To/Sort'

# List all Things in the input dir
list_ = os.listdir(inputpath) 

# go thru every file in the list
for file_ in list_:
    
    # splicing to extract the type of the file
    name, ext = os.path.splitext(file_) 
  
    ext = ext[1:] 
    
#   Skipping if invalid
    if ext == '': 
        continue
    
#   Skipping if the file to sort is a directory
    if os.path.isdir(path + '/' + file_):
        list_.remove(file_)
        print( file_ + " didnt get moved because its a directory.")
        continue        
        
#   if a folder already exists, move it
    if os.path.exists(path+'/'+ext): 
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
        print(name + " got moved to " + path+'/'+ext+'/'+file_)
    
#   if a folder doesnt exists, create it and then move it
    else: 
        os.makedirs(path+'/'+ext) 
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 
        print(name + " got moved to " + path+'/'+ext+'/'+file_)
