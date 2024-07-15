from openai import OpenAI
from portkey_ai import createHeaders
import os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
PORTKEY_GATEWAY_URL = 'http://localhost:8787/v1'

logger.info('Calling openai')

gateway = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=PORTKEY_GATEWAY_URL, 
    default_headers=createHeaders(
        provider="openai"
    )
)
chat_complete = gateway.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[{"role": "user", "content": "What's a fractal?"}]
)
logger.info(f"openai response: {chat_complete} ")

logger.info('Calling aws bedrock')

aws_gateway = OpenAI(
    base_url=PORTKEY_GATEWAY_URL, 
    default_headers=createHeaders(
        provider="bedrock",
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),    
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        aws_region="us-east-1",
    )
)

aws_chat_complete = aws_gateway.chat.completions.create(
    model="amazon.titan-text-express-v1",
    messages=[{"role": "user", "content": "What's a fractal?"}]
)
logger.info(f"aws bedrock response: {aws_chat_complete}")