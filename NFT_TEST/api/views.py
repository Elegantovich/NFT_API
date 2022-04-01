from api.models import Token
from .serializers import TokenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from web3 import Web3
from .abi_code import abi
from eth_account import Account
from dotenv import load_dotenv
from .pagination import CustomPagination
import random
import string
import os

load_dotenv()

rinkeby_key = os.getenv('RINKEBY_KEY')
contract_adress = os.getenv('CONTRACT_ADRESS')
metamask_key = os.getenv('METAMASK_KEY')

"""Connect to provider and get private credential from metamask."""
w3 = Web3(Web3.HTTPProvider(f'https://rinkeby.infura.io/v3/{rinkeby_key}'))
acct = Account.privateKeyToAccount(metamask_key)
key = acct.privateKey
myContract = w3.eth.contract(address=contract_adress, abi=abi)


class APITokenList(APIView, CustomPagination):

    def get(self, request):
        """Get all objects of Token's model."""
        tokens = Token.objects.all()
        results = self.paginate_queryset(tokens, request, view=self)
        serializer = TokenSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)


def create_hash():
    """Create unique code."""
    letters = string.ascii_lowercase + string.digits
    code = ''.join(random.choice(letters) for i in range(20))
    return code


class APIToken(APIView):

    def post(self, request):
        """Input 3 items, which will send on test-etherscan."""
        media_url = request.data.get('media_url')
        owner = request.data.get('owner')
        unique_hash = create_hash()
        acct = Account.privateKeyToAccount(key)
        private_key = acct.privateKey
        nonce = w3.eth.getTransactionCount(acct.address)
        unicorn_txn = myContract.functions.mint(
            owner,
            unique_hash,
            media_url).buildTransaction({
                'chainId': 4,
                'gas': 280000,
                'maxFeePerGas': w3.toWei('2', 'gwei'),
                'maxPriorityFeePerGas': w3.toWei('1', 'gwei'), 'nonce': nonce})
        unicorn_txn.pop('gasPrice')
        signed = w3.eth.account.sign_transaction(unicorn_txn,
                                                 private_key=private_key)
        w3.eth.sendRawTransaction(signed.rawTransaction)
        tx_hash = w3.toHex(w3.keccak(signed.rawTransaction))
        data = {'media_url': media_url,
                'owner': owner,
                'unique_hash': unique_hash,
                'tx_hash': tx_hash}
        serializer = TokenSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APITotalSupply(APIView):

    def get(self, request):
        """Get total supply."""
        response = myContract.functions.totalSupply().call()
        return Response({'response': response})
