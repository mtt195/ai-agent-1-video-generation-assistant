# key point of the application: takes user input, executes prompt generation, saves output

import os
from agent import generate_prompts
from config import SYSTEM_OUTPUT_PATH

if __name__ == "__main__":
    scene = input("Enter scene description: ")
    
    # output generation
    result = generate_prompts(scene)

    # output file path
    output_path = os.path.join(SYSTEM_OUTPUT_PATH, "aiagent_output.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\nOutput saved to: {output_path}")