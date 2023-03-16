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
    src_path = os.getcwd() 
    dir_path = src_path + "/raw"
    out_path = src_path + "/clean"
    try:
        for filename in os.listdir(dir_path):
            name = filename[:-5]
            src_file = os.path.join(dir_path, filename)
            src = open(src_file, "r")
            data = src.read()
            src.close()
            if not os.path.exists(out_path):
                os.makedirs(out_path)
            out_file = os.path.join(out_path, f"{name}.txt")
            out = open(out_file, "w")
            out.write(h.handle(data))
            out.close 
    except Exception as e: 
        logging.error(e)
        logging.error(dir_path)
        logging.error(out_path)
        
    return None

if __name__ == "__main__":
    h = config()
    etl(h)     
        
        