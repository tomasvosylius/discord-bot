import discord

token_file = "token.txt"

def read_token():
    with open("token.txt") as file:
        lines = file.readlines()
        return lines[0].strip()

if __name__ == "__main__":
    print("Starting bot.py!")

    token = read_token()
    print("Token was read succesfully!")

    client = discord.Client()
    print("Running the client now...")

    @client.event 
    async def funcname(parameter_list):
        pass

    @client.event
    async def on_ready():
        print(f"Logged in!")

    @client.event 
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startwith == "!verify":
            
            

    client.run(token)