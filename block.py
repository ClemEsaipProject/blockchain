import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calcule le hash du bloc en utilisant ses attributs.
        """
        hash_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        ).encode()
        
        return hashlib.sha256(hash_string).hexdigest()

    def mine_block(self, difficulty):
        """
        Mine le bloc en trouvant un hash qui commence par le nombre spécifié de zéros.
        """
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        
        print(f"Block miné: {self.hash}")

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du bloc.
        """
        return (f"Block #{self.index}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Hash: {self.hash}\n"
                f"Nonce: {self.nonce}\n")