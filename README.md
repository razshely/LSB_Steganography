# LSB_Steganography

This Project Describes the use of LSB Steganography.
Do check the python script written to implement lsb steganography

#python LSB.py -f <filename> -e <secret_message> : To embed a secret message.
  <br />
#python LSB.py -f <secretfile> -x : To extract the secret message.

## What is LSB Steganography
  LSB Steganography is an image steganography technique in which messages are hidden inside an image by replacing each pixel's least 
  significant bit with the bits of the message to be hidden.

## the application of LSB 
  In a RGB image, each pixel is represented by 24 bits <br />
  Suppose the following are some of the bits in a Grayscale image <br />
  
**11110011_11110011_11110011** <br />
**11011011_11011011_11011011**  <br />
**10110110_10110110_10110110** <br />
**11011100_11011100_11011100** <br />
**11011111_11011111_11011111** <br />
**11010111_11010111_11010111** <br />
**00100110_00100110_00100110** <br />
**01000011_01000011_01000011** <br />
  
Suppose you wish to hide "dad" in it. The ascii value of "dad" is **01100100_01100001_01100100**.
The algorithm simply replaces the last bit of the bytes with the consecutive bits of the word "dad", Giving us

1111001**0**_1111001**1**_1111001**1** <br />
1101101**0**_1101101**0**_1101101**1**  <br />
1011011**0**_1011011**0**_1011011**0** <br />
1101110**1**_1101110**1**_1101110**0** <br />
1101111**0**_1101111**0**_1101111**0** <br />
1101011**1**_1101011**0**_1101011**1** <br />
0010011**1**_0010011**0**_0010011**0** <br />
0100001**1**_0100001**0**_0100001**0** <br />
  
 In addition the code add to the image our end secret *$@FINISH@$* <br />
  and on the decode that is the way the code know where the secret end
  ### Example
  I typed #python LSB.py -f flower.png -e check 1 . 2 . 3 <br />
  and that the two png files that one of them contiend the secret massage(the left)
![flowerr](https://user-images.githubusercontent.com/72939664/168488450-6b77daa9-25f9-43d9-8660-606180f87fb9.png)
  
 when  I typed this: python LSB.py -f end69.png -x <br />
  the The output I received is: 
The secret massage is: check 1 . 2 . 3

