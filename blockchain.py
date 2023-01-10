import datetime
import hashlib
import json
from flask import Flask, jsonify

#Genisis Block
#initialize chain (in it Function)
#create block function
#tools for chain

class Blockchain :

#Building a Blockchain
  def __init__(self):
    self.chain = []
    self.create_block(proof = 1, previous_hash = '0')

  def create_block(self, proof, previous_hash):
    block = {'index': len(self.chain) +1,
             'timestamp': str(datetime.datetime.now()),
             'proof': proof,
             'previous_has': previous_hash}
    self.chain.append(block)
    return block

  def get_previous_block(self):
    return self.chain[-1]

#Mining our Blockchain