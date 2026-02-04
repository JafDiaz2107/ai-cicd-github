from google import genai
import sys

client = genai.Client()

# Define a function that takes a code diff as input
def gemini_code_review(diff:str):

    # Write a multi-line f-string prompt that includes {diff_text}
    # Tell Gemini to act as a code reviewer and focus on security, bugs, performance
    prompt = f"""
    You are a senior software engineer and an expert code reviewer. Your task will be to evaluate the code diff and provide feedback on the following criteria:
    - Security
    - Bugs
    - Performance
    - Code quality
    - Best practices
    - Maintainability
    - Readability
    - Scalability
    - Testability
    Review the following code diff:
    {diff}
    """

    # Send the prompt to the model and get a response
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", contents=prompt
    )

    # Return just the text from the response
    return response.text


# Only run this code when the script is executed directly
if __name__ == "__main__":

    # Check if a filename was passed as a command-line argument
    if len(sys.argv) > 1:

        # Get the filename from sys.argv and read the file
        diff_file = sys.argv[1]
        with open(diff_file, "r") as f:
            diff_content = f.read()

    # If no filename was passed, read from standard input
    else:
        diff_content = sys.stdin.read()

    # Call the review function and print the result
    review = gemini_code_review(diff_content)
    print(review)
