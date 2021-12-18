with open("day16_input.txt", "r") as f:
    hexadecimal = f.read().strip()

print(f"Hex: {hexadecimal}")


def hex2bin(h):
    return bin(int(h, 16))[2:].zfill(len(h) * 4)


b = hex2bin(hexadecimal)
print(f"Bin: {b}")

print()


def decode_header(b):
    packet_version = b[:3]
    packet_type_id = b[3:6]

    return int(packet_version, 2), int(packet_type_id, 2), b[6:]


def decode_literal(b):
    value = ""

    while b:
        seg = b[:5]
        value += seg[-4:]
        b = b[5:]
        if seg[0] == "0":
            break

    return value, b


def decode_operator(b):
    length_type_id = b[:1]

    if length_type_id == "0":
        length_of_subpackets = int(b[1:16], 2)

        remaining = b[16 + length_of_subpackets :]
        b = b[16 : 16 + length_of_subpackets]
        number_of_subpackets = -1
    else:
        number_of_subpackets = int(b[1:12], 2)
        b = b[12:]
        remaining = None

    return length_type_id, number_of_subpackets, b, remaining


result = []


def decode(b):
    while b:
        if all(c == "0" for c in b):
            return

        packet_version, packet_type_id, b = decode_header(b)
        result.append(packet_version)
        print(f"packet_version: {packet_version}, packet_type_id: {packet_type_id}")
        if packet_type_id == 4:
            value, b = decode_literal(b)
            print(f"Literal value {value} is {int(value, 2)}.")
        else:
            length_type_id, number_of_subpackets, block, remaining = decode_operator(b)
            print(
                f"length_type_id: {length_type_id},",
                f"number_of_subpackets: {number_of_subpackets},",
            )
            if number_of_subpackets == -1:
                b = remaining
                decode(block)
            else:
                b = block
                return decode(b)

    return


decode(b)
print()
print(f"Result: {result} -> {sum(result)}")
