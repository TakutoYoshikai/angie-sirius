# angie-sirius
this is a set of steganography program.
It includes them

* [lina](https://github.com/TakutoYoshikai/lina)
* [parade](https://github.com/TakutoYoshikai/parade)
* [sirius](https://github.com/TakutoYoshikai/sirius)
* [cad](https://github.com/TakutoYoshikai/cad)

angie-sirius can be used as a data encoder/decoder.
### Usage
**install**
```bash
pip install git+https://github.com/TakutoYoshikai/angie-sirius.git
```
**encode**
encoding needs them.
* a secret file to hide
* a file as a key(any file type, larger than secret file)
* an image file
* a directory containing image files
* a directory(destination)
```bash
angie-sirius hide -p <PASSWORD> -k <KEY FILE> -i <IMAGE FILE> -f <DIRECTORY CONTAINING IMAGE FILES> -t <DESTINATION DIRECTORY> -d <SECRET FILE>
```

**decode**
decoding needs them.
* a file as a key(any file type, larger than secret file)
* an image file
* a directory containing encoded image files
```bash
angie-sirius reveal -p <PASSWORD> -k <KEY FILE> -i <IMAGE FILE> -f <DIRECTORY CONTAINING ENCODED IMAGE FILES> -o <OUTPUT FILE>
```

### License
MIT LICENSE
