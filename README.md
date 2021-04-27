# Digital Signature Python

Argorithm: hmac-sha256

---


Example code: ```./main/main.py```

- First message: `This is the first content`
- Second message: `This is the second content`
- Secret key: `6a87c625-e186-43bc-8160-b6e80e1a910b`

```python
from util.digital_signature import DigitalSignature

if __name__ == '__main__':
    signature1 = DigitalSignature(data='This is the first content',
                                  secret='6a87c625-e186-43bc-8160-b6e80e1a910b').get_signature()

    signature2 = DigitalSignature(data='This is the second content',
                                  secret='6a87c625-e186-43bc-8160-b6e80e1a910b').get_signature()

    print('{}\n{}'.format(signature1, signature2))

```

Output: 

```
4426b932521806d1f4869ffd41e860f4ae2ea14bcf332e25d774cc2242952d44
37f81da34ff7d59328c2cf3476fc0e74e51bf19d2302600a8bda802f5f73e4f8
```

---

Run Example: ```python3 ./main/main.py```

Python version: 3.x