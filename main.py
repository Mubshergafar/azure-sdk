from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

# Replace with your Azure subscription ID
subscription_id = '0241201a-791f-4165-96fc-8d55c1c1cb31'

# Define the resource group and storage account details
resource_group_name = 'myResourceGroup'
storage_account_name = 'mystorage7472bash'  # Must be globally unique
location = 'eastus'

# Authenticate using DefaultAzureCredential
credential = DefaultAzureCredential()

# Create clients
resource_client = ResourceManagementClient(credential, subscription_id)
storage_client = StorageManagementClient(credential, subscription_id)

async def main():
    try:
        # Create or update the resource group
        print(f"Creating resource group: {resource_group_name}")
        resource_client.resource_groups.create_or_update(resource_group_name, {
            'location': location
        })
        print(f"Resource group created successfully: {resource_group_name}")

        # Define the parameters for the storage account
        storage_account_params = {
            'sku': {'name': 'Standard_LRS'},
            'kind': 'StorageV2',
            'location': location,
            'access_tier': 'Hot'
        }

        # Create the storage account
        print(f"Creating storage account: {storage_account_name}")
        result = storage_client.storage_accounts.begin_create(
            resource_group_name,
            storage_account_name,
            storage_account_params
        ).result()
        print('Storage account created successfully:', result)
    except Exception as err:
        print('Error creating resources:', err)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
