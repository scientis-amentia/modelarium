# Notes for TIGER-Lab/TIGERScore-7B-GGUF
[TIGER-Lab/TIGERScore-7B-GGUF](https://huggingface.co/TIGER-Lab/TIGERScore-7B-GGUF)

## Quants
- q4_0

## Notes
- [prompt template](https://github.com/TIGER-AI-Lab/TIGERScore/blob/main/tigerscore/scorer/tigerscore.py#L9C12-L25C4)
```python
"""You are evaluating errors in a model-generated output for a given instruction.
Instruction: 
${generation_instruction}
${input_context}

Model-generated Output: 
${hypothesis_output}

For each error you give in the response, please also elaborate the following information:
- error location (the words that are wrong in the output)
- error aspect it belongs to.
- explanation why it's an error, and the correction suggestions.
- severity of the error ("Major" or "Minor"). 
- reduction of score (between 0.5 and 5 given the severity of the error)

Your evaluation output:
"""
```

- [inference example](https://huggingface.co/TIGER-Lab/TIGERScore-7B-GGUF#usage)
```python
# example  
instruction = "Write an apology letter."
input_context = "Reason: You canceled a plan at the last minute due to illness."
hypo_output = "Hey [Recipient],\n\nI'm really sorry for ditching our plan. I suddenly got an opportunity for a vacation so I took it. I know this might have messed up your plans and I regret that.\n\nDespite being under the weather, I would rather go for an adventure. I hope you can understand my perspective and I hope this incident doesn't change anything between us.\n\nWe can reschedule our plan for another time. Sorry again for the trouble.\n\nPeace out,\n[Your Name]\n\n---"
results = scorer.score([instruction], [hypo_output], [input_context])
print(results)
```