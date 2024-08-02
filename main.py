import discord
from discord.ext import commands
import random
import io
from PIL import Image, ImageDraw, ImageFont
import json
import string

with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name="verify", description="Start the verification process")
async def verify(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(title="Verification", description="Choose the difficulty level for verification", color=0x479c85)
        embed.set_footer(text="This message will be hidden after choosing difficulty.")
        
        button_easy = discord.ui.Button(label="Easy 🟢", style=discord.ButtonStyle.primary, custom_id="difficulty_easy")
        button_medium = discord.ui.Button(label="Medium 🟡", style=discord.ButtonStyle.primary, custom_id="difficulty_medium")
        button_hard = discord.ui.Button(label="Hard 🔴", style=discord.ButtonStyle.primary, custom_id="difficulty_hard")
        
        async def difficulty_button_callback(interaction: discord.Interaction):
            difficulty = interaction.data['custom_id'].split('_')[-1]
            await interaction.response.send_message("You have selected the difficulty level.", ephemeral=True)
            
            embed2 = discord.Embed(title="Verification", description="Click the button to verify", color=0x479c85)
            embed2.set_image(url="https://files.shapes.inc/af5e4e7c.png")
            button_verify = discord.ui.Button(label="Verify", style=discord.ButtonStyle.primary, custom_id=f"verify_{difficulty}")
            
            async def verify_button_callback(interaction: discord.Interaction):
                role = discord.utils.get(interaction.guild.roles, id=int(config['role_id']))
                if role in interaction.user.roles:
                    await interaction.response.send_message("You are already verified.", ephemeral=True)
                else:
                    random_string = generate_random_string(difficulty)
                    image = create_image_with_text(random_string)
                    
                    embed3 = discord.Embed(title="Enter the text", description=f"Please enter the text shown in the image.")
                    file = discord.File(fp=image, filename="text.png")
                    embed3.set_image(url="attachment://text.png")
                    
                    button_submit = discord.ui.Button(label="Submit", style=discord.ButtonStyle.success, custom_id="submit")
                    
                    async def submit_button_callback(interaction: discord.Interaction):
                        modal = TextModal(random_string)
                        await interaction.response.send_modal(modal)
                    
                    button_submit.callback = submit_button_callback
                    view = discord.ui.View()
                    view.add_item(button_submit)
                    await interaction.response.send_message(embed=embed3, file=file, view=view, ephemeral=True)
            
            button_verify.callback = verify_button_callback
            view = discord.ui.View()
            view.add_item(button_verify)
            
            await interaction.followup.send(embed=embed2, view=view)

        for button in [button_easy, button_medium, button_hard]:
            button.callback = difficulty_button_callback
        
        view = discord.ui.View()
        view.add_item(button_easy)
        view.add_item(button_medium)
        view.add_item(button_hard)
        
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    else:
        await interaction.response.send_message("You do not have the required permissions to use this command.", ephemeral=True)

def generate_random_string(difficulty):
    if difficulty == "easy":
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])
    elif difficulty == "medium":
        return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(6)])
    elif difficulty == "hard":
        return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8)])

def create_image_with_text(text):
    width, height = 400, 200
    background_image_path = './src/bg/background.png'
    
    background_image = Image.open(background_image_path)
    background_image = background_image.resize((width, height))
    
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    image.paste(background_image, (0, 0))
    
    draw = ImageDraw.Draw(image)
    

    try:
        font = ImageFont.truetype("./src/font/font.ttf", size=60) 
    except IOError:
        font = ImageFont.load_default()
    
    text_color = (168,10,16,255) 

    bbox = draw.textbbox((0, 0), text, font=font)
    textwidth, textheight = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    x = (width - textwidth) / 2  
    y = (height - textheight) / 2.5  
    
    draw.text((x, y), text, font=font, fill=text_color)
    
    output = io.BytesIO()
    image.save(output, format='PNG')
    output.seek(0)
    
    return output

class TextModal(discord.ui.Modal, title="Enter the text"):
    def __init__(self, correct_text):
        super().__init__()
        self.correct_text = correct_text
        self.add_item(discord.ui.TextInput(label="Text", placeholder="Enter the text shown in the image"))
    
    async def on_submit(self, interaction: discord.Interaction):
        if self.children[0].value == self.correct_text:
            role = discord.utils.get(interaction.guild.roles, id=int(config['role_id']))
            if role:
                await interaction.user.add_roles(role)
                await interaction.response.send_message("Verification successful! You have been given the Verified role.", ephemeral=True)
            else:
                await interaction.response.send_message("Role not found.", ephemeral=True)
        else:
            await interaction.response.send_message("Incorrect text. Please try again.", ephemeral=True)

bot.run(config['token'])
