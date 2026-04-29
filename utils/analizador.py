def analizar(df, resultados):

    total = len(resultados)

    altos = resultados.count("Alto")
    medios = resultados.count("Medio")
    bajos = resultados.count("Bajo")

    resumen = {
        "total": total,
        "altos": altos,
        "medios": medios,
        "bajos": bajos
    }

    recomendaciones = []

    # 🔴 Problemas detectados
    if df['Horas_Sueno'].mean() < 7:
        recomendaciones.append("Los estudiantes duermen poco. Mejorar horas de sueño.")

    if df['Horas_Estudio_Semanal'].mean() < 5:
        recomendaciones.append("Pocas horas de estudio. Aumentar tiempo de estudio.")

    if df['Alimentacion_Adecuada'].mean() < 0.5:
        recomendaciones.append("Mala alimentación detectada. Mejorar hábitos alimenticios.")

    if bajos > altos:
        recomendaciones.append("Hay muchos estudiantes con bajo rendimiento. Reforzar enseñanza.")

    return resumen, recomendaciones