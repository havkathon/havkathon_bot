import keepalive
import discord
import asyncio
import ast
from discord.ext import commands
import random
client = commands.Bot(command_prefix = '-')
# DO NOT TOUCH ANYTHING ABOVE THIS

with open('leaderboard.txt', 'r') as lead:
    leader = ast.literal_eval(lead.readline())

fact1 = discord.Embed(
    title = 'The concentration of CO2 in our atmosphere has reached an all time high in 2020, reaching over 400 ppm.',
    description = 'Source: <https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know>'
)
fact2 = discord.Embed(
    title = 'There are currently 189 countries who have signed the Paris Agreement!',
    description = 'Source: <https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know>'
)
fact3 = discord.Embed(
    title = 'Climate change directly affects the livelihood of human beings.'
)
fact4 = discord.Embed(
    title = 'Short term temperature fluctuations caused by climate change can impact human health.',
    description = 'Source: <https://www.who.int/features/factfiles/climate_change/facts/en/index2.html>'
)
fact5 = discord.Embed(
    title = 'Rising sea levels is a key impact of climate change, and greatly increases the chance of flooding, threatening more than half of the world’s population.',
    description = 'Source: <https://www.who.int/features/factfiles/climate_change/facts/en/index2.html>'
)
fact6 = discord.Embed(
    title = 'Water and food supply may be affected by climate change, due to reasons such as variable rainfall patterns. Malnutrition and water scarcity are the consequences.',
    description = 'Source: <https://www.who.int/features/factfiles/climate_change/facts/en/index2.html>'
)
fact7 = discord.Embed(
    title = 'The greenhouse effect is natural and vital to our survival, but when the concentration of greenhouse gases in our atmosphere increases unnaturally, it causes climate change.'
)
fact8 = discord.Embed(
    title = 'Global temperature has increased by 2°C since 1880, which causes a much larger impact than you would expect.',
    description = 'The image shows the overall teperature change in recent years.\n\nSources: <https://climate.nasa.gov/>\n<http://imbie.org/data-downloads/>'
)
fact8.set_image(url = 'https://havkathon.000webhostapp.com/Global_Temperature_Trend.png')
fact9 = discord.Embed(
    title = 'Rising sea levels are caused by melting glaciers and ice sheets on land and thermal expansion - the expansion of water as it warms. Both of these phenomena are closely related to global warming.',
    description = 'The image shows the cumulative ice melt from Antartica, showing its overall impact on climate change.\n\nSources: <https://www.jpl.nasa.gov/edu/teach/activity/graphing-sea-level-trends/>\n<http://imbie.org/data-downloads/>'
)
fact9.set_image(url = 'https://havkathon.000webhostapp.com/Antartica_Cumalative_Sea_Level_Contribution.png')
fact10 = discord.Embed(
    title = 'Climate change has caused a significant impact on natural disasters - weather is becoming more and more extreme, with a record-breaking number of hottest days in recent years and intensifying hurricanes and even snowstorms.',
    description = 'Source: <https://www.jpl.nasa.gov/edu/news/2019/10/18/nasas-eyes-on-extreme-weather/>'
)
act1 = discord.Embed(
    title = 'Ride a bike or walk to work/school if it is close enough. If not, opt to take public transport to reduce emission of greenhouse gases.'
)
act2 = discord.Embed(
    title = 'Use less electricity by reconsidering every time you switch on an electrical appliance. Do you really need the air conditioner when it is 25°C/77°F outside?'
)
act3 = discord.Embed(
    title = 'Stop thinking that your contribution is too small to make a change. How you act can affect people around you, and it all adds up.',
    description = 'Source: <https://davidsuzuki.org/what-you-can-do/top-10-ways-can-stop-climate-change/>'
)
act4 = discord.Embed(
    title = 'Change some eating habits. Eating less meat, buying local produce and not wasting food are all impactful on climate change.',
    description = 'Source: <https://davidsuzuki.org/what-you-can-do/top-10-ways-can-stop-climate-change/>'
)
act5 = discord.Embed(
    title = 'Support organisations combating climate change. These organisations likely have power and tools for your help to be more effective!',
    description = 'Source: <https://davidsuzuki.org/what-you-can-do/top-10-ways-can-stop-climate-change/>'
)
act6 = discord.Embed(
    title = 'Spread awareness for climate change. Just casually mentioning the importance of conserving electricity to your friends can make a difference.',
    description = 'Source: <https://davidsuzuki.org/what-you-can-do/top-10-ways-can-stop-climate-change/>'
)
act7 = discord.Embed(
    title = 'Using more energy-efficient electrical appliances (or using fewer in the first place) and choosing public transport over private transport (or simply using less fuel-reliant methods of transport, such as riding a bicycle) help mitigate climate change.',
    description = 'Source: <https://earthobservatory.nasa.gov/blogs/climateqa/what-can-we-do-about-global-warming-2/>'
)
question1 = discord.Embed(
    title = 'Which of the following about LED light bulbs is not true?',
    description = '1. LED light bulbs last longer than incandescent bulbs\n2. LED light bulbs are less likely to break\n3. LED light bulbs can maintain the same brightness until the point it dies\n4. LED light bulbs are not affected by frequently switching between on/off\n\nType the option number to answer!\n\nSource: <https://thesmartcave.com/led-vs-cfl/>'
)
question2 = discord.Embed(
    title = 'Why does eating less meat help with climate change?', description = '1. Rearing livestock emits greenhouse gases\n2. Cooking meat produces greenhouse gases\n3. The packaging of meat increases greenhouse gas concentration\n\nType the option number to answer!'
)
question3 = discord.Embed(
    title = 'Which of the following is not a greenhouse gas?',
    description = '1. Methane\n2. Carbon dioxide\n3. Water vapour\n4. Carbon monoxide\n\nType the option number to answer!\n\nSource: <https://en.wikipedia.org/wiki/Greenhouse_gas>'
)
question4 = discord.Embed(
  title = 'True or false: The CO2 concentration in the atmosphere has been fluctuating long before humans started excessively producing it.', 
  description = '1. True\n2. False\n\nType the option number to answer!\n\nSource: <https://climate.nasa.gov/vital-signs/carbon-dioxide/>'
)
question5 = discord.Embed(
    title = 'Which one of these is not a side effect of global warming?',
    description = '1. More frequent natural disasters\n2. Some animals losing their habitats\n3. Lower sea level\n4. More water evaporation\n\nType the option number to answer!\n\n'
)
question6 = discord.Embed(
    title = 'Which of these human activities do not release greenhouse gases into the atmosphere?',
    description = '1. Eating rice\n2. Concrete production\n3. Eating seafood\n4. None of the above\n\nType the option number to answer!\n\nSource: <https://edition.cnn.com/2019/06/03/world/gallery/surprising-sources-greenhouse-gas-emissions-intl/index.html>'
)
question7 = discord.Embed(
    title = 'How much has the global sea level risen since 1993? (As of March 2020)',
    description = '1. around 30mm\n2. around 50mm\n3. around 70mm\n4. around 90mm\n\nType the option number to answer!\n\nSource: <https://www.jpl.nasa.gov/edu/teach/activity/graphing-sea-level-trends/>'
)
question8 = discord.Embed(
    title = 'Which of the following does not contribute to rising sea levels?',
    description = '1. Melting sea ice\n2. Increased amount of hurricanes\n3. Thermal expansion\n4. Melting glaciers on land\n\nType the option number to answer!\n\nSource: <https://www.jpl.nasa.gov/edu/teach/activity/graphing-sea-level-trends/>'
)
helpmsg = discord.Embed(
    title = 'About Me:',
    description = 'Hello! I am Havkathon-Bot and I am here to spread facts and awareness regarding climate change.\n\nMy prefix is `-`.\n\n__Commands:__\n`-fact`: I will give you a random fact about climate change!\n`-act`: Want to combat climate change? I can suggest a simple action that will make a difference.\n`-trivia`: Answer a random trivia question to learn more about climate change or actions to counter it.\n`-leaderboard`: Shows leaderboard for the trivia.\n`-remove`: Removes yourself from the leaderboard. This resets your score.\n`-website`: Gives link to our website and machine learning data, which contains information regarding climate change and relevant issues.\n`-invite`: Provides link for inviting me to your server!\n`-helpMessage`: Generates this help list!\n\nThank you for using this bot, let\'s fight climate change together!'
)
havkathonLink = discord.Embed(
    title = 'Link to our webpage and Machine Learning data:',
    description = 'https://1earth1lifetime.weebly.com/\nhttps://rpubs.com/havkathon/670274'
)
havkathonLink.set_image(url = 'https://havkathon.000webhostapp.com/havkathongreenheroes.jpg')
inviteLink = discord.Embed(
    title = 'Invite Havkathon-Bot to your server:',
    description = '<https://discord.com/api/oauth2/authorize?client_id=761984202686070795&permissions=19456&scope=bot>\n\n__The Havkathon-Bot Server:__\n<https://discord.gg/rPFJ9cr>'
)
inviteLink.set_image(url = 'https://havkathon.000webhostapp.com/havkathongreenheroes.jpg')

