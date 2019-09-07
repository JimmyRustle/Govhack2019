# Filter data to a ROI from the following dataset: https://data.gov.au/dataset/ds-ga-0f4e635c-81ec-46d0-9c99-65e5fe0b8c01/details?q=bathymetry%20great%20barrier%20reef (ASCII xyz files)
# Specify a set of min and max lat long coords to filter it

dataset_path = "D:\\Downloads\\115066_ASCII_XYZ\\01_ASCII_XYZ\\gbr30_all1.txt"
output_path = "D:\\Downloads\\115066_ASCII_XYZ\\01_ASCII_XYZ\\gbr30_all_water_roi.txt"
f = open(dataset_path)
fw = open(output_path, 'w')

num_read = 0

f.seek(28) # Skip the header (Lat, Long, Depth)

min_long = 152
max_long = 153 # Exclusive
min_lat = -20
max_lat = -19
for line in f:
     line_split = (line.split(',')) # Lat, Long, Depth
     num_read += 1
     latitude = line_split[0]
     longitude = line_split[1]
     if float(longitude) >= min_long and float(longitude) < max_long:
        if float(latitude) >= min_lat and float(latitude) < max_lat:
           fw.write(line)

     if num_read % 100000 == 0: # Print progress, this script is time consuming
        print(num_read)

    
