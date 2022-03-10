# Author: Tracy Vierra
# Date Created: 3/10/2022
# Date Modified: 3/10/2022

# Description:

# Usage:
import zlib, base64



data = open("demo.txt", 'r').read()
print(data)
b_data = bytes(data, 'utf-8')
compressed_data = base64.b64encode(zlib.compress(b_data,9))		
print(compressed_data)
compressed_file = open("compressed.txt", 'w').write(compressed_data.decode('utf-8'))	
print(compressed_file)



