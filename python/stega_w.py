import stega

#wrapper for stega library to provide support for autocompletion

class Stegacrypto:
    def __init__(self):
        self.stegaworker = stega.Stega
        self.cryptoworker = stega.Crypto

    def hide_file_in_temp(self, file):
        self.stegaworker.hide_file_in_temp(file)

    def take_file_from_temp(self, output_dir):
        self.stegaworker.take_file_from_temp(output_dir)

    def hide_file_in_jpeg(self, file, container):
        self.stegaworker.hide_file_in_jpeg(file, container)

    def take_file_from_jpeg(self, container, output_dir):
        self.stegaworker.take_file_from_jpeg(container, output_dir)

    def clean_jpeg(self, container):
        self.stegaworker.clean_jpeg(container)


    def encode_and_hide_file_in_temp(self, password, file):
        self.stegaworker.encode_and_hide_file_in_temp(password, file)

    def decode_and_take_file_from_temp(self, password, output_dir):
        self.stegaworker.decode_and_take_file_from_temp(password, output_dir)

    def encode_and_hide_file_in_jpeg(self, password, file, container):
        self.stegaworker.hide_file_in_jpeg(password, file, container)

    def decode_and_take_file_from_jpeg(self, password, container, output_dir):
        self.stegaworker.take_file_from_jpeg(password, container, output_dir)


    def encrypt_file(self, file, password, output_dir):
        self.cryptoworker.encrypt_file(file, password, output_dir)

    def decrypt_file(self, file, password, output_dir):
        self.cryptoworker.decrypt_file(file, password, output_dir)