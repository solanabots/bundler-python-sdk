import os
import asyncio
from dotenv import load_dotenv
from predator_sdk import PredatorSDK

load_dotenv()

sdk = PredatorSDK()

async def buy_tokens():
    try:
        print('Buying tokens...')
        buy_result = await sdk.buy({
            'privateKeys': os.getenv('PRIVATE_KEYS'),
            'tokenAddress': os.getenv('TOKEN_ADDRESS'),
            'amount': os.getenv('BUY_AMOUNT'),
        })
        print('Buy successful:', buy_result)
    except Exception as error:
        print('Buy operation failed:', str(error))

async def sell_tokens():
    try:
        print('Selling tokens...')
        sell_result = await sdk.sell({
            'privateKeys': os.getenv('PRIVATE_KEYS'),
            'tokenAddress': os.getenv('TOKEN_ADDRESS'),
            'percentage': os.getenv('SELL_PERCENTAGE'),
        })
        print('Sell successful:', sell_result)
    except Exception as error:
        print('Sell operation failed:', str(error))

async def create_token():
    try:
        print('Creating a new token...')
        create_result = await sdk.create({
            'privateKeys': os.getenv('PRIVATE_KEYS'),
            'devPrivateKey': os.getenv('DEV_PRIVATE_KEY'),
            'amount': os.getenv('CREATE_AMOUNT'),
            'name': os.getenv('TOKEN_NAME'),
            'symbol': os.getenv('TOKEN_SYMBOL'),
            'description': os.getenv('TOKEN_DESCRIPTION'),
            'telegram': os.getenv('TOKEN_TELEGRAM'),
            'twitter': os.getenv('TOKEN_TWITTER'),
            'website': os.getenv('TOKEN_WEBSITE'),
            'file': os.getenv('TOKEN_LOGO_URL'),
        })
        print('Token creation successful:', create_result)
    except Exception as error:
        print('Token creation failed:', str(error))

# Uncomment the function you want to run
async def main():
    # await buy_tokens()
    # await sell_tokens()
    # await create_token()
    
    # Or run multiples
    # await create_token()
    # await buy_tokens()
    # await sell_tokens()
    pass

if __name__ == "__main__":
    asyncio.run(main())