"""
### Python’da argument parser ile terminal üzerinden yazdığımız kodlara inputlar verebiliriz.
#Yüklemek için
pip install argparse
---
# program input
python "argparse example.py" --input asd.jpg --output asdout.jpg
# ya da
python "argparse example.py" -i asd.jpg -o asdout.jpg

# program output

args :  Namespace(input='asd.jpg', output='asdout.jpg')
input image name is :  asd.jpg
output image name is :  asdout.jpg

# Ekstra kaynak
https://medium.com/@celikemirhan/python-argument-parser-kullanimi-50511bd6f609
"""
import argparse

def main():
    parser = argparse.ArgumentParser()
    #print("Parser : ", parser)
    parser.add_argument(
        "--input","-i",
        help="Input image filename",
        required=True,
        type=str)

    parser.add_argument(
        "--output","-o",
        help="Output image filename",
        type=str)

    args = parser.parse_args()
    print("args : ", args)
    print("input image name is : ", args.input)
    print("output image name is : ", args.output)

if __name__ == '__main__':
    main()
