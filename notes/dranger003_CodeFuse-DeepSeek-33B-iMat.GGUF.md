# Notes for dranger003/CodeFuse-DeepSeek-33B-iMat.GGUF
[dranger003/CodeFuse-DeepSeek-33B-iMat.GGUF](https://huggingface.co/dranger003/CodeFuse-DeepSeek-33B-iMat.GGUF)

## Quants
- ggml-codefuse-deepseek-33b-iq3_xs.gguf
- ggml-codefuse-deepseek-33b-iq3_xxs.gguf


## Notes
- with Ollama v0.1.27, we get 'invalid file magic' for both of the above files
  - not sure specifically what the issue is
  - I've done lots of iq3-xs and iq3-xxs quants before
    - there must be some other issue with the file that Ollama doesn't like
  - Anyway, setting these aside until they can be converted
