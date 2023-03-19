def config():
    import html2text 
    h = html2text.HTML2Text()
    h.ignore_images = True 
    h.ignore_images = True 
    h.ignore_links = True
    return h
    
def etl(h):
    import os 
    import logging
    import pathlib
    src_path = os.getcwd() 
    dir_path = src_path + "/raw"
    try:
        for path, subdirs, files in os.walk(dir_path):
            for name in files:
                out_path = path.replace("/raw", "/clear")
                src_file = pathlib.PurePath(path, name)
                src = open(src_file, "r")
                data = src.read()
                src.close()
                # print(out_path)
                if not os.path.exists(out_path):
                    os.makedirs(out_path)
                out_file = os.path.join(out_path, f"{name}.txt")
                out = open(out_file, "w")
                out.write(h.handle(data))
                out.close()
    except Exception as e: 
        logging.error(e)        
    return None

if __name__ == "__main__":
    h = config()
    etl(h)     
        
        