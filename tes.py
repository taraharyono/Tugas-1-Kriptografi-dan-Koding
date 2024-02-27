import binascii
import base64

def hexdump_to_base64(hexdump_string):
  """Decodes a hexdump string and converts the result to base64."""
  # Remove any non-hexadecimal characters from the string
  clean_hexdump = "".join(c for c in hexdump_string if c in "0123456789abcdefABCDEF")
  # Convert the hexdump string to bytes
  bytes_data = binascii.unhexlify(clean_hexdump)
  # Encode the bytes as base64
  base64_encoded_data = base64.b64encode(bytes_data).decode("utf-8")
  return base64_encoded_data

# Example usage
hexdump_string = "00000000  87 02 el e6 b9 65 b2 93 le 10 47 bf 9a 82 7d be"
base64_encoded_data = hexdump_to_base64(hexdump_string)
print(f"Base64 encoded data: {base64_encoded_data}")