facts = [fact1, fact2, fact3, fact4, fact5, fact6, fact7, fact8, fact9, fact10]
acts = [act1, act2, act3, act4, act5, act6, act7]

questions = {0: '3', 1: '1', 2: '4', 3: '1', 4: '3', 5: '4', 6: '4', 7: '2'}
questionArr = [question1, question2, question3, question4, question5, question6, question7, question8]

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "us combat climate change together!"))

@client.command()
async def invite(ctx):
    global inviteLink
    inviteLink.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.channel.send(embed = inviteLink)

@client.command()
async def leaderboard(ctx):
    global leader
    with open('leaderboard.txt', 'r') as lead:
        leader = ast.literal_eval(lead.readline())
    leader = sorted(leader.items(), key = lambda x : x[1], reverse = True)
    tex = ''
    x = 0
    for i in leader:
        tex = tex + str(x + 1) + ' - `' + str(i[0]) + '`: ' + str(i[1]) + '\n'
        x += 1
        if (x == 10):
            break
    leadboard = discord.Embed(
        title = 'Havkathon Trivia Leaderboard:',
        description = tex
    )
    leadboard.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.channel.send(embed = leadboard)

@client.command()
async def website(ctx):
    global havkathonLink
    havkathonLink.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.channel.send(embed = havkathonLink) 

