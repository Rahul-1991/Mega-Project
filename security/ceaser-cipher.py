class CeaserCipher(object):

    def get_key_from_user(self):
        while True:
            key = raw_input('Enter key for ceaser cipher : ')
            if key.isdigit():
                break
        return int(key)%26

    def get_string_from_user(self):
        input_string = raw_input('Enter string to encrypt or decrypt : ')
        return input_string

    def perform_cipher(self):
        key = self.get_key_from_user()
        input_string = self.get_string_from_user()
        decrypted_string = ''
        for i in input_string:
            if ord(i) + key > ord('Z'):
                decrypted_string += chr(key + ord(i) + ord('A') - ord('Z') - 1)
            else:
                decrypted_string += chr(ord(i) + key)

        print 'Input String : %s' %input_string
        print 'decrypted String : %s' %decrypted_string

cipher = CeaserCipher().perform_cipher()
