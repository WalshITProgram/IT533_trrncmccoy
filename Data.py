import dbm 

file = dbm.open('movie', 'c')
file['Batman'] = 'Pow!'
file.keys()