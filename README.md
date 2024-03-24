# AI Discord Bot
#### Project Showcase: https://www.youtube.com/watch?v=T-0KNo7aqcw&ab_channel=Saad%27sCodingProjects
## Description
This code comprises a simple Discord bot designed to respond to user messages using OpenAI's GPT-3.5 model. Upon receiving a message in a Discord channel, the bot generates a response based on the received message using the GPT-3.5 model, and then sends the response either in the same channel or as a direct message to the user, depending on the message content.

## Installation
1. Clone the repository:

   ```
   git clone https://github.com/TheSaadster/discord-bot.git
   ```

2. Install the required dependencies:

   ```
   pip install discord
   pip install openai
   pip install python-dotenv    
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Discord bot token and OpenAI API key in the `.env` file:
   
     ```
     DISCORD_TOKEN=your-discord-bot-token
     OPENAI_API_KEY=your-openai-api-key
     ```

## Usage
1. Run the `main.py` file:

   ```
   python main.py
   ```

2. The bot will now be active on Discord. It will respond to messages starting with `?` by sending a direct message to the user and messages without `?` in the channel where they were received.

## Code Structure
- `main.py`: Contains the main code for setting up the Discord bot, handling incoming messages, and defining the main entry point of the application.
- `responses.py`: Defines a function to interact with the OpenAI GPT-3.5 model to generate responses based on user input.