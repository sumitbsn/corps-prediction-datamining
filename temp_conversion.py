from datalabels import *
import xlsxwriter
import pandas as pd

np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_colwidth', -1)
labels=['1','2','3','4','5']
months=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
#months=['January','February','March','April','May','June','July','August','September','October','November','December']
temp=np.ravel(np.array([tempnagapattinam.values,temppudukkottai.values,tempramanathapuram.values,tempsivaganga.values,tempthanjavur.values,temptiruvallur.values,temptiruvarur.values]))


temp=pd.cut(temp,5,right=False,labels=labels)
# print temp
temp3=[]
j=0
for k in range(7):
	temp2=[]
	for i in range(16):
		temp2.append(temp[j:j+12])
		j+=12
	temp3.append(temp2)
# print temp3[0]

dic1 = {'k':temp3[0]}
# print dic1
# print temp3[0][0]
# print dic1
# tempnagapattinam=pd.DataFrame(temp3[0], columns=months)
# tempnagapattinam=pd.DataFrame(temp3[0])
# print tempnagapattinam
# temppudukkottai=pd.DataFrame(temp3[1],columns=months)
# tempramanathapuram=pd.DataFrame(temp3[2],columns=months)
# tempsivaganga=pd.DataFrame(temp3[3],columns=months)
# tempthanjavur=pd.DataFrame(temp3[4],columns=months)
# temptiruvallur=pd.DataFrame(temp3[5],columns=months)
# temptiruvarur=pd.DataFrame(temp3[6],columns=months)

writer = pd.ExcelWriter('/home/sumit/finalyearproject/data/temperature_labels.xlsx')

tempnagapattinam.to_excel(writer,'Nagapattinam')
# temppudukkottai.to_excel(writer,'Pudukkottai')
# tempramanathapuram.to_excel(writer,'Ramanathapuram')
# tempsivaganga.to_excel(writer,'Sivaganga')
# tempthanjavur.to_excel(writer,'Thanjavur')
# temptiruvallur.to_excel(writer,'Tiruvallur')
# temptiruvarur.to_excel(writer,'Tiruvarur')

# temp=np.sort(temp)
# tempstd=np.std(temp)
# tempmean=np.mean(temp)
# tempmedian=np.median(temp)
# print temp
# print tempmean
# print tempstd
# print tempstd**2/len(temp)
# print tempmedian
# workbook = xlsxwriter.Workbook('/home/sumit/finalyearproject/data/temperature_labels.xlsx')
# worksheet = workbook.add_worksheet()

# # Widen the first column to make the text clearer.
# # worksheet.set_column('A:A', 20)
# worksheet = worksheet.add_worksheet('Test')
# # Add a bold format to use to highlight cells.
# # bold = workbook.add_format({'bold': True})
# worksheet.write('A1', 'temp3[0]')