# Picked a fairly arbitrary square of data, aiming for a good patch of ocean. Each row is 3,333 entries long and we want to get a (n x n) region from here where n is a power-of-two + 1 (in order to work with Unity's terrain system)
dataset_path = "C:\\Users\\danie\\Govhack2019\\Python Scripts\\gbr30_all_water_roi.txt" # Generated from filter_reef_data_longlat
f = open(dataset_path)
fw = open("C:\\Users\\danie\\Govhack2019\\Python Scripts\\gbr30_water_nxn.txt", 'w')

column_iter = 0
row_iter = 0

stride = 6667 # Width of row in the hand-picked ROI
n = 12 # Exponent to raise 2 to
n_width = pow(2, n)

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
      
    
