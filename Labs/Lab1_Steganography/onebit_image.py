from turtle import width
from PIL import Image

INPUT_FILE_NAME = 'scarlett.png'
OUTPUT_FILE_NAME = 'out3.png'

def process_image() -> None:
    with Image.open(INPUT_FILE_NAME) as input_file:
        pixin = input_file.load() # type: ignore
        width, height = input_file.size
        
    output_image = Image.new('1', (width, height))
    pixout = output_image.load() # type: ignore
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixin[x, y]
            avg = (r + g + b) // 3
            if avg > 127:
                pixout[x, y] = 0
            else:
                pixout[x, y] = 1
    
    output_image.save(OUTPUT_FILE_NAME)
            
            
            
if '__main__' == __name__:
    process_image()