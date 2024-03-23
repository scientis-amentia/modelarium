# Notes for meetkai/functionary-medium-v2.2-GGUF
[meetkai/functionary-medium-v2.2-GGUF](https://huggingface.co/meetkai/functionary-medium-v2.2-GGUF)

## Quants
- q4_0

## Notes
- prompt template
  - from [model card](https://huggingface.co/meetkai/functionary-medium-v2.2#prompt-template)
    - implies a ChatML-like format
    - interaction via OpanAI API looks nice
  - from [tokenizer_config.json](https://huggingface.co/meetkai/functionary-medium-v2.2/blob/main/tokenizer_config.json)
    - suggests a stop param of "<|stop|>"
- ollama model
  - creation
    - no issues
  - usage
    - no issues so far



## Modelfile

```
FROM ../models/functionary-medium-v2.2.q4_0.gguf
TEMPLATE """
<|from|>system
<|recipient|>all
<|content|>{{ .System }}
<|from|>system
<|recipient|>all
<|content|>A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. The assistant calls functions with appropriate input when necessary
<|from|>user
<|recipient|>all
<|content|>{{ .Prompt }}
"""
SYSTEM """
// Supported function definitions that should be called when necessary.
namespace functions {
// Get the current weather
type get_current_weather = (_: {
// The city and state, e.g. San Francisco, CA
location: string,
}) => any;
} // namespace functions
"""
PARAMETER stop "<|stop|>"
```

## example

```
$ orn mgmacleod/functionary-medium-v2.2.q4_0
>>> hello
<|from|> assistant
<|recipient|>all
<|content|>Hello! How can I assist you today?

>>> i'm new here. what can you tell me?
<|from|> assistant
<|recipient|>all
<|content|>I'm a virtual assistant designed to help answer your questions and provide information on a wide range of topics. 
Whether you want to know about science, culture, technology, or just need assistance with something, feel free to ask! How can 
I assist you today?

>>> what is the weather in ottawa, on, ca?
<|from|> assistant
<|recipient|>get_current_weather
<|content|>{"location": "Ottawa, ON, CA"}

>>> /bye
```
