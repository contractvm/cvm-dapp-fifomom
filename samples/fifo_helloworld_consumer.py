#!/usr/bin/python3
# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from libcontractvm import Wallet, WalletExplorer, ConsensusManager
from fifomom import FIFOManager

consMan = ConsensusManager.ConsensusManager ()
consMan.addNode ("http://127.0.0.1:8181")

wallet = WalletExplorer.WalletExplorer (wallet_file='test.wallet')	
fifoMan = FIFOManager.FIFOManager (consMan, wallet=wallet)

def consume (queue, body):
	print ('[x] Received:', body)


fifoMan.consume ('helloqueue', consume)
fifoMan.startConsumer ()

