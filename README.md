[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU GPLv3 License][license-shield]][license-url]
[![Telegram][telegram-shield]][telegram-url]


# easygen
**Easygen** is a lightweight, easy-to-integrate library that allows you to **generate and validate software licenses** in Python using **digital signatures**. Protect your applications from unauthorized use by linking licenses to the user's machine via HWID, all without relying on external servers. EasyGen is a lightweight and easy to use library that allow

## Features

- Digital signature with private key (RSA)
- Local validation without internet
- Licenses linked to the HWID machine
- Expiration date validation


## Usage/Examples

License validation
```python
from easygen.license_validator import validate_license

if validate_license("license.lic", "public_key.pem"):
    print("Valid license")
```

License generation
```python
from easygen.license_generator import generate_license

generate_license(
    user="pc-i5-2024",
    hwid="EXAMPLE_12345_6789",
    expiry_date_str="2025-12-31",
    private_key_path="private_key.pem",
    output_path="license.lic"
)
```



## Installation

Before using, you need to generate the private and public keys
```bash
# Private key (DO NOT SHARE)
openssl genrsa -out private_key.pem 2048

# Public key (This one must be included with the software)
openssl rsa -in private_key.pem -pubout -out public_key.pem
```
Installation from source 

```bash
git clone https://github.com/freshSauce/easygen.git
cd easygen
pip install .
```
or
```bash
git clone https://github.com/freshSauce/easygen.git
cd easygen
pip install --upgrade build
python -m build
```
    
## Running Tests

To run tests, run the following command

```bash
  pytest .\tests\
```


## License

Distributed under the GNU GPLv3 License. See `LICENSE` for more information.


## Contributing

Want to contribute to the project? Great! Please follow the next steps in order to submit any feature or bug-fix :) You can also send me your ideas to my [Telegram](https://t.me/freshSauce), any submit is **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

[contributors-shield]: https://img.shields.io/github/contributors/freshSauce/easygen.svg?style=for-the-badge
[contributors-url]: https://github.com/freshSauce/easygen/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/freshSauce/easygen.svg?style=for-the-badge
[forks-url]: https://github.com/freshSauce/easygen/network/members
[stars-shield]: https://img.shields.io/github/stars/freshSauce/easygen.svg?style=for-the-badge
[stars-url]: https://github.com/freshSauce/easygen/stargazers
[issues-shield]: https://img.shields.io/github/issues/freshSauce/easygen.svg?style=for-the-badge
[issues-url]: https://github.com/freshSauce/easygen/issues
[license-shield]: https://img.shields.io/github/license/freshSauce/easygen.svg?style=for-the-badge&cacheSeconds=3600
[license-url]: https://github.com/freshSauce/easygen/blob/master/LICENSE
[telegram-shield]: https://img.shields.io/badge/-@freshSauce-black?style=for-the-badge&logo=telegram&colorB=0af
[telegram-url]: https://t.me/freshSauce
