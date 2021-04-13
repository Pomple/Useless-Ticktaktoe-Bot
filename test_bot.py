
import discord
import re


TOKEN = 'ODA5MzgxMDU0MzI2Mzc0NDEw.YCUQ2A.hP9UCtCCABj9JiB7qq2qu4y7S5c'
GUILD = '809379908207771648'

players = ["", ""]
currentPlayer = 0
client = discord.Client()

fieldData = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]


def displayfield(fielddata):
	display = "Board:\n3    " + fielddata[0][0] + "  |   " + fielddata[0][1] + "  |  " + fielddata[0][2] + "   \n " \
					"  ––––|––––|––––\n2 " \
					"   " + fielddata[1][0] + "  |   " + fielddata[1][1] + "  |   " + fielddata[1][2] + "   \n " \
					"  ––––|––––|––––\n1  " \
					"   " + fielddata[2][0] + "  |   " + fielddata[2][1] + "  |   " + fielddata[2][2] + "   " \
					"\n     1         2        3      "
	return display


@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break

		print(client.users)
		print(
			f'{client.user} is connected to the following guild:\n'
			f'{guild.name}(id: {guild.id})'
		)

		members = '\n - '.join([member.name for member in guild.members])
		print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to my Discord server!'
	)


@client.event
async def on_message(message):
	content = message.content
	author = message.author.name
	moves = re.findall('[1-3],[1-3]', content)
	global players
	global currentPlayer
	global currentguild
	global fieldData
	# begin the game

	# test if command has been sent
	if '!registerplayers ' in message.content:
		content = content.split()
		
		# test that no other players have already been registered
		if players[0] != "" and players[1] != "":
			await message.channel.send("Two players are already playing.")
			return
		
		# test that at least 2 players are being registered
		if len(content) < 3:
			await message.channel.send("Please register 2 players!")
			return
		
		# test that not the same player is registered twice
		if content[1] == content[2]:
			await message.channel.send("Please register two different players!")
			return

		# test that the two registerd players are actually on the server
		# ---TODO---
		
		print(content)
		
		players[0] = content[1]
		players[1] = content[2]
		await message.channel.send("Players: \n" + "Player 1 is registered as: " + players[0] + "\n Player 2 is registered as: " + players[1])
		print("Player 1 is: " + players[0] + " |  Player 2 is: " + players[1])
		return
		
	# test if the current player has posted a valid move
	if players[currentPlayer] == author and moves != []:
		move = moves[0].split(",")
		x = int(move[0]) - 1
		y = 2 - (int(move[1]) - 1)

		print(players[currentPlayer] + " made move: " + str(x) + ", " + str(y) + ".")

		if fieldData[y][x] == "X" or fieldData[y][x] == "O":
			await message.channel.send("No Fuck you!")
			return

		if currentPlayer == 0:
			fieldData[y][x] = "O"
		else:
			fieldData[y][x] = "X"
		currentPlayer = (currentPlayer + 1) % 2
		print(fieldData)
		print("it is now " + players[currentPlayer] + "`s turn")
		await message.channel.send(displayfield(fieldData))
		return

	# Reset the game back to its State at the begining of the round
	if author in players and content == '!reset':
		players = ["", ""]
		fieldData = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
		currentPlayer = 0
		await message.channel.send("Board has been reseted!")

client.run(TOKEN)
