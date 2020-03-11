# bot.py 
# http://github.com/tomasvosylius/discord-bot
# using discord.py

import discord

general_channel_name = "bendras"
token_file           = "token.txt"
server_name          = "RealState.lt"
samp_server_ip       = "samp.realstate.lt:7777"
messages             = {
    # message used for DM when new user joins
    "verification_message" : 
        f"Sveikiname prisijungus prie {server_name}! :partying_face:\n"
        f"Norėdamas tapti patvirtintu nariu, pirmiausia turi būti registruotas serveryje adresu `{samp_server_ip}`\n"
        "Žemiau parašyk savo __žaidimo Vardą_Pavardę__ ir lauk **patvirtinimo**",
    "welcome_global" : 
        "Labas, __{0}__! :wave: :tada:\nSveikiname prisijungus prie {1} serverio!",
}

def read_token():
    """
    Function reads token from token.txt file in current directory
    """
    with open("token.txt") as file:
        lines = file.readlines()
        return lines[0].strip()

def get_channel_by_name(name):
    """
    Function returns channel if found by given name 
    """
    for channel in client.get_all_channels():
        if name in channel.name:
            return channel
    return None


if __name__ == "__main__":
    print("Starting bot.py!")

    token = read_token()
    print("Token was read succesfully!")

    client = discord.Client()
    print("Running the client now...")

    gen_channel = None # general channel

    @client.event 
    async def on_ready():
        gen_channel = get_channel_by_name(general_channel_name)
        if gen_channel == None:
            print("Error when looking for channel")
        else:
            print("General channel was found")

    @client.event
    async def on_member_join(member):
        print(f"{str(member)} just joined the server.")
    
        if gen_channel != None:
            # send the message to general channel
            await greet_member(gen_channel, message.author)

        # message the user
        dm = await member.create_dm()
        if dm != None:
            await dm.send(messages['verification_message'])


    @client.event
    async def on_connect():
        print("Connected")

    @client.event 
    async def on_message(message):
        if message.author == client.user:
            return # ignore the bot itself

        if message.content.startswith("!greetme"):
            await greet_member(message.channel, message.author)
            # message.channel.send(messages["welcome_global"].format(message.author.display_name, server_name))

        if message.content.startswith("!dmme"):
            dm = await message.author.create_dm()
            await dm.send(messages['verification_message'])

    async def greet_member(channel, member):
        await channel.send(messages["welcome_global"].format(member.display_name, server_name))

    client.run(token)