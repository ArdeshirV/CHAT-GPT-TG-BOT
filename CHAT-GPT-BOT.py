import os
os.environ['OPENAI_API_KEY'] = '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'


import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-0301",
  messages=[
    {"role": "user", "content": "write me trade solidity code"}
  ]
)

print(completion.choices[0].message)


# import os
# import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.Image.create(
#   prompt="A frog with guitar",
#   n=2,
#   size="1024x1024"
# ))
