import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 5

# TODO: Fill this in!
YOUR_SYSTEM_PROMPT = """
You are a helpful assistant that performs text manipulation tasks.

When asked to reverse letters in a word:
1. Take only the word provided by the user
2. Reverse the order of its letters (last letter becomes first, etc.)
3. Output ONLY the reversed word with no additional explanation, commentary, or formatting
4. Do not include any other text in your response

Make sure the response have the same length of the input word.

For example:
```
"apple" turns into "elppa"

"banana" turns into "ananab"

"jhjhjhjhjhjh" turns into "hjhjhjhjhjhj"

"https" turns into "sptth"

"abcdefg" turns into "gfedcba"

"hello" turns into "olleh"

"world" turns into "dlrow"

"python" turns into "nohtyp"

"computer" turns into "retupmoc"

"keyboard" turns into "draobyek"

"reverse" turns into "esrever"

"example" turns into "elpmaxe"

"string" turns into "gnirts"

"algorithm" turns into "mhtirogla"

"function" turns into "noitcnuf"

"data" turns into "atad"

"code" turns into "edoc"

"httpstatus" turns into "sutatsptth"

"text" turns into "txet"

"mirror" turns into "rorrim"

"palindrome" turns into "emordnilap"
```
"""

USER_PROMPT = """
Reverse the order of letters in the following word. Only output the reversed word, no other text:

httpstatus
"""

EXPECTED_OUTPUT = "sutatsptth"


def test_your_prompt(system_prompt: str) -> bool:
    """Run the prompt up to NUM_RUNS_TIMES and return True if any output matches EXPECTED_OUTPUT.

    Prints "SUCCESS" when a match is found.
    """
    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        response = chat(
            model="mistral-nemo:12b",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": USER_PROMPT
                },
            ],
            options={"temperature": 0.5},
        )
        output_text = response.message.content.strip()
        if output_text.strip() == EXPECTED_OUTPUT.strip():
            print("SUCCESS")
            return True
        else:
            print(f"Expected output: {EXPECTED_OUTPUT}")
            print(f"Actual output: {output_text}")
    return False


if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
