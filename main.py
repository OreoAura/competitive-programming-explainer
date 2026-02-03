import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

print("=== Competitive Programming Problem Explainer ===")
print("\nSelect explanation mode:")
print("1. Beginner (very detailed)")
print("2. Interview (balanced)")
print("3. Contest (concise)")

mode_choice = input("Enter choice (1/2/3): ").strip()

if mode_choice == "1":
    mode = "Beginner"
elif mode_choice == "2":
    mode = "Interview"
elif mode_choice == "3":
    mode = "Contest"
else:
    print("Invalid choice. Defaulting to Interview mode.")
    mode = "Interview"
client = genai.Client(
    api_key=os.getenv("NEW_HACKATHON_GEMINI_API_KEY")
)

model = "gemini-2.5-flash"

while True:
    print("\nEnter problem description (type END on a new line to finish):")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    problem = "\n".join(lines).strip()

    if problem.lower() == "exit":
        print("Goodbye!")
        break

    if not problem:
        print("No problem entered. Try again.")
        continue

    prompt = f"""
You are a Competitive Programming Professor.
The explanation style MUST strictly match this mode: {mode}.
STRICT RULES:
- Follow the EXACT format below
- Do NOT rename sections
- Do NOT change order
- Do NOT merge sections
- Do NOT skip any section
- Use markdown headings exactly as written

==============================
### 1. Problem Restatement
==============================
Explain the problem in simple language (3–4 lines).

==============================
### 2. Intuition
==============================
Explain the core idea without code.

==============================
### 3. Key Observations
==============================
- Bullet points only
- Mention constraints and patterns

==============================
### 4. Optimal Approach
==============================
- Step-by-step algorithm
- Explain WHY it works

==============================
### 5. Dry Run (Example)
==============================
Input:
Explain step-by-step execution.

==============================
### 6. Edge Cases
==============================
- Bullet points only

==============================
### 7. Time Complexity
==============================
Big-O with explanation.

==============================
### 8. Space Complexity
==============================
Big-O with explanation.

==============================
### 9. C++ Implementation
==============================
- Clean
- Commented
- Competitive-programming style

==============================
PROBLEM
==============================
{problem}
"""

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )
    except Exception as e:
        print("\nError:", e)
        continue

    print("\n" + "=" * 70)
    print("🏆 COMPETITIVE PROGRAMMING AI EXPLAINER")
    print("=" * 70 + "\n")
    print(response.text)
    print("\n" + "=" * 70)