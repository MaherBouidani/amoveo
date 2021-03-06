from get_request import request

def share_blocks_test1():
    print("share blocks test 1")
    request(2, "add_peer", [[127,0,0,1], 3010])
    request(1, "add_peer", [[127,0,0,1], 3020], 0.01)
    request(1, "mine_block", [1, 100000], 0.02)
    request(1, "sync", [[127,0,0,1], 3020], 0.05)
    request(2, "mine_block", [1, 100000], 0.02)
    request(1, "sync", [[127,0,0,1], 3020], 0.05)
    #we should check that the heights are the same.
def share_blocks_test2():
    print("share blocks test 2")
    request(1, "mine_block", [50, 100000], 0.1)
    request(1, "sync", [[127,0,0,1], 3020], 0.1)
    request(1, "mine_block", [3, 100000], 0.02)
    request(1, "sync", [[127,0,0,1], 3020], 0.1)
    request(1, "mine_block", [3, 100000], 0.02)
    request(2, "sync", [[127,0,0,1], 3010], 0.1)
    request(3, "sync", [[127,0,0,1], 3010], 0.02)
    request(1, "spend", ["BCjdlkTKyFh7BBx4grLUGFJCedmzo4e0XT1KJtbSwq5vCJHrPltHATB+maZ+Pncjnfvt9CsCcI9Rn1vO+fPLIV4=", 100000000], 0.05)#light node 1
    request(1, "spend", ["BOnadmMfDIoCmio3ReSinirULreS3TbCEdr0R6FDDvoVB5xoAJnvwlL3yMgNhBzEb5l36z7bgizw2EKGn0W9rY8=", 200000000], 0.05)#dev3
    request(1, "spend", ["BJFwMtu8j5VfR6qwuXvZoLaiD+8U0jVvBsDb124RayO3FIrRp+SdwvIhL5+T1IPFaw5TLANGDwqj5whpZ4hWXUI=", 100000000], 0.05)#light node 2
    request(1, "spend", ["BLgYECLeI0Iq7SZqPqhoZocy3zF3ht+fPdYkjJh3OnPU1tr7+BpDbtXGNyzDF8w4gUzV7UvM4KelK6IIvQNZZ6w=", 100000000], 0.05)
    request(1, "mine_block", [1, 100000], 0.02)
    request(3, "sync", [[127,0,0,1], 3010], 0.02)
    request(3, "mine_block", [10, 100000], 0.02)
    request(3, "sync", [[127,0,0,1], 3030], 0.1)

if __name__ == "__main__":
    share_blocks_test1()
    share_blocks_test2()
