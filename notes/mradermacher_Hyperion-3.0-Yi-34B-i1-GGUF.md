# Notes for mradermacher/Hyperion-3.0-Yi-34B-i1-GGUF
[mradermacher/Hyperion-3.0-Yi-34B-i1-GGUF](https://huggingface.co/mradermacher/Hyperion-3.0-Yi-34B-i1-GGUF)

## Quants
- iq2_xs
- iq3_xs
- iq4_xs
- q4_k_m
- 

## Notes
- iq2_xs and q4_k_m can be created
  - but they are behaving oddly
  - lots of repetition, lots of switching roles and asking questions as the user, etc. 
- iq4_xs and iq3_xs are not working
  - can't be created due to `invalid file magic` error
    - ollama v0.1.29
