from Covid19.src.covid19_kr import CovidInfokr

class ThrowInfo:
    def __init__(self):
        self.infotron = CovidInfokr()
        
    def unroll_data(self, datarr):
        datarr = datarr.split('|')
        # increase, patients, deceased, inspection, ratio
        return tuple(datarr)
    
    def csv_data(self):
        fieldnames, fieldvalues = self.infotron.read_csv_data()
        return fieldnames, fieldvalues
        
        
    def parse_data(self):
        fieldnames, fieldvalues = self.csv_data()
        
        keys = ['City', 'Increase from day before', 'Total Patients', 'Total Deceased', 'Under Inspection', 'Increase to Patient Ratio']
        
        datarray = [[datarr[0],*self.unroll_data(datarr[-1])] for datarr in fieldvalues]
        datarray.insert(0,keys)
        return datarray
