import os
import uvicorn
from src.app import app
from dotenv import load_dotenv

(
	load_dotenv(".env.dev", override=True) 
	if os.environ.get("APP_ENV") == "local" 
	else load_dotenv(".env", override=True)
)

PORT = os.environ.get("PORT", 3000)
HOST = os.environ.get("HOST", "0.0.0.0")


def main():
	uvicorn.run(
   'main:app',
   host=str(HOST),
   port=int(PORT),
   reload=True,
   )

if __name__ == "__main__":
	main()
