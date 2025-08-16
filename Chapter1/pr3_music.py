import pygame
pygame.mixer.init()
pygame.mixer.music.load('D:\\Python\\Chapter1\\MusicforCode.mp3')    # Load the music file
pygame.mixer.music.play()  # Play the music
while pygame.mixer.music.get_busy():  # Wait for the music to finish playing
    pygame.time.Clock().tick(10)  # Check every 10 milliseconds if the music is still playing
pygame.mixer.music.stop()  # Stop the music after it finishes playing   
pygame.mixer.quit()  # Quit the mixer module
# Note: Ensure that the path to the music file is correct and that the file exists.  