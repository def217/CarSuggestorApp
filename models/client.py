import openai
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate_response(self, prompt):
        print("\nGenerating response...\n")
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Provide output in valid JSON."},
                    {"role": "user", "content": prompt}
                    ],
                temperature=0.5,
                max_tokens=500,
            )
            
            if response.choices[0].finish_reason == "stop":    
                print(response)
                response_data = json.loads(response.choices[0].message.content)
            else:
                print("More tokens needed.")
            
            return response_data

        except openai.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
            pass
        except openai.APIConnectionError as e:
            print(f"Failed to connect to OpenAI API: {e}")
            pass
        except openai.RateLimitError as e:
            print(f"OpenAI API request exceeded rate limit: {e}")
            pass
        except openai.APITimeoutError:
            print("OpenAI API request timed out.")
        except Exception as e:
            print(e)
            print("Something went wrong with the OpenAI API request.")