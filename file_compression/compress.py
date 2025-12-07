import zlib

data = open('files\demo.txt','r').read() 
data_types = bytes(data,'utf-8')
compressed_file = zlib.compress(data_types)
print(compressed_file)

