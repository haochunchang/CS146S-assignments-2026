Date: 2026-01-22

# K-shot prompting — `week1/k_shot_prompting.py`


# Chain-of-thought — `week1/chain_of_thought.py`

Running test 1 of 5
To find \(3^{12345} \pmod{100}\), we can use the concept of modular arithmetic and look for patterns in powers of 3 modulo 100.

First, let's calculate some initial powers of 3 modulo 100 to see if there is a repeating pattern:

- \(3^1 \equiv 3 \pmod{100}\)
- \(3^2 \equiv 9 \pmod{100}\)
- \(3^3 \equiv 27 \pmod{100}\)
- \(3^4 \equiv 81 \pmod{100}\)

Now, let's continue to the next power:

- \(3^5 \equiv (3^4) \cdot 3 \equiv 81 \cdot 3 \equiv 243 \equiv 43 \pmod{100}\)
- \(3^6 \equiv (3^5) \cdot 3 \equiv 43 \cdot 3 \equiv 129 \equiv 29 \pmod{100}\)
- \(3^7 \equiv (3^6) \cdot 3 \equiv 29 \cdot 3 \equiv 87 \pmod{100}\)
- \(3^8 \equiv (3^7) \cdot 3 \equiv 87 \cdot 3 \equiv 261 \equiv 61 \pmod{100}\)

Now, let's calculate the next power:

- \(3^9 \equiv (3^8) \cdot 3 \equiv 61 \cdot 3 \equiv 183 \equiv 83 \pmod{100}\)
- \(3^{10} \equiv (3^9) \cdot 3 \equiv 83 \cdot 3 \equiv 249 \equiv 49 \pmod{100}\)

Continuing this pattern, we find:

- \(3^{11} \equiv (3^{10}) \cdot 3 \equiv 49 \cdot 3 \equiv 147 \equiv 47 \pmod{100}\)
- \(3^{12} \equiv (3^{11}) \cdot 3 \equiv 47 \cdot 3 \equiv 141 \equiv 41 \pmod{100}\)

Now, let's calculate the next power:

- \(3^{13} \equiv (3^{12}) \cdot 3 \equiv 41 \cdot 3 \equiv 123 \equiv 23 \pmod{100}\)
- \(3^{14} \equiv (3^{13}) \cdot 3 \equiv 23 \cdot 3 \equiv 69 \pmod{100}\)

Continuing this pattern, we find:

- \(3^{15} \equiv (3^{14}) \cdot 3 \equiv 69 \cdot 3 \equiv 207 \equiv 7 \pmod{100}\)
- \(3^{16} \equiv (3^{15}) \cdot 3 \equiv 7 \cdot 3 \equiv 21 \pmod{100}\)

Now, let's calculate the next power:

- \(3^{17} \equiv (3^{16}) \cdot 3 \equiv 21 \cdot 3 \equiv 63 \pmod{100}\)
- \(3^{18} \equiv (3^{17}) \cdot 3 \equiv 63 \cdot 3 \equiv 189 \equiv 89 \pmod{100}\)

Continuing this pattern, we find:

- \(3^{19} \equiv (3^{18}) \cdot 3 \equiv 89 \cdot 3 \equiv 267 \equiv 67 \pmod{100}\)
- \(3^{20} \equiv (3^{19}) \cdot 3 \equiv 67 \cdot 3 \equiv 201 \equiv 1 \pmod{100}\)

We've reached a power of 3 that is congruent to 1 modulo 100. This means the cycle repeats every 20 powers:

- \(3^x \equiv (3^{x \bmod 20})\)

Given this, we can reduce the exponent 12345 by taking its remainder when divided by 20:

- \(12345 \bmod 20 = 5\)

Therefore,

\(3^{12345} \equiv 3^5 \pmod{100}\)

From our initial calculations, we know that:

- \(3^5 \equiv 43 \pmod{100}\)

So,

Answer: 43
SUCCESS

# Tool calling — `week1/tool_calling.py`

