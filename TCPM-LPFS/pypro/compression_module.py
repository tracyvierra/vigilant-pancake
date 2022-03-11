# Author: Tracy Vierra
# Date Created: 3/10/2022
# Date Modified: 3/10/2022

# Description: Compress or decompress a file.

# Usage: 

import zlib, base64

def compress(input_file, output_file):
	data = open(input_file, 'r').read()
	b_data = bytes(data, 'utf-8')
	compressed_data = base64.b64encode(zlib.compress(b_data,9))		
	compressed_file = open(output_file, 'w').write(compressed_data.decode('utf-8'))	
	return compressed_file

def decompress(input_file, output_file):
	compressed_data = open(input_file, 'r').read()
	decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
	decompressed_file = open(output_file, 'w').write(decompressed_data.decode('utf-8'))
	return decompressed_file


# print("1. Compress file ")
# print("2. Decompress file ")
# print("3. Exit ")

# mode = input("Enter 1, 2, or 3: ")

# if mode == "1":
# 	input_file = input("Enter the name of the file to compress: ")
# 	output_file = input("Enter the name of the file to save the compressed data: ")
# 	compressed_file = compress(input_file, output_file)
# 	print("Compressed file: ", compressed_file)
# elif mode == "2":
# 	input_file = input("Enter the name of the file to decompress: ")
# 	output_file = input("Enter the name of the file to save the decompressed data: ")
# 	decompressed_file = decompress(input_file, output_file)
# 	print("Decompressed file: ", decompressed_file)
# elif mode == "3":
# 	print("Exiting")
# 	exit()
# else:
# 	print("Invalid input")
# 	exit()




