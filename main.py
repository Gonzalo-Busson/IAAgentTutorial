from dotenv import load_dotenv
import os

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if __name__ == "__main__":
    print("IA Agent Tutorial - Starting...")
