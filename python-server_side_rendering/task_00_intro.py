#!/usr/bin/python3
"""
Module task_00_intro
Generates personalized invitation files from a template and attendees list.
"""


def generate_invitations(template, attendees):
    """
    Generates invitation files for each attendee based on a template.

    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries containing attendee details.
    """
    # Verify input types
    if not isinstance(template, str):
        print(f"Invalid input type: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Invalid input type: attendees must be a list of dictionaries, got {type(attendees).__name__}.")
        return

    # Check for empty template
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Keys to replace in the template
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))

        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
