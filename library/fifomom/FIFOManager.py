# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import time
from libcontractvm import Wallet, ConsensusManager, DappManager

class FIFOManager (DappManager.DappManager):
	def __init__ (self, consensusManager, wallet = None):
		super (FIFOManager, self).__init__(consensusManager, wallet)
		self.consumers = {}

	def publish (self, queue, body):
		cid = self.produceTransaction ('fifomom.publish_message', [queue, body])

	def consume (self, queue, callback):
		self.consumers [queue] = {'call': callback, 'last': 0}

	def startConsumer (self):
		while True:
			for queue in self.consumers:
				new_ms = self.consensusManager.jsonConsensusCall ('fifomom.get_messages', [queue, self.consumers[queue]['last']])['result']
				for message in new_ms['messages']:
					self.consumers[queue]['call'](queue, message)
				self.consumers [queue]['last'] = new_ms ['size']
			time.sleep (15)
