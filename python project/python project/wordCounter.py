def count_words(text):
    
    #This function counts the number of words in the given text.
    
    words = text.split()  # Split the text into words
    return len(words)  # Return the number of words

def main():

    #This is the main function that asks for input and shows the word count.
    
    user_input = input("Enter a sentence or paragraph: ").strip()  # Ask for input and remove extra spaces

    if user_input == "":  # Check if the input is empty
        print("You didn't enter anything. Please type something.")  # Tell the user to type something
    else:
        word_count = count_words(user_input)  # Count the words
        print(f"The number of words in your text is: {word_count}")  # Show the number of words

if __name__ == "__main__":
    main()  # Run the main function
