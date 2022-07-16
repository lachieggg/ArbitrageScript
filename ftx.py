#!/usr/bin/env python

import ftx

client = ftx.FtxClient()

result = client.get_orderbook('USDC/USD', 1)
