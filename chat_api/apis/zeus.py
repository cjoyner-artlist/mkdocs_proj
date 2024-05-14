from zeus import GenerativeModel
import os

class ZeusAPI(GenerativeModel):

  @classmethod
  def from_env(cls):
    """
    Instantiates a `GeminiAPI` object using the `GEMINI_API_KEY` environment variable.

    This method retrieves the API key from the `GEMINI_API_KEY` environment variable 
    and uses it to create a new `GeminiAPI` instance. It's a convenient way to manage 
    your API key without including it directly in your code.

    **Raises:**

    ValueError: If the `GEMINI_API_KEY` environment variable is not set.

    **Example Usage:**

    ```python
    # Assuming GEMINI_API_KEY is set in the environment
    api = GeminiAPI.from_env()
    ```
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
      raise ValueError("GEMINI_API_KEY environment variable not set")
    return cls(api_key)

  def generate_from_file(self, prompt_file):
    """
    Reads prompts from a text file line by line and generates responses for each.

    This method iterates over each line in the provided text file, treating each line 
    as a separate prompt. It then uses the `generate_text` method inherited from the 
    parent class to generate a response for each prompt. Finally, it prints both the 
    original prompt and the generated response.

    **Args:**

    prompt_file (str): The path to a text file containing prompts, one per line.

    **Example Usage:**

    ```python
    # Assuming you have a file named "prompts.txt" with prompts like:
    # Write a poem about a cat
    # Describe a futuristic city

    api = GeminiAPI.from_env()  # Assuming GEMINI_API_KEY is set
    api.generate_from_file("prompts.txt")

    def my_func(param: int):
        param + 3
        return param
    ```

    This will print the prompts and corresponding generated responses from Gemini.
    """
    with open(prompt_file, 'r') as f:
      for line in f:
        prompt = line.strip()
        response = self.generate_text(prompt)
        print(f"Prompt: {prompt}\nResponse: {response.text}\n")