import re
from collections import defaultdict


def parse_trace(trace_text):
    transfer_pattern = re.compile(
        r'emit Transfer\(param0: (0x[0-9a-fA-F]+), param1: (0x[0-9a-fA-F]+), param2: (\d+ \[.*?\])\)')

    balance_changes = defaultdict(int)

    for match in transfer_pattern.finditer(trace_text):
        from_address = match.group(1)
        to_address = match.group(2)
        value_str = match.group(3)

        value = int(re.search(r'\d+', value_str).group(0))

        balance_changes[from_address] -= value
        balance_changes[to_address] += value

    return balance_changes


trace_text = """
Executing previous transactions from the block.
Traces:
  [690506] 0x84452042cB7be650BE4eB641025ac3C8A0079b67::start()
    ├─ [2465] 0xEc6557348085Aa57C72514D67070dC863C0a5A8c::token0() [staticcall]
    │   └─ ← [Return] 0x00000000000000000000000055d398326f99059ff775485246999027b3197955
    ├─ [2397] 0xEc6557348085Aa57C72514D67070dC863C0a5A8c::token1() [staticcall]
    │   └─ ← [Return] 0x0000000000000000000000008ac76a51cc950d9822d68b83fe1ad97b32cd580d
    ├─ [2638] 0x55d398326f99059fF775485246999027B3197955::allowance(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000000
    ├─ [22462] 0x55d398326f99059fF775485246999027B3197955::approve(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 115792089237316195423570985008687907853269984665640564039457584007913129639935 [1.157e77])
    │   ├─ emit Approval(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param2: 115792089237316195423570985008687907853269984665640564039457584007913129639935 [1.157e77])
    │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    ├─ [9862] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::allowance(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   ├─ [2616] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::allowance(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [delegatecall]
    │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000000
    │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000000
    ├─ [23208] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::approve(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 115792089237316195423570985008687907853269984665640564039457584007913129639935 [1.157e77])
    │   ├─ [22462] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::approve(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 115792089237316195423570985008687907853269984665640564039457584007913129639935 [1.157e77]) [delegatecall]
    │   │   ├─ emit Approval(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param2: 115792089237316195423570985008687907853269984665640564039457584007913129639935 [1.157e77])
    │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    ├─ [3362] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::allowance(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0x129bA1141A5EF746F39F4B3bb07b606b2020496A) [staticcall]
    │   ├─ [2616] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::allowance(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0x129bA1141A5EF746F39F4B3bb07b606b2020496A) [delegatecall]
    │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000000
    │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000000
    ├─ [23208] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::approve(0x129bA1141A5EF746F39F4B3bb07b606b2020496A, 115792089237316195423570985008687907853269984665640564039457584007913129639935 [1.157e77])
    │   ├─ [22462] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::approve(0x129bA1141A5EF746F39F4B3bb07b606b2020496A, 115792089237316195423570985008687907853269984665640564039457584007913129639935 [1.157e77]) [delegatecall]
    │   │   ├─ emit Approval(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0x129bA1141A5EF746F39F4B3bb07b606b2020496A, param2: 115792089237316195423570985008687907853269984665640564039457584007913129639935 [1.157e77])
    │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    ├─ [58928] 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca::depositAsset(0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, 500000000000000000 [5e17])
    │   ├─ [51685] 0x34233E37717451562EDD72dC7EdC4D0A7128C010::depositAsset(0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, 500000000000000000 [5e17]) [delegatecall]
    │   │   ├─ [3296] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::balanceOf(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   │   │   ├─ [2553] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::balanceOf(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [delegatecall]
    │   │   │   │   └─ ← [Return] 0x000000000000000000000000000000000000000000002893043b20ec265d719e
    │   │   │   └─ ← [Return] 0x000000000000000000000000000000000000000000002893043b20ec265d719e
    │   │   ├─ [14386] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::transferFrom(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 500000000000000000 [5e17])
    │   │   │   ├─ [13634] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::transferFrom(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 500000000000000000 [5e17]) [delegatecall]
    │   │   │   │   ├─ emit Transfer(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param2: 500000000000000000 [5e17])
    │   │   │   │   ├─ emit Approval(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param2: 115792089237316195423570985008687907853269984665640564039457084007913129639935 [1.157e77])
    │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   ├─ [1296] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::balanceOf(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   │   │   ├─ [553] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::balanceOf(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [delegatecall]
    │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000028930b2b7c45fa0f719e
    │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000028930b2b7c45fa0f719e
    │   │   ├─ [3076] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::decimals() [staticcall]
    │   │   │   ├─ [2336] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::decimals() [delegatecall]
    │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   ├─ emit NewAssetTransaction(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, param2: true, param3: 50000000 [5e7], param4: 1675352420 [1.675e9])
    │   │   └─ ← [Stop] 
    │   └─ ← [Return] 
    ├─ [463126] 0xEc6557348085Aa57C72514D67070dC863C0a5A8c::swap(191606635567219518304670 [1.916e23], 0, 0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0x00000000000000000000000055d398326f99059ff775485246999027b3197955000000000000000000000000000000000000000000002893043b20ec265d719e)
    │   ├─ [12871] 0x55d398326f99059fF775485246999027B3197955::transfer(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 191606635567219518304670 [1.916e23])
    │   │   ├─ emit Transfer(param0: 0xEc6557348085Aa57C72514D67070dC863C0a5A8c, param1: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param2: 191606635567219518304670 [1.916e23])
    │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   ├─ [414564] 0x84452042cB7be650BE4eB641025ac3C8A0079b67::pancakeCall(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 191606635567219518304670 [1.916e23], 0, 0x00000000000000000000000055d398326f99059ff775485246999027b3197955000000000000000000000000000000000000000000002893043b20ec265d719e)
    │   │   ├─ [1076] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::decimals() [staticcall]
    │   │   │   ├─ [336] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::decimals() [delegatecall]
    │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   ├─ [360706] 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca::swapThroughOrionPool(100000000 [1e8], 0, [0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, 0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE, 0x55d398326f99059fF775485246999027B3197955], true)
    │   │   │   ├─ [359927] 0x34233E37717451562EDD72dC7EdC4D0A7128C010::swapThroughOrionPool(100000000 [1e8], 0, [0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, 0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE, 0x55d398326f99059fF775485246999027B3197955], true) [delegatecall]
    │   │   │   │   ├─ [327433] 0x75CBb08E3C30237409Ce88DC78f2AE450ac1aE6c::4729ed3c(0000000000000000000000000000000000000000000000000000000000000060000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000d2997f29b5285ab74bbca62d26c6723a74500183000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000014000000000000000000000000000000000000000000000000000000000000000030000000000000000000000008ac76a51cc950d9822d68b83fe1ad97b32cd580d000000000000000000000000c4da120a4acf413f9af623a2b9e0a9878b6a0afe00000000000000000000000055d398326f99059ff775485246999027b3197955) [delegatecall]
    │   │   │   │   │   ├─ [2683] 0xd2997F29b5285Ab74BBCa62D26C6723A74500183::isFactory(0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d) [staticcall]
    │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000000
    │   │   │   │   │   ├─ [1076] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::decimals() [staticcall]
    │   │   │   │   │   │   ├─ [336] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::decimals() [delegatecall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   │   ├─ [1296] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::balanceOf(0x84452042cB7be650BE4eB641025ac3C8A0079b67) [staticcall]
    │   │   │   │   │   │   ├─ [553] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::balanceOf(0x84452042cB7be650BE4eB641025ac3C8A0079b67) [delegatecall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000000000006f05b59d3b20000
    │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000000000006f05b59d3b20000
    │   │   │   │   │   ├─ [1362] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::allowance(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   │   │   │   │   │   ├─ [616] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::allowance(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [delegatecall]
    │   │   │   │   │   │   │   └─ ← [Return] 0xfffffffffffffffffffffffffffffffffffffffffffffffff90fa4a62c4dffff
    │   │   │   │   │   │   └─ ← [Return] 0xfffffffffffffffffffffffffffffffffffffffffffffffff90fa4a62c4dffff
    │   │   │   │   │   ├─ [6786] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::transferFrom(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 500000000000000000 [5e17])
    │   │   │   │   │   │   ├─ [6034] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::transferFrom(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 500000000000000000 [5e17]) [delegatecall]
    │   │   │   │   │   │   │   ├─ emit Transfer(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param2: 500000000000000000 [5e17])
    │   │   │   │   │   │   │   ├─ emit Approval(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param2: 115792089237316195423570985008687907853269984665640564039456584007913129639935 [1.157e77])
    │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   │   │   ├─ [291636] 0xd2997F29b5285Ab74BBCa62D26C6723A74500183::doSwapThroughOrionPool(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, (100000000 [1e8], 0, 0xd2997F29b5285Ab74BBCa62D26C6723A74500183, true, false, true, false, true, 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, [0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, 0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE, 0x55d398326f99059fF775485246999027B3197955]))
    │   │   │   │   │   │   ├─ [1076] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::decimals() [staticcall]
    │   │   │   │   │   │   │   ├─ [336] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::decimals() [delegatecall]
    │   │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   │   │   ├─ [2425] 0x55d398326f99059fF775485246999027B3197955::decimals() [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   │   │   ├─ [2622] 0xE52cCf7B6cE4817449F2E6fA7efD7B567803E4b4::getPair(0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, 0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE) [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000008ac64fcfc483d9343ee11be2c4a2f46c329a37df
    │   │   │   │   │   │   ├─ [2517] 0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF::getReserves() [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000000000006f05b59d3b200000000000000000000000000000000000000000000000000008ac7230489e800000000000000000000000000000000000000000000000000000000000063dbd907
    │   │   │   │   │   │   ├─ [2622] 0xE52cCf7B6cE4817449F2E6fA7efD7B567803E4b4::getPair(0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE, 0x55d398326f99059fF775485246999027B3197955) [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x000000000000000000000000129ba1141a5ef746f39f4b3bb07b606b2020496a
    │   │   │   │   │   │   ├─ [2517] 0x129bA1141A5EF746F39F4B3bb07b606b2020496A::getReserves() [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000000000006f05b59d3b200000000000000000000000000000000000000000000000000008ac7230489e800000000000000000000000000000000000000000000000000000000000063dbd901
    │   │   │   │   │   │   ├─ [622] 0xE52cCf7B6cE4817449F2E6fA7efD7B567803E4b4::getPair(0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, 0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE) [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000008ac64fcfc483d9343ee11be2c4a2f46c329a37df
    │   │   │   │   │   │   ├─ [14336] 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca::safeAutoTransferFrom(0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF, 1000000000000000000 [1e18])
    │   │   │   │   │   │   │   ├─ [13581] 0x34233E37717451562EDD72dC7EdC4D0A7128C010::safeAutoTransferFrom(0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF, 1000000000000000000 [1e18]) [delegatecall]
    │   │   │   │   │   │   │   │   ├─ [8839] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::transfer(0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF, 1000000000000000000 [1e18])
    │   │   │   │   │   │   │   │   │   ├─ [8093] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::transfer(0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF, 1000000000000000000 [1e18]) [delegatecall]
    │   │   │   │   │   │   │   │   │   │   ├─ emit Transfer(param0: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param1: 0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF, param2: 1000000000000000000 [1e18])
    │   │   │   │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   │   │   │   │   │   └─ ← [Stop] 
    │   │   │   │   │   │   │   └─ ← [Return] 
    │   │   │   │   │   │   ├─ [2531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000000dcdb35558de819656376
    │   │   │   │   │   │   ├─ [622] 0xE52cCf7B6cE4817449F2E6fA7efD7B567803E4b4::getPair(0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, 0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE) [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000008ac64fcfc483d9343ee11be2c4a2f46c329a37df
    │   │   │   │   │   │   ├─ [622] 0xE52cCf7B6cE4817449F2E6fA7efD7B567803E4b4::getPair(0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE, 0x55d398326f99059fF775485246999027B3197955) [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x000000000000000000000000129ba1141a5ef746f39f4b3bb07b606b2020496a
    │   │   │   │   │   │   ├─ [140489] 0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF::swap(0, 6659986639946559786 [6.659e18], 0x129bA1141A5EF746F39F4B3bb07b606b2020496A, 0x)
    │   │   │   │   │   │   │   ├─ [70326] 0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE::transfer(0x129bA1141A5EF746F39F4B3bb07b606b2020496A, 6659986639946559786 [6.659e18])
    │   │   │   │   │   │   │   │   ├─ emit Transfer(param0: 0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF, param1: 0x129bA1141A5EF746F39F4B3bb07b606b2020496A, param2: 6659986639946559786 [6.659e18])
    │   │   │   │   │   │   │   │   ├─ [48992] 0x84452042cB7be650BE4eB641025ac3C8A0079b67::deposit()
    │   │   │   │   │   │   │   │   │   ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0x84452042cB7be650BE4eB641025ac3C8A0079b67) [staticcall]
    │   │   │   │   │   │   │   │   │   │   └─ ← [Return] 0x000000000000000000000000000000000000000000002893043b20ec265d719f
    │   │   │   │   │   │   │   │   │   ├─ [0] console::log("wh deposit amount", 191606635567219518304671 [1.916e23]) [staticcall]
    │   │   │   │   │   │   │   │   │   │   └─ ← [Stop] 
    │   │   │   │   │   │   │   │   │   ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0x84452042cB7be650BE4eB641025ac3C8A0079b67) [staticcall]
    │   │   │   │   │   │   │   │   │   │   └─ ← [Return] 0x000000000000000000000000000000000000000000002893043b20ec265d719f
    │   │   │   │   │   │   │   │   │   ├─ [40695] 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca::depositAsset(0x55d398326f99059fF775485246999027B3197955, 191606635567219518304671 [1.916e23])
    │   │   │   │   │   │   │   │   │   │   ├─ [39952] 0x34233E37717451562EDD72dC7EdC4D0A7128C010::depositAsset(0x55d398326f99059fF775485246999027B3197955, 191606635567219518304671 [1.916e23]) [delegatecall]
    │   │   │   │   │   │   │   │   │   │   │   ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   │   │   │   │   │   │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000000dcdb35558de819656376
    │   │   │   │   │   │   │   │   │   │   │   ├─ [8834] 0x55d398326f99059fF775485246999027B3197955::transferFrom(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 191606635567219518304671 [1.916e23])
    │   │   │   │   │   │   │   │   │   │   │   │   ├─ emit Transfer(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param2: 191606635567219518304671 [1.916e23])
    │   │   │   │   │   │   │   │   │   │   │   │   ├─ emit Approval(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param2: 115792089237316195423570985008687907853269984665640563847850948440693611335264 [1.157e77])
    │   │   │   │   │   │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   │   │   │   │   │   │   │   │   ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   │   │   │   │   │   │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000001056e3990aed43fc2d515
    │   │   │   │   │   │   │   │   │   │   │   ├─ [425] 0x55d398326f99059fF775485246999027B3197955::decimals() [staticcall]
    │   │   │   │   │   │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   │   │   │   │   │   │   │   ├─ emit NewAssetTransaction(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0x55d398326f99059fF775485246999027B3197955, param2: true, param3: 19160663556721 [1.916e13], param4: 1675352420 [1.675e9])
    │   │   │   │   │   │   │   │   │   │   │   └─ ← [Stop] 
    │   │   │   │   │   │   │   │   │   │   └─ ← [Return] 
    │   │   │   │   │   │   │   │   │   ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0x84452042cB7be650BE4eB641025ac3C8A0079b67) [staticcall]
    │   │   │   │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000000
    │   │   │   │   │   │   │   │   │   ├─ [0] console::log("Ed deposit amount", 0) [staticcall]
    │   │   │   │   │   │   │   │   │   │   └─ ← [Stop] 
    │   │   │   │   │   │   │   │   │   └─ ← [Stop] 
    │   │   │   │   │   │   │   │   ├─ [0] console::log("TokenA counter :", 3) [staticcall]
    │   │   │   │   │   │   │   │   │   └─ ← [Stop] 
    │   │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   │   │   │   │   ├─ [1296] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::balanceOf(0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF) [staticcall]
    │   │   │   │   │   │   │   │   ├─ [553] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::balanceOf(0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF) [delegatecall]
    │   │   │   │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000000000014d1120d7b160000
    │   │   │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000000000014d1120d7b160000
    │   │   │   │   │   │   │   ├─ [582] 0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE::balanceOf(0x8aC64Fcfc483D9343ee11BE2C4a2f46c329a37DF) [staticcall]
    │   │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000002e5a1c746f0b4ed6
    │   │   │   │   │   │   │   ├─ emit Sync(: 1500000000000000000 [1.5e18], : 3340013360053440214 [3.34e18])
    │   │   │   │   │   │   │   ├─ emit Swap(param0: 0xd2997F29b5285Ab74BBCa62D26C6723A74500183, param1: 1000000000000000000 [1e18], param2: 0, param3: 0, param4: 6659986639946559786 [6.659e18], param5: 0x129bA1141A5EF746F39F4B3bb07b606b2020496A)
    │   │   │   │   │   │   │   └─ ← [Stop] 
    │   │   │   │   │   │   ├─ [622] 0xE52cCf7B6cE4817449F2E6fA7efD7B567803E4b4::getPair(0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE, 0x55d398326f99059fF775485246999027B3197955) [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x000000000000000000000000129ba1141a5ef746f39f4b3bb07b606b2020496a
    │   │   │   │   │   │   ├─ [74969] 0x129bA1141A5EF746F39F4B3bb07b606b2020496A::swap(199519351395358266 [1.995e17], 0, 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 0x)
    │   │   │   │   │   │   │   ├─ [8071] 0x55d398326f99059fF775485246999027B3197955::transfer(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, 199519351395358266 [1.995e17])
    │   │   │   │   │   │   │   │   ├─ emit Transfer(param0: 0x129bA1141A5EF746F39F4B3bb07b606b2020496A, param1: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param2: 199519351395358266 [1.995e17])
    │   │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   │   │   │   │   ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0x129bA1141A5EF746F39F4B3bb07b606b2020496A) [staticcall]
    │   │   │   │   │   │   │   │   └─ ← [Return] 0x000000000000000000000000000000000000000000000000042b858ed1f569c6
    │   │   │   │   │   │   │   ├─ [582] 0xC4da120a4Acf413F9AF623a2B9E0A9878B6A0aFE::balanceOf(0x129bA1141A5EF746F39F4B3bb07b606b2020496A) [staticcall]
    │   │   │   │   │   │   │   │   └─ ← [Return] 0x000000000000000000000000000000000000000000000000e7342994a4c4b12a
    │   │   │   │   │   │   │   ├─ emit Sync(: 300480648604641734 [3.004e17], : 16659986639946559786 [1.665e19])
    │   │   │   │   │   │   │   ├─ emit Swap(param0: 0xd2997F29b5285Ab74BBCa62D26C6723A74500183, param1: 0, param2: 6659986639946559786 [6.659e18], param3: 199519351395358266 [1.995e17], param4: 0, param5: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca)
    │   │   │   │   │   │   │   └─ ← [Stop] 
    │   │   │   │   │   │   ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000001056e3c55849f417f6b4f
    │   │   │   │   │   │   ├─ emit OrionPoolSwap(: 0x837962b686Fd5A407fb4e5f92E8Be86A230484Bd, : 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d, : 0x55d398326f99059fF775485246999027B3197955, : 1000000000000000000 [1e18], : 1000000000000000000 [1e18], : 0, : 191606835086570913662937 [1.916e23], : 0xE52cCf7B6cE4817449F2E6fA7efD7B567803E4b4)
    │   │   │   │   │   │   ├─ [1076] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::decimals() [staticcall]
    │   │   │   │   │   │   │   ├─ [336] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::decimals() [delegatecall]
    │   │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   │   │   ├─ [425] 0x55d398326f99059fF775485246999027B3197955::decimals() [staticcall]
    │   │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000000116d31bbf3b1
    │   │   │   │   │   ├─ [425] 0x55d398326f99059fF775485246999027B3197955::decimals() [staticcall]
    │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   │   ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   │   │   │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000001056e3c55849f417f6b4f
    │   │   │   │   │   ├─ [3271] 0x55d398326f99059fF775485246999027B3197955::transfer(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 191606835086570000000000 [1.916e23])
    │   │   │   │   │   │   ├─ emit Transfer(param0: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param1: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param2: 191606835086570000000000 [1.916e23])
    │   │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   │   └─ ← [Stop] 
    │   │   │   └─ ← [Return] 
    │   │   ├─ [425] 0x55d398326f99059fF775485246999027B3197955::decimals() [staticcall]
    │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   ├─ [1676] 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca::getBalance(0x55d398326f99059fF775485246999027B3197955, 0x84452042cB7be650BE4eB641025ac3C8A0079b67) [staticcall]
    │   │   │   ├─ [930] 0x34233E37717451562EDD72dC7EdC4D0A7128C010::getBalance(0x55d398326f99059fF775485246999027B3197955, 0x84452042cB7be650BE4eB641025ac3C8A0079b67) [delegatecall]
    │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000116d308b8271
    │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000116d308b8271
    │   │   ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca) [staticcall]
    │   │   │   └─ ← [Return] 0x00000000000000000000000000000000000000000000dcdb35558de84fdac74f
    │   │   ├─ [31528] 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca::withdraw(0x55d398326f99059fF775485246999027B3197955, 191606635567210000000000 [1.916e23])
    │   │   │   ├─ [30785] 0x34233E37717451562EDD72dC7EdC4D0A7128C010::withdraw(0x55d398326f99059fF775485246999027B3197955, 191606635567210000000000 [1.916e23]) [delegatecall]
    │   │   │   │   ├─ [425] 0x55d398326f99059fF775485246999027B3197955::decimals() [staticcall]
    │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000012
    │   │   │   │   ├─ [3271] 0x55d398326f99059fF775485246999027B3197955::transfer(0x84452042cB7be650BE4eB641025ac3C8A0079b67, 191606635567210000000000 [1.916e23])
    │   │   │   │   │   ├─ emit Transfer(param0: 0xe9d1D2a27458378Dd6C6F0b2c390807AEd2217Ca, param1: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param2: 191606635567210000000000 [1.916e23])
    │   │   │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   │   │   ├─ emit NewAssetTransaction(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0x55d398326f99059fF775485246999027B3197955, param2: false, param3: 19160663556721 [1.916e13], param4: 1675352420 [1.675e9])
    │   │   │   │   └─ ← [Stop] 
    │   │   │   └─ ← [Return] 
    │   │   ├─ [3271] 0x55d398326f99059fF775485246999027B3197955::transfer(0xEc6557348085Aa57C72514D67070dC863C0a5A8c, 192183185122587280145106 [1.921e23])
    │   │   │   ├─ emit Transfer(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0xEc6557348085Aa57C72514D67070dC863C0a5A8c, param2: 192183185122587280145106 [1.921e23])
    │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    │   │   └─ ← [Stop] 
    │   ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0xEc6557348085Aa57C72514D67070dC863C0a5A8c) [staticcall]
    │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000368ee0c5986787c2263d9
    │   ├─ [3296] 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d::balanceOf(0xEc6557348085Aa57C72514D67070dC863C0a5A8c) [staticcall]
    │   │   ├─ [2553] 0xBA5Fe23f8a3a24BEd3236F05F2FcF35fd0BF0B5C::balanceOf(0xEc6557348085Aa57C72514D67070dC863C0a5A8c) [delegatecall]
    │   │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000368ad4f65a43ae66ffb9e
    │   │   └─ ← [Return] 0x0000000000000000000000000000000000000000000368ad4f65a43ae66ffb9e
    │   ├─ emit Sync(: 4122294788042126918837209 [4.122e24], : 4121100580946556904012702 [4.121e24])
    │   ├─ emit Swap(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 192183185122587280145106 [1.921e23], param2: 0, param3: 191606635567219518304670 [1.916e23], param4: 0, param5: 0x84452042cB7be650BE4eB641025ac3C8A0079b67)
    │   └─ ← [Stop] 
    ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0x84452042cB7be650BE4eB641025ac3C8A0079b67) [staticcall]
    │   └─ ← [Return] 0x000000000000000000000000000000000000000000002873c5c478ca19744d2e
    ├─ [25171] 0x55d398326f99059fF775485246999027B3197955::transfer(0x3DabF5e36DF28F6064a7c5638D0c4e01539E35F1, 191030285531192719854894 [1.91e23])
    │   ├─ emit Transfer(param0: 0x84452042cB7be650BE4eB641025ac3C8A0079b67, param1: 0x3DabF5e36DF28F6064a7c5638D0c4e01539E35F1, param2: 191030285531192719854894 [1.91e23])
    │   └─ ← [Return] 0x0000000000000000000000000000000000000000000000000000000000000001
    ├─ [531] 0x55d398326f99059fF775485246999027B3197955::balanceOf(0x3DabF5e36DF28F6064a7c5638D0c4e01539E35F1) [staticcall]
    │   └─ ← [Return] 0x000000000000000000000000000000000000000000002873c5c478ca19744d2e
    ├─ [0] console::log("BUSD of myW:", 191030285531192719854894 [1.91e23]) [staticcall]
    │   └─ ← [Stop] 
    ├─ [0] console::log("BNB of myW:", 100000000000000000 [1e17]) [staticcall]
    │   └─ ← [Stop] 
    └─ ← [SelfDestruct] 


Transaction successfully executed.
Gas used: 611170

"""

# 解析trace文本
balance_changes = parse_trace(trace_text)

# 输出结果
for address, balance_change in balance_changes.items():
    print(f"Address: {address}, Balance Change: {balance_change} wei")