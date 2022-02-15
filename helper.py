def transform_user_input_for_openai(user_input):
    standard_starting_instructions = "\"\"\"\nPython3\n"
    transformed_user_input = f"{user_input}\n\"\"\""

    return standard_starting_instructions + transformed_user_input