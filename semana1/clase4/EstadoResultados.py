# pedir ingresos 
ingresos = float(input('Porfavor digite los ingresos de la empresa: '))
# pedir costos
costos = float(input('Porfavor digite los costos de la empresa: '))
# calcular utilidad bruta ingresos - costos
utilidadBruta = ingresos-costos
print(f'La utilidad bruta de la empresa es $ {utilidadBruta} pesos')

# pedir gastos
gastos = float(input('Porfavor digite los gastos de la empresa: '))
# calcular utilidad operativa  bruta - gastos
utilidadOperativa = utilidadBruta - gastos
print(f'La utilidad operativa de la empresa es $ {utilidadOperativa} pesos')
# calcular impuesto a la renta (operativa * 30%)
impuestoRenta = utilidadOperativa * 30 / 100
print(f'impuesto Renta que debe pagar la empresa es $ {impuestoRenta} pesos')
# calcular utilidad neta (utilidad brutal - impuesto a la renta)
utilidadNeta = utilidadOperativa - impuestoRenta 
print(f'La utilidad Neta de la empresa es $ {utilidadNeta} pesos')