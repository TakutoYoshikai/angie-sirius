from lina import lina
from sirius import sirius
from cad import cad
from parade import parade
import argparse
import os

def hide(data_filepath, key_filepath, image_filepath, password, fr, to):
    sirius.encode(data_filepath, key_filepath, "output1.data")
    parade.generate_key(image_filepath, "output1.data", "output2.png")
    cad.img_to_binary("output2.png", "output3.data")
    lina.hide_into_album("output3.data", password, fr, to)
    os.remove("output1.data")
    os.remove("output2.png")
    os.remove("output3.data")

def reveal(key_filepath, image_filepath, password, fr, output_filepath):
    lina.reveal_from_album(password, fr, "output2-1.data")
    cad.binary_to_img("output2-1.data", "output2-2.png")
    parade.decode("output2-2.png", image_filepath, "output2-3.data")
    sirius.decode("output2-3.data", key_filepath, output_filepath)
    os.remove("output2-1.data")
    os.remove("output2-2.png")
    os.remove("output2-3.data")

def main():
    parser = argparse.ArgumentParser(description="angie-sirius is a powerful encoder/decoder of data")
    parser.add_argument("mode", help="hide or reveal")
    parser.add_argument("-p", "--password")
    parser.add_argument("-k", "--key")
    parser.add_argument("-i", "--image")
    parser.add_argument("-d", "--data")
    parser.add_argument("-f", "--from")
    parser.add_argument("-t", "--to")
    parser.add_argument("-o", "--output")
    args = vars(parser.parse_args())
    if args["mode"] == "hide":
        if args["data"] == None or args["key"] == None or args["image"] == None or args["password"] == None or args["from"] == None or args["to"] == None:
            parser.print_help()
            return
        hide(args["data"], args["key"], args["image"], args["password"], args["from"], args["to"])
    elif args["mode"] == "reveal":
        if args["key"] == None or args["image"] == None or args["password"] == None or args["from"] == None or args["output"] == None:
            parser.print_help()
            return
        reveal(args["key"], args["image"], args["password"], args["from"], args["output"])
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
