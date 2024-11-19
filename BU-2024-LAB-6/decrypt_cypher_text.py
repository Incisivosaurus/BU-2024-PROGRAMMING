def decrypt_cypher_text(encrypted_text, key):
	decrypted_text = "" # New variable to store the decrypted text

	# Loop over each character in encrypted_text
	for character in encrypted_text:
		ascii_code = ord(character) # Get the ascii value (i.e; A=65)
		remainder = (ascii_code - key) % 256 # Find the remainder of the key being subtracted from the ascii_code then divided by 256
		decrypted_text += chr(remainder) # Convert the remainder value to its ascii equivalent and concatenate it to decrypted_text

	return decrypted_text


if __name__ == "__main__":
	# Expected output is "Each error you make in programming is an opportunity to become a better developer"
	print(decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu", 3))
