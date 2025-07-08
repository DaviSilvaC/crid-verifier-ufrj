from brownie import CridVerifier, accounts, network

def main():
    """
    Script de deploy corrigido.
    """
    print("Iniciando o deploy...")


    account = accounts[0]
    
    print(f"Conta usada para o deploy: {account.address}")

    # Parâmetros da transação
    tx_params = {'from': account}

    # Adiciona o preço do gás se estivermos na rede Hardhat
    if network.show_active() == 'hardhat':
        print("Rede Hardhat detectada. Definindo gas_price manualmente.")
        tx_params['gas_price'] = "20 gwei"

    # Faz o deploy usando os parâmetros definidos
    crid_verifier = CridVerifier.deploy(tx_params)
    
    print(f"Contrato 'CridVerifier' implantado com sucesso no endereço: {crid_verifier.address}")
    print("-----")