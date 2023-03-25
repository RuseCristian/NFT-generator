# NFT Generator

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/ac-custom-shaders-patch/acc-extension-config)



A simple passion project done with the role to learn a bit about how images are processed by computers.
A modular NFT generator application that allows you to create NFTs by diving each accesorry of an NFT into 
more parts. For example, a character that has a hat and glasses, can be divided into:

```
- background
- the character itself
- the character's facial parts(ex eyes, mouth etc)
- the glases
- the hat
```


Because of this modularity, its very easy to simply change the code
and the structure a bit to create a completely new collection of unique NFTs.


# Dependencies
- [OpenCV2](https://pypi.org/project/opencv-python/)
- [Numpy](https://numpy.org/install/)
- [PIL](https://pillow.readthedocs.io/en/stable/installation.html)


# How to use it
For every part you want you want to use, create a folder for it and store its variants there
and edit the allready existing code to your needs.
Example, you want to put earrings to your character:

```
\nft_generator
    \earrings
        ---earring_0.png
        ---earring_1.png
        ---earring_2.png
        ---earring_3.png
        ................
        ................
```
Note: If youre gonna have an optional part, that will not always be present on all NFTs,
I Suggest that you create an empty .png with index 0 and call that file for the NFT's that will
not have that optional part, just to make things easier.


# How to create your own parts
If you want to create new parts for yourself, you must respect few rules such that the program will behave normally:
- if you want that part to be colored a specific color when you run the program you must create all the pixels that represent the part with only a single RGB channel
and then specify that channel in the program to be colored the color you desire.
- if you use RGB values like (255,2,3) the program will not change that pixel, since it can see only 1 color channel everytime,
so if you want to change that pixel, you can use something like (255, 0,0) and select the red channel.(you can also do shading by
altering the value in that channel youre using, it doesnt particulary need to be 255, it can be 200 for example and that pixel will be 
darker in color.)
- if you want more complex parts, you can use 3 colors , red , green, blue and call the function to give it color 3 times for all 3 color channels.
Example, you want to make a hat of a specific color in the final product, so you make the hat red in the hat.png, but then
in some hairstyles, the hat doesnt cover the hair, so you make the near background of the hat.png with blue and then
call the function to give it color, but with the blue color channel and give it the same color as the background color of the NFT
and so, there isnt any more hair getting out of the hat.
- if you want a color to not be altered by the color function , simply change the RGB values
such that there arent 2 channels with 0 as values.Example:
        red hat (255,0,0) ---> (255,1,0), 


# Content of this repo:
- Example code with some predefined parts 
- Shading Randomizer for helping when creating new parts

# Example of "NFT"s generated
![14](https://user-images.githubusercontent.com/99805998/227733212-0bdd5c6c-b7f9-4b9d-8ef3-48359877dd4b.png)
![15](https://user-images.githubusercontent.com/99805998/227733215-7d75e477-e6ce-44bb-9cef-f8492c998ad7.png)
![18](https://user-images.githubusercontent.com/99805998/227733235-8402a789-f118-455a-a232-b224d52726a3.png)
