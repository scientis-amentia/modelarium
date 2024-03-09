# Notes for dranger003/mamba-bagel-2.8b-v0.2-GGUF
[dranger003/mamba-bagel-2.8b-v0.2-GGUF](https://huggingface.co/dranger003/mamba-bagel-2.8b-v0.2-GGUF)

## Quants
- q8_0

## Notes
- creation
  - no issues
- usage
  - causes division by zero errors in Ollama when using the model
    - this might because Ollama does not support this model yet