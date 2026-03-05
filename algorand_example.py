from algosdk import account

private_key, address = account.generate_account()

print("Address:", address)
print("Private key:", private_key)
