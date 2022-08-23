from turtle import width
from PIL import Image

INPUT_FILE_NAME = 'scarlett.png'
OUTPUT_FILE_NAME = 'out1.png'

def process_image() -> None:
    with Image.open(INPUT_FILE_NAME) as input_file:
        pixin = input_file.load() # type: ignore
        width, height = input_file.size
        
    output_image = Image.new('RGB', (width, height))
    pixout = output_image.load() # type: ignore
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixin[x, y]
            pixout[x, y] = (r, 0, 0)
    
    output_image.save(OUTPUT_FILE_NAME)
            
            
            
if '__main__' == __name__:
    process_image()