from Covid19.src.covid19_kr import CovidInfokr
from Covid19.src.covid19_wd import CovidInfowd

class ThrowInfo:
    def __init__(self):
        self.infotron = CovidInfokr()
        self.wdinfotron = CovidInfowd()
        
    def unroll_data(self, datarr):
        datarr = datarr.split('|')
        datarr = [int(float(dat)) for dat in datarr]
        # increase, patients, deceased, inspection, ratio
        return tuple(datarr)
    
    def csv_data(self):
        fieldnames, fieldvalues = self.infotron.read_csv_data()
        return fieldnames, fieldvalues
        
        
    def parse_data(self):
        fieldnames, fieldvalues = self.csv_data()
        datarray_chart = []
        keys = ['City', 'Increase from day before', 'Total Patients', 'Total Deceased', 'Under Inspection', 'Increase to Patient Ratio']
        
        datarray = [[datarr[0],*self.unroll_data(datarr[-1])] for datarr in fieldvalues]
        print(f"Current date's status of Covid19:\n{datarray}")
        datarray.insert(0,keys)
        datarray_all = datarray
        
        for cnt, ele in enumerate(datarray):
            try:
                if(cnt==0):
                    datarray_chart.append([ele[0],ele[2]])
                else:
                    datarray_chart.append([ele[0],int(float(ele[2]))])
            except ValueError:
                if(cnt==0):
                    datarray_chart.append([ele[0],ele[2]])
                else:
                    datarray_chart.append([ele[0],int(str(ele[2]))])
        
        return datarray_all, datarray_chart