@client.command()
async def helpMessage(ctx):
    global helpmsg
    helpmsg.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.channel.send(embed = helpmsg)

@client.command()
async def fact(ctx):
    global facts
    n = random.randint(0, len(facts) - 1)
    facts[n].set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.channel.send(embed = facts[n])

@client.command()
async def act(ctx):
    global acts
    n = random.randint(0, len(acts) - 1)
    acts[n].set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.channel.send(embed = acts[n])

@client.command()
async def trivia(ctx):
    n = random.randint(0, len(questionArr) - 1)
    attempts = 0
    questionArr[n].set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.channel.send(embed = questionArr[n])
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        msg = await client.wait_for('message', timeout = 60.0, check = check)
        while (msg.content != questions[n]):
            try:
                attempts += 1
                await ctx.channel.send('Wrong answer or format, try again!')
                msg = await client.wait_for('message', timeout = 60.0, check = check)
            except asyncio.TimeoutError:
                await ctx.channel.send('Trivia game cancelled - sorry, you took too long.')
                break
        if (msg.content == questions[n]):
            await ctx.channel.send('You are correct! Good work :star_struck:')
        if (msg.content == questions[n]) and (attempts == 0):
            with open('leaderboard.txt', 'r') as lead:
                leader = ast.literal_eval(lead.readline())
            if (ctx.author.name not in leader):
                await ctx.channel.send('Would you like to be on the leaderboard? Your username will be recorded. Type `Yes` to agree or `No` to disagree.')
                y = await client.wait_for('message', timeout = 60.0, check = check)
                if (y.content.lower() == 'yes'):
                    try:
                        with open('leaderboard.txt', 'r') as lead:
                            leader = ast.literal_eval(lead.readline())
                        leader[ctx.author.name] = 0
                        with open('leaderboard.txt', 'w') as lead:
                            lead.write(str(leader))
                    except asyncio.TimeoutError:
                        await ctx.channel.send('Leaderboard status cancelled - sorry, you took too long.')
                elif (y.content.lower() == 'no'):
                    await ctx.channel.send('Leaderboard status cancelled.')
            with open('leaderboard.txt', 'r') as lead:
                leader = ast.literal_eval(lead.readline())
            if (ctx.author.name in leader):
                with open('leaderboard.txt', 'r') as lead:
                    leader = ast.literal_eval(lead.readline())
                leader[ctx.author.name] += 1
                await ctx.channel.send('Your current score is ' + str(leader[ctx.author.name]))
                with open('leaderboard.txt', 'w') as lead:
                    lead.write(str(leader))
    except asyncio.TimeoutError:
        await ctx.channel.send('Sorry, you took too long!')

@client.command()
async def remove(ctx):
    global leader
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    with open('leaderboard.txt', 'r') as lead:
        leader = ast.literal_eval(lead.readline())
    if (ctx.author.name not in leader):
        await ctx.channel.send('You are not on the leaderboard.')
    elif (ctx.author.name in leader):
        x = leader[ctx.author.name]
        await ctx.channel.send('Are you sure you want to remove yourself from the leaderboard? Your score of ' + str(x) + ' will be removed. Type `Yes` to agree or `No` to disagree.')
        y = await client.wait_for('message', timeout = 60.0, check = check)
        if (y.content.lower() == 'yes'):
            try:
                with open('leaderboard.txt', 'r') as lead:
                    leader = ast.literal_eval(lead.readline())
                leader.pop(ctx.author.name)
                await ctx.channel.send('Leaderboard status removed.')
                with open('leaderboard.txt', 'w') as lead:
                    lead.write(str(leader))
            except asyncio.TimeoutError:
                    await ctx.channel.send('You are still on the leaderboard - sorry, you took too long.')
        elif (y.content.lower() == 'no'):
            await ctx.channel.send('You are still on the leaderboard.') 
        
# DO NOT TOUCH ANYTHING BELOW THIS
keepalive.keepalive()
client.run('[REDACTED]')
