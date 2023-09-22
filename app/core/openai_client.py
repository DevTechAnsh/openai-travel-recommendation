import re

import openai

from config.config import settings


def get_gpt_recommendations(prompt):
    """
    Generate text completion using the OpenAI GPT-3 model.
    openai parameters:
    - engine (str): The GPT-3 engine to use for text generation
    - prompt (str): input on which openai will generate a output.
    - max_tokens (int): The maximum number of tokens to generate in the completion.
    - api_key (str): the OpenAI API key.
    """
    # request to the OpenAI GPT
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200,
            api_key=settings.OPENAI_API_KEY,
        )


        if response.choices:
            response = response.choices[0].text.split("\n")
            recommendations = [item.strip() for item in response if item.strip()]
            regex = r'\d+\)|\d+\.\s*'
            recommendations = [part.strip() for item in recommendations for part in re.split(regex, item) if part]
            return recommendations
        else:
            raise ValueError("OpenAI response did not contain valid choices.")
    except openai.error.OpenAIError as e:
        # handle OpenAI exceptions
        raise ValueError(f"OpenAI error occurred: {e}")
    except Exception as e:
        # handle other exceptions
        raise ValueError(f"An unexpected error occurred: {e}")
    except IndexError as e:
        # handle list-index exceptions
        raise ValueError(f"List-index error occurred: {e}")

