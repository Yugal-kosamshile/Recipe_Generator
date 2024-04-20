import openai

# Set your OpenAI API key
openai.api_key = 'add openai api key'

def generate_recipe(ingredients):
    if not ingredients:
        raise ValueError("Please provide at least one ingredient.")

    # Define the prompt
    prompt = f"Ingredients: {', '.join(ingredients)}\n\nRecipe:"

    try:
        # Generate the recipe using the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=150
        )
        # Extract and return the generated recipe from the API response
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    ingredients = ['chicken', 'broccoli', 'garlic', 'soy sauce', 'rice']
    try:
        recipe = generate_recipe(ingredients)
        if recipe:
            print("Generated Recipe:")
            print(recipe)
        else:
            print("Failed to generate recipe.")
    except ValueError as ve:
        print(ve)
