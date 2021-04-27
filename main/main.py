from util.digital_signature import DigitalSignature

if __name__ == '__main__':
    signature1 = DigitalSignature(data='abc',
                                  secret='6a87c625-e186-43bc-8160-b6e80e1a910b').get_signature()

    signature2 = DigitalSignature(data='abc',
                                  secret='6a87c625-e186-43bc-8160-b6e80e1a910b').get_signature()

    print('{}\n{}'.format(signature1, signature2))
