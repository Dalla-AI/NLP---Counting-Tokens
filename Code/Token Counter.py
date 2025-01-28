import sys

def count_tokens(file_path):
    try:
        # Open the file and read its content
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Split the text into tokens (default: split by whitespace)
        tokens = text.split()
        
        # Count the number of tokens
        token_count = len(tokens)
        return token_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Replace 'your_file.txt' with the path to your .txt file
    file_path = input("Enter the path to the .txt file: ")
    
    token_count = count_tokens(file_path)
    if token_count is not None:
        print(f"The file contains {token_count} tokens.")
        if token_count >= 50000:
            print("The file has at least 50,000 tokens.")
        else:
            print("The file has less than 50,000 tokens.")
