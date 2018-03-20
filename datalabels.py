import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def kharif(rf):
	khar=(rf['June']+rf['July']+rf['August']+rf['September'])/4
	return khar
def wholeyear(rf):
	wy=(rf.sum(axis=1))/12
	return wy
# def tkharif(t):
# 	tk=(t['June']+t['July']+t['August']+t['September']+t['October'])/5
# 	return tk

def rabi(val):
	tr = (val['October']+val['November']+val['December']+val['January']+val['February'])/5
	return tr

cropdata = pd.read_excel(io='/home/sumit/finalyearproject/data/CropProject.xlsx', sheetname='crop_data')

# cropdata = pd.ExcelFile("/home/sumit/finalyearproject/data/CropProject.csv")

# -tempdata = pd.ExcelFile("/home/sumit/finalyearproject/data/temperature.xlsx")
tempnagapattinam=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='nagapattinam')
temppudukkottai=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='pudukkottai')
tempramanathapuram=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='ramanathapuram')
tempsivaganga=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='sivaganga')
tempthanjavur=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='thanjavur')
temptiruvallur=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='tiruvallur')
temptiruvarur=pd.read_excel(io='/home/sumit/finalyearproject/data/temperature.xlsx',sheetname='tiruvarur')

pressnagapattinam=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='nagapattinam')
presspudukkottai=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='pudukkottai')
pressramanathapuram=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='ramanathapuram')
presssivaganga=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='sivaganga')
pressthanjavur=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='thanjavur')
presstiruvallur=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='tiruvallur')
presstiruvarur=pd.read_excel(io='/home/sumit/finalyearproject/data/pressure.xlsx',sheetname='tiruvarur')

rfnagapattinam=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='nagapattinam')
rfpudukkottai=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='pudukkottai')
rframanathapuram=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='ramanathapuram')
rfsivaganga=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='sivaganga')
rfthanjavur=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='thanjavur')
rftiruvallur=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='tiruvallur')
rftiruvarur=pd.read_excel(io='/home/sumit/finalyearproject/data/rainfall.xlsx',sheetname='tiruvarur')

kharnagapattinam_rainfall=kharif(rfnagapattinam)
kharpudukkottai_rainfall=kharif(rfpudukkottai)
kharramanathapuram_rainfall=kharif(rframanathapuram)
kharsivaganga_rainfall=kharif(rfsivaganga)
kharthanjavur_rainfall=kharif(rfthanjavur)
khartiruvallur_rainfall=kharif(rftiruvallur)
khartiruvarur_rainfall=kharif(rftiruvarur)

wynagapattinam_rainfall=wholeyear(rfnagapattinam)
wypudukkottai_rainfall=wholeyear(rfpudukkottai)
wyramanathapuram_rainfall=wholeyear(rframanathapuram)
wysivaganga_rainfall=wholeyear(rfsivaganga)
wythanjavur_rainfall=wholeyear(rfthanjavur)
wytiruvallur_rainfall=wholeyear(rftiruvallur)
wytiruvarur_rainfall=wholeyear(rftiruvarur)

rbnagapattinam_rainfall=rabi(rfnagapattinam)
rbpudukkottai_rainfall=rabi(rfpudukkottai)
rbramanathapuram_rainfall=rabi(rframanathapuram)
rbsivaganga_rainfall=rabi(rfsivaganga)
rbthanjavur_rainfall=rabi(rfthanjavur)
rbtiruvallur_rainfall=rabi(rftiruvallur)
rbtiruvarur_rainfall=rabi(rftiruvarur)



kharnagapattinam_temp=kharif(tempnagapattinam)
kharpudukkottai_temp=kharif(temppudukkottai)
kharramanathapuram_temp=kharif(tempramanathapuram)
kharsivaganga_temp=kharif(tempsivaganga)
kharthanjavur_temp=kharif(tempthanjavur)
khartiruvallur_temp=kharif(temptiruvallur)
khartiruvarur_temp=kharif(temptiruvarur)

wynagapattinam_temp=wholeyear(tempnagapattinam)
wypudukkottai_temp=wholeyear(temppudukkottai)
wyramanathapuram_temp=wholeyear(tempramanathapuram)
wysivaganga_temp=wholeyear(tempsivaganga)
wythanjavur_temp=wholeyear(tempthanjavur)
wytiruvallur_temp=wholeyear(temptiruvallur)
wytiruvarur_temp=wholeyear(temptiruvarur)

rbnagapattinam_temp=rabi(tempnagapattinam)
rbpudukkottai_temp=rabi(temppudukkottai)
rbramanathapuram_temp=rabi(tempramanathapuram)
rbsivaganga_temp=rabi(tempsivaganga)
rbthanjavur_temp=rabi(tempthanjavur)
rbtiruvallur_temp=rabi(temptiruvallur)
rbtiruvarur_temp=rabi(temptiruvarur)

print kharpudukkottai_temp, wypudukkottai_temp, rbpudukkottai_temp

kharnagapattinam_press=kharif(pressnagapattinam)
kharpudukkottai_press=kharif(presspudukkottai)
kharramanathapuram_press=kharif(pressramanathapuram)
kharsivaganga_press=kharif(presssivaganga)
kharthanjavur_press=kharif(pressthanjavur)
khartiruvallur_press=kharif(presstiruvallur)
khartiruvarur_press=kharif(presstiruvarur)

wynagapattinam_press=wholeyear(pressnagapattinam)
wypudukkottai_press=wholeyear(presspudukkottai)
wyramanathapuram_press=wholeyear(pressramanathapuram)
wysivaganga_press=wholeyear(presssivaganga)
wythanjavur_press=wholeyear(pressthanjavur)
wytiruvallur_press=wholeyear(presstiruvallur)
wytiruvarur_press=wholeyear(presstiruvarur)

rbnagapattinam_press=rabi(pressnagapattinam)
rbpudukkottai_press=rabi(presspudukkottai)
rbramanathapuram_press=rabi(pressramanathapuram)
rbsivaganga_press=rabi(presssivaganga)
rbthanjavur_press=rabi(pressthanjavur)
rbtiruvallur_press=rabi(presstiruvallur)
rbtiruvarur_press=rabi(presstiruvarur)