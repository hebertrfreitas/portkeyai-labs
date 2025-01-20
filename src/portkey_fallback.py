from portkey_ai import Portkey
import os

OPENAI_API_KEY =  os.environ["OPENAI_API_KEY"]
PORTKEY_GATEWAY_URL = 'http://localhost:8787/v1'

config_params = {
    "strategy": {
        "mode": "fallback",
        #"on_status_codes": [429]
    },
    "targets": [
        {
            "provider" : "openai",
            "api_key": "dummy-api-key",
            "custom_host": "http://wiremock:8080/v1",
            #"custom_host": "http://localhost:8787/v1",
            "override_params": { "model": "gpt-4o"}
        },
        {
            "provider": "openai",
            "api_key": OPENAI_API_KEY,
            "override_params": { "model": "o1-mini-123"}
        },
        # {
        #     "provider": "azure-openai",
        #     "api_key": "AZURE_OPENAI_API_KEY",
        #     "deployment_id": "AZURE_MODEL_DEPLOYMENT_NAME",
        #     "resource_name": "AZURE_RESOURCE_NAME",
        #     "api_version": "AZURE_API_VERSION"
        # }
    ]
}


#Calling OpenAI
portkey = Portkey(
  api_key="dummy",
  #provider = "openai",
  #Authorization=OPENAI_API_KEY,
  base_url=PORTKEY_GATEWAY_URL,
  config=config_params
)

response = portkey.chat.completions.create(
  messages = [{ "role": 'user', "content": 'Hello' }],
  model = 'gpt-4o'
)

print(response)





# fallback_config={
#     "strategy": {
#         "mode": "fallback"
#     },
#     "targets": [
#         {
#             "provider": "openai",
#             "api_key": "OPENAI_API_KEY",
#             "override_params": { "model": "gpt-4o"}
#         },
#         {
#             "provider": "azure-openai",
#             "api_key": "AZURE_OPENAI_API_KEY",
#             "deployment_id": "AZURE_MODEL_DEPLOYMENT_NAME",
#             "resource_name": "AZURE_RESOURCE_NAME",
#             "api_version": "AZURE_API_VERSION"
#         }
#     ]
# }


# portkey = Portkey(
#     api_key="dummy", # Pass any value here - this is not considered
#     base_url="http://localhost:8787/v1",
#     config=fallback_config
# )

# response = portkey.chat.completions.create(
#     messages=[ { "role":"user","content":"Arrr!" } ]
# )

# print(response.choices[0].message.content)