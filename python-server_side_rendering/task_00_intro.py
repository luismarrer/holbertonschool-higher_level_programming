import os

def generate_invitations(template, attendees):
    # Verificar que el template sea una cadena
    if not isinstance(template, str):
        print("Error: El template no es una cadena.")
        return

    # Verificar que attendees sea una lista de diccionarios
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Los datos de los asistentes no son una lista de diccionarios.")
        return

    # Verificar si el template está vacío
    if not template.strip():
        print("Error: El template está vacío, no se generaron archivos de salida.")
        return

    # Verificar si la lista de attendees está vacía
    if not attendees:
        print("No se proporcionaron datos, no se generaron archivos de salida.")
        return

    for index, attendee in enumerate(attendees):
        # Reemplazar los valores en el template
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Escribir la invitación en un archivo de salida
        output_filename = f"output_{index + 1}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)

        print(f"Archivo generado: {output_filename}")

# Fin del archivo task_00_intro.py

