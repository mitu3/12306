dict = {'k7727': ['k7727', '--', '--', '--', '有', '有', '--', '26000K772633', 'BXP', 'TJP', '00:42', '02:33', '01:51', 'y2rCRwR%2B9MRLF%2B6tuQOLw1pN1hfgLhr9Bo%2BKySi2G%2BvYoKlRjJw58Za%2FyNo%3D'],
 '2601': ['2601', '--', '--', '2', '有', '有', '--', '280000260414', 'BJP', 'TJP', '04:41', '06:52', '02:11', '2dnMBI%2FNh8bWfHwsoS6wfe2PiA7OYHR1AJ0%2FLX8ambNDYmfHFDWDqe7PCQM%3D'],
 'c2001': ['c2001', '有', '有', '--', '--', '--', '--', '24000C20010M', 'VNP', 'TJP', '06:01', '06:36', '00:35', 'E8oWMdWVi4K5STt%2B2Fkrz1HwkHHMedtZYKEuRZJDgB0LTBtbtZMM1xDGbnI%3D'],
 'c2003': ['c2003', '13', '有', '--', '--', '--', '--', '24000C20030G', 'VNP', 'TJP', '06:14', '06:49', '00:35', '2EsKPHt6rDjs4hjeXY3N%2B169pQkd3lGp19c7fdkQJIQGlQGCyCiz8rbIXRE0za%2BRV5sGmDqGfBc%3D']}

def returnxpath():

    for i in dict.values():

        for j in range(6):
            if i[j+1] != '--' :

                return i[7]

fff = returnxpath()
print(fff)

    # print(i)