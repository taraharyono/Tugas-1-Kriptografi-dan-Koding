import js2py
import base64

def RC4_text(plaintext, key):
    # Define the JavaScript function
    js_function = """
    function RC4(plaintext, key) {
        // Inisialisasi S-box
        var sbox = [];
        for (var i = 0; i < 256; i++) {
            sbox[i] = i;
        }

        // Key-Scheduling Algorithm (KSA)
        var j = 0;
        for (var i = 0; i < 256; i++) {
            j = (j + sbox[i] + key.charCodeAt(i % key.length)) % 256;

            // Menggabungkan dengan konsep vigenere (sbox[i] ditambahkan dengan key)
            var keyChar = key.charCodeAt(i % key.length);
            sbox[i] = (sbox[i] + keyChar);

            // Pertukarkan nilai sbox[i] dan sbox[j]
            var temp = sbox[i];
            sbox[i] = sbox[j];
            sbox[j] = temp;
        }

        // Pseudo-random generation algorithm (PRGA) and encryption
        var ciphertext = "";
        var i = 0;
        var l = 0;
        for (var k = 0; k < plaintext.length; k++) {
            i = (i + 1) % 256;
            l = (l + sbox[i]) % 256;

            // Pertukarkan nilai sbox[i] dan sbox[l]
            var temp = sbox[i];
            sbox[i] = sbox[l];
            sbox[l] = temp;

            // Generate byte ke-k dari aliran
            var t = (sbox[i] + sbox[l]) % 256;
            var keystreamByte = sbox[t];
            ciphertext += String.fromCharCode(keystreamByte ^ plaintext.charCodeAt(k));
        }
        return ciphertext;
    }
    """
    context = js2py.EvalJs()
    context.execute(js_function)
    ciphertext = context.RC4(plaintext, key)

    return ciphertext



# Example usage:
plaintext = "hilmibaskara"
key = "wiu"

encrypted_text = RC4_text(plaintext, key)
print("Encrypted:", encrypted_text)

# Convert encrypted text to Base64
encrypted_base64 = base64.b64encode(encrypted_text.encode()).decode()
print("Encrypted Base64:", encrypted_base64)

decrypted_text = RC4_text(encrypted_text, key)
print("Decrypted:", decrypted_text)
