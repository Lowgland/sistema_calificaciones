def sistema_calificaciones():
    print("\n =====SISTEMA DE CALIFICACIONES ESCOLARES=====")
    estudiantes=int(input("ingrese el numero de estudiantes a registrar: "))
    materias=int(input("ingrese el numero de materias a registrar: "))
    calificaciones=[]
   
    for i in range(estudiantes):
        fila=[]
        print(f"ingresa las calificaciones del estudiante {i+1}: ")
        for j in range(materias):
            cal=float(input(f"calificacion de la materia {j+1}: "))
            fila.append(cal)
        calificaciones.append(fila)

    print("\n ===PROMEDIO POR ESTUDIANTE===")
    for i in range(estudiantes):
        promedio=sum(calificaciones[i])/materias
        print(f"el promedio del estudiante {i+1} es: {promedio:.2f}")

    print("\n =====PROMEDIO POR MATERIA=====")
    for j in range(materias):
        suma=0
        for i in range(estudiantes):
            suma += calificaciones[i][j]
        promedio=suma/estudiantes
        print(f"la califcacion de la materia {j+1} es: {promedio:.2f}")

    total=[cal for fila in calificaciones for cal in fila]
    calificacion_alta=max(total)
    calificacion_baja=min(total)
    print("Estadisticas generales: ")
    print(f"Calificacion mas alta: {calificacion_alta}")
    print(f"Calificacion mas baja: {calificacion_baja}")
sistema_calificaciones()
