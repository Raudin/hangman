import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Set up the fonts
FONT_SIZE = 48
font = pygame.font.SysFont(None, FONT_SIZE)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# List of words for the game
words = ["apple", "apricot", "avocado", "banana", "blackberry", "blackcurrant", "blueberry", "breadfruit", "cactus fruit", "cantaloupe", "cherry", "cloudberry", "coconut", "cranberry", "cucumber", "custard apple", "damson", "date", "dragonfruit", "elderberry",  "gooseberry", "grape", "grapefruit", "guava", "honeydew", "huckleberry", "jackfruit", "jambul", "jujube", "kiwano", "kiwifruit", "kumquat", "lemon", "lime", "loquat", "longan", "lychee", "mango", "mangosteen", "marionberry", "melon", "mulberry", "nectarine", "orange", "papaya", "passionfruit", "peach", "pear", "persimmon", "physalis", "pineapple", "plum", "pomegranate", "pomelo", "purple mangosteen", "quince", "raisin",  "raspberry", "redcurrant",  "star fruit", "strawberry", "tamarillo", "tangerine", "watermelon"]

# Choose a random word from the list
word = random.choice(words)

# Create a list of underscores to represent the hidden word
hidden_word = ["_"] * len(word)

# Keep track of the number of incorrect guesses
incorrect_guesses = 0

# Load the hangman images
images = []
for i in range(7):
    image = pygame.image.load(f"hangman{i}.png")
    images.append(image)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                guess = event.unicode.lower()
                
                # Check if the guess is in the word
                if guess in word:
                    # Replace the underscores with the guessed letter
                    for i in range(len(word)):
                        if word[i] == guess:
                            hidden_word[i] = guess
                else:
                    # Increment the number of incorrect guesses
                    incorrect_guesses += 1
                    
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw the hangman image
    image_index = min(incorrect_guesses, 6)
    image = images[image_index]
    screen.blit(image, (0, 0))
    
    # Draw the hidden word
    hidden_word_text = font.render(" ".join(hidden_word), True, BLACK)
    x = (WIDTH - hidden_word_text.get_width()) / 2
    y = HEIGHT - FONT_SIZE - 10
    screen.blit(hidden_word_text, (x, y))
    
    # Draw the incorrect guesses
    incorrect_guesses_text = font.render(f"Incorrect guesses: {incorrect_guesses}", True, BLACK)
    x = (WIDTH - incorrect_guesses_text.get_width()) / 2
    y = HEIGHT - FONT_SIZE * 2 - 10
    screen.blit(incorrect_guesses_text, (x, y))
    
    # Check if the player has won or lost
    if "".join(hidden_word) == word:
        result_text = font.render("You win!", True, BLACK)
        x = (WIDTH - result_text.get_width()) / 2
        y = FONT_SIZE
        screen.blit(result_text, (x, y))
        running = False
    elif incorrect_guesses == 6:
        result_text = font.render(f"You lose! The word was {word}.", True, BLACK)
        x = (WIDTH - result_text.get_width()) / 2
        y = FONT_SIZE
        screen.blit(result_text, (x, y))
        running = False
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()