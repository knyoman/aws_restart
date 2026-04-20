import jsonFileHandler

# Membaca data dari file JSON
data = jsonFileHandler.readJsonFile('files/insulin.json')

if data != "":
    # Mengambil data molekul
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    
    # Menampilkan informasi dasar
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
    # --- Menghitung Berat Molekul ---
    
    # Mengambil daftar berat asam amino (AA)
    aaWeights = data['weights']
    
    # Menghitung jumlah setiap asam amino
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
    
    # Mengalikan jumlah dengan berat masing-masing
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
    
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    
    # Menghitung persentase error
    percentError = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
    print("Percent error: " + str(percentError))

else:
    print("Error. Exiting program")