import csv
import itertools

def build_csv(lines, header=None, file=None):
    """
    Write parsed lines to csv file
    
    Args:
    lines(iterable): iterable containing the data to write 
    header(list): list of header for the file 
    file(object): a file-like object
    
    Return:
    file(object): file object containing the written lines
    """
    if header:
        lines = itertools.chain([header], lines)   # combine header with the rest of data 
    writer = csv.writer(file, delimiter=',')
    writer.writerows(lines)   # write the data to file 
    file.seek(0)              # redirect pointer to first line
    return file
