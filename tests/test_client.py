import unittest
from b2binpay import client as cl
from tests.config_test import *
import asyncio



class TestClient(unittest.TestCase):

    def test_connection(self):
        loop = asyncio.get_event_loop()

        new_client = loop.run_until_complete(cl.AsyncClient.create(API_KEY, API_SEC))

        loop.run_until_complete(new_client.close_connection())

        self.assertIsNotNone(new_client._access_token)

    def test_get_wallets(self):
        loop = asyncio.get_event_loop()

        new_client = loop.run_until_complete(cl.AsyncClient.create(API_KEY, API_SEC))
        wallets = loop.run_until_complete(new_client.get_wallets())

        loop.run_until_complete(new_client.close_connection())

        self.assertNotEqual({}, wallets)