Failed to parse tool call: Model did not return valid JSON for the tool call
{'tool': 'output_every_func_return_type', 'args': {}}
Generated tool call: {'tool': 'output_every_func_return_type', 'args': {'file_path': '/Users/hcchang/backend-practice/modern-software-dev-assignments/week1/tool_calling.py'}}
Generated output: _annotation_to_str: str
_list_function_return_types: List[Tuple[str, str]]
add: int
compute_expected_output: str
execute_tool_call: str
extract_tool_call: Dict[str, Any]
greet: str
output_every_func_return_type: str
resolve_path: str
run_model_for_tool_call: Dict[str, Any]
test_your_prompt: bool
SUCCESS

# Self-consistency prompting — `week1/self_consistency_prompting.py`

Running test 1 of 5
Run 1 answer: Answer: 25
Running test 2 of 5
Run 2 answer: Answer: 5
Running test 3 of 5
Run 3 answer: To solve this problem, let's break it down step by step:

1. Henry made two stops during his 60-mile bike trip.
2. He stopped after 20 miles for the first stop.
3. His second stop was 15 miles before the end of the trip.

We know that the total distance is 60 miles and he stopped 20 miles into it, so there are 60 - 20 = 40 miles remaining to his second stop. We also know that his second stop is 15 miles before the end of the trip, so the distance from the first stop to the second stop is (60 - 15) - 20 = 25 miles.

Now we need to find out how many miles he traveled between these two stops.

The second stop is 25 miles after the first stop. So we can add them up: 
We know that his first stop was at mile 20, so there are 60- 20 = 40 miles remaining to his second stop. His second stop is at 15 miles before the end of the trip which is 60 - 15 = 45 miles and he stopped at mile 20.

Now we need to find the length of each part of this journey, 
First segment:
Mileage to the first rest-stop: Miles 1- 20  
The mileage for the first segment then must be between 0 and 20 (that means it was 20) 
Then the second stop is at mile marker 45 so you need to find the distance traveled on the second part of the journey. To do that, we need to subtract the last rest-stop from the total number of miles:
Second segment: Mileage between the two stops. (Mile 20 - Mile 45).
We will then take a final value for each leg and add them together to find the total distance traveled.

First part
0-20 = 20 
Second part:
45 - 20 = 25

Finally, we can determine that he traveled: 
60 (the entire journey) – 20 (the first segment) - 25 (second segment): The trip was made in two parts 20 and 25.
Running test 4 of 5
Run 4 answer: Answer: 25
Running test 5 of 5
Run 5 answer: Answer: 25
Majority answer: Answer: 25 (3/5)
SUCCESS

# RAG (Retrieval-Augmented Generation) — `week1/rag.py`

Running test 1 of 5
```python
import requests

def fetch_user_name(user_id: str, api_key: str) -> str:
    """
    Fetch a user by id from the API and return their name as a string.

    Args:
        user_id (str): The ID of the user to fetch.
        api_key (str): The API key for authentication.

    Returns:
        str: The name of the fetched user.

    Raises:
        requests.exceptions.RequestException: If the request fails or returns a non-200 status code.
    """
    url = f"https://api.example.com/v1/users/{user_id}"
    headers = {"X-API-Key": api_key}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 responses
    
    user_data = response.json()
    return user_data["name"]
```
SUCCESS

# Reflexion — `week1/reflexion.py`

Initial code:
def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    for char in password:
        if not (char.isalnum() or char in "!@#$%^&*()_+-="):
            return False
    return True
FAILURE (initial implementation failed some tests): ['Input: password1! → expected False, got True. Failing checks: missing uppercase', 'Input: Password! → expected False, got True. Failing checks: missing digit', 'Input: Password1 → expected False, got True. Failing checks: missing special']
REFLECTION CONTEXT: Here is your current answer: def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    for char in password:
        if not (char.isalnum() or char in "!@#$%^&*()_+-="):
            return False
    return True, and these are the failures: ['Input: password1! → expected False, got True. Failing checks: missing uppercase', 'Input: Password! → expected False, got True. Failing checks: missing digit', 'Input: Password1 → expected False, got True. Failing checks: missing special'], After generating your answers, 
review them by checking if it is correct or not.
If you feel confident that it is correct, then follow the system prompt to output your answer.
If you are not confident, then iterate and improve your answers for a few times.


Improved code:
def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in "!@#$%^&*()_+-=" for char in password)

    return has_uppercase and has_digit and has_special_char
SUCCESS