import csv

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    with open('FB.csv',newline="") as fbFile:
        fbData = csv.reader(fbFile,delimiter=",")

        resultados = [["Fecha","Mean-Min-Max","Concepto"]]

        highest_mean = 0
        date_highest_mean = ''

        lowest_mean = 0
        date_lowest_mean= ''

        for index, row in enumerate(fbData):
            if index>0:

                highestPrice = float(row[2])
                lowestPrice= float(row[3])
                date = row[0]
                concepto = ''

                promedio = (highestPrice + lowestPrice)/2

                # conditional to initialize lowest_mean value
                if index < 2:
                    lowest_mean = promedio          
                    date_lowest_mean = date      
                
                if promedio < lowest_mean:
                    lowest_mean = promedio
                    date_lowest_mean = date


                if promedio > highest_mean:
                    highest_mean = promedio
                    date_highest_mean = date

                if promedio < 239:
                    concepto = 'MUY BAJO'
                    resultados.append([date,promedio,concepto])
                elif promedio >= 239 and promedio < 265:
                    concepto = 'BAJO'
                    resultados.append([date,promedio,concepto])
                elif promedio >= 265 and promedio < 291:
                    concepto = 'MEDIO'
                    resultados.append([date,promedio,concepto])
                elif promedio >= 291 and promedio < 317:
                    concepto = 'ALTO'
                    resultados.append([date,promedio,concepto])
                elif promedio >= 317:
                    concepto = 'MUY ALTO'
                    resultados.append([date,promedio,concepto])

                # print(f'{index} - {row}')

        with open('analisis_archivo.csv','w',newline="") as resultCSV:
            writer = csv.writer(resultCSV,delimiter="\t")
            for fila in resultados:
                writer.writerow(fila)

    print(f'date_lowest_mean: {date_lowest_mean} - lowest_mean {lowest_mean}')
    print(f'date_highest_mean: {date_highest_mean} - highest_mean {highest_mean}')
    
    return date_lowest_mean, lowest_mean, date_highest_mean, highest_mean

solucion()
