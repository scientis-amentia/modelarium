# Notes for dranger003/Qwen1.5-72B-Chat-iMat.GGUF
[dranger003/Qwen1.5-72B-Chat-iMat.GGUF](https://huggingface.co/dranger003/Qwen1.5-72B-Chat-iMat.GGUF)

## Quants
- iq2_xs
- iq2_xxs

## Notes
- creation
  - no issues
- usage
   - loads without issues
   - runs very slowly
     - this is apparently because it is mostly running on CPU, despite fully fitting on the GPU
     - this is the only such model that seems to do this, not sure why.
     - quants updated on 2024/03/19 but updating made no difference