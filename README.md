# angie-sirius
this is a set of steganography programs.
It includes below

* [lina](https://github.com/TakutoYoshikai/lina)
* [parade](https://github.com/TakutoYoshikai/parade)
* [sirius](https://github.com/TakutoYoshikai/sirius)
* [cad](https://github.com/TakutoYoshikai/cad)

angie-sirius can be used as a powerful steganography program.
### Usage
**install**
```bash
pip install git+https://github.com/TakutoYoshikai/angie-sirius.git
```
**hide**

These are required

* a secret file to hide
* a file as a key(any file type, larger than secret file)
* an image file
* a directory containing image files
* a directory(destination)
```bash
angie-sirius hide -p <PASSWORD> -k <KEY FILE> -i <IMAGE FILE> -f <DIRECTORY CONTAINING IMAGE FILES> -t <DESTINATION DIRECTORY> -d <SECRET FILE>
```

**reveal**

These are required
* a file as a key(any file type, larger than secret file)
* an image file
* a directory containing image files having secret file
```bash
angie-sirius reveal -p <PASSWORD> -k <KEY FILE> -i <IMAGE FILE> -f <DIRECTORY CONTAINING ENCODED IMAGE FILES> -o <OUTPUT FILE>
```

### License
MIT LICENSE
