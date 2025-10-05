# enhanced_rule_based_chatbot_v3.py
# An enhanced rule-based chatbot with small changes for initial self-introduction.
# Topic: Movie Recommendations (with expanded genres).
# Features:
# - Introduction pop-up on startup using tkinter.
# - After pop-up, the bot sends an initial self-introduction message in the console.
# - Expanded if-else conditions for genres and queries.
# - Handles greetings, farewells, help, thanks, name, empty inputs, and unknown inputs.
# - Console-based interaction.


def show_intro_popup():
    """
    Prints an introduction message when the chatbot starts (console-based).
    """
    print("\n" + "="*50)
    print("Welcome to Movie Recommendation Chatbot!")
    print("Hi! I'm your friendly movie recommendation bot.\n")
    print("I can suggest movies based on genres like action, comedy, drama, horror, romance, sci-fi, thriller, animation, fantasy, adventure, documentary, musical, western, or superhero.\n")
    print("Just type a genre in the console, say 'help' for options, 'best' for a top pick, or 'bye' to exit.\n")
    print("How may I help you today? Let's chat about movies!")
    print("="*50 + "\n")

def get_movie_recommendation(user_input):
    """
    Analyzes user input and returns a response based on keywords using expanded if-else conditions.
    Handles empty inputs by providing a self-introduction.
    Topic: Recommends movies based on genres and other queries.
    """
    user_input = user_input.lower().strip()
    
    # Handle empty or no input
    if not user_input:
        return "Hi! I'm the Movie Recommendation Bot. I love suggesting great films based on genres. Tell me what you're in the mood for, like 'action' or 'romance', or say 'help' to get started!"
    
    # Greeting handling
    if 'hello' in user_input or 'hi' in user_input or 'hey' in user_input or 'hii' in user_input:
        return "Hi there! I'm your movie recommendation bot. Tell me a genre like 'action', 'comedy', 'drama', 'horror', 'romance', 'sci-fi', 'thriller', 'animation', 'fantasy', 'adventure', 'documentary', 'musical', 'western', or 'superhero' for a suggestion! How may I help you?"
    
    # Farewell handling
    elif 'bye' in user_input or 'goodbye' in user_input or 'exit' in user_input or 'quit' in user_input:
        return "Goodbye! Thanks for chatting. Enjoy your movies! Have a great day!"
    
    # Genre recommendations (expanded with more if-else conditions)
    elif 'action' in user_input:
        return "For action, I recommend 'Mad Max: Fury Road' (2015) directed by George Miller. High-octane thrills and stunning visuals!"
    
    elif 'comedy' in user_input:
        return "For comedy, I recommend 'Superbad' (2007) directed by Greg Mottola. A hilarious coming-of-age story full of laughs!"
    
    elif 'drama' in user_input:
        return "For drama, I recommend 'Forrest Gump' (1994) directed by Robert Zemeckis. An inspiring journey through life and history."
    
    elif 'horror' in user_input:
        return "For horror, I recommend 'Hereditary' (2018) directed by Ari Aster. A deeply unsettling family nightmare!"
    
    elif 'romance' in user_input:
        return "For romance, I recommend 'The Notebook' (2004) directed by Nick Cassavetes. A timeless love story that tugs at the heartstrings."
    
    elif 'sci-fi' in user_input or 'scifi' in user_input or 'science fiction' in user_input:
        return "For sci-fi, I recommend 'Interstellar' (2014) directed by Christopher Nolan. An epic space exploration with mind-bending concepts!"
    
    elif 'thriller' in user_input:
        return "For thriller, I recommend 'Gone Girl' (2014) directed by David Fincher. A twisty psychological suspense ride!"
    
    elif 'animation' in user_input or 'animated' in user_input:
        return "For animation, I recommend 'Spirited Away' (2001) directed by Hayao Miyazaki. A magical adventure in a spirit world!"
    
    elif 'fantasy' in user_input:
        return "For fantasy, I recommend 'The Lord of the Rings: The Fellowship of the Ring' (2001) directed by Peter Jackson. An epic quest in a mythical world!"
    
    elif 'adventure' in user_input:
        return "For adventure, I recommend 'Indiana Jones: Raiders of the Lost Ark' (1981) directed by Steven Spielberg. Treasure hunts and daring escapes!"
    
    elif 'documentary' in user_input:
        return "For documentary, I recommend 'Won't You Be My Neighbor?' (2018) about Fred Rogers. Heartwarming insights into kindness and childhood."
    
    elif 'musical' in user_input:
        return "For musical, I recommend 'La La Land' (2016) directed by Damien Chazelle. A dreamy romance set to jazz and song!"
    
    elif 'western' in user_input:
        return "For western, I recommend 'The Good, the Bad and the Ugly' (1966) directed by Sergio Leone. A classic spaghetti western showdown."
    
    elif 'superhero' in user_input or 'marvel' in user_input or 'dc' in user_input:
        return "For superhero, I recommend 'The Dark Knight' (2008) directed by Christopher Nolan. Batman's battle against chaos with Heath Ledger's iconic Joker!"
    
    # Additional general queries (new if-else conditions)
    elif 'best' in user_input or 'top' in user_input or 'favorite' in user_input:
        return "My top recommendation overall is 'The Shawshank Redemption' (1994). It's a timeless drama about hope and redemption. What's your all-time favorite?"
    
    elif 'director' in user_input:
        return "I love directors like Christopher Nolan or Steven Spielberg! Mention a director's name or a genre, and I'll recommend something from their work."
    
    elif 'year' in user_input or 'old' in user_input or 'new' in user_input:
        return "For classic movies (pre-2000), try 'Casablanca' (1942). For recent ones (post-2010), check out 'Parasite' (2019). Specify a year or genre for more!"
    
    elif 'list' in user_input or 'genres' in user_input:
        return "Available genres: action, comedy, drama, horror, romance, sci-fi, thriller, animation, fantasy, adventure, documentary, musical, western, superhero.\nPick one!"
    
    # Help handling (updated with more options)
    elif 'help' in user_input or 'what can you do' in user_input:
        return "I can recommend movies for genres like action, comedy, drama, horror, romance, sci-fi, thriller, animation, fantasy, adventure, documentary, musical, western, superhero.\nSay 'best' for a top pick, 'director' for tips, or 'list genres' to see options. Type 'hi' to greet or 'bye' to exit."
    
    # Thanks handling
    elif 'thank' in user_input or 'thanks' in user_input:
        return "You're welcome! If you need more recommendations, just ask. What's your favorite genre?"
    
    # Name handling
    elif 'name' in user_input:
        return "I'm the Movie Recommendation Bot! What's your name?"
    
    # Unknown input fallback
    else:
        return "I'm not sure about that. Try mentioning a movie genre like 'fantasy', 'adventure', or 'superhero'. Type 'help' for a full list, 'best' for a top pick, or 'hi' to start over!"

def main():
    """
    Main function to run the chatbot.
    Shows intro pop-up first, then prints an initial self-introduction message,
    and runs the console loop.
    """
    # Show the introduction in the console
    show_intro_popup()
    print("Movie Recommendation Chatbot Started!")
    print("Type your message below. Use 'bye' or 'exit' to quit.\n")
    
    # Initial self-introduction message from the bot
    initial_response = get_movie_recommendation("")  # Empty input triggers self-intro
    print("Bot:", initial_response)
    print()
    
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ['bye', 'goodbye', 'exit', 'quit']:
            print("Bot: " + get_movie_recommendation(user_input))
            print("\nChatbot session ended. Goodbye!")
            break
        
        response = get_movie_recommendation(user_input)
        print("Bot:", response)
        print()  # Empty line for readability

if __name__ == "__main__":
    main()
