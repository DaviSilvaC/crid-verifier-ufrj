import pytest
from brownie import CridVerifier, accounts, exceptions
from brownie.network import gas_price  # Importamos a função para definir o gás

@pytest.fixture
def crid_verifier():
    # --- CORREÇÃO FINAL ---
    # Define um preço de gás padrão para TODAS as transações nesta sessão de teste.
    gas_price("20 gwei")
    
    # Agora o Brownie usará este preço padrão para todas as transações,
    # incluindo o deploy abaixo.
    return CridVerifier.deploy({'from': accounts[0]})

def test_deployment_sets_owner(crid_verifier):
    assert crid_verifier.owner() == accounts[0]

def test_owner_can_register_crid(crid_verifier):
    owner_account = accounts[0]
    dre = "123456789".encode('utf-8')
    semester = "2025.1".encode('utf-8')
    doc_hash = "0x" + "a" * 64

    # Esta chamada agora herdará o gas_price padrão definido na fixture.
    crid_verifier.registerCrid(dre, semester, doc_hash, {'from': owner_account})
    
    assert crid_verifier.cridHashes(dre, semester) == doc_hash

def test_non_owner_cannot_register_crid(crid_verifier):
    non_owner_account = accounts[1]
    dre = "987654321".encode('utf-8')
    semester = "2025.1".encode('utf-8')
    doc_hash = "0x" + "b" * 64

    with pytest.raises(exceptions.VirtualMachineError):
        # Esta chamada também herdará o gas_price padrão.
        crid_verifier.registerCrid(dre, semester, doc_hash, {'from': non_owner_account})

# (Mantenha todo o código que você já tem no arquivo e adicione estas duas funções no final)

# Teste 4 (NOVO): Sucesso na verificação
def test_verify_crid_success(crid_verifier):
    """
    Testa se a verificação retorna 'true' para um CRID registrado corretamente.
    """
    owner_account = accounts[0]
    dre = "111222333".encode('utf-8')
    semester = "2025.2".encode('utf-8')
    doc_hash = "0x" + "c" * 64

    # 1. Registra o hash primeiro
    crid_verifier.registerCrid(dre, semester, doc_hash, {'from': owner_account})

    # 2. Verifica com os dados corretos e espera 'true'
    assert crid_verifier.verifyCrid(dre, semester, doc_hash) is True

# Teste 5 (NOVO): Falha na verificação
def test_verify_crid_failure(crid_verifier):
    """
    Testa se a verificação retorna 'false' para um hash incorreto.
    """
    owner_account = accounts[0]
    dre = "444555666".encode('utf-8')
    semester = "2025.2".encode('utf-8')
    correct_hash = "0x" + "d" * 64
    wrong_hash = "0x" + "e" * 64

    # 1. Registra o hash correto
    crid_verifier.registerCrid(dre, semester, correct_hash, {'from': owner_account})

    # 2. Verifica com um hash incorreto e espera 'false'
    assert crid_verifier.verifyCrid(dre, semester, wrong_hash) is False