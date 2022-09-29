import pandas as pd

class CMF:
    def __init__(self,close,low,high,volume,data):
        self.close = close
        self.low = low
        self.high = high
        self.volume = volume
        self.data = data
        
    #1. Money Flow Multiplier = [(Close  -  Low) - (High - Close)] /(High - Low) 
    def money_flow_multiplier(close,low,high):
        mfm = ((close - low) - (high - close)) / (high - low)
        return mfm

    # 2. Money Flow Volume = Money Flow Multiplier x Volume for the Period
    def money_flow_volume(mfm, volume):
        mfv = mfm * volume
        return mfv
    
    # 3. 20-period CMF = 20-period Sum of Money Flow Volume / 20 period Sum of Volume 
<<<<<<< HEAD
    def cmf(money_flow_multiplier,money_flow_volume,data):
        result1 = money_flow_multiplier(data.loc[:,"Close"],data.loc[:,"Low"],data.loc[:,"High"])
        result2 = money_flow_volume(result1, data.loc[:, "Volume"])
        cmf = result2.rolling(window=20).sum() / data["Volume"].rolling(window=20).sum()
        return cmf
=======
    for i in range(20):
        result1 = money_flow_multiplier(data.loc[i,"Close"],data.loc[i,"Low"],data.loc[i,"High"])
        result2 = money_flow_volume(result1, data.loc[i, "Volume"])
        CMF = result2.sum() / data["Volume"].sum()
        print(CMF)
>>>>>>> 3278b0f31fd4884022cf1642d97495e643c3bbd2