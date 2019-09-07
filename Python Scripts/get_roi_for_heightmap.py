# Picked a fairly arbitrary square of data, aiming for a good patch of ocean. Each row is 3,333 entries long and we want to get a (n x n) region from here where n is a power-of-two + 1 (in order to work with Unity's terrain system)
dataset_path = "D:\\Downloads\\115066_ASCII_XYZ\\01_ASCII_XYZ\\gbr30_all_water_roi.txt" # Generated from filter_reef_data_longlat
f = open(dataset_path)
fw = open("D:\\Downloads\\115066_ASCII_XYZ\\01_ASCII_XYZ\\gbr30_water_nxn.txt", 'w')

column_iter = 0
row_iter = 0

stride = 3333 # Width of row in the hand-picked ROI
n = 3 # Exponent to raise 2 to
n_width = pow(2, n) + 1
f.seek(16) # Skip header (lat, long, depth)

total = 0
for line in f:
    if row_iter == n_width:
        break
    if column_iter < n_width:
       line_split = line.split(',')
       total += 1
       fw.write(line_split[2].rstrip() + ',') # Depth
    column_iter += 1
    if column_iter == stride:
       column_iter = 0
       fw.write('\n')
       row_iter += 1

print(total)
f.close()
      
    
