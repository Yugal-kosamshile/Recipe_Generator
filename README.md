# Recipe Generator

## Description
The Recipe Generator project utilizes OpenAI's GPT-3 API to generate cooking recipes based on provided ingredients. This project aims to demonstrate the practical application of AI in everyday tasks and assists in understanding prompt structuring for desired outputs.

## Requirements
- OpenAI API key
- Python environment with the `openai` library installed

## Usage
1. **Setting Up:**
   - Obtain an OpenAI API key from the official website.
   - Install the `openai` library in your Python environment.
   
2. **Running the Script:**
   - Replace `'your-api-key'` in the script with your actual OpenAI API key.
   - Modify the `ingredients` list with the desired ingredients.
   - Run the script.

3. **Example:**
   ```python
   ingredients = ['chicken', 'broccoli', 'garlic', 'soy sauce', 'rice']
   recipe = generate_recipe(ingredients)
   print(recipe)
   ```

## Future Enhancements
- Improving prompt design for more accurate recipe generation.
- Enhancing error handling for better user experience.
- Experimenting with different parameters to optimize recipe output.

## References
- [OpenAI's GPT-3 API Documentation](https://openai.com/)
- [Learn more about natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)
