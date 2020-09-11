import os
from math import ceil
from os import listdir, mkdir
from os.path import isfile, isdir, join

def split(file, outPath, chunkSize, namePrefix):
    """
        Split a file to multiple chunks.

        ---
        (Req) file          str     "./path/to/file"    Original file path.

        (Req) outPath       str     "./output/path"    

        (Req) chunkSize     int     512 (KiB)           Each chunk size.

        (Req) namePrefix    str     "JustPrefix"        Output chunk name prefix.
    """


    fileExist = isfile(file)
    chunkSize = chunkSize * 1024

    if(fileExist):
        chunks = ceil(os.stat(file).st_size / chunkSize)
        zeroLeadingLength = len(str(chunks))

        if(not isdir(outPath)):
            mkdir(outPath)

        with open(file, "rb") as f:
            for i in range(chunks):
                i = str(i).zfill(zeroLeadingLength)
                outputFilePath = f"{outPath}/{namePrefix}{i}"
                
                with open(outputFilePath, "wb") as of:
                    data = f.read(chunkSize)
                    of.write(data)
    else:
        print(f"File not found, check the file path is correct.\n\"{file}\"")
        return 0

split("./test/test.png", "./test/split", 32, "splited_")