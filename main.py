from blockchain import *
from block import *
import time

def main():
    # Créer une nouvelle blockchain
    my_blockchain = Blockchain()
    previous_hash = my_blockchain.get_latest_block().hash

    # Ajouter quelques blocs
    my_blockchain.add_block(Block(len(my_blockchain.chain), time.time(), {"amount": 4}, previous_hash))
    

    # Afficher la blockchain
    print(my_blockchain)

    # Vérifier la validité de la chaîne
    print(f"\nLa blockchain est valide : {my_blockchain.is_chain_valid()}")

if __name__ == "__main__":
    main()