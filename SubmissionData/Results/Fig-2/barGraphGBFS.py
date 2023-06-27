
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import random
from matplotlib.lines import Line2D



# fig, ax = plt.subplots()
figure(figsize=(6, 3.5), dpi=80)
# We change the fontsize of minor ticks label 


xtickVal = np.arange(0, 49, step=6)
xtickLabel = []
j = 0

for i in xtickVal:
    if i < 48:
        xtickLabel.append(str(j))
        j +=3
xtickLabel.append(str(23))


plt.xticks(xtickVal, xtickLabel,
       rotation=0)
x2 =  [44, 48, 48, 49, 48, 50, 51, 54, 80, 81, 81, 81, 82, 84, 84, 86, 92, 90, 94, 92, 91, 93, 90, 92, 96, 99, 106, 114, 110, 114, 122, 127, 142, 153, 144, 159, 170, 186, 193, 202, 213, 230, 241, 258, 270, 280, 282, 297]

plt.plot(x2, color = 'r', linewidth=4)



x2 = [46, 47, 47, 51, 48, 52, 54, 56, 82, 81, 84, 85, 86, 83, 86, 89, 97, 92, 93, 94, 95, 96, 95, 96, 99, 102, 108, 117, 115, 120, 122, 127, 150, 160, 144, 167, 172, 192, 197, 213, 212, 228, 249, 265, 281, 287, 279, 299]

plt.plot(x2, color = 'k',  linestyle = '-.',linewidth=2, alpha=1)




x2 = [1336, 1376, 1344, 1320, 1352, 1368, 1328, 1304, 808, 936, 1008, 1064, 1080, 1120, 1152, 1136, 1104, 1112, 1120, 1128, 1144, 1168, 1184, 1200, 1208, 1224, 1256, 1280, 1312, 1352, 1400, 1424, 1440, 1472, 1488, 1528, 1576, 1640, 1704, 1776, 1840, 1920, 2032, 2120, 2312, 2496, 2520, 2656]

plt.plot(x2, color = 'pink', linewidth=4)

x2 = [1362, 1408, 1357, 1325, 1368, 1385, 1363, 1295, 812, 952, 1032, 1056, 1089, 1134, 1154, 1125, 1102, 1142, 1145, 1140, 1171, 1197, 1202, 1217, 1221, 1216, 1254, 1302, 1344, 1366, 1434, 1439, 1439, 1478, 1485, 1556, 1618, 1657, 1708, 1826, 1866, 1953, 2057, 2140, 2357, 2509, 2563, 2638]

plt.plot(x2, color = 'k',  linestyle = '-.',linewidth=2, alpha=1)


x2 = [53, 53, 54, 58, 67, 101, 0, 19, 46, 46, 46, 45, 45, 45, 46, 47, 46, 47, 49, 50, 49, 50, 48, 49, 51, 51, 53, 56, 55, 56, 58, 59, 65, 67, 64, 67, 68, 73, 71, 73, 74, 79, 79, 82, 88, 98, 118, 186]

plt.plot(x2, color = 'g', linewidth=4)

x2 = [65, 71, 66, 69, 71, 116, 0, 19, 47, 52, 46, 60, 49, 49, 58, 51, 50, 56, 53, 70, 50, 66, 48, 56, 60, 53, 54, 75, 75, 66, 69, 79, 80, 69, 84, 88, 90, 79, 86, 97, 104, 85, 103, 94, 97, 124, 133, 260]

plt.plot(x2, color = 'k', linestyle = '-.',linewidth=2, alpha=1)



x2 =[814, 781, 806, 806, 756, 730, 747, 764, 747, 840, 865, 898, 932, 915, 890, 882, 873, 882, 873, 865, 856, 856, 856, 856, 865, 865, 873, 882, 898, 890, 873, 873, 856, 856, 865, 873, 882, 898, 890, 907, 932, 932, 999, 1033, 1041, 1167, 1369, 1344]


plt.plot(x2, color = 'olive', linewidth=4)

x2 = [807, 806, 835, 837, 756, 759, 759, 778, 750, 872, 906, 906, 938, 943, 922, 913, 873, 924, 884, 874, 876, 874, 867, 856, 899, 904, 872, 916, 918, 930, 867, 904, 851, 879, 899, 875, 924, 904, 894, 917, 930, 931, 1011, 1054, 1086, 1217, 1403, 1391]

plt.plot(x2, color = 'k', linestyle = '-.',linewidth=2, alpha=1)



l1 = Line2D([0], [0], label='WDC: June 25, 2019', lw=2, color='r')
l2 = Line2D([0], [0], label='DTW: June 25, 2019', color='g')
l3 = Line2D([0], [0], label='WDC:  March 20, 2021', color='pink')
l4 = Line2D([0], [0], label='DTW: March 20, 2021', color='olive')
l5 = Line2D([0], [0], label='Provider API', color='k',linestyle = '-.')


plt.tick_params(axis='both', which='major', labelsize=14)


handles, labels = plt.gca().get_legend_handles_labels()

handles.extend([l1,l2,l3,l4,l5])
plt.legend(handles=handles, fontsize=14)

plt.title("Introduced methods VS provider supply APIs", size=15)

plt.xlabel('Hours of the day', size=15)
plt.ylabel('Number of DES', size=15)

plt.savefig('barGrphGBFS.png', bbox_inches='tight')
plt.savefig('barGrphGBFS.eps', bbox_inches='tight')
