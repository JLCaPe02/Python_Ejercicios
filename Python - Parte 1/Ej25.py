'''La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
control switch).'''

nombre = input('Introduzca el nombre del postulante ')
uni = input('¿En qué universidad va a estudiar? ').lower()
IGV = 0
mensualidad = 0
importe = 0
monto_final = 0

match(uni):
    case 'ingenieria de sistemas':
        importe = 350
        mensualidad = 650
        IGV = 0.18 * (importe + mensualidad)
        monto_final = importe + mensualidad + IGV

    case 'derecho':
        importe = 300
        mensualidad = 550
        IGV = 0.18 * (importe + mensualidad)
        monto_final = importe + mensualidad + IGV

    case 'ingenieria naviera':
        importe = 300
        mensualidad = 500
        IGV = 0.18 * (importe + mensualidad)
        monto_final = importe + mensualidad + IGV

    case 'ingenieria pesquera':
        importe = 310
        mensualidad = 460
        IGV = 0.18 * (importe + mensualidad)
        monto_final = importe + mensualidad + IGV

    case 'contabilidad':
        importe = 280
        mensualidad = 490
        IGV = 0.18 * (importe + mensualidad)
        monto_final = importe + mensualidad + IGV

    case 'administración':
        importe = 360
        mensualidad = 520
        IGV = 0.18 * (importe + mensualidad)
        monto_final = importe + mensualidad + IGV

print(f"{nombre}, su postulación a la universidad de {uni} contiene los siguientes gastos: \nImporte:{importe} euros\nMensualidad: {mensualidad}\nIGV: {IGV} euros sumados al monto final  \nMonto Final a pagar: {monto_final} euros")
