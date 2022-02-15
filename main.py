import components

selected_temperature, selected_tokens = components.sidebar()
components.header()
user_input = components.user_instructions_input()
transformed_user_input = components.openai_code(user_input, selected_temperature, selected_tokens)
components.translated_instructions(transformed_user_input)