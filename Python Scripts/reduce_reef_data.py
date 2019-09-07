# Trying to remove irrelevant land data from the following dataset: https://data.gov.au/dataset/ds-ga-0f4e635c-81ec-46d0-9c99-65e5fe0b8c01/details?q=bathymetry%20great%20barrier%20reef (ASCII xyz files)
# A lot of the entries in the data set had negative depths, which seems to correspond to points on land, not water
# So we will filter out the data set to only include positive depths, because we are only concerned with ocean data
# We reduced the ~42GB dataset to about half using this script

dataset_path = "D:\\Downloads\\115066_ASCII_XYZ\\01_ASCII_XYZ\\gbr30_all1.txt"
output_path = "D:\\Downloads\\115066_ASCII_XYZ\\01_ASCII_XYZ\\gbr30_all_water_only.txt"
f = open(dataset_path)
fw = open(output_path, 'w')

num_read = 0

f.seek(28) # Skip the header (Lat, Long, Depth)


for line in f:
     line_split = (line.split(',')) # Lat, Long, Depth
     num_read += 1
     depth = line_split[2]
     if float(depth) > 0: # Only keep the values width a depth greater than zero
        fw.write(line)

     if num_read % 100000 == 0: # Print progress
        print(num_read)

    
