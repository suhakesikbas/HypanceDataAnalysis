# import pandas as pd
# import numpy as np
# 
# class ATR:
#    
#     def __init__(self, data_all):
#         self.data_all = data_all
#       
# 
#     def AverageTrueRange(self):
#    
#         #First calculating true ranges. Substarcting high,low and close values.
#         #data_all=np.array([data_close,data_high,data_low])
#         TR=[abs(data_all[1][0]-data_all[2][0])]            
#         for i in range(1,30):
#             TR.append(max(abs(data_all[0][i-1]-data_all[1][i]),
#                          abs(data_all[0][i-1]-data_all[2][i]),
#                          abs(data_all[1][i]-data_all[2][i])))
#         
#         At the end  we calculating avarage ture ranges.
#         ATR=[]
#         ATR.append(np.mean(TR[0:14]))
#         for i in range(16):
#             ATR.append((ATR[i]*13+TR[i+14])/14)
#      
#         return ATR
