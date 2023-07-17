import pytest
import pytest_asyncio
from eth_utils import keccak

from tests.utils.constants import ZERO_ADDRESS
from tests.utils.errors import kakarot_error


@pytest_asyncio.fixture(scope="module")
async def verifier(deploy_solidity_contract, owner):
    return await deploy_solidity_contract(
        "ezkl",
        "Verifier",
        caller_eoa=owner
    )

@pytest.mark.asyncio
@pytest.mark.ezkl
# @pytest.mark.usefixtures("starknet_snapshot")
class TestVerifier:
    class TestDeploy:
        async def test_should_accept_pubinput_and_proof(self, verifier):
            assert await verifier.verify([0, 0], "0x0") == False