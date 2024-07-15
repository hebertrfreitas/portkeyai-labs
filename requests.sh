echo "Request OpenAI...."
curl 'http://localhost:8787/v1/chat/completions' \
  -H 'x-portkey-provider: openai' \
  -H "Authorization: $OPENAI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{ "model": "gpt-3.5-turbo-16k", "messages": [{"role": "user","content": "What is a fractal ?"}] }'


echo "Request Bedrock..."
curl 'http://localhost:8787/v1/chat/completions' \
  -H 'x-portkey-provider: bedrock' \
  -H "x-portkey-aws-access-key-id: $AWS_ACCESS_KEY_ID" \
  -H "x-portkey-aws-secret-access-key: $AWS_SECRET_ACCESS_KEY" \
  -H "x-portkey-aws-region: us-east-1" \
  -H 'Content-Type: application/json' \
  -d '{ "model": "amazon.titan-text-express-v1", "messages": [{"role": "user","content": "What is a fractal ?"}] }'
