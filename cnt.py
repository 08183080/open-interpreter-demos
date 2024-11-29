import os                                                                                                                                                                    
                                                                                                                                                                        
def list_files(directory):                                                                                                                                                   
    for root, dirs, files in os.walk(directory):                                                                                                                             
        for file in files:                                                                                                                                                   
            print(os.path.join(root, file))                                                                                                                                  
                                                                                                                                                                            
# 调用函数，遍历D盘                                                                                                                                                          
list_files('D:\\')      