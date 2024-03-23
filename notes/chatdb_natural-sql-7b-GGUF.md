# Notes for chatdb/natural-sql-7b-GGUF
[chatdb/natural-sql-7b-GGUF](https://huggingface.co/chatdb/natural-sql-7b-GGUF)

## Quants
- q5_k_m

## Notes
- prompt template
  - from [model card](https://huggingface.co/chatdb/natural-sql-7b#prompt-template)
    - used the template as-is, with Ollama substitutes for {{ .Prompt }} etc.
  - and [tokenizer config](https://huggingface.co/chatdb/natural-sql-7b/blob/main/tokenizer_config.json)
    - partly based on the config and partly based on model behaviour, settled on the following stop params
      - "<｜end▁of▁sentence｜>"
      - "```"
      - "# Task"
