# PredatorSDK

PredatorSDK is a Python library for interacting with the Predator Bundler API. It provides a simple interface for buying, selling, and creating tokens on Raydium, Moonshot and pumpfun.

## Installation

To use PredatorSDK, you can use git:

```
git clone https://github.com/solanabots/bundler-python-sdk
```

Install requirements

```
pip install -r requirements 
```
or 
```
pip3 install -r requirements 
```
## Usage

First, import the SDK and create an instance:

```python
from predator_sdk import PredatorSDK

sdk = PredatorSDK()
```

### Initialization

The SDK needs to be initialized before making any API calls. This is done automatically when you call any of the main methods (`buy`, `sell`, `create`), but you can also do it manually:

```python
await sdk.initialize()
```

### Buying Tokens

To buy tokens:

```python
try:
    result = await sdk.buy({
        'privateKeys': 'your_private_keys',
        'tokenAddress': 'token_address',
        'amount': 'amount_to_buy',
    })
    print('Buy successful:', result)
except Exception as error:
    print('Buy operation failed:', str(error))
```

### Selling Tokens

To sell tokens:

```python
try:
    result = await sdk.sell({
        'privateKeys': 'your_private_keys',
        'tokenAddress': 'token_address',
        'percentage': 'percentage_to_sell',
    })
    print('Sell successful:', result)
except Exception as error:
    print('Sell operation failed:', str(error))
```

Note: The `percentage` must be a number between 0 and 100.

### Creating a New Token

To create a new token:

```python
try:
    result = await sdk.create({
        'privateKeys': 'your_private_keys',
        'devPrivateKey': 'dev_private_key',
        'amount': 'token_amount',
        'name': 'token_name',
        'symbol': 'token_symbol',
        'description': 'token_description',
        'telegram': 'telegram_link',
        'twitter': 'twitter_link',
        'website': 'website_link',
        'file': 'logo_file_url',
    })
    print('Token creation successful:', result)
except Exception as error:
    print('Token creation failed:', str(error))
```

## Error Handling

All methods can raise exceptions. It's recommended to wrap API calls in try-except blocks to handle potential errors.

## Security

The SDK uses encryption to secure data sent to the API. The encryption key is automatically retrieved from the server during initialization.

## Environment Variables

For security reasons, it's recommended to use environment variables for sensitive information like private keys. You can use a library like `python-dotenv` to load environment variables from a `.env` file:

```python
from dotenv import load_dotenv
import os

load_dotenv()

private_keys = os.getenv('PRIVATE_KEYS')
```
## Fees

To guarantee transactions a successful landing our api will charge 0.005 SOL each successful request + 2.5% of SOL bought or sold. This will cover any blockchain fee.

## Asynchronous Operation

The SDK uses asynchronous methods. Make sure to use `await` when calling SDK methods and run your code in an asynchronous context.

## Example

Here's a complete example of how to use the SDK:

```python
import asyncio
from predator_sdk import PredatorSDK
import os
from dotenv import load_dotenv

load_dotenv()

sdk = PredatorSDK()

async def main():
    try:
        buy_result = await sdk.buy({
            'privateKeys': os.getenv('PRIVATE_KEYS'),
            'tokenAddress': os.getenv('TOKEN_ADDRESS'),
            'amount': os.getenv('BUY_AMOUNT'),
        })
        print('Buy successful:', buy_result)

        sell_result = await sdk.sell({
            'privateKeys': os.getenv('PRIVATE_KEYS'),
            'tokenAddress': os.getenv('TOKEN_ADDRESS'),
            'percentage': os.getenv('SELL_PERCENTAGE'),
        })
        print('Sell successful:', sell_result)

    except Exception as error:
        print('Operation failed:', str(error))

if __name__ == "__main__":
    asyncio.run(main())
```

## Disclaimer

This SDK is for educational purposes only. Always ensure you're complying with all relevant laws and regulations when trading cryptocurrencies or creating tokens.
