# Notes for dranger003/alpaca-dragon-72b-v1-iMat.GGUF
[dranger003/alpaca-dragon-72b-v1-iMat.GGUF](https://huggingface.co/dranger003/alpaca-dragon-72b-v1-iMat.GGUF)

## Quants
- iq2-xs

## Notes
- very slow to load and run
  - despite the size, it seems to run mostly on CPU
- extraneous text
  - `<|endoftext|>` kicked out at the end fairly regularly
  - it will also answer its own questions, but that might be more due to the stop token
