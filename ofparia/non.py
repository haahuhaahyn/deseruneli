from web3 import Web3

# Initialize web3. Make example to replace 'your_provider_url' with your actual provider URL.
web3 = Web3(Web3.HTTPProvider('your_provider_url'))

# Replace 'your_contract_address' with the actual contract address and 'your_abi' with the contract ABI.
contract = web3.eth.contract(address='your_contract_address', abi='your_abi')

# Set the default account - replace 'your_account_address' with the actual account address.
default_account = 'your_account_address'
web3.eth.defaultAccount = default_account

# Function to mint and stake GLP-ETH
def mint_and_stake_glp_eth(amount_in, min_glp_amount, min_lp_amount, deadline, receiver):
    # Build the transaction
    contract_txn = contract.functions.mintAndStakeGlpETH(
        amount_in,
        min_glp_amount,
        min_lp_amount,
        deadline,
        receiver
    ).buildTransaction({
        'gasPrice': web3.eth.gasPrice,  # Fetch the current gas price from the network
        'gas': 1000000,  # Set the gas limit
        'nonce': web3.eth.getTransactionCount(web3.eth.defaultAccount)  # Get the nonce for the default account
    })
    return contract_txn

# Example usage:
# Replace the following values with actual data.
amount_in = 1
min_glp_amount = 1
min_lp_amount = 1
deadline = 1742680400  # Example Unix timestamp
receiver = 'receiver_address'

# Call the function with the parameters
transaction = mint_and_stake_glp_eth(amount_in, min_glp_amount, min_lp_amount, deadline, receiver)

# Output the optimized transaction
print(transaction)
