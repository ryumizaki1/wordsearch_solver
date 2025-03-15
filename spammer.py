# Created by : @OchoOcho21
from telethon import TelegramClient
import asyncio
from rich import print
from rich.panel import Panel
from rich.progress import track
from rich.table import Table
from rich.text import Text

# Replace these with your own values
api_id = 'your_api_id'
api_hash = 'your_api_hash'
phone_number = 'your_phone_number'

async def spam_messages(message, count, channel_link):
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.connect()
        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            client.sign_in(phone_number, input('Enter the code: '))

        # Display all information in a rich table
        table = Table(title="Spamming Configuration", title_style="bold magenta")
        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="cyan", no_wrap=True)
        table.add_row("API ID", api_id)
        table.add_row("API Hash", api_hash)
        table.add_row("Phone Number", phone_number)
        table.add_row("Channel Link", channel_link)
        table.add_row("Message", message)
        table.add_row("Number of Messages", str(count))
        print(table)

        for _ in track(range(count), description="Sending messages..."):
            await client.send_message(channel_link, message)
            print(f'[bold green]Sent message: {message}[/bold green]')
            await asyncio.sleep(1)  # Delay to avoid hitting rate limits

if __name__ == "__main__":
    # Create a rich table for inputs
    input_table = Table(title="Spamming Inputs", title_style="bold magenta")
    input_table.add_column("Field", style="cyan", no_wrap=True)
    input_table.add_column("Value", style="cyan", no_wrap=True)

    # Get inputs using rich table
    channel_link = input(Text.from_markup("[bold blue]Enter the Telegram channel link: [/bold blue]"))
    input_table.add_row("Channel Link", channel_link)
    message_to_send = input(Text.from_markup("[bold blue]Enter the message you want to spam: [/bold blue]"))
    input_table.add_row("Message", message_to_send)
    number_of_times = int(input(Text.from_markup("[bold blue]Enter the number of times to send the message: [/bold blue]")))
    input_table.add_row("Number of Messages", str(number_of_times))
    print(input_table)  # Print the input table

    loop = asyncio.get_event_loop()
    loop.run_until_complete(spam_messages(message_to_send, number_of_times, channel_link))
