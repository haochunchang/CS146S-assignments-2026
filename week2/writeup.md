# Week 2 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **TODO** \
SUNet ID: **TODO** \
Citations: **TODO**

This assignment took me about **TODO** hours to do. 


## YOUR RESPONSES
For each exercise, please include what prompts you used to generate the answer, in addition to the location of the generated response. Make sure to clearly add comments in your code documenting which parts are generated.


### Exercise 1: Scaffold a New Feature
Using Copilot "Auto"

Prompt: 
```
Analyze the existing extract_action_items() function in week2/app/services/extract.py, which currently extracts action items using predefined heuristics.

Your task is to implement an LLM-powered alternative, extract_action_items_llm(), that utilizes Ollama to perform action item extraction via a large language model.
``` 

Generated Code Snippets:
```
app/services/extract.py#L90-179
```

### Exercise 2: Add Unit Tests

Using Copilot "GPT-5 mini"
Prompt: 
```
Write unit tests for extract_action_items_llm() covering multiple inputs (e.g., bullet lists, keyword-prefixed lines, empty input) in #file:test_extract.py .
``` 

Generated Code Snippets:
```
tests/test_extract.py#L4
tests/test_extract.py#L21-62
```

### Exercise 3: Refactor Existing Code for Clarity
Using Copilot "GPT-5 mini"
Prompt: 
```
Perform a refactor of the code in the backend, focusing in particular on well-defined API contracts/schemas, database layer cleanup, app lifecycle/configuration, error handling. 
``` 

Generated/Modified Code Snippets:
```

app/services/extract.py#L90-L179
app/db.py#L24-L26, L52-L61, L64-L72, L75-L86, L89-L104, L107-L122, L125-L135
app/main.py#L11, L18-L24
app/routers/action_items.py#L10, L15-L37, L40-L53, L56-L92
app/routers/notes.py#L9, L14-L32, L35-L48
app/schemas.py#L1-L43

```


### Exercise 4: Use Agentic Mode to Automate a Small Task
Prompt: 
```
TODO
``` 

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```


### Exercise 5: Generate a README from the Codebase
Prompt: 
```
TODO
``` 

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```


## SUBMISSION INSTRUCTIONS
1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields. 
2. Make sure you have all changes pushed to your remote repository for grading.
3. Submit via Gradescope. 